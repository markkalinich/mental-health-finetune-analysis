---
language: en
license: apache-2.0
tags:
- text-classification
- sentiment-analysis
- distilbert
- pytorch
datasets:
- imdb
metrics:
- accuracy
---

# DistilBERT Sentiment Analysis

Fine-tuned `distilbert-base-uncased` on the IMDB movie review dataset for binary sentiment classification (positive / negative).

## Results

| Metric | Score |
|--------|-------|
| Test accuracy | 91.33% |
| Training loss | 0.238 |
| Validation loss | 0.225 |
| Epochs | 1 |

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="BlessedDovis/distilbert-sentiment-analysis"
)

result = classifier("This movie was absolutely fantastic!")
# POSITIVE — 99.52% confidence
```

## Training

- **Base model:** distilbert-base-uncased
- **Dataset:** IMDB (25,000 train / 25,000 test)
- **Hardware:** Google Colab T4 GPU
- **Framework:** HuggingFace Transformers + PyTorch
- **Batch size:** 16
- **Mixed precision:** fp16
