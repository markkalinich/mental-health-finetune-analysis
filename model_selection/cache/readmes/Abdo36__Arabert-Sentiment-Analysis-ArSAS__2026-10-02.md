---
language: ar
tags:
  - arabic
  - sentiment-analysis
  - Farasa
  - AraBERT
datasets:
  - ArSAS
license: apache-2.0
---

# Arabert Sentiment Model with Farasa Preprocessing

This is a fine-tuned version of `AraBERT` using the ArSAS dataset for **sentiment analysis**.
The text was preprocessed using **Farasa** for optimal tokenization of Arabic text.

## Model Details

- **Base Model**: AraBERT v2
- **Dataset**: ArSAS (Arabic Sentiment Analysis)
- **Preprocessing**: Farasa Tokenization
- **Tasks**: Sentiment Classification (`negative`, `neutral`, `positive` , `mixed`)

## Usage

```python
from transformers import pipeline

sentiment_pipeline = pipeline(
    task="text-classification",
    model="Abdo36/Arabert-Sentiment-Analysis-ArSAS"
)

result = sentiment_pipeline("هذا المنتج رائع للغاية")
print(result)
```

## Training Details

- **Number of Epochs**: 2

- **Training Loss**: 0.6

- **Validation Accuracy**: 0.5
