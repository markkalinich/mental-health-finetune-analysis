---
license: mit
language:
- en
metrics:
- accuracy
base_model:
- google-bert/bert-base-uncased
pipeline_tag: text-classification
tags:
- sentiment-analysis
- bert
- imdb
- fine-tuned
- text-classification
---

# 📊 Sentiment Analysis with Fine-Tuned BERT (IMDB)

This repository contains a fine-tuned BERT model for binary sentiment classification using the IMDB movie reviews dataset. The model classifies reviews as **positive** or **negative**, and is built using Hugging Face Transformers and PyTorch.

## 🚀 Model Performance

| Metric           | Value       |
|------------------|-------------|
| Accuracy         | 89.4%       |
| Validation Loss  | 0.375       |
| Epochs Trained   | 3           |
| Inference Speed  | ~434 samples/sec |

## 🧠 Model Details

- **Base Model**: `bert-base-uncased`
- **Dataset**: IMDB (binary sentiment)
- **Framework**: Hugging Face Transformers
- **Fine-Tuning Setup**:
  - Learning rate: 2e-5
  - Batch size: 32
  - Mixed-precision: ✅ (`fp16`)
  - Early stopping: ❌ (trained for full 3 epochs)

## 🛠️ How to Use

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="Harsha901/tinybert-imdb-sentiment-analysis-model")
classifier("This movie was absolutely amazing!")
