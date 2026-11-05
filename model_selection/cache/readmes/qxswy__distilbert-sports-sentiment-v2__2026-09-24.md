---
language: en
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- sentiment-analysis
- text-classification
- amazon-reviews
- sports-outdoors
- value-proposition
metrics:
- f1
---

# distilbert-sports-sentiment-v2

Binary sentiment classifier for Sports & Outdoors product reviews. Fine-tuned as part of a methodology for analyzing consumer value perception — a domain transfer experiment extending [v1 research](https://huggingface.co/qxswy/deberta-card-sentiment) from board games to fitness equipment.

## Performance

Evaluated on an unbalanced held-out test set (original class distribution: ~77% positive, ~23% negative):

| | Negative | Positive | Macro avg |
|---|---|---|---|
| Precision | 0.94 | 0.99 | 0.97 |
| Recall | 0.96 | 0.98 | 0.97 |
| F1 | 0.95 | 0.99 | **0.97** |
| Accuracy | | | 0.98 |

## Training

- **Base model:** `distilbert-base-uncased` (67M parameters)
- **Dataset:** Amazon Reviews 2023, Sports & Outdoors — Fit Simplify Resistance Loop Exercise Bands (14,766 reviews → 6,000 after balanced sampling)
- **Labels:** 4–5 stars = positive, 1–3 stars = negative
- **Technique:** Oversampling of minority class (negative) to balance training set

## Usage

```python
from transformers import pipeline

pipe = pipeline(
    "text-classification",
    model="qxswy/distilbert-sports-sentiment-v2"
)

reviews = [
    "These bands are incredibly durable, love them!",
    "Snapped after two weeks, complete waste of money."
]
print(pipe(reviews))
```

## Context

Part of a two-model NLP pipeline for value proposition analysis through consumer reviews. Paired with [`qxswy/modernbert-sports-ner-v2`](https://huggingface.co/qxswy/modernbert-sports-ner-v2) for named entity recognition of value components.

See also: v1 models trained on board game reviews — [`qxswy/deberta-card-sentiment`](https://huggingface.co/qxswy/deberta-card-sentiment) and [`qxswy/roberta-card-ner`](https://huggingface.co/qxswy/roberta-card-ner).