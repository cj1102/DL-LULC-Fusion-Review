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
