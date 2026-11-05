---
language: ru
library_name: transformers
tags:
- text-classification
- icd10
- medical
- knowledge-distillation-teacher
---

# ICD-10 Russian Chapter Teacher: alexyalunin/RuBioRoBERTa

Fine-tuned BERT-family teacher model for Russian ICD-10 chapter/group prediction.
This model is exported from `train_extended_models.ipynb` as teacher #1 of top-5, selected by validation Top-3 accuracy.

- Base model: `alexyalunin/RuBioRoBERTa`
- Repo: `Dmitry43243242/icd10-ru-chapter-teacher-alexyalunin_rubioroberta`
- Labels: ICD-10 chapter letters, excluding U
- Intended use: teacher model for knowledge distillation and top-3 decision support

## Metrics

| Split | Top-1 | Top-3 | F1 macro | F1 weighted |
|---|---:|---:|---:|---:|
| Validation | 0.7010 | 0.8795 | 0.4554 | 0.6971 |
| Test | 0.7104 | 0.8794 | 0.3777 | 0.7047 |

This is a decision-support model, not an automatic diagnosis system.
