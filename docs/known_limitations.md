# Known limitations of this working repository

1. The currently supplied WoS export is not demonstrably the frozen 261-record
   corpus reported in the manuscript.
2. The exact January 2026 retrieval date is not confirmed.
3. Full VOSviewer settings and saved network files are not yet available.
4. Original thesaurus mappings include some concept-level aggregation rather than
   only spelling and abbreviation normalisation.
5. The authors confirm that 163 records satisfied a second-stage fusion-level
   content screen, while 98 records did not satisfy its eligibility rule. The
   surviving workbook preserves the 163 assignments but contains only 255 rather
   than 261 titles and does not provide a complete 261-row eligibility log.
   Reconciliation also identified seven records in the historical WoS snapshot
   that are absent from the working sheet.
6. The current manuscript source references
   `Figures/newplot_original_pdf_fig8.pdf`, which was not present under that name
   in the supplied source directory. To permit a clean compilation, the repository
   provides a byte-identical compatibility copy of the supplied `newplot.pdf`
   under the referenced filename. The authors must still confirm that
   `newplot.pdf` is the intended archival Figure 8 asset.
7. The repository records existing outputs but does not yet contain scripts for
   regenerating every figure.
