---
language: en
license: mit
tags:
- sentiment-analysis
- text-classification
- distilbert
datasets:
- custom
metrics:
- accuracy:  0.9512
- f1:        0.9526
- precision: 0.9489
- recall:    0.9564
---

# DistilBERT Sentiment Classifier

A fine-tuned DistilBERT model for binary sentiment classification, trained on a custom dataset (with VADER features).

## Usage

    from transformers import pipeline
    classifier = pipeline("sentiment-analysis", model="waseemrazakhan/distilbert-sentiment-classifier")
    print(classifier("I really enjoyed this movie!"))

## Training & Evaluation

- Base model: `distilbert-base-uncased`
- Epochs: 3  
- Batch size: 8  
- Max sequence length: 128  

| Metric    | Value   |
|:---------:|:-------:|
| Accuracy  | 0.9512 |
| F1 Score  | 0.9526       |
| Precision | 0.9489|
| Recall    | 0.9564   |

## Limitations

- English-only
- May not generalize to very different domains
