#!/usr/bin/env python3
"""Summarise a Web of Science tagged-text export without modifying it."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path


FIELD_RE = re.compile(r"^([A-Z0-9]{2}) (.*)$")


def parse_records(path: Path) -> list[dict[str, list[str]]]:
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    records: list[dict[str, list[str]]] = []

    for block in re.split(r"\nER\s*\n", text):
        fields: dict[str, list[str]] = {}
        current_tag: str | None = None

        for line in block.splitlines():
            match = FIELD_RE.match(line)
            if match:
                current_tag = match.group(1)
                fields.setdefault(current_tag, []).append(match.group(2).strip())
            elif line.startswith("   ") and current_tag and fields[current_tag]:
                fields[current_tag][-1] += " " + line.strip()

        if fields.get("UT"):
            records.append(fields)

    return records


def value(record: dict[str, list[str]], tag: str) -> str:
    return " ".join(record.get(tag, [])).strip()


def summarise(records: list[dict[str, list[str]]]) -> dict[str, object]:
    identifiers = [value(record, "UT") for record in records]
    return {
        "records": len(records),
        "unique_ut": len(set(identifiers)),
        "duplicate_ut": len(identifiers) - len(set(identifiers)),
        "years": dict(sorted(Counter(value(r, "PY") or "[missing]" for r in records).items())),
        "languages": dict(sorted(Counter(value(r, "LA") or "[missing]" for r in records).items())),
        "document_types": dict(sorted(Counter(value(r, "DT") or "[missing]" for r in records).items())),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="WoS tagged-text export")
    parser.add_argument("--json", action="store_true", help="print machine-readable JSON")
    args = parser.parse_args()

    report = summarise(parse_records(args.input))
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return

    print(f"File: {args.input}")
    print(f"Records: {report['records']}")
    print(f"Unique UT: {report['unique_ut']}")
    print(f"Duplicate UT: {report['duplicate_ut']}")
    for heading, key in (
        ("Years", "years"),
        ("Languages", "languages"),
        ("Document types", "document_types"),
    ):
        print(f"\n{heading}:")
        for label, count in report[key].items():
            print(f"  {label}: {count}")


if __name__ == "__main__":
    main()

