# Keyword cleaning and thesaurus protocol

## Files

The retained keyword figures use three author-created VOSviewer thesauri:

- `thesaurus_keywords_2016_2020_original.txt`
- `thesaurus_keywords_2021_2025_original.txt`
- `thesaurus_keywords_all_original.txt`

They are preserved verbatim. The full-period public analysis input is
`data/raw/wos/wos_export_screened_261.txt`; temporal analyses use the corresponding
publication-year subsets. In VOSviewer 1.6.20, the workflow is bibliographic-data
map creation, keyword co-occurrence, *All keywords*, application of the relevant
thesaurus, and export of the network or average-publication-year overlay.

## Replacement rules

The first thesaurus column is the source label and the second is the replacement.
The mappings include:

1. spelling and abbreviation normalisation, such as convolutional neural-network
   variants to `cnn`, synthetic aperture radar to `sar`, and light detection and
   ranging to `lidar`;
2. hyphenation and singular/plural normalisation; and
3. broader aggregation, such as several fusion-related expressions to `fusion`.

Because the third category is broader than lexical cleaning, it can affect node
occurrence and TLS. The maps are therefore interpreted as descriptive views under
the archived vocabulary rules, not as evidence of performance, superiority or
field-wide prevalence.

## Retained software settings

Only the visible normalisation, layout, clustering and visualisation controls in
the supplied screenshots are reported. They are listed in
`retained_network_settings.md`. No threshold, random seed or hidden advanced
setting is inferred from a screenshot that does not show it. Quantitative values
remain those reported in the manuscript and retained item tables.
