# Source data

The analysis input is
[`wos_export_screened_261.txt`](wos/wos_export_screened_261.txt). It contains 261
unique Web of Science accession numbers (`UT`) from 2015--2025, all recorded as
English and within the retained Article/Proceedings Paper grouping used in the
manuscript.

The file was created by matching the verified 261-record corpus manifest against
the retained WoS export and copying the selected records verbatim. Five records
outside the analytical corpus were omitted: three Chinese-language records, one
2026 record, and one English 2022 record whose fixed, non-learned convolutional
kernels did not satisfy the applied deep-learning scope. The original export is
preserved separately in the authors' local archive.

The input can be checked with:

```bash
python3 code/validate_wos_records.py data/raw/wos/wos_export_screened_261.txt
```

Its record count and SHA-256 checksum are stored in
[`private_source_manifest.csv`](private_source_manifest.csv). The original
screening workbook is not public; a limited, auditable coding supplement is
provided under `data/processed/coding/`.
