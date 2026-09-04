#!/usr/bin/env python3
"""Build the public 261-record screened-corpus manifest.

The manifest reconciles the 255 non-empty titles in the historical working
sheet with six documented eligible records restored after review.  It exports
only limited bibliographic metadata to the CSV/JSON manifest; the complete
screened tagged-text input is maintained separately under `data/raw/wos/`.
"""

from __future__ import annotations

import argparse
import csv
import difflib
import json
import re
import unicodedata
from pathlib import Path


RESTORED_UTS = {
    "WOS:000359245800001",
    "WOS:000801592300001",
    "WOS:001535717700001",
    "WOS:001470427000006",
    "WOS:001527641000001",
    "WOS:001571488500021",
}


def normalise_title(value: str) -> str:
    value = unicodedata.normalize("NFKC", value or "").lower()
    value = re.sub(r"^retracted\s*[:\-]?\s*", "", value)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return " ".join(value.split())


def parse_wos(path: Path) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    record: dict[str, str] = {}
    last_tag: str | None = None
    for line in path.read_text(encoding="utf-8-sig", errors="replace").splitlines():
        if line == "ER":
            if record.get("UT"):
                records.append(record)
            record = {}
            last_tag = None
            continue
        if len(line) >= 3 and line[:2].isalnum() and line[2] == " ":
            last_tag = line[:2]
            record[last_tag] = line[3:].strip()
        elif line.startswith("   ") and last_tag:
            record[last_tag] = f"{record.get(last_tag, '')} {line.strip()}".strip()
    return records


def best_record(
    title: str,
    records: list[dict[str, str]],
) -> tuple[dict[str, str], str, float]:
    key = normalise_title(title)
    by_title = {normalise_title(record.get("TI", "")): record for record in records}
    if key in by_title:
        return by_title[key], "exact_normalised_title", 1.0

    choices = list(by_title)
    candidates = difflib.get_close_matches(key, choices, n=1, cutoff=0.85)
    if not candidates:
        raise ValueError(f"No WoS title match for: {title}")
    candidate = candidates[0]
    score = difflib.SequenceMatcher(None, key, candidate).ratio()
    return by_title[candidate], "reviewed_title_variant", round(score, 4)


def make_record(
    wos: dict[str, str],
    inclusion_source: str,
    source_row: int | None,
    match_method: str,
    match_score: float | None,
) -> dict[str, object]:
    title = wos.get("TI", "")
    raw_document_type = wos.get("DT", "")
    reported_document_type_group = (
        "Proceedings Paper" if "Proceedings Paper" in raw_document_type else "Article"
    )
    return {
        "ut": wos.get("UT", ""),
        "doi": wos.get("DI", ""),
        "title": title,
        "publication_year": int(wos["PY"]) if wos.get("PY", "").isdigit() else None,
        "language": wos.get("LA", ""),
        "document_type_as_tagged_in_later_snapshot": raw_document_type,
        "reported_document_type_group": reported_document_type_group,
        "inclusion_source": inclusion_source,
        "source_workbook_row": source_row,
        "title_match_method": match_method,
        "title_match_score": match_score,
        "later_snapshot_status_note": (
            "Title is marked as retracted in the retained later WoS snapshot; "
            "the record is retained here because it is present in the historical "
            "255-title analytical working sheet."
            if title.lower().startswith("retracted")
            else ""
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--working-sheet-csv", required=True, type=Path)
    parser.add_argument("--wos", required=True, type=Path)
    parser.add_argument("--output-json", required=True, type=Path)
    parser.add_argument("--output-csv", required=True, type=Path)
    args = parser.parse_args()

    wos_records = parse_wos(args.wos)
    by_ut = {record.get("UT", ""): record for record in wos_records}
    with args.working_sheet_csv.open(encoding="utf-8-sig", newline="") as handle:
        sheet_rows = list(csv.DictReader(handle))

    output_records: list[dict[str, object]] = []
    for source_row, row in enumerate(sheet_rows, start=2):
        title = (row.get("Title") or "").strip()
        if not title:
            continue
        wos, match_method, match_score = best_record(title, wos_records)
        output_records.append(
            make_record(
                wos,
                "historical_255_title_working_sheet",
                source_row,
                match_method,
                match_score,
            )
        )

    for ut in sorted(RESTORED_UTS):
        if ut not in by_ut:
            raise ValueError(f"Restored record is absent from WoS input: {ut}")
        output_records.append(
            make_record(
                by_ut[ut],
                "documented_restored_inclusion",
                None,
                "ut_match",
                1.0,
            )
        )

    output_records.sort(
        key=lambda record: (
            record["publication_year"] or 0,
            str(record["title"]).casefold(),
            str(record["ut"]),
        )
    )
    for index, record in enumerate(output_records, start=1):
        record["corpus_sequence"] = index

    uts = [str(record["ut"]) for record in output_records]
    if len(output_records) != 261:
        raise ValueError(f"Expected 261 records, found {len(output_records)}")
    if len(set(uts)) != 261 or any(not ut for ut in uts):
        raise ValueError("The reconciled manifest must contain 261 unique UT values")
    if sum(r["inclusion_source"] == "historical_255_title_working_sheet" for r in output_records) != 255:
        raise ValueError("Expected 255 records from the historical working sheet")
    if sum(r["inclusion_source"] == "documented_restored_inclusion" for r in output_records) != 6:
        raise ValueError("Expected six restored records")

    payload = {
        "scope_note": (
            "This is the public identifier/title manifest for the 261-publication "
            "analytical corpus reported in the manuscript. It is reconstructed "
            "from the 255 non-empty titles in the historical working sheet plus "
            "six documented eligible inclusions."
        ),
        "provenance_note": (
            "The 261 records were selected by WoS accession number from the "
            "retained source export. Included records were copied verbatim to "
            "the public screened tagged-text analysis input."
        ),
        "record_count": 261,
        "composition": {
            "historical_working_sheet": 255,
            "documented_restored_inclusions": 6,
        },
        "records": output_records,
    }
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_csv.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    fieldnames = [
        "corpus_sequence",
        "ut",
        "doi",
        "title",
        "publication_year",
        "language",
        "document_type_as_tagged_in_later_snapshot",
        "reported_document_type_group",
        "inclusion_source",
        "source_workbook_row",
        "title_match_method",
        "title_match_score",
        "later_snapshot_status_note",
    ]
    with args.output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(output_records)


if __name__ == "__main__":
    main()
