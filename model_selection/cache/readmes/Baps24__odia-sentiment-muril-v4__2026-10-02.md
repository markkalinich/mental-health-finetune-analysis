---
language: [or]
tags: [text-classification, sentiment-analysis, odia, muril, indic-languages]
license: apache-2.0
base_model: google/muril-base-cased
---

# Odia Sentiment Classifier v4
Fine-tuned `google/muril-base-cased` for **Odia language sentiment analysis**.

Built with ❤️ for **45 million Odia speakers** 🇮🇳
Dedicated to **Lord Jagannath and Lord Lingaraj (We are from old town :) Parakaran Sahi)** and the people of Odisha 🙏

## Results
| Metric   | Score |
|----------|-------|
| Accuracy | 0.838 (83.8%) |
| F1 Score | 0.834 |
| Samples  | 37 test samples |

## Previous versions
| Version | Accuracy |
|---------|----------|
| v1 | ~33% |
| v2 | ~30% (auto-label bug) |
| v3 | 77.8% |
| **v4** | **83.8%** |

## Usage
```python
from transformers import pipeline
pipe = pipeline("text-classification", model="Baps24/odia-sentiment-muril-v4")
pipe("ଏହି ଉତ୍ପାଦ ଭଲ")   # Positive
pipe("ଏ ଜିନିଷ ଖରାପ")     # Negative
pipe("ଠିକ ଅଛି")           # Neutral
```

## Community
This model is part of the **Odias in ML** initiative.
https://odisha-ml.github.io
