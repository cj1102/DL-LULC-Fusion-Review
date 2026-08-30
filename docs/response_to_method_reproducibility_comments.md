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
> Finally, the previously reported 80.9% value has been corrected to 131/163
> (80.4%). A record-level supplementary workbook now documents all 163 retained
> assignments using UT, DOI, title, publication year, retained model, dataset and
> fusion-method notes, original labels, standardised categories, and operational
> basis codes. The manuscript states that this percentage describes the archived
> coded subset and is not an exhaustive estimate for all 261 records.

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
