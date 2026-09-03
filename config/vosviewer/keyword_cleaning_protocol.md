# Keyword cleaning and thesaurus protocol

## Scope

The retained keyword figures were produced with three period-specific VOSviewer
thesaurus files:

- `thesaurus_keywords_2016_2020_original.txt`
- `thesaurus_keywords_2021_2025_original.txt`
- `thesaurus_keywords_all_original.txt`

These files are preserved verbatim so that the labels and reported total link
strength values remain traceable to the figures. No post-hoc changes were applied
to the thesauri during manuscript revision.

## Full-period keyword-map processing chain

The author identified the following retained workflow for the full-period keyword
map:

1. Load the private WoS tagged-text file
   `Wos_raw_data_records_2006-2025.txt` into VOSviewer 1.6.20 using *Create a map
   based on bibliographic data*.
2. Select a co-occurrence analysis using *All keywords* as the unit of analysis.
3. Apply `all_keywords(1).txt` as the thesaurus file. The public, byte-identical
   copy is `thesaurus_keywords_all_original.txt`.
4. Apply the visible normalisation, layout, clustering, weighting, label, and line
   controls documented in `retained_network_settings.md` and the cropped evidence
   panels.
5. Export the retained keyword network figure.

The thesaurus standardises or aggregates keyword labels; it is not a
publication-screening file and does not remove bibliographic records. The private
source manifest records the exact local input filename, record count, and SHA-256
without redistributing licensed WoS full-record content.

## Temporal keyword-map processing chains

The author confirmed that the two temporal maps used the same analysis sequence
with period-specific inputs and thesauri:

- **2021–2025 panel:** load the private `21-25.txt` tagged-text file, select
  co-occurrence analysis with *All keywords*, apply `21-25Keyword.txt`, apply the
  retained VOSviewer settings, and export the average-publication-year overlay.
  The public thesaurus is the byte-identical
  `thesaurus_keywords_2021_2025_original.txt`; the private input is identified by
  checksum in `data/raw/private_source_manifest.csv`.
- **2016–2020 panel:** load the corresponding period tagged-text file, select
  co-occurrence analysis with *All keywords*, apply `16-20keyword.txt`, apply the
  retained VOSviewer settings, and export the average-publication-year overlay.
  The public thesaurus is the byte-identical
  `thesaurus_keywords_2016_2020_original.txt`. The period tagged-text file is
  pending author upload and is therefore not assigned a filename, record count,
  or checksum here.

The retained screenshots show association-strength normalisation, attraction 2,
repulsion −2, clustering resolution 1.60, minimum cluster size 1, small-cluster
merging, occurrence weights, and average-publication-year scoring for both
temporal overlays. The 2016–2020 threshold dialogue shows a minimum occurrence of
three, with 16 of 288 keywords meeting the threshold. The corresponding
2021–2025 threshold dialogue has not been supplied, so that threshold is not
reconstructed from the displayed node count.

## Applied replacement rules

The first column (`Label`) contains the source term and the second column
(`Replace by`) contains the retained term. Replacement was therefore directional,
not a symmetric similarity relation. The mappings include:

1. **Orthographic and abbreviation normalisation**, such as variants of
   `convolutional neural network` to `cnn`, `synthetic aperture radar` to `sar`,
   and `light detection and ranging` to `lidar`.
2. **Hyphenation and singular/plural normalisation**, such as `land cover
   classification` to `land-cover classification`.
3. **Broader concept aggregation**, such as `multimodal fusion` or `data fusion`
   to `fusion`. Some retained mappings are broader still, including `network` to
   `cnn` and generic `classification` to a classification label.

The third group is not purely lexical cleaning and can increase the occurrence
count and total link strength of the destination node. For this reason, the
manuscript interprets the keyword networks as descriptive maps of attention under
the archived vocabulary rules. Node size, occurrence, and total link strength are
not used as evidence of technical performance, superiority, replacement, or
prevalence across the entire LULC field.

## Reproducibility boundary

The exact mapping files and cropped visible-setting panels are public, but some
VOSviewer GUI settings and saved map/network project files were not retained. The
repository therefore distinguishes confirmed settings, settings inferred from
retained outputs, and unavailable settings. Re-running the analysis with a more
conservative thesaurus would be a new analysis and would change the published node
frequencies and total link strength values; it was not performed retrospectively.
