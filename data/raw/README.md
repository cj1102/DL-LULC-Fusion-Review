# Restricted source data

The complete Web of Science (WoS) tagged-text exports and the original screening
workbook are retained in the authors' private research archive and are not
redistributed in this public repository. WoS records may contain licensed
abstracts, cited references, and database-added metadata.

The public reproducibility package provides instead:

- the database, interface, field, query, time window, language, document types,
  and export format in `config/search_strategy.md`;
- a limited-metadata manifest of the 261-record analytical corpus in
  `data/processed/corpus/`;
- public identifiers and non-restricted coding fields for the 163 records with
  archived fusion assignments in `data/processed/coding/`;
- the original keyword thesauri and retained software-output tables;
- validation and table-building code; and
- an explicit record of settings and source materials that were not retained.

Researchers with authorised WoS access can rerun the documented query and freeze
their reconstruction by WoS accession number (`UT`). Because database content and
record status can change, a later rerun is not expected to reproduce the historical
result count without the original licensed snapshot.

## Retained private keyword-map inputs

The privately retained file identified by the author as the source loaded for the
full-period keyword-map workflow is:

| Archive filename | Local repository alias | Records | SHA-256 | Public file |
|---|---|---:|---|---|
| `Wos_raw_data_records_2006-2025.txt` | `data/raw/wos/wos_export_full_original.txt` | 266 | `a25e1bafad9ab8afc4b947d0591e453578730ea96bdf6c5adf217250c381ded2` | No |
| `21-25.txt` | `data/raw/wos/wos_export_period_subset_original.txt` | 210 | `0f303905703ee9335528757481d8c41da0f362b95e15231f9b7d7ba0bc283f85` | No |

Each named archive file is byte-identical to its corresponding local repository
alias. The metadata are also stored in `private_source_manifest.csv`. The
tagged-text files are excluded by `.gitignore` because they contain licensed full
records, abstracts, cited references, addresses, and database-supplied metadata.

The public file
`config/vosviewer/thesaurus_keywords_all_original.txt` is byte-identical to the
author-supplied `all_keywords(1).txt` (SHA-256
`3cff979e97e056cf3431c569e74d0bc7307569fcebde000e7f6292cb53a5712b`).
Unlike the WoS export, this author-created thesaurus is included publicly.

The public `thesaurus_keywords_2021_2025_original.txt` and
`thesaurus_keywords_2016_2020_original.txt` files are likewise byte-identical to
the author-supplied `21-25Keyword.txt` and `16-20keyword.txt`, respectively. The
2016–2020 tagged-text input has not yet been supplied, so its filename, record
count, and checksum are not entered in the manifest.

Validation of `21-25.txt` finds 210 unique records: 27 from 2021, 30 from 2022,
35 from 2023, 47 from 2024, 70 from 2025, and one from 2026; 207 records are
English and three are Chinese. These are properties of the retained historical
input and are not silently rewritten in the public provenance record.
