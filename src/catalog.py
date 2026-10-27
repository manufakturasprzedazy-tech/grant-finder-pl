"""Floor 1 input for H0 (CAG): the raw call catalogue rendered as text.

Decision 1A (2026-09-25): raw cell values, both competitive sheets, no parsing.
Consequence we accept on purpose: a date known only to the month (display format
`mmm-yy`) becomes an ordinary date here, so that information never reaches the model.
"""
from datetime import datetime
from pathlib import Path

import openpyxl

SHEETS = ["Aktualne_konkurencyjne", "NOWE_konkurencyjne"]


def _cell(value) -> str:
    if value is None:
        return ""
    if isinstance(value, datetime):
        return value.date().isoformat()          # raw value; the display format is lost
    return str(value).replace("\n", " ").strip()


def load_catalogue(path: Path) -> str:
    workbook = openpyxl.load_workbook(path, data_only=True)
    parts = []
    for name in SHEETS:
        rows = list(workbook[name].iter_rows(values_only=True))
        width = max(i for i, c in enumerate(rows[0]) if c is not None) + 1   # drop empty trailing columns
        header = " | ".join(_cell(c) for c in rows[0][:width])
        lines = [
            f"row {number} | " + " | ".join(_cell(c) for c in row[:width])
            for number, row in enumerate(rows[1:], start=2)
            if any(c is not None for c in row)
        ]
        parts.append(f'<sheet name="{name}">\nheader | {header}\n' + "\n".join(lines) + "\n</sheet>")
    return "\n".join(parts)
