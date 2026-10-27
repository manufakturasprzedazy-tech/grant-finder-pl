"""H0 — CAG: the whole catalogue goes into the context window with every question.

This module is the SYSTEM UNDER TEST. It knows nothing about eval cases or scoring.
"""
import time

from openai import OpenAI

from src.prompt import build_system_prompt, build_user_message

OPENROUTER_BASE = "https://openrouter.ai/api/v1"
MODEL = "deepseek/deepseek-v4-flash"
PROVIDER = "streamlake/fp8"   # pinned: otherwise we measure routing between providers, not the system
TEMPERATURE = 0.2

# Reasoning tokens count toward max_tokens, so the reasoning budget must stay well below it.
CONFIGS = {
    "reasoning-off": {"max_tokens": 2500, "reasoning": {"enabled": False}},
    "reasoning-on": {"max_tokens": 8000, "reasoning": {"max_tokens": 4000}},
}


def answer(client: OpenAI, catalogue: str, question: str, as_of, config: str) -> dict:
    cfg = CONFIGS[config]
    started = time.perf_counter()
    response = client.chat.completions.create(
        model=MODEL,
        temperature=TEMPERATURE,
        max_tokens=cfg["max_tokens"],
        messages=[
            {"role": "system", "content": build_system_prompt(catalogue)},
            {"role": "user", "content": build_user_message(question, as_of)},
        ],
        extra_body={
            "provider": {"order": [PROVIDER], "allow_fallbacks": False},
            "reasoning": cfg["reasoning"],
        },
    )
    usage = response.usage
    return {
        "answer": response.choices[0].message.content,
        "finish_reason": response.choices[0].finish_reason,
        "latency_s": round(time.perf_counter() - started, 2),
        "provider": getattr(response, "provider", None),
        "prompt_tokens": usage.prompt_tokens,
        "completion_tokens": usage.completion_tokens,
        "reasoning_tokens": getattr(usage.completion_tokens_details, "reasoning_tokens", None),
        # OpenRouter returns the reasoning text in message.reasoning (billed either way, so we keep it).
        "reasoning": getattr(response.choices[0].message, "reasoning", None),
        "cached_tokens": getattr(usage.prompt_tokens_details, "cached_tokens", None),
        "cost_usd": getattr(usage, "cost", None),
    }
