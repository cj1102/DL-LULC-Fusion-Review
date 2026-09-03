# Manuscript

`main.tex` is the current revised LaTeX source. The active figures and required
local style files are included. A compiled manuscript PDF is intentionally not
tracked because the previously supplied build predates the latest source edits;
the submission PDF should be regenerated from `main.tex` before resubmission.

The source references `Figures/newplot_original_pdf_fig8.pdf`. This active asset
is the byte-identical original-PDF version selected by the author for Figure 8.
The duplicate `newplot.pdf` and the unused rasterised `newplot_300dpi.pdf` were
removed from the public working tree; their earlier versions remain recoverable
from Git history.

The bibliography remains in `interactapasample.bib`, the filename referenced by
`main.tex`. The byte-identical convenience copy `references.bib` was removed to
avoid maintaining duplicate bibliography sources.

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
