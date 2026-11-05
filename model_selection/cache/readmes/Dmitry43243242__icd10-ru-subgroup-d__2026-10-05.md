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

# ICD-10 subgroup classifier - group D (distilled specialist)

Multi-label classifier over 3-character ICD-10 subgroups inside chapter **D**.
This specialist was distilled from local BERT teacher models into `alexyalunin/RuBioBERT`. Teacher weights are not uploaded to Hugging Face.

## Intended use / Назначение
- **EN:** Decision-support signal for suggesting candidate ICD-10 subgroups from Russian clinical notes. **Not** a substitute for clinician judgment; not validated for autonomous diagnosis.
- **RU:** Вспомогательный сигнал для предложения кандидатных 3-символьных кодов МКБ-10 по русскому клиническому тексту. **Не заменяет** врача и не предназначен для автономных клинических решений.

## Training data / Обучающие данные
- Source CSV: `datasets/subgroups/group_D.csv`
- SHA-256: `10c1c6d836234bbd276eca3443a555ca9dfd77bab22f6ec5afcb6b938252fbc3`
- Splits: train=528 · val=113 · test=112
- Labels: 57; rare/interface-only ids are listed in `label_map.json`.

## Training route
- Approach: `direct_hard_training_no_distillation`
- Base model: `alexyalunin/RuBioBERT`
- Direct validation hit@3: `0.9203539823008849`
- No-distillation threshold: `0.9`
- Teacher models (fallback KD only): `[]`
- Selected KD config (fallback only): temperature=`None`, hard_loss_weight=`None`

## Metrics (test split)
| metric | final specialist | teacher ensemble / fallback |
|---|---:|---:|
| macro_f1 | 0.6698 | |
| micro_f1 | 0.7299 | |
| weighted_f1 | 0.7358 | |
| subset_accuracy | 0.4732 | |
| hit@1 | 0.8571 | |
| hit@3 | 0.9286 | |
| recall@3 | 0.9286 | |
| mrr | 0.8996 | |

Full per-label breakdown is available in `metrics.json`.

## Inference
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

repo = "Dmitry43243242/icd10-ru-subgroup-d"
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
