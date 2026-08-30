# Code

`validate_wos_records.py` reads a WoS tagged-text export and reports record, year,
language, document-type, and identifier counts. It uses only the Python standard
library and does not modify the input file.

`build_archived_coding_subset.py` reconstructs the public 163-record JSON from an
authorised local WoS export and a CSV conversion of the original private coding
workbook. It deliberately excludes rows without an archived assignment and does
not export abstracts or cited references.

`validate_archived_coding_subset.py` checks the public JSON without requiring
licensed source data:

```bash
python3 code/validate_archived_coding_subset.py
```

The check requires 163 unique UT identifiers, 131 feature-level-only, 18 hybrid,
seven data-level-only, and seven decision-level-only records; it also checks the
12 data--feature and six feature--decision hybrid patterns.

Future scripts should follow a numbered workflow and declare every input and
output path. Do not add scripts that cannot be connected to a retained manuscript
table or figure.
