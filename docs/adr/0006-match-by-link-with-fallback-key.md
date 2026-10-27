# ADR-0006: Match records by link, falling back to action number + name + start date

- **Status:** Accepted
- **Date:** 2026-09-23

## Context
Upserts need an identifier that says "this row is the same call as that one". Two traps:

- **Action number + name identify a programme action, not a call.** Action 1.3
  *Kadry nowoczesnej gospodarki* had seven separate calls, each with its own dates and link.
- Some rows have no link — the cell says *"Brak linku do naboru"* or holds a whole sentence.

A good key field must meet **two** conditions at once:
1. it does not change when a record is corrected,
2. it differs between records.

## Decision
- Primary key: the call's URL, normalised (lower case, no `#fragment`, no trailing slash).
- Fallback, when there is no URL: action number + normalised name + start date.

## Alternatives considered
- **A.** Name only.
- **B.** Action number + name.
- **C.** Action number + name + start date.
- **D.** Include the budget.

## Prediction (written before measuring)
The student predicted few records would be wrongly treated as new, because *"public offices
like things to stay stable"*.

## Measurement
Seven monthly files, March–September 2026:

- **Names never changed spelling** — normalisation did not trigger once in six transitions.
  The prediction held.
- Competitive calls: **4** rows without a link, **0** key collisions.
- Collisions within a single month: **11** with name only, **9** with name + start date.
  Removing a field from a key can only merge more records, never fewer.
- Records wrongly treated as new: roughly 2–3 of 43. *Estimated by inspecting the gap between
  start dates, not measured.* The clearest case is a call announced with the start date
  *"July, probably the second half — to be confirmed"*, which later received a real date.

## Cost of this choice
When the ministry corrects a start date, the corrected call looks like a new one.

## Rejected — and why
- **A** and **B.** Stable, but not unique: they merge different calls.
- **D.** The budget changes in corrections (May), so a corrected call would look new.
