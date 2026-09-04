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
> The repository now provides the screened 261-record tagged-text input and a
> matching UT-level manifest. Cropped VOSviewer panels document only the visible
> normalisation, layout, clustering, weighting, label, and line-display controls.
> We do not infer thresholds, random seeds, or hidden advanced parameters from
> screenshots that do not display them. The reported node counts, occurrence
> values, and Total Link Strength values remain those stated in the manuscript
> and retained item tables.
>
> Keyword cleaning is now documented explicitly. The archived thesauri contain
> both lexical normalisation and broader concept aggregation. Because changing
> these mappings would alter occurrence and TLS values, the original files were
> retained verbatim and the resulting networks are interpreted descriptively
> under the archived vocabulary rules. Keyword occurrence, TLS, and co-citation
> are not treated as evidence of technical performance or replacement.
>
> Finally, we clarified the second-stage fusion-level content analysis. A record
> received a fusion-level assignment only when its abstract, keywords, dataset
> information, and model description supported reliable assignment of an explicit
> integration stage to data-, feature-, decision-, or hybrid-level fusion. The
> archived materials retain 163 such assignments. The other 98 bibliometric
> records comprise 92 working-sheet rows without a retained qualifying assignment
> and the six records restored during title-level reconciliation; no fusion
> categories were reconstructed retrospectively for the latter records. To avoid
> presenting the archived-subset percentage as if it described all 261 records, we
> removed it from the Abstract and Conclusion. A record-level workbook documents
> the 163 archived assignments using UT, DOI, title, publication year, model,
> dataset and fusion-method notes, original labels, standardised categories, and
> operational basis codes.
>
> The screened tagged-text file and limited-metadata manifest identify the same
> 261 analytical records by WoS accession number. The screened file was created
> by retaining the verified analytical UTs and omitting five records outside the
> period, language, or applied deep-learning scope. The original source archive
> was preserved separately rather than overwritten.

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

The original VOSviewer map/network project files and an editable final layout were
not retained, so enlarging every internal node label would require recalculating
the layout. We have not claimed to have done so. Instead, the revision uses the
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
> coding protocol, 261-record analytical-corpus manifest, 163-record coding
> supplement, screened 261-record tagged-text input, original keyword thesauri,
> retained item tables, software and figure manifests, data-audit notes, and
> validation code. The new section also recommends reporting public benchmark
> identifiers, geographic and temporal hold-outs, class definitions, random
> seeds, preprocessing, code and configurations, compute, per-class and
> calibration metrics, and missing-modality stress tests.
