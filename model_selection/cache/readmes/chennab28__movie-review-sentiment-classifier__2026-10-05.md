---
license: apache-2.0
language:
  - en
library_name: transformers
pipeline_tag: text-classification
tags:
  - sentiment-analysis
  - movie-reviews
  - bert
  - tiny
datasets:
  - chennab28/movie-review-sentiment
base_model: google/bert_uncased_L-4_H-256_A-4
model-index:
  - name: movie-review-sentiment-classifier
    results:
      - task:
          type: text-classification
          name: Sentiment Analysis
        dataset:
          type: chennab28/movie-review-sentiment
          name: Movie Review Sentiment (Mini)
          split: test
        metrics:
          - type: accuracy
            value: 0.9762
            name: Accuracy
---

# 🍿 Movie Review Sentiment Classifier

A **tiny** BERT model (`google/bert_uncased_L-4_H-256_A-4`, ~10M params)
fine-tuned for 3-way **movie review sentiment** classification:

`positive` / `negative` / `neutral`

Trained on the companion dataset
[`chennab28/movie-review-sentiment`](https://huggingface.co/datasets/chennab28/movie-review-sentiment)
in a couple of minutes on CPU.

## Quick inference

```python
from transformers import pipeline

pipe = pipeline("text-classification", model="chennab28/movie-review-sentiment-classifier")

print(pipe("A breathtaking masterpiece with stunning cinematography."))
# [{'label': 'positive', 'score': 0.99}]
```

## Metrics

| Task                  | Acc (test) |
|-----------------------|------------|
| Sentiment (3 classes) | 97.6%      |

## Why so small?

This is deliberately a *minimal end-to-end* example of the Hugging Face
workflow — **Dataset → Model → Space**. Despite having only ~10M parameters,
the model reaches 97.6% accuracy on the held-out test split.

## Training details

| Config        | Value                          |
|---------------|--------------------------------|
| base model    | `google/bert_uncased_L-4_H-256_A-4` |
| epochs        | 30                             |
| batch size    | 16                             |
| lr            | 5e-5                           |
| max seq len   | 128                            |
| data          | 168 train / 42 test rows       |

Reproduce with `train/train.py --epochs 30` in this repo.

## Try it live

👉 [Gradio demo Space](https://huggingface.co/spaces/chennab28/movie-review-sentiment-demo)