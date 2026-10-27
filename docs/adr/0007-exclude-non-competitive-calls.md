# ADR-0007: Exclude non-competitive calls

- **Status:** Accepted
- **Date:** 2026-09-23

## Context
The national call list contains two kinds of calls:

- **Competitive** — any eligible company can apply; applications compete for funding.
- **Non-competitive** — the beneficiary is named in advance, usually a public body.
  The source says so directly, e.g. *"Call intended for: Państwowe Gospodarstwo Wodne
  Wody Polskie"* or *"Invitation sent directly to the applicant"*.

The target users of this system are **private SMEs with no links to the state**.

## Decision
Non-competitive calls are excluded from the index.

## Alternatives considered
- **A.** Exclude them entirely.
- **B.** Keep them as information only, answering *"this call is not open to you"*.

## Prediction (written before measuring)
None. This was a product decision, not a measured one. The measurement below was
taken afterwards and turned out to support it for an independent reason.

## Measurement
Seven monthly files, March–September 2026 (measured 2026-09-23):

| call type | rows without a link | key collisions |
|---|---|---|
| competitive | 4 | 0 |
| non-competitive | 52 | 8 |

Non-competitive calls account for 93% of rows without a link and **all** key collisions.
Excluding them removes almost the entire record-matching problem as a side effect.

## Cost of this choice
If a user asks about a non-competitive call by name, the system answers that it does
not know the call. Accepted: that user could not apply to it anyway.

## Rejected — and why
**B.** It adds data an SME cannot act on. Telling a company about a call it cannot enter
is like explaining rocket design to a car mechanic: interesting at a conference,
useless for the business decision in front of them.

## 🔑 Revisit when
- the target users change to **public institutions or state-linked companies**, or
- the product becomes **informational rather than decision-support** — for example
  a tool for journalists tracking public spending.
