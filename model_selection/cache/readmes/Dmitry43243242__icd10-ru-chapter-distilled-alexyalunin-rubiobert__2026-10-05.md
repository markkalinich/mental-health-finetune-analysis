---
language: ru
library_name: transformers
tags:
- text-classification
- icd10
- medical
- knowledge-distillation
---

# ICD-10 Russian Chapter Distilled Student

Distilled student model for Russian ICD-10 chapter/group prediction.

- Student base model: `alexyalunin/RuBioBERT`
- Teacher source: `repo_ids`
- Teachers: `Dmitry43243242/icd10-ru-chapter-teacher-alexyalunin_rubiobert`, `Dmitry43243242/icd10-ru-chapter-teacher-alexyalunin_rubioroberta`, `Dmitry43243242/icd10-ru-chapter-teacher-ai_forever_rubert_base`, `Dmitry43243242/icd10-ru-chapter-teacher-cointegrated_rubert_tiny2`, `Dmitry43243242/icd10-ru-chapter-teacher-deeppavlov_rubert_base_cased`
- Selected KD run: `t2p0_hard0p5`
- Temperature: `2.0`
- Loss: `0.50 * CE + 0.50 * KL * T^2`
- Class-weighted hard loss: `True`

This is a decision-support model, not an automatic diagnosis system.
