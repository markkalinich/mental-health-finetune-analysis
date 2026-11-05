---
language: en
license: apache-2.0
tags:
  - finance
  - sentiment-analysis
  - indian-stock-market
  - nse
  - bse
  - finbert
  - text-classification
datasets:
  - financial_phrasebank
metrics:
  - accuracy
  - f1
pipeline_tag: text-classification
---

# FinEdgeX-Sentiment

A specialized financial sentiment analysis model fine-tuned for the **Indian stock market** (NSE/BSE).

## Model Description

FinEdgeX-Sentiment is built on top of [FinBERT](https://huggingface.co/ProsusAI/finbert) and further fine-tuned with:
- **Financial PhraseBank** (4,840 sentences with 66%+ annotator agreement)
- **Custom Indian Market Dataset** (55 curated examples covering NSE, BSE, SEBI, RBI contexts)

## Labels

| Label | Description |
|-------|-------------|
| BULLISH | Positive financial sentiment (growth, profit, upgrades) |
| BEARISH | Negative financial sentiment (losses, downgrades, risks) |
| NEUTRAL | No strong directional sentiment |

## Usage

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="Somadhi-Chaitanya-09/finedgex-sentiment")
result = classifier("Reliance Industries reports record quarterly profit of ₹19,878 crores")
print(result)
# [{'label': 'BULLISH', 'score': 0.97}]
```

## Training

- **Base Model:** ProsusAI/finbert
- **Framework:** PyTorch + HuggingFace Transformers
- **Training Data:** Financial PhraseBank + Custom Indian Market Data
- **Epochs:** 5 (with early stopping)
- **Learning Rate:** 2e-5
- **Batch Size:** 16

## Built By

[FinEdgeX](https://fin-edge-x.vercel.app) — AI-Powered Indian Stock Market Intelligence Platform

## License

Apache 2.0
