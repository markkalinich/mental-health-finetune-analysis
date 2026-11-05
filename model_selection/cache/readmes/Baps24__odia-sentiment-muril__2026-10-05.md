---
language:
- or
tags:
- text-classification
- sentiment-analysis
- odia
- indic-languages
- muril
license: apache-2.0
base_model: google/muril-base-cased
---

# Odia Sentiment Classifier

Fine-tuned `google/muril-base-cased` for **sentiment analysis in Odia language**.

Built to serve the **45 million Odia speakers** of Odisha, India.

## Usage

```python
from transformers import pipeline
pipe = pipeline("text-classification", model="Baps24/odia-sentiment-muril")
pipe("ଏହି ଉତ୍ପାଦ ଭଲ")  # Positive
```

## Labels
- Positive (ସକାରାତ୍ମକ)
- Negative (ନକାରାତ୍ମକ)
- Neutral  (ନିରପେକ୍ଷ)

## Training
- Base model: google/muril-base-cased
- Task: Sentiment Classification (3 classes)
- Language: Odia (or)
- Test Accuracy: 0.333
- Test F1: 0.167
