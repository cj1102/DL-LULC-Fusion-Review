# Restricted source data

The complete Web of Science (WoS) tagged-text exports and the original screening
workbook are retained in the authors' private research archive and are not
redistributed in this public repository. WoS records may contain licensed
abstracts, cited references, and database-added metadata.

The public reproducibility package provides instead:

- the database, interface, field, query, time window, language, document types,
  and export format in `config/search_strategy.md`;
- public identifiers and non-restricted coding fields for the 163 records with
  archived fusion assignments in `data/processed/coding/`;
- the original keyword thesauri and retained software-output tables;
- validation and table-building code; and
- an explicit record of settings and source materials that were not retained.

Researchers with authorised WoS access can rerun the documented query and freeze
their reconstruction by WoS accession number (`UT`). Because database content and
record status can change, a later rerun is not expected to reproduce the historical
result count without the original licensed snapshot.

## Retained full-period keyword-map input

The privately retained file identified by the author as the source loaded for the
full-period keyword-map workflow is:

| Archive filename | Local repository alias | Records | SHA-256 | Public file |
|---|---|---:|---|---|
| `Wos_raw_data_records_2006-2025.txt` | `data/raw/wos/wos_export_full_original.txt` | 266 | `a25e1bafad9ab8afc4b947d0591e453578730ea96bdf6c5adf217250c381ded2` | No |

The two files are byte-identical in the authors' local archive. The metadata are
also stored in `private_source_manifest.csv`. The tagged-text file is excluded by
`.gitignore` because it contains licensed full records, abstracts, cited
references, addresses, and database-supplied metadata.

The public file
`config/vosviewer/thesaurus_keywords_all_original.txt` is byte-identical to the
author-supplied `all_keywords(1).txt` (SHA-256
`3cff979e97e056cf3431c569e74d0bc7307569fcebde000e7f6292cb53a5712b`).
Unlike the WoS export, this author-created thesaurus is included publicly.
