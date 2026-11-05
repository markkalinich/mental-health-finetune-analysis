---
language: en
license: mit
tags:
  - medical
  - clinical
  - classification
  - hospital-in-the-home
  - HITH
  - Bio_ClinicalBERT
base_model: emilyalsentzer/Bio_ClinicalBERT
datasets:
  - podfastio/hith-eligibility-dataset
metrics:
  - roc_auc
  - f1
  - average_precision
pipeline_tag: text-classification
---

# Hospital-in-the-Home (HITH) Eligibility Classifier

A fine-tuned [Bio_ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT) model that predicts whether a patient is suitable for Hospital-in-the-Home care based on clinical features.

## Model Description

This model uses a **pseudo-note fusion approach** (inspired by the MEME paper) to combine structured and unstructured clinical data into a single text input for classification:

- **Presenting complaint** → text
- **Ward** → text  
- **Length of stay** → numeric, serialized to text
- **Primary diagnosis** → text
- **Nurse handover notes** → free text
- **Allied health notes** → free text

All features are serialized into a structured pseudo-note format and classified using Bio_ClinicalBERT with a classification head.

## Input Format

The model expects a single text string in pseudo-note format:

```
PRESENTING COMPLAINT: [complaint]. WARD: [ward]. LENGTH OF STAY: [days] days. PRIMARY DIAGNOSIS: [diagnosis]. NURSE HANDOVER: [nurse notes] ALLIED HEALTH: [allied health notes]
```

## Performance (Synthetic Data)

| Metric | Score |
|--------|-------|
| AUROC | 1.000 |
| AUPRC | 1.000 |
| F1 | 1.000 |

⚠️ **Note**: These results are on synthetic training data with clear class separation. Real-world performance will differ and the model should be retrained on actual clinical data before any clinical use.

## Training Details

- **Base model**: emilyalsentzer/Bio_ClinicalBERT (110M params)
- **Training data**: 2,000 synthetic clinical records
- **Train/Val/Test split**: 70/15/15
- **Max sequence length**: 512 tokens
- **Learning rate**: 2e-5
- **Batch size**: 16
- **Epochs**: 4 (early stopping, patience=3)
- **Optimizer**: AdamW with weight decay 0.01
- **Hardware**: NVIDIA T4 GPU

## Intended Use

This is a **prototype/research model** for exploring HITH eligibility prediction. It is trained on synthetic data and is **NOT suitable for clinical decision-making** without:

1. Retraining on real clinical data
2. Extensive clinical validation
3. Regulatory approval
4. Integration with clinical governance frameworks

## Key Features (SHAP Analysis from XGBoost baseline)

The most predictive features identified by SHAP analysis:
- **Pro-HITH**: "stable", "improving", "drinking", "mobilising", "independent", "cellulitis"
- **Anti-HITH**: "cardiac monitoring", "ICU", "ventilated", "sedated", "high acuity", "bed rest"

## Two-Model System

This repository contains the ClinicalBERT model. A companion XGBoost + TF-IDF baseline model is also available, providing:
- Faster inference
- Better interpretability via SHAP feature importance
- Comparable performance on this task

## Citation

If you use this model, please cite:
- Bio_ClinicalBERT: Alsentzer et al. (2019) "Publicly Available Clinical BERT Embeddings"
- MEME approach: Yang et al. (2024) "MEME: Machine Learning Enhanced Medical Embeddings for ED Disposition Prediction"
