# ADR-0010: Pin one provider for the generation model; switch from Alibaba to StreamLake

- **Status:** Proposed (used for the H0 baseline; final after the full run gives latency data)
- **Date:** 2026-10-15

## Context
Decision 3 (2026-09-25) fixed the generation model for the H0 (CAG) baseline:
`deepseek/deepseek-v4-flash` through OpenRouter, provider **pinned** to `alibaba/fp8`
with `allow_fallbacks: False`. Two reasons: without pinning we would measure OpenRouter's
routing between providers rather than the system, and prompt caching had already been
measured on this provider in RODO-RAG (78% and 99.6% of input tokens read from cache,
2026-09-18/19).

On 2026-10-14/15 the first runs hit `429` twice within about 15 minutes. The error came
from OpenRouter's **shared pool** at Alibaba (`limit_source: upstream_provider_shared_pool`,
`provider_error_code: insufficient_quota`), not from our account or our code. A 24-call
measurement cannot finish reliably under these conditions.

## Decision
Keep the same model and keep the provider pinned, but pin it to **`streamlake/fp8`**
instead of `alibaba/fp8`.

## Alternatives considered
- **A.** Stay on Alibaba and retry later.
- **B.** Stay on Alibaba and raise the client's `max_retries`.
- **C.** Allow fallbacks (`allow_fallbacks: True`), Alibaba first.
- **D.** Pin another fp8 provider of the same model. **(chosen: StreamLake)**
- **E.** Change the model (e.g. a Claude model).
- **F.** Bring our own Alibaba key (BYOK), as the error message suggests.

## Prediction (written before measuring)
None. The switch was forced by an outage, not planned.

## Measurement
Smoke tests and runs through `eval/run.py`, config `reasoning-off`. One call per row,
so every number below is **n=1**.

| when | provider | case | result | time | input / output tokens | cached | cost (USD) |
|---|---|---|---|---|---|---|---|
| 2026-10-14 23:59 | Alibaba | D05 | `429` | — | — | — | — |
| 2026-10-15, 00:00–00:11 | Alibaba | D05 | ok | 2.44 s | 9 713 / 119 | 0 | 0.00149 |
| 2026-10-15 00:11 | Alibaba | full run | R01 ok, then `429` on R02 | 14.24 s (R01) | 9 718 / 1 816 | 9 216 | 0.00090 |
| 2026-10-15 00:18 | StreamLake | D05 | ok | 9.86 s | 9 713 / 213 | 0 | 0.00071 |

Providers of this model, from OpenRouter's endpoint list
(`/api/v1/models/deepseek/deepseek-v4-flash/endpoints`, read 2026-10-15 around 00:15):
16 providers; 7 of them serve fp8 **and** support implicit caching.

| provider slug | uptime, last 24 h | input, USD per 1M tokens | cache read, USD per 1M tokens |
|---|---|---|---|
| `streamlake/fp8` | 100% | 0.07 | 0.014 |
| `gmicloud/fp8` | 100% | 0.091 | 0.018 |
| `deepinfra/fp8` | 99.7% | 0.09 | 0.018 |
| `parasail/fp8` | 100% | 0.14 | 0.07 |
| `alibaba/fp8/us-east-1` | 99.9% (**100% in the last 30 min, while we got two `429`s**) | 0.15 | 0.03 |

StreamLake was chosen for a full day at 100% uptime and cache reads at one fifth of the
input price. In CAG this matters, because the input carries the whole catalogue: on the
Alibaba D05 call the input was **97.6%** of the cost.

## Cost of this choice
- **Slower on the one comparable call:** 9.86 s against 2.44 s. Part of the gap is the
  answer length (213 tokens against 119). Both are single calls, so this is an event,
  not a property of either provider.
- **Cache numbers are no longer comparable** with the RODO-RAG measurements on Alibaba.
- **Cheaper on the same call:** 0.00071 USD against 0.00149 USD (n=1).
- **Reliability is unknown.** OpenRouter's uptime showed Alibaba at 100% while it was
  refusing us, so uptime does not predict `429` from a shared pool.

## Rejected — and why
- **A.** Two `429`s in about 15 minutes; a 24-call run cannot be planned around that.
- **B.** The client waits before each retry, and that wait is counted in `latency_s`.
  More retries would hide the outage inside the time measurement.
- **C.** Answers in one baseline could come from different providers. That is exactly
  the routing we pinned the provider to avoid.
- **E.** Changes the system under test, and both written predictions are about
  DeepSeek V4 Flash. A Claude model is planned later as another system on the same ruler.
- **F.** Needs a separate Alibaba Cloud account and key; too much setup for a baseline.
- Morph (`morph/fp8`) was also considered: it does not serve this model
  (OpenRouter lists only Morph's own models).

## 🔑 Revisit when (optional)
- the full run shows a median latency above the time budget (the budget is not defined
  yet and has to be set before production);
- StreamLake returns `429` during a run;
- a comparison of providers on the same cases shows a difference in answer quality.
