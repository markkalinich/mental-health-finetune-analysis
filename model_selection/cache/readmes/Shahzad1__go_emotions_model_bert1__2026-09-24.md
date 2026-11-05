---
pipeline_tag: text-classification
library_name: transformers
base_model: distilbert-base-uncased
tags:
  - pytorch
  - goemotions
  - emotion-classification
  - distilbert
---

# Go Emotions Classifier (DistilBERT)

This model is a fine-tuned version of `distilbert-base-uncased` on the [GoEmotions dataset](https://github.com/google-research/google-research/tree/master/goemotions). It is designed to detect multiple emotions in English text, supporting **multi-label text classification**.

## 🧠 Model Details

- **Base model**: DistilBERT (`distilbert-base-uncased`)
- **Framework**: PyTorch
- **Task**: Multi-label Emotion Classification
- **Training data**: GoEmotions (Google Research)
- **Labels**: 27 emotions + neutral (e.g. joy, sadness, anger, surprise, etc.)

## ✨ Example Usage

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="Shahzad1/go_emotions_model_bert1", top_k=None)
result = classifier("I'm feeling optimistic and excited for what's to come!")
print(result)
