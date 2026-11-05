---
language: en
license: apache-2.0
tags:
- text-classification
- sentiment-analysis
- distilbert
- imdb
- huggingface
datasets:
- imdb
metrics:
- accuracy
---

# DistilBERT Sentiment Analysis (IMDB)

This model is a fine-tuned version of **DistilBERT-base-uncased** for **binary sentiment classification** on movie reviews.

It classifies reviews as **Positive** or **Negative**.

## Model Details

- **Base Model**: distilbert-base-uncased
- **Dataset**: IMDB Movie Reviews (25k train, 25k test)
- **Task**: Sentiment Analysis (Positive / Negative)
- **Training**: Fine-tuned using Hugging Face Trainer API

## Results

- **Accuracy on small subset (2k examples)**: **89.0%**
- Expected accuracy on full dataset: **~92-94%**

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis", 
    model="kckdeepak/imdb-distilbert-sentiment-analysis"
)

result = classifier("This movie was fantastic!")
print(result)