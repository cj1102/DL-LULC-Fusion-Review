# Supporting methodological notes

## Keyword processing and retained settings

Keyword variants were processed with the period-specific and full-period VOSviewer thesaurus files archived with the supporting materials. These files include orthographic and abbreviation normalisation, such as variants of convolutional neural networks, LiDAR, and SAR, together with broader concept aggregation, such as mapping several fusion-related expressions to “fusion”. Because retrospectively changing these mappings would alter node frequencies and Total Link Strength (TLS), the original thesauri were retained verbatim and the networks are interpreted under their archived vocabulary rules. The retained 2016–2020 and full-period item tables contain 16 and 162 items, respectively, with a minimum retained occurrence of three. This is consistent with an occurrence threshold of three, although the complete GUI settings, counting method, layout seed, and map/network project files were not preserved. The supporting repository therefore distinguishes confirmed settings from values inferred from outputs and does not claim exact reconstruction of every network layout.

The retained screenshots document keyword-map controls: association-strength normalisation, clustering resolution 1.60 and minimum cluster size 1. These screenshots do not establish the settings used for the document co-citation network. The author subsequently confirmed that the maps displayed in Figures 9–11 all use association-strength normalisation, VOSviewer clustering resolution 1.00 and minimum cluster size 1. The current figure captions and reviewer response report these author-confirmed settings. The earlier screenshot value of 1.60 remains part of the archive and is not the resolution reported for the displayed maps.

## Document co-citation settings

The author separately confirmed on 9 September 2026 that the document co-citation network used association-strength normalisation and the VOSviewer clustering algorithm with resolution 1.00 and minimum cluster size 1. Section 4.2 reports these confirmed settings and explains reference nodes, citation counts, co-citation links, network distances and cluster colours. The co-citation settings are supported by this author confirmation; they are not inferred from the keyword-map screenshots. This confirmation does not establish unrecorded layout seeds or guarantee identical reconstruction of every network layout.

## Corpus reconciliation and fusion coding

The manuscript reports a 261-record bibliometric corpus. The current reconciled 261-record manifest and public WoS input contain the same 261 unique UTs. The retained manual working sheet contained 255 titles. Reconciliation with the archived WoS records identified seven candidate omissions: six records satisfied the stated period, language, document-type, deep-learning, and LULC-classification scope and were restored to the bibliometric corpus, whereas one record was excluded because its method used fixed, non-learned convolutional kernels and explicitly avoided network training. The retained materials therefore reconcile the final corpus as 255 + 6 = 261.

A separate second-stage manual content screen was used for fusion-level analysis. A record received a fusion-level assignment only when its abstract, author keywords, dataset information, and reported model description identified an explicit information-integration operation whose position in the classification pipeline could be assigned reliably to at least one predefined fusion level. The occurrence of the terms “fusion” or “ensemble” in a bibliographic record was not, by itself, sufficient. Data-level fusion was assigned when integration occurred before representation learning; feature-level fusion was assigned when intermediate representations were combined before prediction; and decision-level fusion was assigned when independently generated scores, probabilities, labels, or maps were aggregated. Studies reporting explicit integration at more than one stage were coded as hybrid. The archived working materials retain fusion-level assignments for 163 records.

The other 98 bibliometric records comprise 92 rows in the 255-title working sheet without a retained qualifying fusion-level assignment and the six records restored during title-level reconciliation. No fusion category was assigned retrospectively to the six restored records. All 98 continued to contribute to publication, author, journal, institution, country, keyword, and citation analyses but were not included in the fusion-level category counts. Accordingly, the 163-record result describes the archived, criterion-defined fusion-level subset rather than the distribution of fusion levels across all 261 bibliometric records.

A record-level table for the 163 records with archived fusion-level assignments is provided with the supporting materials. It reports the WoS accession number, DOI, title, publication year, model, dataset and fusion-method notes retained in the working sheet, the original fusion label, and the standardised fusion level. This table reproduces the reported category totals without retrospectively assigning a fusion level to the other 98 bibliometric records.

Before institution-level aggregation, affiliation names were manually checked for duplicate institutional identities arising from obvious spelling variants, abbreviations, and alternative name forms. No affiliation thesaurus-based merging is documented in the retained materials.

## Relationship to the manuscript

Section 2.2 retains the cleaning rules, threshold evidence boundary, fusion-coding criteria and distinction between the 261-record bibliometric corpus and the 163-record fusion subset. The detailed archival and reconciliation account is provided here and in the responses to Reviewer 1 Comment 2 and Reviewer 3 Comment 3. This documentation does not rerun the analyses. It distinguishes retained output evidence, the separately author-confirmed co-citation settings, and other historical settings that remain unavailable.

## Record-level verification

The 261-record manifest and public WoS input were checked on 10 September 2026:
both contain 261 unique UTs, and their UT sets agree without missing or duplicate
records. The list was established through title reconciliation and record-level
UT matching. The seven candidate decisions are documented in
`docs/coding_sheet_omissions.md`; the identifier check and file checksums are
recorded in `docs/corpus_validation_20260910.json`.
