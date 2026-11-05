---
language: ru
library_name: transformers
tags:
- text-classification
- icd10
- medical
- knowledge-distillation-teacher
---

# ICD-10 Russian Chapter Teacher: cointegrated/rubert-tiny2

Fine-tuned BERT-family teacher model for Russian ICD-10 chapter/group prediction.
This model is exported from `train_extended_models.ipynb` as teacher #4 of top-5, selected by validation Top-3 accuracy.

- Base model: `cointegrated/rubert-tiny2`
- Repo: `Dmitry43243242/icd10-ru-chapter-teacher-cointegrated_rubert_tiny2`
- Labels: ICD-10 chapter letters, excluding U
- Intended use: teacher model for knowledge distillation and top-3 decision support

## Metrics

| Split | Top-1 | Top-3 | F1 macro | F1 weighted |
|---|---:|---:|---:|---:|
| Validation | 0.6719 | 0.8637 | 0.3590 | 0.6638 |
| Test | 0.6866 | 0.8556 | 0.3530 | 0.6797 |

This is a decision-support model, not an automatic diagnosis system.
