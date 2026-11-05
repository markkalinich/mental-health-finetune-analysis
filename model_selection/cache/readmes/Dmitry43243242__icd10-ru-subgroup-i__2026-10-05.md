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

# ICD-10 subgroup classifier — group I (Russian)

Multi-label classifier over 3-character ICD-10 subgroups inside chapter **I**.  
Fine-tuned from [`ai-forever/ruBert-base`](https://huggingface.co/ai-forever/ruBert-base) on Russian clinical text.

## Intended use / Назначение
- **EN:** Decision-support signal for suggesting candidate ICD-10 subgroups from Russian clinical notes. **Not** a substitute for clinician judgment; not validated for autonomous diagnosis.
- **RU:** Вспомогательный сигнал для предложения кандидатных 3-символьных кодов МКБ-10 по русскому клиническому тексту. **Не заменяет** врача и не предназначен для автономных клинических решений.

## Training data / Обучающие данные
- Source CSV: `datasets/subgroups/group_I.csv`
- SHA-256: `9f277d2bf673422bf44bd7a445079b896f0ba9e66384859d719c13508bc8c9eb`
- Produced by `ml/build_subgroup_datasets.ipynb` (iterative multi-label stratification by `parse_id`).
- Splits: train=740 · val=156 · test=161
- Labels: 63 (ordered, includes `I_OTHER` for rare codes collapsed during dataset build).

## Metrics (test split)
| metric | value |
|---|---|
| macro_f1 | 0.5897 |
| micro_f1 | 0.5959 |
| weighted_f1 | 0.6320 |
| subset_accuracy | 0.2547 |
| hit@1 | 0.7329 |
| hit@3 | 0.8634 |
| recall@3 | 0.8428 |
| mrr | 0.8141 |

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

repo = "Dmitry43243242/icd10-ru-subgroup-i"
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
