---
language:
- en
library_name: transformers
pipeline_tag: text-classification
tags:
- emotion-classification
- distilbert
- text-classification
---

# Emotion Classification with DistilBERT

## Model Description

A DistilBERT model fine-tuned for six-class English emotion
classification.

## Base Model

`distilbert/distilbert-base-uncased`

## Dataset

`dair-ai/emotion`

The dataset contains six emotion classes:
sadness, joy, love, anger, fear, and surprise.

## Task

Text classification.

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="stake52/emotion-distilbert"
)

result = classifier("I am very happy today!")
print(result)
```

## Evaluation

The model was evaluated using accuracy and macro-F1 on the
held-out test split. Report the exact values from the completed
run.

## Limitations

Emotion classification is subjective and text can contain
multiple or ambiguous emotions. Predictions should not be
interpreted as reliable measurements of a person's mental state.

## Intended Use

Educational projects, NLP experimentation, and research.
