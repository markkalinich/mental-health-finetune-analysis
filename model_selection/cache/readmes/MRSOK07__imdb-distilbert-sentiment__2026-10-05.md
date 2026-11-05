---
language: en
license: apache-2.0
tags:
- text-classification
- sentiment-analysis
- distilbert
datasets:
- imdb
metrics:
- accuracy
---

# IMDb Sentiment Classifier

Fine-tuned `distilbert-base-uncased` on IMDb for binary sentiment.

**Test accuracy:** 0.8640  
**Training samples:** 2000  
**Author:** JAI AADHAVAN V ([MRSOK07](https://huggingface.co/MRSOK07))

## Usage

```python
from transformers import pipeline
clf = pipeline("text-classification", model="MRSOK07/imdb-distilbert-sentiment")
clf("This movie was absolutely amazing!")
```

## Training config

| Parameter | Value |
|-----------|-------|
| Base model | distilbert-base-uncased |
| Epochs | 3 |
| Learning rate | 2e-5 |
| Batch size | 16 |
| Max length | 256 |
