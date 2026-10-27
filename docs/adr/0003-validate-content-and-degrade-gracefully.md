# ADR-0003: Validate the content type; degrade gracefully when no new file is available

- **Status:** Accepted
- **Date:** 2026-09-23

## Context
Requesting a file that did not exist yet returned **HTTP 200** and a 99 KB HTML page
(`text/html`), not a 404. Code that checks only the status code would have stored a web page
under the name `nabory.xlsx` — and failed silently afterwards.

## Decision
- Accept a download only if its content type is a spreadsheet
  (`application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`).
- If no valid new file is available, keep serving the last good file and **tell the user
  which date the data comes from**.

## Alternatives considered
- **A.** Trust the HTTP status code.
- **B.** Check the content type.
- **C.** Stop answering when the data may be stale.

## Prediction (written before measuring)
None recorded.

## Measurement
Measured 2026-09-22/23: one soft 404 observed; all seven real monthly files passed the
content-type check.

## Cost of this choice
Users may get answers based on data a few days old. They are told so.

## Rejected — and why
- **A.** Would silently store an HTML page as the index.
- **C.** Leaves the user with nothing, when the most likely cause is a delay of a day or two.

## Open
How a **human** is alerted when validation fails is not decided yet. Handling an error and
notifying someone are two different things: a handled error that nobody sees stays silent.
