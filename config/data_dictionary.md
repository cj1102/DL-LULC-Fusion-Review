# Data dictionary

## WoS tagged-text files

| Tag | Meaning used in this repository |
|---|---|
| `UT` | Web of Science accession number; primary cross-file record identifier |
| `TI` | Document title |
| `PY` | Publication year in the exported snapshot |
| `LA` | Language |
| `DT` | Document type as exported by WoS |
| `SO` | Source title |
| `DE` | Author keywords |
| `ID` | Keywords Plus |
| `CR` | Cited references |

## HistCite-derived tables

| Column | Meaning |
|---|---|
| `Recs` | Number of records associated with the entity; totals may exceed corpus size for multi-author, multi-institution, or multi-country records |
| `LCS` | Local citation score within the analysed collection |
| `GCS` | Global citation score reported by the source database/tool |

## VOSviewer item tables

| Column | Meaning |
|---|---|
| `occurrences` / `documents` | Item frequency in the configured analysis |
| `citations` | Citation count associated with an item where applicable |
| `total link strength` | Sum of link strengths in that particular configured network; not a performance or quality measure |

TLS values depend on corpus size, thresholding, counting, and network structure.
They should not be treated as directly comparable performance indicators across
independently constructed time-period networks.

