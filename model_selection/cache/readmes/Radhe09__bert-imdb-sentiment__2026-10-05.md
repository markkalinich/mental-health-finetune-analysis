---
language: en
license: apache-2.0
tags:
- text-classification
- sentiment-analysis
- bert
- imdb
datasets:
- imdb
metrics:
- accuracy
- f1
---

# BERT Fine-tuned on IMDB Sentiment Analysis

## Model Description
This model is a fine-tuned version of `bert-base-uncased` 
on the IMDB movie reviews dataset for sentiment analysis.

## Training Details
- Base Model: bert-base-uncased
- Dataset: IMDB (2000 train, 500 test samples)
- Epochs: 3
- Learning Rate: 2e-5
- Batch Size: 16
- Framework: HuggingFace Transformers

## Results
| Metric   | Score |
|----------|-------|
| Accuracy | ~88%  |
| F1 Score | ~0.88 |

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    'sentiment-analysis',
    model='your-hf-username/bert-imdb-sentiment'
)

result = classifier("This movie was absolutely amazing!")
print(result)
# [{'label': 'POSITIVE', 'score': 0.98}]
```

## Labels
- LABEL_0 → Negative 😠
- LABEL_1 → Positive 😊
