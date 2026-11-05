---
language: en
license: apache-2.0
tags:
- text-classification
- sentiment-analysis
- product-reviews
- distilbert
- fine-tuned
datasets:
- amazon_polarity
metrics:
- accuracy
- f1
---

# 🛍️ Product Review Sentiment Classifier

A fine-tuned **DistilBERT** model for classifying product reviews as **Positive** or **Negative**.

Fine-tuned on the Amazon Polarity dataset with 5,000 training samples.

## 📊 Model Performance

| Metric | Score |
|--------|-------|
| Accuracy | 92.10% |
| F1 Score | 0.9210 |

## 🚀 Usage

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="JuhiSaxena2002/opinion-mining")

result = classifier("This product is absolutely amazing! Best purchase ever.")
print(result)  # [{'label': 'POSITIVE', 'score': 0.99}]

result = classifier("Terrible quality. Broke after one day. Very disappointed.")
print(result)  # [{'label': 'NEGATIVE', 'score': 0.98}]
```

## 🏗️ Model Architecture

- **Base Model:** `distilbert-base-uncased`
- **Task:** Binary Sequence Classification
- **Labels:** `POSITIVE`, `NEGATIVE`
- **Max Sequence Length:** 128 tokens
- **Training Epochs:** 3

## 📦 Training Details

- **Dataset:** Amazon Polarity
- **Train samples:** 5,000
- **Test samples:** 1,000
- **Learning Rate:** 2e-5
- **Batch Size:** 32
- **Optimizer:** AdamW with warmup

## 🙋 Author

Built and fine-tuned by [JuhiSaxena2002](https://huggingface.co/JuhiSaxena2002)
