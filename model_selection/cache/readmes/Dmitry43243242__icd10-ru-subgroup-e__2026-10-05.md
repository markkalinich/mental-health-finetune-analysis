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

# ICD-10 subgroup classifier - group E (distilled specialist)

Multi-label classifier over 3-character ICD-10 subgroups inside chapter **E**.
This specialist was distilled from local BERT teacher models into `alexyalunin/RuBioBERT`. Teacher weights are not uploaded to Hugging Face.

## Intended use / Назначение
- **EN:** Decision-support signal for suggesting candidate ICD-10 subgroups from Russian clinical notes. **Not** a substitute for clinician judgment; not validated for autonomous diagnosis.
- **RU:** Вспомогательный сигнал для предложения кандидатных 3-символьных кодов МКБ-10 по русскому клиническому тексту. **Не заменяет** врача и не предназначен для автономных клинических решений.

## Training data / Обучающие данные
- Source CSV: `datasets/subgroups/group_E.csv`
- SHA-256: `7bd98fc0eea937b8edf1391e86ca15afd2aed5c98996951f822684805713ed0b`
- Splits: train=919 · val=200 · test=199
- Labels: 45; rare/interface-only ids are listed in `label_map.json`.

## Training route
- Approach: `local_teacher_ensemble_knowledge_distillation`
- Base model: `alexyalunin/RuBioBERT`
- Direct validation hit@3: `0.835`
- No-distillation threshold: `0.9`
- Teacher models (fallback KD only): `['alexyalunin/RuBioRoBERTa', 'ai-forever/ruBert-base', 'DeepPavlov/rubert-base-cased']`
- Selected KD config (fallback only): temperature=`2.0`, hard_loss_weight=`0.5`

## Metrics (test split)
| metric | final specialist | teacher ensemble / fallback |
|---|---:|---:|
| macro_f1 | 0.6122 | 0.6805 |
| micro_f1 | 0.5606 | 0.6541 |
| weighted_f1 | 0.5830 | 0.6549 |
| subset_accuracy | 0.2965 | 0.4824 |
| hit@1 | 0.6482 | 0.6784 |
| hit@3 | 0.8241 | 0.8442 |
| recall@3 | 0.8147 | 0.8382 |
| mrr | 0.7516 | 0.7735 |

Full per-label breakdown is available in `metrics.json`.

## Inference
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

repo = "Dmitry43243242/icd10-ru-subgroup-e"
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
