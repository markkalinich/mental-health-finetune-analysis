---
language: ru
library_name: transformers
tags:
- text-classification
- icd10
- medical
- knowledge-distillation-teacher
---

# ICD-10 Russian Chapter Teacher: alexyalunin/RuBioBERT

Fine-tuned BERT-family teacher model for Russian ICD-10 chapter/group prediction.
This model is exported from `train_extended_models.ipynb` as teacher #2 of top-5, selected by validation Top-3 accuracy.

- Base model: `alexyalunin/RuBioBERT`
- Repo: `Dmitry43243242/icd10-ru-chapter-teacher-alexyalunin_rubiobert`
- Labels: ICD-10 chapter letters, excluding U
- Intended use: teacher model for knowledge distillation and top-3 decision support

## Metrics

| Split | Top-1 | Top-3 | F1 macro | F1 weighted |
|---|---:|---:|---:|---:|
| Validation | 0.7142 | 0.8760 | 0.4301 | 0.7083 |
| Test | 0.7377 | 0.8812 | 0.4028 | 0.7331 |

This is a decision-support model, not an automatic diagnosis system.
