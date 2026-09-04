# Current data audit

Audit updated: 4 September 2026.

## Analytical corpus

The repository contains
`data/raw/wos/wos_export_screened_261.txt`, a tagged-text file with 261 records
and 261 unique Web of Science accession numbers (`UT`). Its membership matches
the public 261-row CSV/JSON corpus manifest.

Validation gives the following publication-year counts: 2015: 1; 2016: 1;
2017: 3; 2018: 10; 2019: 15; 2020: 23; 2021: 27; 2022: 29; 2023: 37;
2024: 47; and 2025: 68. All 261 records are recorded as English. The manuscript's
mutually exclusive document-type grouping is reproduced as 231 Articles and 30
Proceedings Papers, with records tagged as both grouped under Proceedings Paper.

The screened file was produced by matching the verified analytical UT list to the
retained source export and copying the selected records verbatim. Five records
outside the analytical corpus were removed: three Chinese-language records, one
2026 record, and one 2022 fixed-kernel method that did not meet the applied
deep-learning scope. The retained source export remains in the authors' local
archive and was not overwritten.

## Fusion coding

The historical working sheet contains 255 non-empty unique titles and 163 retained
fusion-level assignments: 131 feature-level only, 18 hybrid, seven data-level
only, and seven decision-level only. Six eligible records restored during
title-level reconciliation complete the 261-record bibliometric corpus; no fusion
category was assigned to those six records retrospectively. Therefore, the other
98 bibliometric records comprise 92 unassigned working-sheet rows and the six
restored records.

The former percentage based on the 163 assigned records is not used as a
corpus-level estimate. The record-level assigned subset and the six-inclusion,
one-exclusion reconciliation are both included in the repository.

## VOSviewer evidence

VOSviewer version 1.6.20 and the two cropped screenshots are archived. The
screenshots document only visible normalisation, layout, clustering and display
controls. They do not establish thresholds, random seeds or hidden advanced
parameters. Reported occurrence, TLS and node values remain those stated in the
manuscript and retained item tables.
