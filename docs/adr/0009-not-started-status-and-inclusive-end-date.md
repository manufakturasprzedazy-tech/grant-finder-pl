# ADR-0009: Fourth status "not started"; the end date is inclusive and the last day is announced

- **Status:** Accepted
- **Date:** 2026-09-25

## Context
ADR-0008 derives the status only from the **end** date. While writing the first eval
cases on 2026-09-25 (snapshot published 2026-08-31, sheet `Aktualne_konkurencyjne`),
one call did not fit: row 17 starts on 2026-09-30. On 2026-09-25 the ADR-0008 rules
would call it **open**, although no application can be submitted yet.

The same cases raised a second question the ADRs did not answer: is a call still open
**on** its end date?

## Decision
1. A call's status has **four** values: **open**, **closed**, **undetermined**, **not started**.
   If the start date is later than the query date, the status is **not started** and the
   answer gives the start date.
2. The end date is **inclusive**: on the end date the call is still open.
3. On the last day the answer says explicitly that **today is the last day**. A user who
   hears only "open" may plan to apply tomorrow.

## Alternatives considered
- **A.** Keep three statuses; a call that has not started counts as open.
- **B.** Keep three statuses; a call that has not started counts as undetermined.
- **C.** A fourth status, "not started", with the start date in the answer.

## Prediction (written before measuring)
None: this decision comes from designing eval cases, not from a measurement.

## Measurement
Snapshot published 2026-08-31, sheet `Aktualne_konkurencyjne`, statuses computed with a
script on 2026-09-25: 17 open · 8 closed · 3 undetermined · **1 not started** (row 17).
Eval cases that test this ADR: D08 (last day), D09 (day after), D11 (not started).

## Cost of this choice
- The status function needs the start date as well, and the start-date column has the
  same problems as the end-date column (text, month precision, merged cells).
- "Inclusive" is an assumption about how the ministry means its dates. A call that in
  fact closes at a given hour on the last day would still be shown as open all day.

## Rejected — and why
- **A.** Tells the user they can apply when they cannot.
- **B.** The start date is known exactly; hiding it behind "undetermined" throws away a
  fact the user needs.
