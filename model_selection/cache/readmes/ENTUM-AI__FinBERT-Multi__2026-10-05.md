---
language:
- en
license: apache-2.0
library_name: transformers
tags:
- text-classification
- bert
- finbert
- finance
- sentiment
- sentiment-analysis
- financial-sentiment
datasets:
- FinanceInc/auditor_sentiment
- nickmuchi/financial-classification
- warwickai/financial_phrasebank_mirror
- NOSIBLE/financial-sentiment
- TimKoornstra/financial-tweets-sentiment
pipeline_tag: text-classification
---

# 🎯 FinBERT-Multi

Financial sentiment analysis model. Fine-tuned [ProsusAI/finbert](https://huggingface.co/ProsusAI/finbert) on **143K+ samples** from 5 combined financial datasets.

The model outputs softmax outputs for three sentiment classes: **Positive**, **Negative**, **Neutral**.

## 🚀 Usage

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="ENTUM-AI/FinBERT-Multi")

classifier("Stock price soars on record-breaking earnings report")
# [{'label': 'Positive', 'score': 0.99}]

classifier("Company announces quarterly earnings results")
# [{'label': 'Neutral', 'score': 0.98}]

classifier("Revenue decline signals weakening market position")
# [{'label': 'Negative', 'score': 0.97}]
```

## 📊 Training Data

| Dataset | Samples |
|---------|---------|
| [FinanceInc/auditor_sentiment](https://huggingface.co/datasets/FinanceInc/auditor_sentiment) | ~4.8K |
| [nickmuchi/financial-classification](https://huggingface.co/datasets/nickmuchi/financial-classification) | ~5K |
| [warwickai/financial_phrasebank_mirror](https://huggingface.co/datasets/warwickai/financial_phrasebank_mirror) | ~4.8K |
| [NOSIBLE/financial-sentiment](https://huggingface.co/datasets/NOSIBLE/financial-sentiment) | ~100K |
| [TimKoornstra/financial-tweets-sentiment](https://huggingface.co/datasets/TimKoornstra/financial-tweets-sentiment) | ~38K |

## ⚠️ Limitations

- English only
