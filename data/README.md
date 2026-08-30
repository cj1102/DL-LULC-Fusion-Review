# Data directories

## `raw/`

The public repository contains only a README in this directory. Complete Web of
Science tagged-text exports and the original author coding workbook remain in the
authors' private archive because they contain licensed bibliographic content.
They are not required to verify the published 163-record coding-subset totals.

## `interim/`

Record-level crosswalks, screening decisions, and reviewed manual coding. Files in
this directory should make every reported denominator reproducible.

## `processed/`

Outputs supplied from bibliometric software. The suffix `_original` indicates that
the file was renamed for clarity but its content was not changed.

The `coding/` subdirectory contains the public, record-level table for the 163
archived fusion assignments, a machine-readable JSON copy, and no abstracts or
cited-reference lists.

The distinction between `raw`, `interim`, and `processed` describes provenance; it
does not imply that the current collection has passed the consistency checks in
`docs/current_data_audit.md`.

SHA-256 hashes of the public derived data, software-output, and thesaurus files are
listed in `docs/source_file_checksums.sha256` so that accidental content changes
can be detected independently of filenames. Hashes are integrity metadata, not a
substitute for source-data redistribution rights.
