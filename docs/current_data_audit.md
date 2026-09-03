# Current data audit

Audit updated: 31 August 2026. This report describes files retained in the authors'
private source archive; it does not change inclusion decisions or manuscript
results. The licensed WoS exports and original workbook named below are not
redistributed in the public repository.

## WoS exports

### Full supplied snapshot

`data/raw/wos/wos_export_full_original.txt` contains 266 records and 266 unique
`UT` identifiers.

| Field | Observed values |
|---|---|
| Publication years | 2015: 1; 2016: 1; 2017: 3; 2018: 10; 2019: 15; 2020: 23; 2021: 27; 2022: 30; 2023: 37; 2024: 48; 2025: 70; 2026: 1 |
| Languages | English: 263; Chinese: 3 |
| Document types | Article: 232; Proceedings Paper: 27; Article + Proceedings Paper: 3; Article + Early Access: 2; Article + Retracted Publication: 2 |

This 266-record file is a retained archival WoS snapshot, not the screened corpus
used to define the manuscript denominator. The author-confirmed historical
screening flow was 283 initial records, followed by exclusion of two non-English
records and 20 records outside the eligible document types, yielding the original
final corpus of 261 publications (231 Articles and 30 Proceeding Papers). The
manuscript and response letter therefore consistently use 261 as the denominator
for the reported bibliometric analyses.

The later 266-record archival snapshot is documented only for provenance. It does
not supersede the completed screening decisions and should not be used to revise
the historical corpus count. The title-level corpus reconciliation is instead
based on the 255-title working sheet and seven candidate omissions. Six candidates
met the stated scope and were restored, while one non-trained, fixed-kernel method
was excluded, giving `255 + 6 = 261`. The seven decisions and their `UT`
identifiers are documented in `docs/coding_sheet_omissions.md`.

The reconciliation has now been materialised as
`data/processed/corpus/screened_corpus_261_manifest.csv` and a parallel JSON file.
The manifest contains 261 unique `UT` identifiers: 255 matched to non-empty titles
in the historical working sheet and six matched directly by the documented
restored `UT` values. It contains 261 English-language records from 2015--2025 and
reproduces the reported mutually exclusive grouping of 231 Articles and 30
Proceedings Papers; records tagged as both Article and Proceedings Paper are
grouped under Proceedings Paper for that reported total.

On 3 September 2026, the author identified this same byte-level file as the source
loaded for the retained full-period keyword-map workflow. The associated
`all_keywords(1).txt` file is byte-identical to the public
`config/vosviewer/thesaurus_keywords_all_original.txt`. The thesaurus transforms
keyword labels but does not screen publications. Consequently, this provenance
statement identifies the retained figure input; it does not convert the 266-record
archival file into the separately reconciled 261-publication manuscript corpus.

### Supplied period snapshot

`data/raw/wos/wos_export_period_subset_original.txt` contains 210 unique records.
It is a UT-level subset of the 266-record file. It includes records from 2021–2026,
not exclusively 2021–2025. The 56 records found only in the full snapshot comprise
53 records from 2015–2020 and three later records carrying Early Access or
retraction-related document types. These two retained snapshot files are described
for archival provenance and do not redefine the screened 261-publication corpus.

On 3 September 2026, the author identified this 210-record file as the source
loaded for the later temporal keyword panel, together with `21-25Keyword.txt` as
the VOSviewer thesaurus. The latter is byte-identical to the public
`thesaurus_keywords_2021_2025_original.txt`. The source contains one 2026 record
and three Chinese-language records, so the provenance record does not describe it
as a strictly filtered 2021–2025 English subset. The 2016–2020 thesaurus has also
been verified byte for byte, while its corresponding tagged-text input remains
pending.

## Screening and fusion coding workbook

`data/raw/screening/fusion_coding_original.xls`, Sheet1, contains 255 non-empty,
unique titles. The `Type of fusion` column is populated for 163 rows:

| Original label or grouped variant | Count |
|---|---:|
| `feature` | 131 |
| `data+feature` | 12 |
| `decision` | 7 |
| `data` / `data fusion` | 7 |
| feature + decision variants | 6 |
| Blank | 92 |

The 163 populated fusion-level rows retain the assignments produced by the
second-stage content analysis: a record received an assignment only when the
abstract, keywords, dataset information, and model description supported reliable
classification of an explicit integration stage. The previous 80.9% value has
been withdrawn as a corpus-level finding. The complete 261-record corpus remains
in the bibliometric analyses, while only the archived 163-record subset is used
for the reported fusion-level category counts. Those counts remain available in
the supplement for transparency but are not presented as a distribution for all
261 records.

The surviving workbook contains 163 populated fusion labels and 92 blank rows
among 255 titles. Title-level reconciliation identified seven candidate omissions;
six were restored to the bibliometric corpus and one was excluded from the
deep-learning scope. Consequently, the final bibliometric denominator is
`255 + 6 = 261`, while the 98 records outside the archived fusion-level subset
comprise the 92 blank workbook rows and the six restored bibliometric records.
No fusion category was assigned retrospectively to those six records, and the
archived 163-record category totals were not changed.

## HistCite and VOSviewer files

- The retained journal table contains 81 journal rows and its record-count column
  sums to 266, indicating that this particular archival output is associated with
  the retained 266-record snapshot. It is preserved for provenance and must not be
  used to redefine the original screened corpus of 261 publications.
- Author, country, and institution record-count columns are non-exclusive and may
  legitimately sum above the corpus size.
- The VOSviewer item files contain item counts and total link strength but do not
  contain sufficient edge, coordinate, cluster, and setting information to
  reconstruct all displayed networks exactly.
- Two cropped screenshots document visible controls for the represented keyword
  map configuration. They do not establish the original counting method,
  thresholds for every map, hidden advanced parameters, or saved map/network
  projects. The manuscript-authoritative full-period count remains the retained
  162-item table.

## Interpretation and remaining record-level documentation

1. The reported corpus size is defined by the completed historical screening flow:
   283 initial records, 22 exclusions, and 261 included publications.
2. The retained 266-record export is a separate archival snapshot and does not
   alter the final screened count used in the manuscript.
3. The title-level composition is reconciled as the 255-title working sheet plus
   six documented inclusions selected from seven candidate omissions. The public
   261-row `UT`/title manifest provides identifier-level traceability without
   relabelling the separate 266-record archival snapshot.
4. If an exhaustive record-level fusion distribution is required, create a
   reviewed 261-row fusion table and document any newly assigned records separately
   from the archived 163-record coding subset.
5. Freeze all inputs used in any future reanalysis and update the figure manifest.
