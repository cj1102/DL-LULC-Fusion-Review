# Web of Science source exports

This directory is the expected local location for authorised Web of Science
tagged-text inputs. Complete full-record exports are intentionally excluded from
the public Git repository because they contain database-supplied abstracts,
cited references, addresses, and other licensed metadata.

The filenames and SHA-256 checksums of the author-retained inputs are recorded in
[`../private_source_manifest.csv`](../private_source_manifest.csv). An authorised
user may place matching exports in this directory and validate them without
changing their contents:

```bash
python3 ../../../code/validate_wos_records.py /path/to/authorised-export.txt
```

Publicly redistributable derived tables, thesauri, search instructions, and
record-level coding evidence are stored elsewhere in the repository.
