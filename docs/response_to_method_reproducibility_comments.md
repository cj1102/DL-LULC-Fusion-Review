# Draft responses: bibliometric methods, figures, and open science

## Reviewer 3, Comment 1

> **Response:** We agree that the original search design cannot demonstrate that
> fusion has become dominant across the broader LULC field, because both
> `fusion/ensemble` and `deep learning` were mandatory components of the
> search query. We have therefore removed statements suggesting field-wide
> methodological replacement, dominance, or prevalence. The revised Abstract,
> Results, and Conclusion now interpret the observed increase only as growing
> publication activity and research attention within the predefined intersection
> of deep learning, multi-source fusion, and LULC classification. We explicitly
> state that the analysed corpus does not estimate the share of fusion research in
> the broader LULC literature.

## Reviewer 1, Comment 2 / Reviewer 3, Comment 3

> **Response:** Thank you for requesting a more rigorous and reproducible account
> of the bibliometric workflow. We expanded the Methods section to report the
> database, Advanced Search interface, Topic (`TS`) field, the fields searched by
> `TS`, the default WoS Core Collection index coverage, the complete Boolean
> query, period, language and document-type criteria, export format, screening
> counts, and duplicate-handling rule. The workflow figure now reports the search
> and screening stages. We also identify VOSviewer version 1.6.20 and archive the
> exact period-specific and full-period keyword thesaurus files.
>
> The revision distinguishes settings that are confirmed from those inferred from
> retained outputs. The retained 2016–2020 and full-period keyword item tables
> contain 16 and 162 items, respectively, with a minimum retained occurrence of
> three, which is consistent with an occurrence threshold of three. The original
> counting method, normalisation choice, layout seed, attraction/repulsion,
> clustering resolution, and saved map/network project files were not retained.
> We therefore report these values as unavailable rather than reconstructing them
> retrospectively, and we no longer claim exact graphical reproducibility.
>
> Keyword cleaning is now documented explicitly. The archived thesauri contain
> both lexical normalisation and broader concept aggregation. Because changing
> these mappings would alter occurrence and TLS values, the original files were
> retained verbatim and the resulting networks are interpreted descriptively
> under the archived vocabulary rules. Keyword occurrence, TLS, and co-citation
> are not treated as evidence of technical performance or replacement.
>
> Finally, we withdrew the previously reported 80.9% value as a corpus-level
> finding. The 163 retained assignments were not produced through a prospective
> or representative sampling design. Their category counts are now reported only
> as a descriptive audit of the archived working materials and have been removed
> from the Abstract and Conclusion. A record-level supplementary workbook
> documents the retained UT, DOI, title, publication year, model, dataset and
> fusion-method notes, original labels, standardised categories, and operational
> basis codes without retrospectively assigning the other 98 records.

> During preparation of the public materials, we also found that the surviving
> WoS snapshot is not demonstrably identical to the frozen 261-record file used
> for the reported analysis. We therefore do not claim UT-level reconstruction
> from that snapshot. The repository reports the 283, 266, 261, and 255 counts as
> a documented archival discrepancy and keeps the surviving files separate. An
> exact record-level reconstruction would require a new frozen retrieval and
> exclusion crosswalk. We have disclosed this limitation rather than selecting
> records retrospectively to force the counts to agree.

## Reviewer 1, Comment 8

> **Response:** We improved readability without recalculating or altering the
> underlying bibliometric networks. The two temporal keyword networks were split
> into enlarged panels, while the full-period keyword and document co-citation
> networks are displayed at near-full text width. Captions now clarify that labels
> are displayed only for more prominent nodes to reduce overlap, while all
> retained nodes contribute to network construction. Source-file inspection shows
> that the temporal keyword, co-citation, and density PDFs contain approximately
> 1677, 838, and 727 ppi raster content at their native page sizes, respectively,
> while the full-period keyword map is predominantly vector. The original
> topology, occurrence counts, TLS, and clustering were unchanged.

The original VOSviewer map/network project files and GUI layout settings were not
retained, so enlarging every internal node label would require recalculating the
layout. We have not claimed to have done so. Instead, the revision uses the
highest-resolution retained exports, enlarges their placement in the manuscript,
and explains the software's selective label display in the captions. This closes
the resolution and placement aspects of the comment, but exact re-export with a
larger internal font remains unavailable from the archived materials.

## Reviewer 1, Comment 9

> **Response:** We edited the manuscript for British English, terminology,
> article use, number agreement, punctuation, abbreviations, units, figure and
> table references, and consistent hyphenation. We also replaced categorical
> wording such as “dominant”, “replacement”, and “superior” where it was not
> supported by the review design. The revision has been checked systematically;
> however, we do not describe this as independent professional language editing.

## Reviewer 1, Comment 10

> **Response:** We added a dedicated “Reproducibility and Open Science” section
> and a public companion repository. The repository provides the search strategy,
> coding protocol, 163-record coding supplement, original keyword thesauri,
> retained item tables, software and figure manifests, data-audit notes, and
> validation code. Complete WoS full-record exports are not redistributed because
> access and redistribution are governed by the database licence; instead, the
> repository provides executable retrieval instructions and non-restricted
> derived materials. The new section also recommends reporting public benchmark
> identifiers, geographic and temporal hold-outs, class definitions, random
> seeds, preprocessing, code and configurations, compute, per-class and
> calibration metrics, and missing-modality stress tests.
