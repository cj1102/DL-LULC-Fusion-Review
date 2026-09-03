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
