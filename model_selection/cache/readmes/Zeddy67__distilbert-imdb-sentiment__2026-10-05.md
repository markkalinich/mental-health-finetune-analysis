---
language: en
license: apache-2.0
tags:
- text-classification
- sentiment-analysis
- distilbert
- imdb
datasets:
- imdb
metrics:
- accuracy
---

# DistilBERT IMDb Sentiment Classifier

Fine-tuned `distilbert-base-uncased` on the IMDb dataset for binary sentiment classification.

## Usage
```python
from transformers import pipeline

pipe = pipeline("text-classification", model="zeddy67/distilbert-imdb-sentiment")
print(pipe("This movie was absolutely fantastic!"))
```

## Training
- **Base model:** distilbert-base-uncased
- **Dataset:** IMDb (25k train / 25k test)
- **Epochs:** 3
- **Learning rate:** 2e-5
