---
license: apache-2.0
language: en
library_name: transformers
pipeline_tag: text-classification
tags:
  - sentiment-analysis
  - customer-feedback
  - distilbert
datasets:
  - Yelp/yelp_review_full
metrics:
  - f1
  - accuracy
base_model: distilbert-base-uncased
widget:
  - text: "The delivery was three days late and the box arrived damaged."
  - text: "Absolutely brilliant service, the team resolved my issue in minutes."
  - text: "It works as described. Nothing special, but the price is reasonable."
---

# PulseAI — DistilBERT Customer Sentiment

`distilbert-base-uncased` fine-tuned for 3-class customer sentiment
(**negative / neutral / positive**) on Yelp business reviews.

Built for [PulseAI](https://github.com/AkashKeshari111/pulseai-sentiment-dashboard),
a customer sentiment intelligence platform.

## Results — held-out test set (2,000 reviews)

| Model | Accuracy | Macro-F1 |
|---|---|---|
| TF-IDF + Logistic Regression (baseline) | 0.7250 | 0.7237 |
| DistilBERT, `max_seq_length=128` | 0.7170 | 0.7180 |
| **DistilBERT, `max_seq_length=256`** ← this model | **0.7400** | **0.7390** |

### Per class

| Class | Precision | Recall | F1 |
|---|---|---|---|
| negative | 0.826 | 0.786 | 0.806 |
| neutral | 0.637 | 0.611 | 0.624 |
| positive | 0.755 | 0.823 | 0.788 |

## The context-window finding

The first fine-tuning run used a 128-token window and **lost to the bag-of-words
baseline**. The cause was not the model. WordPiece splits review text into roughly
**1.29 tokens per word**, so 128 tokens covered only **~51%** of the corpus — the
transformer was reading half of every long review while TF-IDF read all of it.

At 256 tokens (~82% coverage), with architecture, data, seed and every other
hyper-parameter held constant, macro-F1 rose **+2.1 points**. Both runs are published
so the comparison can be checked.

## Usage

```python
from transformers import pipeline

clf = pipeline("text-classification", model="akashkeshari111/pulseai-distilbert-sentiment")
clf("The delivery was late and the box arrived damaged.")
# [{'label': 'negative', 'score': 0.98}]
```

Inference runs at roughly **87 ms** per sample on CPU.

## Training

- 12,000 balanced training reviews, 2,000 validation, 2,000 test (stratified)
- Star ratings mapped to sentiment: 1–2 negative, 3 neutral, 4–5 positive
- 2 epochs, batch size 16, learning rate 3e-5, linear warmup over 10% of steps
- AdamW with decoupled weight decay (not applied to LayerNorm or biases)
- Gradient clipping at norm 1.0, dynamic per-batch padding
- Checkpoint selected on **validation macro-F1**, never training loss
- Trained CPU-only

## Limitations

- **Label noise.** Neutral is defined by a 3-star mapping and 3-star reviews are
  genuinely ambiguous. This caps neutral-class performance; better labels need human
  annotation, not a bigger model.
- **Domain.** English business reviews. Short social posts, code-mixed text and
  technical support tickets are out of distribution and unmeasured. Very short inputs
  (a few words) are unreliable — the model was trained on text averaging 165 tokens.
- **Sarcasm** is not handled.
- **Intended use:** in front of a human triage workflow — routing and ranking. Not for
  automated action on an individual customer.
