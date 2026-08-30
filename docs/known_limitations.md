# Known limitations of this working repository

1. The currently supplied WoS export is not demonstrably the frozen 261-record
   corpus reported in the manuscript.
2. The exact January 2026 retrieval date is not confirmed.
3. Full VOSviewer settings and saved network files are not yet available.
4. Original thesaurus mappings include some concept-level aggregation rather than
   only spelling and abbreviation normalisation.
5. The revised fusion-level calculation uses 131/163 (80.4%) and is explicitly
   limited to the subset with archived paper-level assignments. The supplied
   workbook contains 255 rather than 261 titles, and reconciliation identified
   seven records in the historical WoS snapshot that are absent from the working
   sheet. A complete record-level table is still required before the coding can be
   described as exhaustive for all 261 bibliometric records.
6. The current manuscript source references
   `Figures/newplot_original_pdf_fig8.pdf`, which was not present under that name
   in the supplied source directory. To permit a clean compilation, the repository
   provides a byte-identical compatibility copy of the supplied `newplot.pdf`
   under the referenced filename. The authors must still confirm that
   `newplot.pdf` is the intended archival Figure 8 asset.
7. The repository records existing outputs but does not yet contain scripts for
   regenerating every figure.
