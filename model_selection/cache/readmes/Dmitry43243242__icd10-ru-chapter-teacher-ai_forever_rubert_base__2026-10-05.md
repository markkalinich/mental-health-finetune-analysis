---
language: ru
library_name: transformers
tags:
- text-classification
- icd10
- medical
- knowledge-distillation-teacher
---

# ICD-10 Russian Chapter Teacher: ai-forever/ruBert-base

Fine-tuned BERT-family teacher model for Russian ICD-10 chapter/group prediction.
This model is exported from `train_extended_models.ipynb` as teacher #3 of top-5, selected by validation Top-3 accuracy.

- Base model: `ai-forever/ruBert-base`
- Repo: `Dmitry43243242/icd10-ru-chapter-teacher-ai_forever_rubert_base`
- Labels: ICD-10 chapter letters, excluding U
- Intended use: teacher model for knowledge distillation and top-3 decision support

## Metrics

| Split | Top-1 | Top-3 | F1 macro | F1 weighted |
|---|---:|---:|---:|---:|
| Validation | 0.7071 | 0.8707 | 0.4288 | 0.7028 |
| Test | 0.7262 | 0.8952 | 0.4193 | 0.7186 |

This is a decision-support model, not an automatic diagnosis system.
