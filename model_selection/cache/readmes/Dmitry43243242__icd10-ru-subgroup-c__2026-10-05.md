---
language:
- ru
license: apache-2.0
tags:
- medical
- icd-10
- multi-label-classification
- russian
- conditional-distillation
base_model: alexyalunin/RuBioBERT
pipeline_tag: text-classification
---

# ICD-10 subgroup classifier - group C (distilled specialist)

Multi-label classifier over 3-character ICD-10 subgroups inside chapter **C**.
This specialist was distilled from local BERT teacher models into `alexyalunin/RuBioBERT`. Teacher weights are not uploaded to Hugging Face.

## Intended use / Назначение
- **EN:** Decision-support signal for suggesting candidate ICD-10 subgroups from Russian clinical notes. **Not** a substitute for clinician judgment; not validated for autonomous diagnosis.
- **RU:** Вспомогательный сигнал для предложения кандидатных 3-символьных кодов МКБ-10 по русскому клиническому тексту. **Не заменяет** врача и не предназначен для автономных клинических решений.

## Training data / Обучающие данные
- Source CSV: `datasets/subgroups/group_C.csv`
- SHA-256: `9526d7bd571f6aa94d0e162b727474a36dc63f71f79f0d78f400195b786bec26`
- Splits: train=346 · val=75 · test=75
- Labels: 70; rare/interface-only ids are listed in `label_map.json`.

## Training route
- Approach: `direct_hard_training_no_distillation`
- Base model: `alexyalunin/RuBioBERT`
- Direct validation hit@3: `0.96`
- No-distillation threshold: `0.9`
- Teacher models (fallback KD only): `[]`
- Selected KD config (fallback only): temperature=`None`, hard_loss_weight=`None`

## Metrics (test split)
| metric | final specialist | teacher ensemble / fallback |
|---|---:|---:|
| macro_f1 | 0.5899 | |
| micro_f1 | 0.5926 | |
| weighted_f1 | 0.6300 | |
| subset_accuracy | 0.2133 | |
| hit@1 | 0.8667 | |
| hit@3 | 0.9200 | |
| recall@3 | 0.8813 | |
| mrr | 0.9023 | |

Full per-label breakdown is available in `metrics.json`.

## Inference
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

repo = "Dmitry43243242/icd10-ru-subgroup-c"
tok = AutoTokenizer.from_pretrained(repo)
mdl = AutoModelForSequenceClassification.from_pretrained(repo)
mdl.eval()

text = "жалобы пациента..."
inp = tok(text, return_tensors="pt", truncation=True, max_length=512)
with torch.no_grad():
    probs = torch.sigmoid(mdl(**inp).logits)[0]
preds = [mdl.config.id2label[i] for i, p in enumerate(probs.tolist()) if p >= 0.5]
top5 = sorted(
    [(mdl.config.id2label[i], p) for i, p in enumerate(probs.tolist())],
    key=lambda x: -x[1],
)[:5]
print(preds, top5)
```
