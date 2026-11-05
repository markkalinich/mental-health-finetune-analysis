---
language:
- en
license: mit
tags:
- text-classification
- sentiment-analysis
- distilbert
- amazon-reviews
- nlp
datasets:
- amazon_polarity
metrics:
- accuracy
- f1
---
# 🛍️ pranalyzer — Sentiment Analysis Model

Fine-tuned **DistilBERT** on Amazon product reviews for binary sentiment classification (POSITIVE / NEGATIVE).

Part of the [pranalyzer](https://github.com/Vedant-Nagarkar/product-review-analyzer) end-to-end NLP pipeline.

---

## 📊 Model Performance

| Metric | Score |
|---|---|
| Accuracy | 93.00% |
| F1 Score | 0.9299 |
| Loss | 0.1923 |

- **Dataset**: `amazon_polarity` (5,000 train / 1,000 test samples)
- **Hardware**: T4 GPU (Google Colab)
- **Epochs**: 3
- **Batch size**: 32
- **Learning rate**: 2e-5

---

## 🚀 Quick Start
```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="Ved2001/pranalyzer"
)

result = classifier("This product is absolutely amazing!")
print(result)
# [{'label': 'POSITIVE', 'score': 0.98}]
```

---

## 🏋️ Training Details

**Base model**: `distilbert-base-uncased`  
**Task**: Binary sentiment classification  
**Labels**: `NEGATIVE (0)`, `POSITIVE (1)`  
**Dataset**: Amazon Polarity — 3.6M reviews (sampled 5K for fine-tuning)

---

## 🔍 Part of pranalyzer Pipeline

This model is the sentiment component of a 4-model pipeline:

| Task | Model |
|---|---|
| **Sentiment** | `Ved2001/pranalyzer` (this model) |
| Category | `facebook/bart-large-mnli` |
| Aspects | `cross-encoder/nli-roberta-base` |
| Summary | `facebook/bart-large-xsum` |

---

## 👤 Author

**Vedant Nagarkar**  
[GitHub](https://github.com/Vedant-Nagarkar) • [HuggingFace](https://huggingface.co/Ved2001)