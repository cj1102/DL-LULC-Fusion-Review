#!/usr/bin/env python3
"""Build the archived fusion-coding subset from author-supplied working files.

The script intentionally exports only the 163 rows that already contain a
fusion-level assignment. It does not infer labels for blank rows or copy WoS
abstracts/cited-reference fields into the public output.
"""

from __future__ import annotations

import argparse
import csv
import difflib
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path


BASIS = {
    "data": (
        "D",
        "Information sources are combined before learned representation extraction.",
    ),
    "feature": (
        "F",
        "Intermediate representations are combined before the final prediction.",
    ),
    "decision": (
        "C",
        "Independently produced scores, probabilities, labels, or maps are combined.",
    ),
    "hybrid": (
        "H",
        "Fusion occurs at two or more analytically distinct stages.",
    ),
}


def normalise_title(value: str) -> str:
    value = unicodedata.normalize("NFKC", value or "").lower()
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return " ".join(value.split())


def parse_wos(path: Path) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    record: dict[str, str] = {}
    last_tag: str | None = None
    for line in path.read_text(encoding="utf-8-sig", errors="replace").splitlines():
        if line == "ER":
            if record:
                records.append(record)
            record = {}
            last_tag = None
            continue
        if len(line) >= 3 and line[:2].isalpha() and line[2] == " ":
            last_tag = line[:2]
            record[last_tag] = line[3:].strip()
        elif line.startswith("   ") and last_tag:
            record[last_tag] = f"{record.get(last_tag, '')} {line.strip()}".strip()
    return records


def standardise_level(raw_label: str) -> tuple[str, str]:
    compact = re.sub(r"\s+", "", raw_label.lower())
    if compact == "feature":
        return "feature", "feature"
    if compact in {"data", "datafusion"}:
        return "data", "data"
    if compact == "decision":
        return "decision", "decision"
    if compact == "data+feature":
        return "hybrid", "data-feature"
    if compact in {"feature+decision", "featuredecision"}:
        return "hybrid", "feature-decision"
    raise ValueError(f"Unsupported fusion label: {raw_label!r}")


def best_record(
    title: str,
    by_title: dict[str, dict[str, str]],
) -> tuple[dict[str, str], str, float]:
    key = normalise_title(title)
    if key in by_title:
        return by_title[key], "exact_normalised_title", 1.0
    choices = list(by_title)
    candidates = difflib.get_close_matches(key, choices, n=1, cutoff=0.85)
    if not candidates:
        raise ValueError(f"No WoS title match for: {title}")
    candidate = candidates[0]
    score = difflib.SequenceMatcher(None, key, candidate).ratio()
    return by_title[candidate], "fuzzy_normalised_title", round(score, 4)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--coding-csv", required=True, type=Path)
    parser.add_argument("--wos", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    wos_records = parse_wos(args.wos)
    by_title = {normalise_title(record.get("TI", "")): record for record in wos_records}

    with args.coding_csv.open(encoding="utf-8-sig", newline="") as handle:
        source_rows = list(csv.DictReader(handle))

    output_records: list[dict[str, object]] = []
    for source_row, row in enumerate(source_rows, start=2):
        raw_level = (row.get("Type of fusion") or "").strip()
        if not raw_level:
            continue
        standard_level, hybrid_pattern = standardise_level(raw_level)
        wos, match_method, match_score = best_record(row.get("Title", ""), by_title)
        basis_code, basis_definition = BASIS[standard_level]
        output_records.append(
            {
                "source_workbook_row": source_row,
                "ut": wos.get("UT", ""),
                "doi": wos.get("DI", ""),
                "publication_year": int(wos["PY"]) if wos.get("PY", "").isdigit() else None,
                "title": wos.get("TI", row.get("Title", "")),
                "model_architecture": (row.get("Model") or "").strip(),
                "dataset": (row.get("DataSet") or "").strip(),
                "fusion_method_note": (row.get("Fusion method") or "").strip(),
                "original_fusion_label": raw_level,
                "standardised_fusion_level": standard_level,
                "hybrid_pattern": hybrid_pattern if standard_level == "hybrid" else "",
                "operational_basis_code": basis_code,
                "operational_basis_definition": basis_definition,
                "title_match_method": match_method,
                "title_match_score": match_score,
                "coding_status": "archived paper-level assignment",
            }
        )

    if len(output_records) != 163:
        raise ValueError(f"Expected 163 coded records, found {len(output_records)}")
    uts = [record["ut"] for record in output_records]
    if len(set(uts)) != len(uts):
        raise ValueError("Duplicate or missing UT values in coded subset")

    counts = Counter(record["standardised_fusion_level"] for record in output_records)
    patterns = Counter(
        record["hybrid_pattern"]
        for record in output_records
        if record["standardised_fusion_level"] == "hybrid"
    )
    expected = {"feature": 131, "hybrid": 18, "decision": 7, "data": 7}
    if dict(counts) != expected:
        raise ValueError(f"Unexpected category totals: {dict(counts)}")

    payload = {
        "scope_note": (
            "This file documents the 163 records with fusion-level assignments "
            "retained in the authors' working coding materials. It is not an "
            "exhaustive fusion-level assignment for all 261 bibliometric records."
        ),
        "source_note": (
            "Bibliographic identifiers were matched to the supplied WoS snapshot. "
            "Model, dataset, fusion-method, and original-label fields were "
            "transcribed from the author-supplied working coding sheet."
        ),
        "record_count": len(output_records),
        "category_counts": dict(sorted(counts.items())),
        "hybrid_pattern_counts": dict(sorted(patterns.items())),
        "feature_only_share": 131 / 163,
        "records": output_records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
