---
language: en
license: mit
datasets: imdb
tags:
  - sentiment-analysis
  - transformers
  - huggingface
---

# 🎬 IMDb Sentiment Classifier  
This is a fine-tuned **DistilBERT model** for analyzing sentiment in IMDb movie reviews.

## 📌 Dataset
- **Source:** IMDb dataset from Hugging Face Datasets  
- **Task:** Binary classification (Positive / Negative)

## 📌 Training Details
- **Model:** `distilbert-base-uncased`
- **Learning rate:** `2e-5`
- **Batch size:** `4`
- **Epochs:** `1`
- **Loss function:** CrossEntropyLoss

## 📌 Evaluation Results
| Metric     | Score  |
|------------|--------|
| Accuracy   | 92.5%  |
| F1-score   | 92.6%  |
| Precision  | 92.9%  |
| Recall     | 92.3%  |

## 📌 How to Use
```python
from transformers import pipeline

classifier = pipeline("text-classification", model="Camilla9000/imdb-sentiment-classifier")
print(classifier("This movie was amazing!"))
