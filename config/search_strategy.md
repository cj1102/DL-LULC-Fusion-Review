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

## Required corpus-freeze record

Before public release, create a UT-level file containing the complete 261-record
corpus and record:

- exact retrieval date and local time;
- query copied directly from WoS;
- selected timespan and all active filters;
- raw result count before each filter;
- export batch names if more than one export was needed;
- WoS accession number (`UT`) for every included and excluded record;
- treatment of Early Access, retracted publications, combined document types, and
  records whose publication year changes after indexing.

Do not infer the frozen corpus merely by subtracting categories from the currently
available 266-record snapshot.

