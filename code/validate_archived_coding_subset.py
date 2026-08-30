#!/usr/bin/env python3
"""Validate the public archived fusion-coding subset.

This check uses only the derived JSON distributed in the public repository. It
does not require access to licensed Web of Science full records.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


EXPECTED_COUNTS = {"data": 7, "decision": 7, "feature": 131, "hybrid": 18}
EXPECTED_HYBRIDS = {"data-feature": 12, "feature-decision": 6}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "json_file",
        nargs="?",
        type=Path,
        default=Path("data/processed/coding/archived_fusion_coding_subset.json"),
    )
    args = parser.parse_args()

    payload = json.loads(args.json_file.read_text(encoding="utf-8"))
    records = payload["records"]
    counts = Counter(record["standardised_fusion_level"] for record in records)
    hybrids = Counter(
        record["hybrid_pattern"]
        for record in records
        if record["standardised_fusion_level"] == "hybrid"
    )
    identifiers = [record["ut"] for record in records]

    assert len(records) == 163, f"expected 163 records, found {len(records)}"
    assert dict(sorted(counts.items())) == EXPECTED_COUNTS, counts
    assert dict(sorted(hybrids.items())) == EXPECTED_HYBRIDS, hybrids
    assert all(identifiers), "one or more records have no UT"
    assert len(identifiers) == len(set(identifiers)), "UT values are not unique"
    assert abs(payload["feature_only_share"] - 131 / 163) < 1e-12

    print("Archived coding subset validated")
    print(f"Records: {len(records)}")
    print(f"Category counts: {dict(sorted(counts.items()))}")
    print(f"Hybrid patterns: {dict(sorted(hybrids.items()))}")
    print(f"Feature-level-only share: {131 / 163:.1%}")


if __name__ == "__main__":
    main()
