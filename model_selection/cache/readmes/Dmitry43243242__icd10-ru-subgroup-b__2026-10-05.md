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

# ICD-10 subgroup classifier - group B (distilled specialist)

Multi-label classifier over 3-character ICD-10 subgroups inside chapter **B**.
This specialist was distilled from local BERT teacher models into `alexyalunin/RuBioBERT`. Teacher weights are not uploaded to Hugging Face.

## Intended use / Назначение
- **EN:** Decision-support signal for suggesting candidate ICD-10 subgroups from Russian clinical notes. **Not** a substitute for clinician judgment; not validated for autonomous diagnosis.
- **RU:** Вспомогательный сигнал для предложения кандидатных 3-символьных кодов МКБ-10 по русскому клиническому тексту. **Не заменяет** врача и не предназначен для автономных клинических решений.

## Training data / Обучающие данные
- Source CSV: `datasets/subgroups/group_B.csv`
- SHA-256: `596f1d3a237321d643a001d20be62a228f9a88578ccbd4a33df5a529065a8562`
- Splits: train=265 · val=57 · test=58
- Labels: 30; rare/interface-only ids are listed in `label_map.json`.

## Training route
- Approach: `direct_hard_training_no_distillation`
- Base model: `alexyalunin/RuBioBERT`
- Direct validation hit@3: `0.9473684210526315`
- No-distillation threshold: `0.9`
- Teacher models (fallback KD only): `[]`
- Selected KD config (fallback only): temperature=`None`, hard_loss_weight=`None`

## Metrics (test split)
| metric | final specialist | teacher ensemble / fallback |
|---|---:|---:|
| macro_f1 | 0.7392 | |
| micro_f1 | 0.7623 | |
| weighted_f1 | 0.8235 | |
| subset_accuracy | 0.4310 | |
| hit@1 | 0.8793 | |
| hit@3 | 0.9310 | |
| recall@3 | 0.8621 | |
| mrr | 0.9094 | |

Full per-label breakdown is available in `metrics.json`.

## Inference
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

repo = "Dmitry43243242/icd10-ru-subgroup-b"
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
