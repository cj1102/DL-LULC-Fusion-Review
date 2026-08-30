# Current data audit

Audit date: 26 August 2026. This report describes files retained in the authors'
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

The numeric operation `266 - 3 Chinese - 2 retracted = 261` is not accepted as a
corpus reconstruction because it retains the 2026 record and has not been linked
to the manuscript's stated exclusion process.

### Supplied period snapshot

`data/raw/wos/wos_export_period_subset_original.txt` contains 210 unique records.
It is a UT-level subset of the 266-record file. It includes records from 2021–2026,
not exclusively 2021–2025. The 56 records found only in the full snapshot comprise
53 records from 2015–2020 and three later records carrying Early Access or
retraction-related document types.

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

The revised manuscript uses all 163 populated fusion-level rows as the technical
coding denominator. It therefore reports 131 feature-level-only studies out of
163 coded studies (80.4%), rather than the previous 80.9%. The complete
261-record corpus remains in the bibliometric analyses, whereas the other 98
records are not included in the fusion-level distribution because the original
working materials do not retain a complete auditable assignment for them. The
supplied workbook still contains only 255 titles, so the 131/163 result is now
described as a distribution within the archived coded subset rather than an
exhaustive estimate for all 261 records.

A title-level reconciliation against the supplied 266-record WoS snapshot
identified seven English records from 2006--2025 that are present in that snapshot
but absent from the 255-title working sheet. These seven records are treated as
omissions from the intermediate coding sheet; no retrospective fusion assignment
has been added from titles alone.

## HistCite and VOSviewer files

- The journal table contains 81 journal rows and its record-count column sums to
  266, consistent with the supplied full snapshot rather than a 261-record corpus.
- Author, country, and institution record-count columns are non-exclusive and may
  legitimately sum above the corpus size.
- The VOSviewer item files contain item counts and total link strength but do not
  contain sufficient edge, coordinate, cluster, and setting information to
  reconstruct all displayed networks exactly.

## Required resolution

1. Locate or reconstruct the frozen final corpus using `UT`, not title alone.
2. Explain the relationship among the 283 initial results, 266 supplied records,
   261 reported final records, and 255 workbook titles.
3. Record the handling of the 2026, non-English, Early Access, combined-type, and
   retracted records.
4. If an exhaustive record-level distribution is required, create a reviewed
   261-row fusion table and document any newly assigned records separately from the
   archived 163-record coding subset.
5. Freeze all figure inputs after the above decisions and update the manifest.
