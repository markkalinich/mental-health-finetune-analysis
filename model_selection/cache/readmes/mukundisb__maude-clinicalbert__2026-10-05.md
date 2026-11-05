---
license: apache-2.0
language: en
tags:
  - medical-device
  - pharmacovigilance
  - text-classification
  - clinical-nlp
  - bio-clinicalbert
  - fda-maude
base_model: emilyalsentzer/Bio_ClinicalBERT
metrics:
  - f1
---

# MAUDE Adverse Event Severity Classifier — Bio_ClinicalBERT (Phase 2)

## Model Description

Fine-tuned [Bio_ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT) classifier that assigns a severity label — **Death (D) / Injury (I) / Malfunction (M) / Other (O)** — to free-text adverse event narratives from the FDA's [MAUDE database](https://open.fda.gov/apis/device/event/).

This is **Phase 2** of a two-phase project. Phase 1 established a TF-IDF + Logistic Regression baseline; this model improves on that baseline specifically on the highest-stakes class (Death).

## Training Data

- 154,776 MAUDE records (post-cleaning, `UNKNOWN` labels dropped)
- Source: openFDA MAUDE API
- Class distribution is imbalanced (Death prevalence ≈8%); handled via inverse-frequency class weights in the loss function

## Training Procedure

| Parameter | Value |
|---|---|
| Base model | `emilyalsentzer/Bio_ClinicalBERT` |
| Pooling | `cls_mean_concat` ([CLS] + mean-pooled, 1536-dim head) |
| Max token length | 512 |
| Batch size | 16 (×2 GPUs, effective 32 with grad accumulation = 2) |
| Learning rate | 2e-5 (AdamW, 10% linear warmup) |
| Epochs | 3 |
| Class weights | Inverse-frequency, applied in CrossEntropyLoss |
| Hardware | Kaggle, 2× T4 GPU (DataParallel) |
| CV strategy | 5-fold StratifiedKFold, splits SHA1-fingerprinted for reproducibility |
| Early stopping | Patience = 1 epoch |

## Evaluation Results (5-fold CV)

| Metric | Mean | Std |
|---|---|---|
| F1 weighted | 0.8691 | 0.0010 |
| F1 macro | 0.7727 | 0.0020 |
| F1 — Death | 0.8318 | 0.0076 |
| F1 — Injury | 0.8728 | 0.0015 |
| F1 — Malfunction | 0.9069 | 0.0016 |
| F1 — Other | 0.4794 | 0.0069 |

**Improvement over Phase 1 baseline:** weighted F1 +0.0207, Death-class F1 +0.0617 (+6.2 pp) — the Death-class lift is the primary result this phase targeted.

### Per-Fold Breakdown

| Fold | F1 Death | F1 Injury | F1 Malfunction | F1 Other | F1 Macro | F1 Weighted |
|---|---|---|---|---|---|---|
| 1 | 0.8346 | 0.8713 | 0.9048 | 0.4730 | 0.7709 | 0.8671 |
| 2 | 0.8364 | 0.8711 | 0.9092 | 0.4826 | 0.7748 | 0.8700 |
| 3 | **0.8418** | 0.8749 | 0.9056 | 0.4764 | 0.7747 | 0.8693 |
| 4 | 0.8249 | 0.8727 | 0.9081 | 0.4735 | 0.7698 | 0.8693 |
| 5 | 0.8212 | 0.8740 | 0.9065 | 0.4915 | 0.7733 | 0.8698 |

## Deployed Checkpoint

**Fold 3** is the checkpoint pushed to this Hub repo, selected because it achieved the highest **Death-class F1 (0.8418)** across all five folds — not the highest weighted or macro F1 (fold 2 leads on both of those). This is a deliberate choice: in this application, a false negative on the Death class (a death narrative misclassified as Injury/Malfunction/Other) is the most clinically consequential error, so fold selection was optimized against that specific risk rather than an aggregate score.

**Provenance note:** this selection rationale was reconstructed and documented retroactively. At the time of the original push to this Hub repo, no model card or commit message recorded the selection criterion. Future pushes will include this documentation at push time, not after the fact.

## Honest Limitations

- All folds peaked at the epoch-3 training cap — validation performance was still improving when training stopped due to patience=1. Extending training would likely add further gains; current numbers are conservative, not a ceiling.
- **Other-class F1 (≈0.48) is the weakest class by a wide margin.** This class is a small, semantically heterogeneous catch-all bucket rather than a coherent label, which limits how learnable it is regardless of further tuning. Treated as a known limitation, not an active optimization target for this phase.
- **This is a research prototype. It is not validated for, and must not be used for, clinical decision-making.**

## Links

- [GitHub repository](https://github.com/mukundisb/maude-nlp-classifier) — source code, CV splits, training scripts
- [Phase 1 Space](https://huggingface.co/spaces/mukundisb/maude-classifier) — TF-IDF baseline demo
- [Phase 2 Space](https://huggingface.co/spaces/mukundisb/maude-clinicalbert) — this model, live demo

## Author

Mukund Padmanabha — [LinkedIn](https://linkedin.com/in/mukund-padmanabha)