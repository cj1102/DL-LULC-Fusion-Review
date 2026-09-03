# Deep learning and multi-level fusion for LULC classification

This public companion repository contains the manuscript source and the available
reproducibility materials for:

> *Deep learning and multi-level fusion for land-use and land-cover
> classification: Technological evolution and future directions*

The repository separates derived software outputs, method settings, manuscript
files, validation code, and materials that still require verification. Complete
Web of Science full-record exports are intentionally not redistributed.

## Current status

The manuscript reports a final corpus of 261 publications retrieved from the Web
of Science Core Collection (WoSCC) for 2006–2025. The retained working materials
contain archived paper-level fusion assignments for 163 records:

- 131 feature-level only;
- 18 hybrid, comprising 12 data–feature and six feature–decision records;
- seven data-level only; and
- seven decision-level only.

The corpus count is reconciled at title level as the 255 publications in the
intermediate working sheet plus six eligible publications restored from seven
candidate omissions, giving `255 + 6 = 261`. The excluded candidate used fixed,
non-learned convolutional kernels and explicitly avoided network training, so it
did not meet the applied deep-learning scope. The record-level decisions are
listed in [`docs/coding_sheet_omissions.md`](docs/coding_sheet_omissions.md).

The retained working materials contain 163 assignments from a separate,
second-stage fusion-content analysis associated with the 261-record bibliometric
corpus. An assignment was retained only when the abstract, keywords, dataset
information, and model description supported a reliable classification of an
explicit data-, feature-, decision-, or hybrid-level fusion operation. The other
98 records remained in the bibliometric corpus but are outside this archived
assigned subset: 92 are unassigned rows in the 255-title working sheet and six
are the restored bibliometric records for which no fusion category was created
retrospectively.

The record-level source for the 163 category assignments is available as
[`archived_fusion_coding_subset.xlsx`](data/processed/coding/archived_fusion_coding_subset.xlsx),
with a machine-readable JSON counterpart and a standard-library validation/build
script. The table includes UT, DOI, title, publication year, retained model,
dataset and fusion-method notes, original labels, standardised categories, and
operational basis codes. This is a criterion-defined analytical subset, not a
random sample. The table does not assign a fusion level to the other 98
bibliometric records, and its category totals are not presented as a fusion-level
distribution for the complete corpus.

The six restored bibliometric records were not assigned fusion categories
retrospectively. Accordingly, the 98 records outside the archived 163-record
fusion-level subset consist of the 92 blank rows in the intermediate sheet plus
these six restored records; the archived category totals remain unchanged.

These points are recorded in [`docs/current_data_audit.md`](docs/current_data_audit.md).
They are verification tasks, not corrections made to the authors' data.

## Repository structure

```text
manuscript/       Current LaTeX source and active figures
data/raw/         Public README only; licensed source exports remain private
data/interim/     Templates for future screening and reviewed coding
data/processed/   Supplied HistCite and VOSviewer outputs
config/           Search, coding, software, and VOSviewer documentation
code/             Validation utilities and future analysis scripts
figures/          Figure provenance and reproduction manifest
docs/             Audit findings, limitations, and reproducibility checklist
```

## Search strategy reported in the manuscript

- Database: Web of Science Core Collection
- Interface: Advanced Search
- Field: Topic (`TS`)
- Index coverage: the default WoSCC coverage available through the authors'
  institutional subscription; no individual citation index was manually selected
- Period: 2006–2025
- Language: English
- Document types: Article and Proceedings Paper
- Export: plain text, Full Record and Cited References
- Retrieval date: January 2026; approximately 10 January was recalled, but the
  exact day was not retained and is therefore not reported as certain

```text
TS=(("ensemble" OR "fusion") AND
    ("land use classification" OR "land cover classification" OR
     "land use recognition" OR "land cover recognition" OR
     "land use detection" OR "land cover detection") AND
    ("deep learning"))
```

The manuscript reports 283 initial records, followed by exclusion of two
non-English records and 20 records outside the eligible document types, yielding
the original final corpus of 261 publications. This completed screening flow
defines the denominator used in the manuscript and response letter. The retained
266-record WoS file is a later archival snapshot documented for provenance; it
does not replace or revise the screened 261-publication corpus. See
[`config/search_strategy.md`](config/search_strategy.md).

## Reproduction workflow

1. Rerun the documented WoS query under an authorised institutional subscription.
2. Freeze any reconstructed corpus by Web of Science accession number (`UT`).
3. Record every exclusion in `data/interim/screening_log_template.csv`.
4. Review or extend fusion-level coding using
   `data/interim/fusion_coding_reviewed_template.csv` and the documented protocol.
5. Use the archived thesauri and
   [`retained_network_settings.md`](config/vosviewer/retained_network_settings.md)
   to distinguish confirmed settings from unavailable GUI values.
6. Link each manuscript figure to its input, software or script, settings, and
   output in `figures/figure_manifest.csv`.

Authorised users who create their own local WoS tagged-text export can inspect it
without changing it:

```bash
python3 code/validate_wos_records.py \
  /path/to/authorised-wos-export.txt
```

## Software information

VOSviewer 1.6.20 is confirmed from the supplied application information. Exact
versions of CiteSpace, HistCite, Bibliometrix, R, and Python used for the manuscript
analysis remain to be recorded in
[`config/software_versions.md`](config/software_versions.md).

## VOSviewer materials

The supplied keyword and author tables report item-level counts and total link
strength. Two cropped screenshots document the visible normalisation, layout,
clustering, weighting, label, and line-display controls for the represented
keyword-map configuration. They do not establish all network edges, coordinates,
counting methods, thresholds, hidden advanced parameters, or saved project files.
Confirmed, output-inferred, and unavailable settings are reported in
[`retained_network_settings.md`](config/vosviewer/retained_network_settings.md).
The corresponding unedited screenshots are archived in
[`config/vosviewer/evidence`](config/vosviewer/evidence/).

The original thesauri are preserved verbatim. Some replacements merge related but
non-equivalent concepts (for example, `network` into `cnn`, or `multimodal fusion`
into `fusion`). Their use and limitations are documented in
[`keyword_cleaning_protocol.md`](config/vosviewer/keyword_cleaning_protocol.md).
No keyword frequencies were recomputed during revision.

For the retained full-period keyword map, the documented chain is: private WoS
tagged-text input → VOSviewer co-occurrence analysis using *All keywords* → the
public full-period thesaurus → the archived visible settings → exported network
figure. The restricted input is identified by record count and SHA-256 in
[`data/raw/private_source_manifest.csv`](data/raw/private_source_manifest.csv),
without republishing the licensed full records.

## Data access and licensing

Complete WoS exports, abstracts, and cited-reference records are not included in
this public repository because their redistribution is governed by the database
licence. The public package instead provides the search strategy, record
identifiers for the archived coded subset, derived tables, protocols, validation
code, and figures. Licensing boundaries are documented in
[`docs/licensing.md`](docs/licensing.md); code is covered by the MIT `LICENSE`.

## Citation

Preliminary citation metadata are provided in [`CITATION.cff`](CITATION.cff).
Version and DOI information should be added only when the reviewed replication
package is released.
