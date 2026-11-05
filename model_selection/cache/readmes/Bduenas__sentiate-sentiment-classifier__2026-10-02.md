---
license: apache-2.0
language: en
tags:
  - sentiment
  - roberta
  - amazon
  - 4-class
  - text-classification
datasets:
  - amazon_polarity
metrics:
  - accuracy
  - f1
pipeline_tag: text-classification
base_model: roberta-base
---

# Sentiate: Amazon Review Sentiment Classifier (4-Class, RoBERTa)

`sentiate-sentiment-classifier` is a fine-tuned RoBERTa model built to classify **Amazon Electronics product reviews** into one of **four sentiment classes**:

- **0 — Low Sentiment** (strongly negative)
- **1 — Medium-Low** (somewhat negative/mixed)
- **2 — Medium-High** (somewhat positive)
- **3 — High Sentiment** (strongly positive)

## 🔍 Use Cases
- eCommerce product research
- Dropshipping product analysis
- Brand sentiment tracking
- Batch review scoring at scale

## 🧠 Model Details
- Base: `roberta-base`
- Trained on: 394,000 Amazon Electronics reviews
- Framework: Hugging Face Transformers
- Classes: 4-class multi-class sentiment
- Evaluation Accuracy: ~81.9%
- F1 Score: ~0.80 (weighted)

## 🚀 How to Use

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained("your-username/sentiate-sentiment-classifier")
tokenizer = AutoTokenizer.from_pretrained("your-username/sentiate-sentiment-classifier")

text = "This charger broke after one week. I'm disappointed."
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
outputs = model(**inputs)
sentiment = outputs.logits.argmax().item()
