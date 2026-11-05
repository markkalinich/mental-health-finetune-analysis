---
language: az
license: mit
tags:
- sentiment-analysis
- azerbaijani
- bert
datasets:
- hajili/azerbaijani_review_sentiment_classification
base_model: allmalab/bert-base-aze
metrics:
- accuracy
- f1
---

# AzSentiment - Azerbaijani Sentiment Analysis

Fine-tuned aLLMA-BASE model for binary sentiment classification of Azerbaijani customer reviews.

## Model Performance

| Metric | Test Score |
|--------|------------|
| Accuracy | 93.3% |
| F1 Score | 96.2% |

## Usage

from transformers import pipeline
classifier = pipeline("text-classification", model="StartZer0/az-sentiment-bert")
classifier("Bu mehsul cox yaxsidir!")

## Citation

@inproceedings{isbarov-etal-2024-open,
    title = "Open foundation models for Azerbaijani language",
    author = "Isbarov, Jafar and Huseynova, Kavsar and Mammadov, Elvin and Hajili, Mammad and Ataman, Duygu",
    booktitle = "SIGTURK 2024",
    year = "2024",
    url = "https://aclanthology.org/2024.sigturk-1.2"
}
