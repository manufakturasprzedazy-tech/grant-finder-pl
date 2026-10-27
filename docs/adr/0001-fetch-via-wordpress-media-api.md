# ADR-0001: Find source files through the WordPress media API; newest publication date wins

- **Status:** Accepted
- **Date:** 2026-09-23

## Context
The Ministry of Funds and Regional Policy publishes a monthly XLSX list of open calls on
`funduszeeuropejskie.gov.pl`. The file names follow no stable pattern:

- `maj.xlsx`, `maj-1.xlsx`, `maj-2.xlsx`
- `czerwiec_do-publikacji.xlsx`
- `KWIECIENwersja2.xlsx`
- the August file exists in **two folders under the same name**.

Corrections are uploaded as **new files under new names**, not as overwrites. The old URL
never changes, so watching it shows nothing.

## Decision
Discover files through `GET /wp-json/wp/v2/media?search=NABORY_Krajowe`. Only `GET`
requests are sent. The version with the **most recent publication date** is authoritative;
the file name is never used to decide which version is newest.

## Alternatives considered
- **A.** Build the URL from a naming pattern.
- **B.** Scrape download links from the HTML page.
- **C.** Query the WordPress media API.

## Prediction (written before measuring)
None recorded.

## Measurement
Measured 2026-09-23:

| method | files found |
|---|---|
| guessing URLs from the pattern | 3 |
| WordPress media API | **17** (July 2025 – August 2026), each with a publication date |

## Cost of this choice
It depends on an interface the ministry never promised. It can be switched off without
notice. Only files whose name contains `NABORY_Krajowe` are found.

## Rejected — and why
- **A.** The naming pattern changed at least four times in seven months, and the approach
  misses every correction by design.
- **B.** Breaks on any redesign of the page, and the page does not expose publication dates.

The WordPress routes list `POST`, `PUT` and `DELETE` as well. That is standard WordPress,
not a vulnerability: every write goes through a permission check first
(`rest_cannot_create`, `rest_cannot_delete`). Verified in the WordPress source code, **not**
by sending write requests to the ministry's server.
