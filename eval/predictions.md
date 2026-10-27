# Predictions — written BEFORE measuring

Each prediction is recorded before the run it predicts. It is never edited afterwards;
the result goes in a separate line below it.

## H0 · CAG baseline (eval set v1, 12 cases)

- **Written:** 2026-09-25 18:20 (local time), before any run.
- **Configurations:** whole catalogue in the context window (both competitive sheets,
  raw cell values), `deepseek/deepseek-v4-flash`, (a) reasoning off, (b) reasoning on.
- **Prediction (author):** both configurations pass **11 of 12**. The one failure:
  **D04** (counting open calls), because the model gets two sheets with the same 7 calls
  and counts them twice. "No other failures expected for now."

**Result:** _to be filled in after the run_

## H0 · second prediction (sum rows)

- **Written:** 2026-10-14 18:50, before any run.
- **Prediction (author):** R03 i D04: wiersze sum nic nie zmienią, model odczyta dane bez problemu.
**Result (reasoning-off, 2026-10-15, StreamLake, n=12):** 8/12. Failed: R01, R02, D04, D10.
D04 failed, but not because of double counting (row 27 counted as open; rows 22–23 left out).
Second prediction confirmed: the sum rows did not affect R03 or D04.
Graded by the mentor at the author's request.

## H0 · third prediction (reasoning on)

- **Written:** 2026-10-28 00:32, before the full run (only a D05 smoke test so far:
  11.81 s, `finish=stop`, 237 reasoning tokens, n=1).
- **Configuration:** same as the baseline, one change only: reasoning on
  (`max_tokens` 8000, reasoning budget 4000), `streamlake/fp8`.
- **Prediction (author):** **11 of 12.** Reasoning fixes R01, R02 and D04, because they
  failed on comparing dates in long lists while the data was correct. D10 still fails:
  the trace (2026-10-27) shows the month-only date is lost in `catalog.py` (decision 1A),
  so the model never receives it. Median latency **8 s** (baseline 5.3 s).

**Result:** _to be filled in after the run, graded by the author_