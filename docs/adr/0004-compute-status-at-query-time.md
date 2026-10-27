# ADR-0004: Compute each call's status from its dates at query time

- **Status:** Accepted
- **Date:** 2026-09-23

## Context
The sheet named `Aktualne_konkurencyjne` ("current, competitive") contained calls whose
deadline had already passed. The list is published once a month and not updated in between,
so it goes stale a little more every day.

## Decision
The sheet name is never used as a status. Whether a call is open or closed is computed from
its end date on every query.

## Alternatives considered
- **A.** Trust the sheet label.
- **B.** Compute the status once, when the file is loaded.
- **C.** Compute it on every query.

## Prediction (written before measuring)
None recorded.

## Measurement

| date | calls in the "current" sheet | already closed |
|---|---|---|
| 2026-09-21 | 29 | **7 (24%)** |
| 2026-09-22 | 29 | **8** |

Same file, one day later, one more closed call.

## Cost of this choice
Every end date must be machine-readable — and it is not. The date column holds five kinds of
values: a real date, a date written in Polish words, a range such as `2026/2027`, a note about
continuous intake, and "to be announced". How to handle each one is still open.

## Rejected — and why
- **A.** Wrong for a quarter of the rows.
- **B.** Correct on the day of loading, wrong the next day.
