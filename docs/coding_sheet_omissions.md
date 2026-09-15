# Reconciliation of records omitted from the intermediate coding sheet

Comparison of the historical Web of Science snapshot with the 255-title working
coding sheet identified seven candidate records from 2006--2025 that were absent
from the intermediate sheet. Eligibility was then checked against the stated
scope: English-language Articles or Proceeding Papers that apply a deep-learning
method to the retrieved LULC-classification intersection. Six records satisfied
these criteria and were restored to the bibliometric corpus. One record was not
restored because its abstract explicitly describes fixed, pre-determined
convolutional kernels and avoidance of network training rather than an applied
deep-learning model. The reconciliation is therefore `255 + 6 = 261`.

| UT | Year | Decision | Title | Decision basis |
|---|---:|---|---|---|
| WOS:000359245800001 | 2015 | Include | Urban Land Use and Land Cover Classification Using Remotely Sensed SAR Data through Deep Belief Networks | Applies a deep belief network to LULC classification. |
| WOS:000801592300001 | 2022 | Include | AGFP-Net: Attentive geometric feature pyramid network for land cover classification using airborne multispectral LiDAR data | Reports a point-wise deep-learning method for land-cover classification. |
| WOS:000781895600023 | 2022 | Exclude | Two-step discriminant analysis based multi-view polarimetric SAR image classification with high confidence | Uses fixed, non-learned convolutional kernels and explicitly avoids network training; deep learning is discussed as background rather than used as the study method. |
| WOS:001535717700001 | 2025 | Include | AFNE-Net: Semantic Segmentation of Remote Sensing Images via Attention-Based Feature Fusion and Neighborhood Feature Enhancement | Applies a deep attention and feature-fusion network to remote-sensing semantic classification. |
| WOS:001470427000006 | 2025 | Include | HCAFNet: Hierarchical Cross-Modal Attention Fusion Network for HSI and LiDAR Joint Classification | Applies a deep cross-modal attention network to joint HSI--LiDAR land-cover classification. |
| WOS:001527641000001 | 2025 | Include | Multi-Scale Context Enhancement Network with Local-Global Synergy Modeling Strategy for Semantic Segmentation on Remote Sensing Images | Applies a Vision Mamba and cross-attention network to land-cover-related remote-sensing segmentation. |
| WOS:001571488500021 | 2025 | Include | Multilevel Differential Aggregation With Gated Discrimination Network for Hyperspectral-LiDAR Joint Land Cover Classification | Applies a deep gated multimodal network to HSI--LiDAR land-cover classification. |

The six restored records complete the current reconciled 261-record list. They
were not assigned fusion categories retrospectively, so the archived 163-record
fusion-coding subset and its reported category totals remain unchanged.

## Record-level verification

The current list was established by checking titles and then linking each record
to its unique Web of Science accession number (UT), rather than by matching a
total count alone. The six steps are:

| Step | Procedure and evidence |
|---|---|
| 1. Intermediate sheet | Retain 255 non-empty, unique titles from the working sheet. |
| 2. Candidate omissions | Compare these titles with the retained WoS records and identify seven candidate omissions. |
| 3. Eligibility decisions | Include six candidates under the documented decisions above and exclude the fixed, non-learned convolutional-kernel study: 255 + 6 = 261. |
| 4. Record manifest | Link each included title to UT, DOI, publication year and inclusion source. |
| 5. Public input | Extract the records matching those 261 UTs from the retained export; do not remove arbitrary records to reach a target count. |
| 6. Identity check | Verify 261 manifest rows, 261 public input records, 261 unique UTs in each, and identical UT sets with no duplicates or missing records. |

The check was repeated on 10 September 2026. Record counts and file
SHA-256 values are recorded in
[the machine-readable verification](corpus_validation_20260910.json). The
[manifest](../data/processed/corpus/screened_corpus_261_manifest.csv) and
[public WoS input](../data/raw/wos/wos_export_screened_261.txt) therefore agree
at record-identity level.

The `283 → 281 → 261` sequence reports the screening described in the manuscript.
The `255 + 6` account documents the later reconciliation of retained working
materials.
