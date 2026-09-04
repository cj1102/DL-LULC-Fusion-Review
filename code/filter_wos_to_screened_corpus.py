#!/usr/bin/env python3
"""Filter a retained WoS tagged-text snapshot to a public UT manifest.

The output remains a licensed private source file.  Records are copied verbatim;
only records whose Web of Science accession number occurs in the manifest are
retained.  Header and end-of-file markers are preserved.
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--wos", required=True, type=Path)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    with args.manifest.open(encoding="utf-8", newline="") as handle:
        manifest_uts = {row["ut"] for row in csv.DictReader(handle)}
    if len(manifest_uts) != 261:
        raise ValueError(f"Expected 261 unique manifest UTs, found {len(manifest_uts)}")

    source = args.wos.read_text(encoding="utf-8-sig", errors="strict")
    header_match = re.match(r"\A(FN .*?\nVR .*?\n)", source)
    if not header_match:
        raise ValueError("WoS header was not recognised")

    selected: list[tuple[str, str]] = []
    for match in re.finditer(r"(?ms)^PT .*?^ER\s*$", source):
        block = match.group(0).rstrip()
        ut_match = re.search(r"(?m)^UT (WOS:\d+)\s*$", block)
        if ut_match and ut_match.group(1) in manifest_uts:
            selected.append((ut_match.group(1), block))

    selected_uts = [ut for ut, _ in selected]
    missing = sorted(manifest_uts - set(selected_uts))
    duplicates = len(selected_uts) - len(set(selected_uts))
    if missing or duplicates or len(selected) != 261:
        raise ValueError(
            f"Filtering failed: selected={len(selected)}, missing={missing}, "
            f"duplicate_count={duplicates}"
        )

    output = header_match.group(1) + "\n\n".join(block for _, block in selected)
    output += "\n\nEF\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(output, encoding="utf-8")
    print(f"Wrote {len(selected)} records to {args.output}")


if __name__ == "__main__":
    main()
