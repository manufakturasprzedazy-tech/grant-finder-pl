# ADR-0005: Update the index with upserts and never delete

- **Status:** Accepted
- **Date:** 2026-09-23

## Context
Each monthly edition drops calls that have closed. Corrections change single fields.

## Decision
Upsert every row from the newest file: overwrite changed records, add new ones, and **keep
records the source dropped**.

## Alternatives considered
- **A.** Replace the whole index with the newest file.
- **B.** Upsert without deleting.

## Prediction (written before measuring)
The student predicted that a new edition means "the previous month drops out, but something
may be added or changed" — and asked for it to be checked on data rather than assumed.

## Measurement
Compared on 2026-09-23, matched by link:

| comparison | added | removed | changed | unchanged |
|---|---|---|---|---|
| correction, May → May-1 | 0 | 0 | 1 (budget) | 51 |
| correction, May-1 → May-2 | 0 | 0 | 0 | 52 |
| new edition, Aug → Sep | 8 | 8 | 2 | 37 |

All eight calls removed in September had closed in August. A new edition is the old list
minus closed calls plus new ones — not a fresh list.

## Cost of this choice
The index grows over time. Closed calls stay in it and must be shown as closed, which
ADR-0004 already guarantees.

## Rejected — and why
**A.** A user asking about a call that closed on 20 August would get *"unknown call"* instead
of *"this call closed on 20 August"*.

Upserts also keep successive rounds of the same programme for free. *Polskie Mosty
Technologiczne*: one round closed on 19 August, the next is open until 30 October — both stay,
under different links.

A row identical to the stored one needs no special handling: writing the same values again
changes nothing.
