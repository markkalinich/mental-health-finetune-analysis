---
tags:
- DistilRoBERTa
- fine-tune
- financial
- crypto
- sentiment
library_name: transformers
pipeline_tag: text-classification
---
# Crypto Sentiment Classifier - DistilRoBERTa

## Model Description
This fine-tuned DistilRoBERTa model classifies financial/crypto tweets into BEARISH (0), BULLISH (1), or NEUTRAL (2) sentiments. Trained on 9.5k+ Twitter financial news samples with class weighting for imbalance.

## Intended Uses
- Real-time sentiment analysis on crypto tweets.
- Integration into trading bots or dashboards.

## Performance
| Metric | Value |
|--------|-------|
| Eval F1 (weighted) | 0.8811 |
| Accuracy | 0.8790 |

## Limitations & Bias
- Heavy Neutral skew may underperform on extreme sentiments.
- Trained on general financial tweets; fine-tune further for pure crypto jargon.