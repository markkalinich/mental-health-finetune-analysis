---
language:
- en
license: apache-2.0
tags:
- distilbert
- emotion
- text-classification
- emobooks
base_model: distilbert-base-uncased
pipeline_tag: text-classification
---

# EmoBooks — Emotion Classifier

A `distilbert-base-uncased` fine-tuned to classify English (and
Singlish-normalized) user utterances into 8 emotion labels for the
[emoBooks](https://huggingface.co/DiyRex/emobooks-llama3-lora) Sinhala
novel recommender.

## Labels

`sadness`, `joy`, `love`, `anger`, `fear`, `surprise`, `disgust`, `calm`

The runtime additionally maps these to `lonely` and `anxious` via simple
keyword rules (see `emobooks/classifier.py::LABEL_ALIAS`).

## Training

| Parameter | Value |
|---|---|
| Base model | `distilbert-base-uncased` |
| Dataset | 42 k / 2.5 k / 2.5 k (train/val/test) — `dataset/training.csv` etc. in the [emobooks repo](https://github.com/) |
| Epochs | 4 |
| Batch size | 32 |
| Max seq len | 160 |
| Learning rate | 2.0e-5 (cosine, 6% warmup) |
| Weight decay | 0.01 |

## Test metrics (held-out 2.5 k split)

| Metric | Value |
|---|---|
| eval_accuracy | **0.9356** |
| eval_loss | 0.2372 |

## Inference

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tok = AutoTokenizer.from_pretrained("DiyRex/emobooks-emotion-classifier")
model = AutoModelForSequenceClassification.from_pretrained(
    "DiyRex/emobooks-emotion-classifier"
).eval()

text = "i feel really lonely tonight"
ids = tok(text, return_tensors="pt", truncation=True, max_length=160)
with torch.no_grad():
    logits = model(**ids).logits
label = model.config.id2label[int(logits.argmax(-1))]
print(label)  # → "sadness"  (then mapped to "lonely" by the runtime)
```

## Singlish input

The runtime pre-normalises Singlish/Sinhala affect tokens to English
hints before this model runs (see `emobooks/normalize.py`):

  - `mata hari duka` → `i feel sad. mata hari sad` → **sadness**
  - `mata satutui`   → `i feel happy. mata happy` → **joy**
  - `mata loku bayak tiyenne` → fear-cue prepended → **fear**

## Place in the stack

```
user text
   ↓ normalize       (Singlish → English hints)
   ↓ this classifier (one of 8 emotion labels)
   ↓ retrieve        (xlm-roberta-base mean-pooled, cosine)
   ↓ filter          (emotion → tone/pacing/theme rules)
   ↓ dialog          (state machine)
   ↓ respond         (Llama-3-8B + DiyRex/emobooks-llama3-lora)
   ↓ guardrail       (catalog index check; no fake books)
```

## License
Apache 2.0
