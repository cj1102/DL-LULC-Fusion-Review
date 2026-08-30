# Manuscript

`main.tex` is the current revised LaTeX source. The active figures and required
local style files are included. A compiled manuscript PDF is intentionally not
tracked because the previously supplied build predates the latest source edits;
the submission PDF should be regenerated from `main.tex` before resubmission.

The source references `Figures/newplot_original_pdf_fig8.pdf`, but the supplied
figure directory contained `newplot.pdf` and `newplot_300dpi.pdf` instead. A
byte-identical copy of `newplot.pdf` is provided under the referenced filename so
that the source can compile. This compatibility step is documented here and the
intended archival Figure 8 asset still requires author confirmation.

The original bibliography filename was `interactapasample.bib`; a clearer copy is
also retained as `references.bib`. Update the LaTeX bibliography reference only
after confirming the intended archival source.

## Build check

The repository was compiled successfully from a clean temporary directory with
Tectonic 0.17.0 on 26 August 2026:

```bash
cd manuscript
tectonic main.tex
```

The clean build produced a 31-page A4 PDF. TeX reported non-fatal underfull and
overfull box warnings and warnings about included PDF version 1.7 versus output
PDF version 1.5; these are layout/compatibility warnings rather than missing-file
errors.
