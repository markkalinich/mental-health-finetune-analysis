---
language: en
license: apache-2.0
tags:
- sentiment-analysis
- finance
- indian-finance
- finbert
- text-classification
- nlp
datasets:
- kdave/Indian_Financial_News
metrics:
- accuracy
- f1
---

# FinBERT-Indian-Sentiment

## Overview
**FinBERT-Indian-Sentiment** is a fine-tuned financial sentiment analysis model designed specifically for **Indian financial news and market-related text**.

The model classifies input text into three sentiment categories:
- **Negative**
- **Neutral**
- **Positive**

It is based on **ProsusAI/finbert** and fine-tuned on an India-focused financial news dataset to better capture domain-specific language such as RBI policy statements, market movements, and macroeconomic commentary.

---

## Motivation
Generic financial sentiment models often struggle with:
- Indian market terminology
- RBI policy language
- Macro-economic neutrality
- Mixed-signal financial news

This model aims to improve sentiment understanding in the **Indian financial context**, where cautious and neutral language is common.

---

## Training Data
- **Dataset**: `kdave/Indian_Financial_News`
- **Total samples**: ~22,000
- **Classes**: Negative, Neutral, Positive
- **Split**: 85% training / 15% test (stratified)

The dataset consists of Indian financial news articles covering:
- Stock markets
- Banking and finance
- RBI announcements
- Corporate earnings
- Macroeconomic indicators

---

## Model Details
- **Base model**: ProsusAI/finbert
- **Architecture**: BERT-based sequence classification
- **Number of labels**: 3
- **Label mapping**:
  - `0` → Negative  
  - `1` → Neutral  
  - `2` → Positive
- **Max sequence length**: 512
- **Framework**: PyTorch / Hugging Face Transformers

---

## Evaluation Results
Evaluation was performed on a held-out test set.

| Metric | Score |
|------|------|
| Accuracy | ~0.89 |
| Weighted F1-score | ~0.89 |

### Confusion Matrix Summary
- Strong diagonal dominance across all classes
- Minimal confusion between **positive** and **negative**
- Neutral sentiment remains the most challenging class (expected for financial text)
- False positives and false negatives remain below 10% across classes

These results indicate balanced and reliable performance suitable for real-world applications.

---

## Intended Use
This model is suitable for:
- Financial news sentiment analysis
- Market sentiment monitoring
- Academic and research projects
- NLP experimentation in finance
- Backend APIs for sentiment classification

---

## Limitations
- Long, mixed-signal macroeconomic articles may lead to overconfident predictions
- Neutral sentiment may lean toward positive or negative in ambiguous cases
- Confidence calibration may be required for high-stakes production use

⚠️ This model is **not intended for investment advice or automated trading decisions**.

---