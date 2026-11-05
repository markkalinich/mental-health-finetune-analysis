---
language: en
license: apache-2.0
tags:
  - text-classification
  - sentiment-analysis
  - roberta
  - pytorch
  - transformers
datasets:
  - imdb
  - glue
  - tweet_eval
  - yelp_review_full
pipeline_tag: text-classification
---

# 🎭 Sentiment Analysis — airzipm

A powerful **3-class sentiment analysis** model fine-tuned from `roberta-base`
on a combined corpus of 200 000+ samples spanning movie reviews, short sentences,
tweets, and restaurant reviews.

## 🏷️ Labels

| ID | Label    | Description                   |
|----|----------|-------------------------------|
| 0  | Negative | Negative sentiment / opinion  |
| 1  | Neutral  | Neutral / mixed sentiment     |
| 2  | Positive | Positive sentiment / opinion  |

## 📊 Performance

| Metric          | Value                  |
|-----------------|------------------------|
| Val Accuracy    | 0.8239  |
| Val F1 (macro)  | 0.7827  |

## 🚀 Quick Usage

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="airzipm/sentiment-analysis-roberta",
)

# Single prediction
print(classifier("This movie was absolutely amazing!"))
# [{'label': 'Positive', 'score': 0.97}]

# Batch prediction
texts = [
    "Great product, highly recommend!",
    "It was okay, nothing special.",
    "Terrible experience, waste of money.",
]
for t, r in zip(texts, classifier(texts)):
    print(f"{t[:45]:50s} → {r['label']} ({r['score']:.1%})")
```

## 🛠️ Training Details

| Setting          | Value             |
|------------------|-------------------|
| Base model       | `roberta-base`    |
| Max token length | 128               |
| Batch size       | 32                |
| Learning rate    | 2e-5              |
| Optimizer        | AdamW + warmup    |
| Mixed precision  | FP16              |
| Label smoothing  | 0.1               |
| Class weights    | Balanced          |

## 📦 Training Data

| Dataset     | Domain          | Samples |
|-------------|-----------------|---------|
| IMDB        | Movie reviews   | 50 000  |
| SST-2       | Short sentences | 50 000  |
| Tweet Eval  | Twitter posts   | 50 000  |
| Yelp Review | Business review | 50 000  |

## 🖼️ Training Curves & Confusion Matrix

See `training_curves.png` and `confusion_matrix.png` in this repository.

## 👤 Author

Created by **airzipm** — [Hugging Face Profile](https://huggingface.co/airzipm)
