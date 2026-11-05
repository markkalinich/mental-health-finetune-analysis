---
language:
- en
license: other
base_model: distilbert-base-uncased
tags:
- text-classification
- emotion-classification
- distilbert
pipeline_tag: text-classification
metrics:
- accuracy
- f1
---

# DistilBERT Emotion Classifier

This model is a fine-tuned `distilbert-base-uncased` classifier for the six-class `emotion` dataset.

## Labels

| ID | Label |
| ---: | --- |
| 0 | sadness |
| 1 | joy |
| 2 | love |
| 3 | anger |
| 4 | fear |
| 5 | surprise |

## Validation Results

| Metric | Score |
| --- | ---: |
| Accuracy | 0.941 |
| Weighted F1 | 0.941 |
| Macro F1 | 0.915 |

## Usage

```python
from transformers import pipeline

classifier = pipeline("text-classification", model=".")
print(classifier("I saw a movie today and it was really good."))
```

