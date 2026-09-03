# Data directories

## `raw/`

The public repository contains documentation and a private-source manifest in
this directory, but not the complete Web of Science tagged-text exports or the
original author coding workbook. Those files remain in the authors' private
archive because they contain licensed bibliographic content. They are not
required to verify the archived 163-record coding-subset totals.

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
limited bibliographic metadata only and must not be confused with the separately
retained 266-record WoS archival snapshot.

The distinction between `raw`, `interim`, and `processed` describes provenance; it
does not imply that the current collection has passed the consistency checks in
`docs/current_data_audit.md`.

SHA-256 hashes of the public derived data, software-output, and thesaurus files are
listed in `docs/source_file_checksums.sha256` so that accidental content changes
can be detected independently of filenames. Hashes are integrity metadata, not a
substitute for source-data redistribution rights.
