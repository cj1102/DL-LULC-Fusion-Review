# Data directories

## `raw/`

This directory contains the screened 261-record WoS tagged-text input, its
checksum manifest, and documentation. The original author coding workbook remains
private; the public 163-record coding supplement is stored under `processed/`.

## `interim/`

Record-level crosswalks, screening decisions, and reviewed manual coding. Files in
this directory should make every reported denominator reproducible.

## `processed/`

Outputs supplied from bibliometric software. The suffix `_original` indicates that
the file was renamed for clarity but its content was not changed.

The `coding/` subdirectory contains the public, record-level table for the 163
archived fusion assignments, a machine-readable JSON copy, and no abstracts or
cited-reference lists.

The `corpus/` subdirectory contains the public 261-record analytical-corpus
manifest in CSV and JSON formats. It was reconciled from 255 non-empty titles in
the historical working sheet plus six documented eligible inclusions. It contains
limited bibliographic metadata and matches the 261 accession numbers in the
screened tagged-text input.

The distinction between `raw`, `interim`, and `processed` describes provenance; it
does not imply that the current collection has passed the consistency checks in
`docs/current_data_audit.md`.

SHA-256 hashes of the public derived data, software-output, and thesaurus files are
listed in `docs/source_file_checksums.sha256` so that accidental content changes
can be detected independently of filenames. Hashes are integrity metadata, not a
substitute for source-data redistribution rights.
