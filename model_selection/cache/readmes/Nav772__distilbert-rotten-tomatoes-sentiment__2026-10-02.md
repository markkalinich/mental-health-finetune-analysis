
---
license: mit
language: en
datasets:
- rotten_tomatoes
metrics:
- accuracy
pipeline_tag: text-classification
tags:
- sentiment-analysis
- distilbert
---

# DistilBERT Fine-tuned on Rotten Tomatoes

## Model Description

This model is a fine-tuned version of `distilbert-base-uncased` for binary sentiment classification (positive/negative movie reviews).

## Training Data

- **Dataset**: Rotten Tomatoes movie reviews
- **Train samples**: 8,530
- **Test samples**: 1,066

## Training Procedure

- **Base model**: distilbert-base-uncased
- **Epochs**: 3
- **Batch size**: 16
- **Learning rate**: 2e-5
- **Max sequence length**: 128

## Evaluation Results

- **Accuracy**: ~85% on test set

## Usage
```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="Nav772/distilbert-rotten-tomatoes-sentiment")
result = classifier("This movie was great!")
print(result)
```

## Limitations

- Trained only on movie reviews; may not generalize to other domains
- English language only
- Binary classification only (no neutral category)
