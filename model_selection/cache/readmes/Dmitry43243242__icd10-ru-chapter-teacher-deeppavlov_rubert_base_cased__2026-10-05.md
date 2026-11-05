---
language: ru
library_name: transformers
tags:
- text-classification
- icd10
- medical
- knowledge-distillation-teacher
---

# ICD-10 Russian Chapter Teacher: DeepPavlov/rubert-base-cased

Fine-tuned BERT-family teacher model for Russian ICD-10 chapter/group prediction.
This model is exported from `train_extended_models.ipynb` as teacher #5 of top-5, selected by validation Top-3 accuracy.

- Base model: `DeepPavlov/rubert-base-cased`
- Repo: `Dmitry43243242/icd10-ru-chapter-teacher-deeppavlov_rubert_base_cased`
- Labels: ICD-10 chapter letters, excluding U
- Intended use: teacher model for knowledge distillation and top-3 decision support

## Metrics

| Split | Top-1 | Top-3 | F1 macro | F1 weighted |
|---|---:|---:|---:|---:|
| Validation | 0.6851 | 0.8575 | 0.4099 | 0.6818 |
| Test | 0.6875 | 0.8724 | 0.3695 | 0.6867 |

This is a decision-support model, not an automatic diagnosis system.
