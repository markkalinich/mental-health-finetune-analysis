---
tags:
- sentiment-analysis
- finance
- stock-market
- english
pipeline_tag: text-classification
license: mit
language: en
---

# 🧠 FinancialBERT Sentiment Analysis (FinNews Binary)

This is a fine-tuned BERT model for **binary sentiment classification** of financial news headlines, adapted for real-time **stock market sentiment prediction**.

## 🔍 Model Details

- **Architecture**: BERT (12-layer, 768-hidden, 12-heads)
- **Base model**: `ahmedrachid/FinancialBERT-Sentiment-Analysis`
- **Fine-tuned task**: Binary classification – `Positive` or `Negative`
- **Problem type**: `single_label_classification`
- **Special tokens**: `[CLS]`, `[SEP]`, `[PAD]`, `[MASK]`, `[UNK]`

Neutral headlines are **mapped to Positive** to simplify binary output.

## 🧾 Training Summary

- **Dataset**: 5,000+ manually labeled financial news headlines
- **Tokenizer**: Custom WordPiece tokenizer
- **Max sequence length**: 128
- **Framework**: Transformers v4.51.3 (PyTorch backend)
- **Output labels**:
  - `LABEL_0 = Negative`
  - `LABEL_1 = Positive`

## 📈 Intended Use

Ideal for:

- Real-time market sentiment dashboard
- Trading signal pipelines
- Event-driven NLP analysis

## 🚀 Usage (Example)

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="your-username/your-model-name")
classifier("Apple's Q4 earnings beat expectations amid strong iPhone sales")
# Output: [{'label': 'LABEL_1', 'score': 0.98}]
