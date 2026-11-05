---
language:
- ur
license: apache-2.0
tags:
- text-classification
- sentiment-analysis
- urdu
- bert
- fine-tuned
- nlp
datasets:
- mirfan899/imdb_urdu_reviews
metrics:
- accuracy
- f1
model-index:
- name: urdu-sentiment-classifier
  results:
  - task:
      type: text-classification
    dataset:
      name: IMDB Urdu Reviews
      type: mirfan899/imdb_urdu_reviews
    metrics:
    - type: accuracy
      value: 0.81
    - type: f1
      value: 0.8098
---

# Urdu Sentiment Classifier 🇵🇰

A fine-tuned **bert-base-multilingual-cased** model for **Urdu sentiment analysis** — classifying Urdu text as positive or negative.

## Live Demo

 [Try it on HuggingFace Spaces](https://huggingface.co/spaces/H-Layba/urdu-sentiment-classifier)

## Performance

| Metric | Score |
|--------|-------|
| Accuracy | 81.00% |
| F1 Score (weighted) | 0.8098 |

## Example Predictions

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="H-Layba/urdu-sentiment-classifier")

classifier("یہ فلم بہت اچھی تھی")
# [{'label': 'positive', 'score': 0.9936}]

classifier("آج کا دن بہت برا تھا")
# [{'label': 'negative', 'score': 0.9918}]
```

## Training Details

- **Base model:** bert-base-multilingual-cased
- **Dataset:** 50,000 Urdu movie reviews
- **Epochs:** 5
- **Learning rate:** 2e-5
- **Batch size:** 32 (train), 64 (eval)
- **Hardware:** Kaggle T4 GPU
- **Mixed precision:** fp16

## Dataset

Trained on `mirfan899/imdb_urdu_reviews` — 50,000 Urdu translations of IMDB movie reviews with positive/negative sentiment labels.

## Part of Urdu NLP Suite

This model is part of a larger collection of fine-tuned Urdu NLP models:
- [x] Sentiment Classification ← this model
- [ ] Text Summarization
- [ ] Question Answering  
- [ ] Urdu → English Translation