---
library_name: transformers
license: apache-2.0
base_model: bert-base-uncased
tags:
- sentiment-analysis
- text-classification
- bert
- transformers
- pytorch
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: finetuned-bert-sentiment
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      name: IMDb Movie Reviews
      type: imdb
    metrics:
      - type: accuracy
        value: 0.9225
      - type: f1
        value: 0.9238
      - type: precision
        value: 0.9086
      - type: recall
        value: 0.9395
---

# 🎬 Finetuned BERT for Sentiment Analysis

This model is a fine-tuned version of **BERT (bert-base-uncased)** for binary sentiment classification (positive vs negative).

It is trained on the **IMDb movie reviews dataset**, a widely used benchmark for sentiment analysis tasks.

---

## 🚀 Model Performance

| Metric     | Score  |
|------------|--------|
| Accuracy   | 92.25% |
| F1 Score   | 92.38% |
| Precision  | 90.86% |
| Recall     | 93.95% |

### Confusion Matrix Insights
- Strong balance between positive and negative predictions  
- Slight tendency toward higher recall (fewer false negatives)  
- Overall robust generalization on full test dataset (25,000 samples)

---

## 📌 Model Description

This project demonstrates fine-tuning of a pre-trained Transformer model for NLP classification tasks using the Hugging Face ecosystem.

Key features:
- Pretrained **BERT encoder**
- Fine-tuned for **binary sentiment classification**
- Implemented using **Hugging Face Transformers Trainer API**
- Evaluated using standard classification metrics

---

## 📊 Dataset

- **Name:** IMDb Movie Reviews Dataset  
- **Size:**  
  - Train: 25,000 samples  
  - Test: 25,000 samples  
- **Classes:**  
  - `0` → Negative  
  - `1` → Positive  

The dataset is balanced across both classes.

---

## 🏋️ Training Procedure

### Hyperparameters

- Learning rate: `2e-5`
- Batch size: `8`
- Epochs: `2`
- Optimizer: AdamW
- Scheduler: Linear decay
- Mixed precision: Enabled (FP16)

### Training Details

- Framework: Hugging Face `Trainer`
- Hardware: Google Colab GPU
- Loss function: Cross-entropy

---

## 🧠 Intended Use

This model can be used for:
- Sentiment analysis on movie reviews
- Product review classification
- Social media sentiment detection
- NLP learning and experimentation

---

## ⚠️ Limitations

- Trained only on English text
- Domain-specific (movie reviews) → may not generalize perfectly to other domains
- Binary classification only (no neutral sentiment)
- May inherit biases present in training data

---

## 🛠️ How to Use

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="ashwini10521/finetuned_bert")

result = classifier("This movie was absolutely amazing!")
print(result)