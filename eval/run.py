"""Harness: runs eval cases against the system under test and saves the raw answers.

Scoring in v1 is manual (12 cases: reading every answer is the error analysis).
Usage, from the project root:
    uv run python -m eval.run --config reasoning-off [--only D05]
"""
import argparse
import json
import os
from datetime import date
from pathlib import Path

import yaml
from dotenv import load_dotenv
from openai import OpenAI

from src.cag import OPENROUTER_BASE, CONFIGS, answer
from src.catalog import load_catalogue

ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", choices=CONFIGS, required=True)
    parser.add_argument("--only", help="run a single case id, e.g. D05 (smoke test)")
    args = parser.parse_args()

    load_dotenv(ROOT / ".env")
    client = OpenAI(base_url=OPENROUTER_BASE, api_key=os.environ["OPENROUTER_API_KEY"])

    spec = yaml.safe_load((ROOT / "eval" / "cases.yaml").read_text(encoding="utf-8"))
    catalogue = load_catalogue(ROOT / spec["snapshot"])
    cases = [c for c in spec["cases"] if not args.only or c["id"] == args.only]
    if not cases:
        raise SystemExit(f"No case with id {args.only!r}")

    out_dir = ROOT / "eval" / "results"
    out_dir.mkdir(exist_ok=True)
    out = out_dir / f"{date.today().isoformat()}_h0-cag_{args.config}{'_' + args.only if args.only else ''}.jsonl"

    print(f"catalogue: {len(catalogue):,} characters · cases: {len(cases)} · config: {args.config}")
    with out.open("w", encoding="utf-8") as f:
        for i, case in enumerate(cases, start=1):
            result = answer(client, catalogue, case["question"], case["as_of"], args.config)
            row = {"id": case["id"], "as_of": case["as_of"].isoformat(), "question": case["question"], **result}
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
            print(f"[{i}/{len(cases)}] {case['id']}  {result['latency_s']} s  "
                  f"finish={result['finish_reason']}  in={result['prompt_tokens']}  "
                  f"out={result['completion_tokens']}  cached={result['cached_tokens']}  cost={result['cost_usd']}")
    print(f"saved: {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
