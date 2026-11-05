---
language:
  - ru
license: mit
tags:
  - sentiment-analysis
  - russian
  - brand-monitoring
  - roberta
  - text-classification
datasets:
  - MonoHime/ru_sentiment_dataset
  - DmitrySharonov/ru_sentiment_neg_pos_neutral
  - mteb/SentiRuEval2016
base_model: ai-forever/ruRoBERTa-large
pipeline_tag: text-classification
metrics:
  - f1
---

# ProdRadar Sentiment v2 — ruRoBERTa-large

Fine-tuned [ai-forever/ruRoBERTa-large](https://huggingface.co/ai-forever/ruRoBERTa-large) (355M params) for Russian sentiment analysis with advanced training techniques.

## Metrics (28K test set)

| Metric | Score |
|---|---|
| **F1-macro** | **0.868** |
| F1-positive | 0.917 |
| F1-negative | 0.918 |
| F1-neutral | 0.770 |

## Training

- **Data**: 318K samples from 4 open-source Russian datasets + 188K proprietary + 10K synthetic
- **Techniques**: LLRD + Focal Loss + FGM Adversarial Training + R-Drop
- **Hardware**: NVIDIA L4 GPU, ~4.5 hours
- **Labels**: positive (0), negative (1), neutral (2)

## Usage

```python
from transformers import pipeline
classifier = pipeline("text-classification", model="Daniil125/prodradar-sentiment-ru")
result = classifier("Ужасный сервис!")
```
