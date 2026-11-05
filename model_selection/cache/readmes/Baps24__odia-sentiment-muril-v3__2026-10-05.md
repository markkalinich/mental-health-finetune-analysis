---
language: [or]
tags: [text-classification, sentiment-analysis, odia, muril]
license: apache-2.0
base_model: google/muril-base-cased
---

# Odia Sentiment Classifier v3
Fine-tuned `google/muril-base-cased` for Odia sentiment.
Built for **45 million Odia speakers** 🇮🇳 — Dedicated to Lord Jagannath 🙏

**Accuracy: 0.778 (77.8%) | F1: 0.773**

```python
from transformers import pipeline
pipe = pipeline("text-classification", model="Baps24/odia-sentiment-muril-v3")
pipe("ଏହି ଉତ୍ପାଦ ଭଲ")  # Positive
pipe("ଏହି ଜିନିଷ ଖରାପ")  # Negative
```
Community: https://odisha-ml.github.io
