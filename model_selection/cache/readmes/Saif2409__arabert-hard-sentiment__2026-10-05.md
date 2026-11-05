---
language: ar
license: mit
base_model: aubmindlab/bert-base-arabertv02
pipeline_tag: text-classification
tags: [arabic, sentiment-analysis, arabert, dialect, hotel-reviews]
datasets: [hard]
metrics: [accuracy, f1]
---

# AraBERT fine-tuned for Arabic hotel-review sentiment

`aubmindlab/bert-base-arabertv02` fine-tuned on **HARD** (Hotel Arabic Reviews
Dataset, ~105K Booking.com reviews) for binary sentiment.

| model | test accuracy | macro F1 | ROC-AUC |
|---|---|---|---|
| TF-IDF + LogisticRegression baseline | 87.48% | 0.8748 | 0.9432 |
| **this model** | **91.73%** | **0.9173** | **0.9685** |

33.9% reduction in errors over the baseline (paired bootstrap, p < 0.001).

## Important: the labels leak in raw HARD

Booking.com prepends an auto-generated rating descriptor to the review body
(«مخيب للأمل», «استثنائي», «ضعيف جداً»). It is a deterministic function of the star
rating the labels derive from, and it covers **41.3%** of the corpus. This model
was trained on text with that header **stripped**. Numbers from work that does not
strip it (≈94% for the same baseline) are not comparable.

## Accuracy by language register

| register | n | accuracy |
|---|---|---|
| dialect | 1,970 | 95.84% |
| msa | 1,827 | 92.50% |
| unmarked | 6,500 | 90.26% |

Dialectal reviews are *easier* than MSA here, and the gap survives matching on
review length within every quintile — dialectal writing in this corpus is blunter
and more lexically explicit.

## Known limitation

The official `ArabertPreprocessor` **strips emoji**, so «الفندق 😍» reaches the
model as «الفندق». If emoji carry sentiment in your data, load it with
`keep_emojis=True` and re-tune.

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

repo = "Saif2409/arabert-hard-sentiment"
tok = AutoTokenizer.from_pretrained(repo)
model = AutoModelForSequenceClassification.from_pretrained(repo).eval()

text = "الفندق وايد زين والطاقم متعاون"
with torch.inference_mode():
    probs = torch.softmax(model(**tok(text, return_tensors="pt")).logits, -1)[0]
print(model.config.id2label[int(probs.argmax())], float(probs.max()))
```

Full code, error analysis and probe suite:
https://github.com/Saif2409/arabic-sentiment
