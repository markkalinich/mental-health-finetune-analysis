---
license: apache-2.0
language:
- ar
base_model:
- Kalmundi/Q8BERTA
tags:
- transformers
- safetensors
- sentiment-analysis
---


# Fine-Tuned SA-Q8BERTA Model for Sentiment Analysis

This model is a fine-tuned version of [Kalmundi/Q8BERTA](https://huggingface.co/Kalmundi/Q8BERTA), which was trained on a customized dataset for sentiment analysis.
This model mainly focuses on Sentiment Analysis for the Kuwaiti Dialect.

## Model Details

- **Base Model**: The original model is [Kalmundi/Q8BERTA](https://huggingface.co/Kalmundi/Q8BERTA), a transformer-based model pre-trained on a sufficient size Kuwaiti Dialect dataset.
- **Fine-Tuning**: This model was fine-tuned on a dataset for sentiment analysis related to Kuwaiti Dialect, and it can classify text as either positive or negative.
- **Fine-Tuning Task**: The model was fine-tuned for 5 epochs with a learning rate of `2e-5`.

## Model Usage

To use the model for sentiment analysis:

```python
from transformers import pipeline

# Load the fine-tuned model
classifier = pipeline("text-classification", model="Kalmundi/Q8BERTA-SA")

# Test the classifier
result = classifier("الجو اليوم وايد حلو")
print(result)