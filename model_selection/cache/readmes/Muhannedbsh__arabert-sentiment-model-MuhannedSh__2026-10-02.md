---
library_name: transformers
tags:
- sentiment-analysis
- arabic
- classification
---

# Model Card for Arabic Sentiment Muhannedsh

## Model Details

### Model Description

This is a fine-tuned BERT-based Arabic sentiment analysis model, specifically adapted from the `aubmindlab/bert-base-arabertv02` model. It has been fine-tuned for binary sentiment classification tasks (positive vs. negative sentiment) and achieves excellent performance on the validation set. 

- **Developed by:** Muhanned Shaheen
- **Model type:** BERT-based model for sequence classification
- **Language(s) (NLP):** Arabic
- **License:** Apache 2.0
- **Finetuned from model:** `aubmindlab/bert-base-arabertv02`

### Model Sources

- **Repository:** https://huggingface.co/Muhannedbsh/arabert-sentiment-model-MuhannedSh

### Training Metrics
- **Training Loss:** 0.0315
- **Training Accuracy:** 99.31%
- **Training F1-Score:** 99.28%

### Validation Metrics
- **Validation Loss:** 0.2464
- **Validation Accuracy:** 92.24%
- **Validation F1-Score:** 92.89%

## Uses

### Direct Use

This model is intended to be used for binary sentiment analysis tasks in Arabic. It can classify Arabic text into positive or negative sentiment.

### Downstream Use

The model can be fine-tuned further for other tasks in Arabic text classification or sentiment analysis.

### Out-of-Scope Use

The model is not recommended for tasks involving non-Arabic text or for sentiment analysis with more than two classes.

## Bias, Risks, and Limitations

### Recommendations

Users should be aware that the model's performance is tied to the data used during fine-tuning. Biases in the dataset could affect predictions.

## How to Get Started with the Model

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name = "muhannedshaheen/Arabic_Sentiment_Muhannedsh"

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Example
text = "هذا المنتج رائع جدا"
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)
print(outputs.logits)