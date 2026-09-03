# Retained VOSviewer network settings and evidence

VOSviewer version 1.6.20 is confirmed from the supplied application information.
The manuscript and retained item tables remain the authority for reported item
counts. This record distinguishes visible screenshot settings, values inferred
from retained outputs, and settings that remain unavailable.

## Visible keyword-map controls

The cropped settings screenshots show:

- association-strength normalisation;
- layout attraction 2 and repulsion −2, with default layout values disabled;
- clustering resolution 1.60, minimum cluster size 1, and merging of small
  clusters enabled;
- occurrence-based node weights;
- circular nodes, maximum label length 30, and Open Sans labels; and
- minimum displayed link strength 0, a maximum of 1000 displayed links, and
  coloured curved lines.

These values document the visible temporal keyword-map configuration represented
by the supplied panels. Display controls do not alter the occurrence or TLS
values. The panels do not establish the counting method, occurrence threshold,
hidden advanced parameters, or settings of every other network figure.

## Figure-specific retained evidence

| Manuscript figure | Analysis/unit | Threshold evidence | Thesaurus | Remaining unavailable information |
|---|---|---|---|---|
| Temporal keyword map, 2016–2020 | Keyword co-occurrence; keyword unit | Retained item table has 16 items and a minimum occurrence of 3; consistent with a threshold of 3 | `thesaurus_keywords_2016_2020_original.txt` | Counting method, hidden advanced parameters, seed, and saved project |
| Temporal keyword map, 2021–2025 | Keyword co-occurrence; keyword unit | GUI threshold and complete retained item table unavailable | `thesaurus_keywords_2021_2025_original.txt` | Threshold, counting method, hidden advanced parameters, seed, and saved project |
| Full-period keyword map | Keyword co-occurrence; keyword unit | Retained item table has 162 items and a minimum occurrence of 3; consistent with a threshold of 3 | `thesaurus_keywords_all_original.txt` | Manuscript-compatible GUI capture, counting method, hidden advanced parameters, seed, and saved project |
| Keyword density map | Same retained full-period keyword vocabulary | Uses the archived full-period visual output | `thesaurus_keywords_all_original.txt` | Exact density, layout, and saved-project settings |
| Document co-citation map | Document co-citation | Retained citation-relation table documents 797 links after its header | Not applicable | Threshold, counting method, normalisation, clustering, seed, and saved project |

## Evidence files

Only the requested cropped parameter panels are public. They are archived with
checksums in [`evidence/`](evidence/). The original full-window screenshots and
threshold dialogues are not included in the repository.

## Interpretation boundary

The repository supports auditing of the retained item counts and reported
item-level occurrence and TLS values, but it cannot recreate every network layout
pixel for pixel. The manuscript therefore avoids claims based on exact node
positions and does not treat absolute TLS values from independently constructed
temporal networks as directly comparable measures of technical development.
