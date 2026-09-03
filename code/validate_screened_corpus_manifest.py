#!/usr/bin/env python3
"""Validate the public 261-record analytical-corpus manifest."""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "manifest",
        nargs="?",
        type=Path,
        default=Path("data/processed/corpus/screened_corpus_261_manifest.csv"),
    )
    args = parser.parse_args()

    with args.manifest.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    uts = [row["ut"] for row in rows]
    sources = Counter(row["inclusion_source"] for row in rows)
    types = Counter(row["reported_document_type_group"] for row in rows)
    languages = Counter(row["language"] for row in rows)
    years = [int(row["publication_year"]) for row in rows]

    assert len(rows) == 261, f"expected 261 rows, found {len(rows)}"
    assert len(set(uts)) == 261 and all(uts), "UT values must be present and unique"
    assert sources == {
        "historical_255_title_working_sheet": 255,
        "documented_restored_inclusion": 6,
    }, sources
    assert types == {"Article": 231, "Proceedings Paper": 30}, types
    assert languages == {"English": 261}, languages
    assert min(years) == 2015 and max(years) == 2025, (min(years), max(years))
    print("Validated: 261 unique records; 255 + 6; 231 Articles + 30 Proceedings Papers.")


if __name__ == "__main__":
    main()
