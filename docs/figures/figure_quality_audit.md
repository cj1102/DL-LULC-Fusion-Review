# Figure readability and resolution audit

The retained keyword and co-citation figures were inspected at source-file level.

| Asset | Retained format | Source characteristics | Manuscript treatment |
|---|---|---|---|
| `picture_8.pdf` | PDF containing a 12016 × 3540 raster image | Approximately 1677 ppi at the PDF page size | Split into two enlarged temporal panels without changing nodes, TLS, or clustering |
| `new_all.pdf` | Predominantly vector PDF | Text and network geometry remain scalable | Displayed at 0.98 line width; caption explains selective label display |
| `picture_9.pdf` | PDF containing a 6008 × 3540 raster image | Approximately 838 ppi | Displayed at 0.98 line width; caption defines node, cluster, and link meanings |
| `new_Relitu.pdf` | PDF containing a 6008 × 3540 raster image | Approximately 727 ppi | Displayed at full column width |

The files exceed a 300 ppi raster target or retain vector geometry. The remaining
readability constraint is label density, not source resolution. To preserve the
reported networks, the revision increases effective display size and documents
selective label display rather than recalculating the maps or claiming that the
internal VOSviewer font settings were changed.
