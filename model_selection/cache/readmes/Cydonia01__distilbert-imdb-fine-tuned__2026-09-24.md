---
license: apache-2.0
language:
- en
metrics:
- accuracy
base_model:
- distilbert/distilbert-base-uncased
pipeline_tag: text-classification
tags:
- sentiment-analysis
- imdb
- distilbert
---

# DistilBERT fine-tuned on IMDB

This model is a fine-tuned version of `distilbert-base-uncased` on the [IMDB movie reviews dataset](https://huggingface.co/datasets/imdb) for binary sentiment classification (positive/negative). It was trained using Hugging Face's `Trainer` API.

## Model Details

- **Base model:** distilbert-base-uncased
- **Fine-tuned on:** IMDB dataset
- **Language:** English
- **Task:** Sentiment classification (positive vs. negative)
- **License:** Apache-2.0

## Usage

You can load and use this model with:

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="Cydonia01/distilbert-imdb-fine-tuned")
classifier("The movie was absolutely amazing!")
```

## Training Details

- Epochs: 3
- Batch size: 16
- Max sequence length: 512
- Optimizer: AdamW
- Loss: CrossEntropyLoss
- Evaluation metric: Accuracy

## Evaluation

- Dataset: IMDB test set (25,000 samples)
- Accuracy: 93.46%

## Limitations & Biases

This model is trained only on movie reviews and may not generalize well to other domains. It may also inherit biases present in the IMDB dataset.

## Author

- Cydonia01