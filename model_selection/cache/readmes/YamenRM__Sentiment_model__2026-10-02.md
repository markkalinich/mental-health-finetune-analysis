---
language: en
tags:
- sentiment-analysis
- text-classification
- transformers
- distilbert
datasets:
- lakshmi25npathi/imdb-dataset-of-50k-movie-reviews
model-index:
- name: DistilBERT Sentiment Classifier
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      name: IMDB Dataset of 50K Movie Reviews
      type: text
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.93
    - name: F1
      type: f1
      value: 0.93
    - name: Precision
      type: precision
      value: 0.93
    - name: Recall
      type: recall
      value: 0.93
license: apache-2.0
metrics:
- accuracy
- precision
- recall
---


# DistilBERT Sentiment Classifier
## Model Details

 - Model Type: Transformer-based classifier (DistilBERT)

 - Base Model: distilbert-base-uncased

 - Language: English

 - Task: Sentiment Analysis (binary classification)

**Labels:**

0 → Negative

1 → Positive

Framework: Hugging Face Transformers

## Intended Uses & Limitations

#### Intended Use:

Sentiment classification of English reviews, comments, or feedback.

Not Intended Use:

Other languages.

Multi-label sentiment tasks (neutral/mixed).

## ⚠️ Limitations:

 - May not generalize well outside movie/review-style data.

 - Training data may contain cultural and linguistic bias.

## Training Dataset

 - Source: Kaggle Cleaned IMDB Reviews Dataset

 - Size: ~50,000 reviews

 - Classes: positive, negative

 - Converted to integers: positive → 1, negative → 0

## Training Procedure

 - Epochs: 3

 - Batch Size: 16

 - Optimizer: AdamW

 - Learning Rate: 5e-5

 - Framework: Hugging Face Trainer API

## Evaluation

The model was tested on a held-out validation set of 9,917 reviews.

Class	Precision	Recall	F1-score	Support
Negative (0)	0.93	0.93	0.93	4,939
Positive (1)	0.93	0.93	0.93	4,978

## Overall

 - Accuracy: 93%

 - Macro Avg F1: 0.93

 - Weighted Avg F1: 0.93


## How to Use
```
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

model_name = "YamenRM/distilbert-sentiment-classifier"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

nlp = pipeline("text-classification", model=model, tokenizer=tokenizer)

print(nlp("I really loved this movie, it was amazing!"))
```
```
# [{'label': 'POSITIVE', 'score': 0.98}]
```