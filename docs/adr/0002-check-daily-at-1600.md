# ADR-0002: Check for new files once a day at 16:00

- **Status:** Accepted
- **Date:** 2026-09-23

## Context
Corrections arrive on arbitrary days of the month: 5 March, 3 April, 6 May, 13 May,
1 June, 3 August 2026. Public offices work until about 15:30. Users of this system do not need
same-hour updates — a new list the next day is acceptable.

## Decision
Query the API once a day at 16:00.

## Alternatives considered
- **A.** Once a month, on the last day.
- **B.** Once a day, at 16:00.
- **C.** Every hour.

## Prediction (written before measuring)
None recorded.

## Measurement
- Six mid-month corrections in seven months. A monthly check would have served an outdated
  May list for up to three weeks, after the ministry had corrected it twice.
- Publication times of all 17 files found through the API: **between 09:23 and 15:06**,
  none after 16:00 (measured 2026-09-23). The check is placed after office hours rather than
  after the typical publication time, so a late upload is still caught the same day.

**If the ministry publishes several versions on the same day, nothing breaks.** The 16:00 run
takes the version with the newest publication date (ADR-0001), and the last correction is the
one that is true. Intermediate versions do not matter.

## Cost of this choice
A file published after 16:00 is picked up the next day.

## Rejected — and why
- **A.** Misses every correction made during the month.
- **C.** The source changes at most a few times a month. Hourly polling adds load on a public
  server and gains nothing.
