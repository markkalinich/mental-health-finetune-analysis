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
pipeline_tag: text-classification
---

# 🎯 FinBERT-Pro

An improved financial sentiment model built on [ProsusAI/finbert](https://huggingface.co/ProsusAI/finbert). Fine-tuned on 3 expert-annotated financial datasets for more robust sentiment classification.

The model provides softmax outputs for three sentiment classes: **Positive**, **Negative**, **Neutral**.

## 🚀 Usage

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="ENTUM-AI/FinBERT-Pro")

classifier("Stock price soars on record-breaking earnings report")
# [{'label': 'Positive', 'score': 0.99}]

classifier("Company announces quarterly earnings results")
# [{'label': 'Neutral', 'score': 0.98}]

classifier("Revenue decline signals weakening market position")
# [{'label': 'Negative', 'score': 0.98}]
```

## 📊 Training Data

Fine-tuned on 3 expert-annotated public datasets:

| Dataset | Samples |
|---------|---------|
| [FinanceInc/auditor_sentiment](https://huggingface.co/datasets/FinanceInc/auditor_sentiment) | ~4.8K |
| [nickmuchi/financial-classification](https://huggingface.co/datasets/nickmuchi/financial-classification) | ~5K |
| [warwickai/financial_phrasebank_mirror](https://huggingface.co/datasets/warwickai/financial_phrasebank_mirror) | ~4.8K |

Unlike the original FinBERT (trained on a single dataset), FinBERT-Pro combines multiple expert-annotated sources for better generalization across different financial text styles.

## 🔍 What's Different from FinBERT?

- **Multiple data sources** — trained on 3 expert-annotated datasets instead of 1
- **Class-weighted training** — handles imbalanced label distributions
- **Better generalization** — diverse training data improves robustness on unseen financial texts

## ⚠️ Limitations

- English only
- Designed for short financial texts (headlines, news, reports)
