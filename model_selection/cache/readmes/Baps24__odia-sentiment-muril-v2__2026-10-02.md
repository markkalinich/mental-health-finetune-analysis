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
datasets:
- Baps24/odia-sentiment-dataset
---

# Odia Sentiment Classifier v2

Fine-tuned `google/muril-base-cased` for **Odia language sentiment analysis**.

Built with ❤️ for the **45 million Odia speakers** of Odisha 🇮🇳

Dedicated to **Lord Jagannath** and the people of Odisha 🙏

## Improvements over v1
- Larger dataset: 66 samples (auto-labeled from OdiaGenAI corpus)
- Better class balance
- Higher accuracy

## Usage

```python
from transformers import pipeline
pipe = pipeline("text-classification", model="Baps24/odia-sentiment-muril-v2")
pipe("ଏହି ଉତ୍ପାଦ ଭଲ")  # Positive
pipe("ଏହି ଜିନିଷ ଖରାପ")  # Negative
```

## Labels
- Positive (ସକାରାତ୍ମକ)
- Negative (ନକାରାତ୍ମକ)
- Neutral (ନିରପେକ୍ଷ)

## Training
- Base: google/muril-base-cased
- Dataset: Baps24/odia-sentiment-dataset
- Accuracy: 0.300
- F1 Score: 0.138

## Community
This model is part of the Odias in ML initiative.
Visit: https://odisha-ml.github.io
