
---
language: en
license: apache-2.0
tags:
- sentiment-analysis
- imdb
- text-classification
datasets:
- imdb
model_name: Finetuned IMDB Sentiment Model
---

# Finetuned IMDB Sentiment Model 🎬✨

This model is a fine-tuned version of **distilbert-base-uncased** on the IMDB dataset.
It classifies movie reviews as **positive (1)** or **negative (0)**.

## 📊 Training Details
- Optimizer: AdamW
- Learning Rate: 2e-5
- Batch size: 16
- Epochs: 3
- Train/Test split: 80/20

## 📈 Evaluation
The model achieves around **89.52% accuracy** on the test set.

## 🚀 Usage
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

tokenizer = AutoTokenizer.from_pretrained("SabaAnver/finetuned-imdb-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("SabaAnver/finetuned-imdb-sentiment")

nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
print(nlp("This movie was amazing!"))
```