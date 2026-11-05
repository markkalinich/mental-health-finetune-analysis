---
language:
- ru
license: apache-2.0
tags:
- medical
- icd-10
- multi-label-classification
- russian
base_model: ai-forever/ruBert-base
pipeline_tag: text-classification
---

# ICD-10 subgroup classifier — group S (Russian)

Multi-label classifier over 3-character ICD-10 subgroups inside chapter **S**.  
Fine-tuned from [`ai-forever/ruBert-base`](https://huggingface.co/ai-forever/ruBert-base) on Russian clinical text.

## Intended use / Назначение
- **EN:** Decision-support signal for suggesting candidate ICD-10 subgroups from Russian clinical notes. **Not** a substitute for clinician judgment; not validated for autonomous diagnosis.
- **RU:** Вспомогательный сигнал для предложения кандидатных 3-символьных кодов МКБ-10 по русскому клиническому тексту. **Не заменяет** врача и не предназначен для автономных клинических решений.

## Training data / Обучающие данные
- Source CSV: `datasets/subgroups/group_S.csv`
- SHA-256: `9c986818c4b97058e6f088821cd3d84a9c96b26327dd5d6de375b2b7389c4b4c`
- Produced by `ml/build_subgroup_datasets.ipynb` (iterative multi-label stratification by `parse_id`).
- Splits: train=257 · val=54 · test=52
- Labels: 45 (ordered, includes `S_OTHER` for rare codes collapsed during dataset build).

## Metrics (test split)
| metric | value |
|---|---|
| macro_f1 | 0.6207 |
| micro_f1 | 0.6403 |
| weighted_f1 | 0.6724 |
| subset_accuracy | 0.3846 |
| hit@1 | 0.9038 |
| hit@3 | 0.9423 |
| recall@3 | 0.9038 |
| mrr | 0.9284 |

Full per-label breakdown in `metrics.json`.

## Limitations / Ограничения
- Russian only; heavy reliance on clinical abbreviations (АД, ТТГ, УЗИ, etc.).
- Training text had PII redacted (`*ДАТА*`, `*ГОРОД*`, ...); model may behave differently on non-redacted input.
- Small chapters (train rows < 250) were trained with heavy regularization; some labels may have low support.
- Rare labels without positives in train are kept in the label map (see `label_map.json → rare_label_ids`) for interface stability but will effectively never fire.

## Inference
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

repo = "Dmitry43243242/icd10-ru-subgroup-s"
tok = AutoTokenizer.from_pretrained(repo)
mdl = AutoModelForSequenceClassification.from_pretrained(repo)
mdl.eval()

text = "жалобы пациента..."
inp = tok(text, return_tensors="pt", truncation=True, max_length=512)
with torch.no_grad():
    probs = torch.sigmoid(mdl(**inp).logits)[0]
preds = [mdl.config.id2label[i] for i, p in enumerate(probs.tolist()) if p >= 0.5]
top3 = sorted(
    [(mdl.config.id2label[i], p) for i, p in enumerate(probs.tolist())],
    key=lambda x: -x[1],
)[:3]
print(preds, top3)
```

## Citation / Ссылка
Built as part of the `ai-app` ICD-10 classification pipeline. Upstream model: `ai-forever/ruBert-base` (ai-forever).
