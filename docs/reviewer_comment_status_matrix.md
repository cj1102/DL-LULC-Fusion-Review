# Reviewer-comment status matrix

This matrix records how each reviewer comment has been addressed in the revised
manuscript and response letter. “Addressed” means that the scientific or
editorial issue has been dealt with through revision, correction, narrowed
inference, additional supporting evidence, or an explicit methodological
boundary. It does not imply that unavailable historical software projects or
settings have been reconstructed.

## Referee 1

| Comment | Status | Revision and location | Remaining limitation or response rationale |
|---|---|---|---|
| 1. Add recent 2024--2026 studies | Addressed | Introduction; *Learning Strategies Beyond Architecture Design*; *Remote Sensing Foundation Models and Multimodal Pre-training*; *Challenges*. The revision discusses crowdsourced geographic information, lightweight models, wetland classification, UAV localisation, SAR applications, physical--data-driven retrieval, and polarisation imaging. | The 2026 papers are identified as narrative updates after the 2006--2025 search window and are not included in bibliometric counts. Adjacent detection/localisation papers are presented as transferable directions, not direct LULC-classification evidence. |
| 2. Expand bibliometric methods and add a flow diagram | Addressed | *Data Collection* and *Research Framework and Methodology* now report WoSCC Advanced Search, Topic (`TS`), default subscription index coverage, full Boolean query, period, language, document types, export format, screening counts, duplicate rule, keyword thesauri, VOSviewer 1.6.20, retained threshold evidence, and unavailable settings. Two cropped panels in the repository document the visible controls for the represented keyword-map configuration. The workflow figure reports 283 to 281 to the original screened corpus of 261. The separately retained 266-record snapshot is documented as an archival file and does not revise this denominator. | The exact retrieval day, a record-by-record 261-item UT manifest, the counting method, thresholds for every map, hidden advanced parameters, manuscript-compatible full-period and co-citation GUI records, and saved map/network projects are not included in the retained materials. The screening total and final denominator are nevertheless reported consistently; a recovered manifest would add UT-level traceability rather than change the corpus size. |
| 3. Replace descriptive architecture summary with critical analysis | Addressed | CNN, Transformer, attention, Mamba, data-, feature-, and decision-level sections now compare inductive bias, data needs, computation, alignment, missing modalities, calibration, evaluation leakage, and appropriate use conditions. | Conclusions remain conditional because the reviewed studies use heterogeneous datasets and protocols. |
| 4. Expand foundation models | Addressed | Dedicated *Remote Sensing Foundation Models and Multimodal Pre-training* subsection discusses SatMAE, RemoteCLIP, foundation-model adaptation, multimodal fine-tuning, transfer, geographic bias, compute, and pretraining/evaluation leakage. | The section does not rank models across incomparable benchmarks. |
| 5. Add fusion-level comparison | Addressed | Table *Conditional design patterns and minimum evaluation evidence for multimodal LULC fusion levels* compares integration requirements, representative complexity, scalability, failure modes, evaluation evidence, and suitable conditions, with supporting citations. | Cross-paper accuracy and runtime values were not pooled because datasets, resolutions, hardware, training budgets, and splits differ; presenting them as directly comparable would be misleading. |
| 6. Strengthen conclusion and recommendations | Addressed | Conclusion recommends geographically and temporally disjoint evaluation, uncertainty-aware learning, domain adaptation/generalisation, continual learning, explainable interaction, standardised missing-modality tests, foundation-model auditing, and transparent comparisons. | Recommendations are framed as research priorities, not performance predictions. |
| 7. Use terminology consistently | Addressed | The manuscript uses *LULC classification* consistently and explicitly distinguishes multi-source fusion, multimodal learning, foundation models, vision--language models, and remote sensing foundation models. | Bibliographic titles are preserved verbatim. |
| 8. Improve figure readability and resolution | Addressed | Temporal keyword networks are shown as enlarged panels; the overall keyword and co-citation maps use near-full text width; captions explain selective label display; the retained keyword/co-citation exports have been audited for native resolution. Cropped panels document the visible keyword display controls. | Original VOSviewer project files and an editable final layout were not retained, so every internal label cannot be enlarged without recalculating the networks. The original topology and quantitative values were preserved. Several non-network line-art figures remain raster and should ideally be regenerated as vector or at least 600 ppi before final submission. |
| 9. English editing | Addressed | British spelling, grammar, number agreement, punctuation, abbreviations, units, captions, and conditional scientific wording were reviewed throughout the LaTeX source. | This was a systematic author-side edit, not certification by an independent professional language-editing service. |
| 10. Reproducibility and open science | Addressed | A dedicated section links to the public repository and discusses benchmarks, code/configuration, spatial and temporal hold-outs, seeds, preprocessing, compute, per-class/calibration metrics, and missing-modality tests. | Licensed complete WoS full records are not publicly redistributed; query instructions, identifiers in permitted derived tables, thesauri, settings records, audit notes, and validation code are provided instead. |

## Referee 2

| Comment | Status | Revision and location | Remaining limitation or response rationale |
|---|---|---|---|
| Temper claims about Mamba | Addressed | Mamba is described as promising but insufficiently validated; theoretical sequence-scaling properties are separated from empirical evidence in 2D, multimodal, cross-region, and long-term LULC settings. | No accuracy--efficiency breakthrough is claimed. |
| Add real-world data, imbalance, temporal mismatch, and domain-shift challenges | Addressed | Dedicated data- and algorithm-level challenge subsections discuss source quality, registration, asynchronous acquisition, class imbalance, taxonomy inconsistency, benchmark representativeness, domain shift, uncertainty, efficiency, and deployment. | The review recommends evaluation protocols rather than inferring operational robustness from small benchmarks. |
| Cover learning strategies beyond architectures | Addressed | Dedicated subsection covers self-supervised and semi-supervised learning, domain adaptation/generalisation, class-aware learning, uncertainty calibration, missing/corrupted modalities, and compute-aware comparison. | — |
| Unify LULC terminology | Addressed | LULCC, LUCC simulation, mapping, and classification are no longer treated as interchangeable in the authors' prose. | Verbatim titles in references are not rewritten. |
| Add Table 1 caption | Addressed | Table 1 is captioned *Literature search strategy and Boolean query*. | — |
| Restore/correct Figure 2 | Addressed | The yearly output figure is present and explicitly covers 2015--2025, with zero-count 2006--2014 years explained in the text and caption. | — |
| Add benchmark-table caption | Addressed | The benchmark table is captioned *Technical specifications of representative multimodal benchmark datasets used in LULC classification*. | — |
| Correct Simonyan citation | Addressed | The text uses “Simonyan and Zisserman”; the bibliography lists both authors consistently. | — |

## Referee 3

| Comment | Status | Revision and location | Remaining limitation or response rationale |
|---|---|---|---|
| 1. Search design cannot prove field-wide replacement or dominance | Addressed | Abstract, Introduction, Results, keyword analysis, and Conclusion restrict inference to the predefined intersection of deep learning, fusion, and LULC classification. They explicitly state that the corpus cannot estimate whether fusion is mainstream in the broader field. | A no-fusion LULC comparison corpus was not constructed; the corresponding field-wide claim was withdrawn rather than defended. |
| 2. Classification, change detection, and simulation are distinct | Addressed | Scope and terminology are standardised to LULC classification; multi-source fusion and multimodal learning are separately defined. | Adjacent tasks are cited only when their potential transfer is explicitly qualified. |
| 3. Missing fields, screening, cleaning, parameters, and 80.9% coding basis | Addressed | WoSCC interface/field/default coverage, query, filters, export, screening, duplicate rule, keyword cleaning, affiliation-name check, VOSviewer version and retained threshold evidence are now reported. Cropped panels document visible controls for the represented keyword-map configuration. The manuscript explains that 163 records form the explicit fusion-level subset, and a record-level supplement documents those assignments. The bibliometric denominator is reconciled at title level as 255 working-sheet records plus six eligible inclusions selected from seven candidate omissions, giving 261; the seventh candidate and its exclusion basis are documented. The eligible-subset percentage has been removed from the Abstract and Conclusion. | A single 261-row UT manifest for the original 255 working-sheet records and the original counting method, thresholds for every map, hidden advanced parameters, manuscript-compatible full-period and co-citation GUI records, and saved VOSviewer projects are not available. The six restored bibliometric records were not assigned fusion categories retrospectively, so the archived 163-record category totals remain unchanged. |
| 4. Keywords/citations do not prove superiority or replacement | Addressed | Keyword occurrence, TLS, co-citation, TLCS, and TGCS are described as frequency/connectivity/citation indicators affected by corpus size, publication age, database coverage, and highly cited records. Performance, replacement, and national/institutional “strength” claims were removed. | — |
| 5. EuroSAT is not a multimodal fusion benchmark | Addressed | EuroSAT was removed from the multimodal benchmark table, MUUFL Gulfport was added, and Berlin/Augsburg modalities, dimensions, and resolutions were revised with source citations. | Dataset specifications should still be checked once more against the cited primary releases before submission. |

## Items that cannot be closed by wording alone

Four archival issues require new source recovery or a partial rerun rather than a
more persuasive explanation:

1. identifying the exact 261 Web of Science accession numbers if the editor asks
   for record-by-record reconstruction of the author-confirmed screened corpus;
2. reconciling institution-ranking differences between the retained CSV and the
   existing Figure 5/related prose;
3. recovering or recreating the unavailable VOSviewer project files and remaining
   GUI settings if exact layout reproduction is required; and
4. regenerating the remaining raster line-art figures from verified source data
   if strict 600-ppi/vector compliance is required.

These are reported as limitations. They should not be described as solved unless
the missing files are located or the relevant analyses are rerun.
