---
library_name: transformers
tags:
  - text-classification
  - transformers
  - distilbert
  - sentiment-analysis
  - huggingface
---

# Model Card for `r831/finetuned-distilbert-sentiment`

A binary sentiment classifier based on `distilbert-base-uncased`, fine-tuned on the IMDB dataset using the 🤗 Transformers `Trainer` API and Hugging Face Datasets. This model can classify movie reviews as either **positive** or **negative**.

---

## Model Details

### Model Description

This model is a fine-tuned version of `distilbert-base-uncased`, a lightweight transformer model developed by Hugging Face, designed for sequence classification tasks.

- **Developed by:** `r831`
- **Model type:** Transformer-based binary classifier
- **Language(s):** English
- **License:** Apache 2.0 (inherited from DistilBERT)
- **Finetuned from model:** `distilbert-base-uncased`

### Model Sources

- **Repository:** https://huggingface.co/r831/finetuned-distilbert-sentiment
- **Paper (DistilBERT):** https://arxiv.org/abs/1910.01108

---

## Uses

### Direct Use

You can directly use this model to classify movie reviews or other short English texts into **positive** or **negative** sentiment using Hugging Face Pipelines or Transformers.

### Downstream Use

Can be embedded in apps for:
- Review moderation
- Opinion mining
- User feedback classification

### Out-of-Scope Use

- Multilingual sentiment analysis
- Domain-specific sentiment tasks without re-finetuning

---

## Bias, Risks, and Limitations

The model was trained on the IMDB movie review dataset and may not generalize well to other domains (e.g., financial reviews, product reviews). It may reflect biases present in the IMDB dataset.

### Recommendations

Avoid deploying this model in sensitive domains without further fine-tuning and evaluation. For critical applications, human review is recommended.

---

## How to Get Started with the Model

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="r831/finetuned-distilbert-sentiment")
result = classifier("The movie was absolutely fantastic!")
print(result)
