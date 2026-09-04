# Code

`validate_wos_records.py` reads a WoS tagged-text export and reports record, year,
language, document-type, and identifier counts. It uses only the Python standard
library and does not modify the input file.

`build_archived_coding_subset.py` reconstructs the public 163-record JSON from an
authorised local WoS export and a CSV conversion of the original private coding
workbook. It deliberately excludes rows without an archived assignment and does
not export abstracts or cited references.

`build_screened_corpus_manifest.py` reconciles the 255 non-empty titles in a CSV
conversion of the private historical working sheet with the six documented
eligible inclusions. It writes the public 261-record CSV and JSON manifests and
checks the record count, unique WoS accession numbers, and 255-plus-six
composition. The supplied private WoS file is used only to recover identifiers and
limited bibliographic metadata; it is not presented as the analytical corpus.

`validate_screened_corpus_manifest.py` validates the public manifest without
access to the private source files:

```bash
python3 code/validate_screened_corpus_manifest.py
```

`filter_wos_to_screened_corpus.py` uses the public 261-record UT manifest to
filter an authorised local WoS tagged-text snapshot. It copies the selected
records verbatim and writes a 261-record tagged-text input suitable for rerunning
bibliometric software. The generated screened input is included in this
repository at the author's request.

`validate_archived_coding_subset.py` checks the public JSON independently of the
tagged-text source:

```bash
python3 code/validate_archived_coding_subset.py
```

The check requires 163 unique UT identifiers, 131 feature-level-only, 18 hybrid,
seven data-level-only, and seven decision-level-only records; it also checks the
12 data--feature and six feature--decision hybrid patterns.

Future scripts should follow a numbered workflow and declare every input and
output path. Do not add scripts that cannot be connected to a retained manuscript
table or figure.
