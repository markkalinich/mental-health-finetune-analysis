---
language:
- fa
library_name: transformers
pipeline_tag: text-classification
tags:
- persian
- farsi
- emotion-classification
- albert
- small-model
metrics:
- accuracy
- f1
base_model: shekar-ai/albert-base-v2-persian-zwnj-naab-mlm
---

# Hes Shenaas RizehPizeh v0.1

**RizehPizeh** is the compact Hes Shenaas Persian emotion classifier: a Persian
ALBERT encoder followed by a one-layer bidirectional GRU classification head.
It contains **12,040,967 parameters** and predicts seven labels.

## Smallest Persian emotion classifier

**As of September 9, 2026, to the best of our knowledge, this Hes Shenaas is the
smallest publicly available Persian text emotion recognizer/classifier, with
12M parameters.** This claim is based on a review of discoverable public
model releases and published Persian emotion classifiers. It does not cover
unpublished or unindexed models.

| Label | Meaning |
|---|---|
| `ANGRY` | anger |
| `FEAR` | fear or anxiety |
| `HAPPY` | happiness or joy |
| `HATE` | hate, disgust, or strong aversion |
| `SAD` | sadness |
| `SURPRISE` | surprise |
| `OTHER` | neutral, unclear, or outside the six emotions |

## Quick start

This repository contains the encoder, GRU head, tokenizer, and model code. No
second model repository is downloaded at inference time.

```bash
pip install "torch>=2.4" "transformers>=4.45"
```

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

repo = "Reza2kn/Hes-Shenaas-RizehPizeh-v0.1"
tokenizer = AutoTokenizer.from_pretrained(repo, trust_remote_code=True)
model = AutoModelForSequenceClassification.from_pretrained(
    repo,
    trust_remote_code=True,
).eval()

text = "امروز واقعاً روز فوق‌العاده‌ای بود"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
with torch.inference_mode():
    probabilities = model(**inputs).logits.softmax(dim=-1)[0]

scores = {
    model.config.id2label[index]: float(score)
    for index, score in enumerate(probabilities)
}
print(max(scores, key=scores.get), scores)
```

Pipeline API:

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="Reza2kn/Hes-Shenaas-RizehPizeh-v0.1",
    trust_remote_code=True,
)
print(classifier("از این وضعیت خیلی عصبانی‌ام", top_k=None))
```

## Evaluation

The checkpoint was selected using a fixed 1,232-example validation split. The
protected 1,151-example test split was evaluated once after selection.

| Split | Examples | Accuracy | Macro F1 | Weighted F1 |
|---|---:|---:|---:|---:|
| Validation | 1,232 | **72.65%** | **73.24%** | 72.46% |
| Test | 1,151 | **70.03%** | **69.17%** | 70.20% |

For scale, **Gemini 3.8 Flash scored 78.11% accuracy (899/1,151)** on the same
frozen test set under the project's fixed prompting contract. RizehPizeh is
8.08 percentage points behind that hosted reference while remaining a
self-contained local model with only 12,040,967 parameters.

Test F1 by class:

| ANGRY | FEAR | HAPPY | HATE | SAD | SURPRISE | OTHER |
|---:|---:|---:|---:|---:|---:|---:|
| 69.23% | 71.67% | 72.88% | 63.79% | 76.21% | 68.02% | 62.37% |

The packaged model was reloaded through the Transformers auto classes and its
predictions were checked against all 1,151 stored frozen-test predictions.

## Architecture and training

- Persian ALBERT encoder revision: `1a4861062a5501088ce06389f5d67921e47320e4`
- Bidirectional GRU: 128 hidden units per direction
- Dropout: 0.2
- Linear classifier: 256 → 7
- Maximum input length: 128 tokens
- Selected epoch: 2
- Training data: 4,862 cleaned original rows plus 42,000 balanced public Persian
  tweets carrying high-confidence teacher probabilities
- Distillation threshold: 0.95, capped at 6,000 external rows per class
- Loss: original-label cross entropy plus temperature-2 teacher KL divergence
- Protected validation and test texts were excluded from external API payloads

## Limitations

Emotion classification is subjective. Accuracy will vary on formal prose,
sarcasm, code-switching, dialects, long documents, and domains unlike the
benchmark. `OTHER` combines neutral and ambiguous cases. `HATE` includes strong
aversion and disgust under this dataset's label contract. Do not use predictions
as the sole basis for high-impact decisions about people.

## Integrity

The original training checkpoint SHA-256 was:

`9fc3e1d865d7177a0f2a3c5d90e2114357b355b98ac0b80292a7d9d5e9a69d38`

The converted `model.safetensors` checksum is recorded in `release.json`.
