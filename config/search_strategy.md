# Search strategy and corpus freeze

## Confirmed manuscript description

| Item | Recorded value |
|---|---|
| Database | Web of Science Core Collection |
| Interface | Advanced Search |
| Search field | Topic (`TS`) |
| Index coverage | Default WoSCC coverage available through the institutional subscription; no individual index manually selected |
| Publication period | 2006–2025 |
| Language | English |
| Eligible document types | Article and Proceedings Paper |
| Export format | Plain text; Full Record and Cited References |
| Retrieval month | January 2026 |
| Exact retrieval date | To confirm; approximately 10 January 2026 was recalled by the author |

## Boolean query

```text
TS=(("ensemble" OR "fusion") AND
    ("land use classification" OR "land cover classification" OR
     "land use recognition" OR "land cover recognition" OR
     "land use detection" OR "land cover detection") AND
    ("deep learning"))
```

## Reported screening flow

The manuscript currently reports:

1. Initial search: 283 records.
2. Two non-English records excluded: 281 records.
3. Twenty records outside Article or Proceedings Paper excluded: 261 records.
4. Final composition: 231 articles and 30 proceedings papers.

The completed screening process therefore defines the original final corpus as
261 publications. The separately retained 266-record WoS snapshot is an archival
file and is not used to revise that historical screened count.

The retained title-level materials reconcile the final count as 255 records in the
intermediate working sheet plus six eligible records restored after review of
seven candidate omissions. The remaining candidate was excluded because it used
fixed, non-learned convolutional kernels rather than an applied deep-learning
model. See `docs/coding_sheet_omissions.md` for the `UT`-level decisions.

## Additional record-level freeze recommended for future reanalysis

If the historical file is recovered or the search is rerun, create a UT-level file
containing the complete 261-record corpus and record:

- exact retrieval date and local time;
- query copied directly from WoS;
- selected timespan and all active filters;
- raw result count before each filter;
- export batch names if more than one export was needed;
- WoS accession number (`UT`) for every included and excluded record;
- treatment of Early Access, retracted publications, combined document types, and
  records whose publication year changes after indexing.

Do not attempt to replace the author-confirmed screening flow by subtracting
categories retrospectively from the currently retained 266-record snapshot. A
future crosswalk would strengthen UT-level traceability, but it would not redefine
the reported final denominator of 261 publications.
