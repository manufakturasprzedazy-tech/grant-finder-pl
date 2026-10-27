# ADR-0008: Three-valued call status; an imprecise end date is an interval

- **Status:** Accepted
- **Date:** 2026-09-24

## Context
ADR-0004 computes each call's status from its end date. That only works if the end date
is a date. On 2026-09-24 the end-date column was read with `openpyxl` — the same way the
ingest will read it — instead of looking at it in a spreadsheet app. The two views differ.

## Decision
A call's status has **three** values: **open**, **closed**, **undetermined**.

| what the end-date cell holds | status |
|---|---|
| a real date, or a date written in words (converted to a date) | open or closed, from the date |
| a date known only to the month, or a range of years | the end date is an **interval**: before it → open · after it → closed · inside it → undetermined |
| rounds, continuous intake | undetermined |

An undetermined answer quotes the sheet word for word and gives the call's link.
Saying "I don't know the date" is the correct answer when the data does not contain it.

## Alternatives considered
- **A.** Two values; when only the month is known, assume the **first** day of the month.
- **B.** Two values; assume the **last** day of the month.
- **C.** Three values with the interval rule.
- **D.** Look up the exact date on each call's website automatically.

## Prediction (written before measuring)
None recorded. The file had been seen before, so a prediction would not have been one.

## Measurement
National call list published 2026-08-31, sheet `Aktualne_konkurencyjne`, n = 29,
measured 2026-09-24:

| what the parser gets from "end date" | rows | example |
|---|---|---|
| a real date | 23 | |
| a real date, but only the month is meaningful (display format `mmm-yy`, stored day = 1) | 2 | row 30: shown `XII-27`, stored `2027-12-01` |
| text that looks exactly like a date | 1 | row 20: `'30 października 2026'` |
| text: a range of years | 1 | row 27: `'2026/2027'` |
| empty — a merged cell; the sentence lives in the start-date column | 2 | row 22 (rounds), row 23 (continuous intake) |

The list in ADR-0004 does not match this sheet: "to be announced" does not occur here,
and "rounds" was not on it.

Links of the five uncertain rows (for alternative D): three different websites, one link
is a bank's home page rather than a call page, and one cell holds two URLs.

## Cost of this choice
- A continuous-intake loan is most likely open, yet the system says "undetermined".
  The user has to check it themselves.
- The parser has to know the twelve Polish month names in the genitive
  (`października`, not `październik`).

## Rejected — and why
- **A.** Its only error is saying "closed" during that month while the call may still be
  open — and that error is the expensive one. A company that is told "closed" loses the
  grant. A company that is told "open" when it is closed loses preparation time and
  perhaps an adviser's fee. A conservative assumption is safe only if it protects against
  the more expensive error. This one does the opposite.
- **B.** The opposite error, hidden in the code where the user cannot see it.
- **D.** It concerns 5 of 29 rows (17%), spread over three differently built websites.
  That is a separate subsystem, not a parser rule. Parked: undetermined status is the
  natural signal for routing such calls to floor 2 later.
