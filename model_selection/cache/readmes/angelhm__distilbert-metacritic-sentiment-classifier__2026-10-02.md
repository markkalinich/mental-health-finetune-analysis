
---
language: en
license: apache-2.0
tags:
- sentiment-analysis
- text-classification
- distilbert
- video-game-reviews
datasets:
- Wada1/Metacritic_Games_Reviews_Dataset
metrics:
- accuracy
- f1
- precision
- recall
pipeline_tag: text-classification
---

# DistilBERT Metacritic Sentiment Classifier

## Description

This model performs sentiment analysis on video game reviews from Metacritic.

It has been fine-tuned from distilbert-base-uncased using the dataset:
Wada1/Metacritic_Games_Reviews_Dataset

The model classifies reviews into:

- Positive
- Negative

Neutral reviews were removed before training.

## Dataset

Features used:

- Review → review text
- Sentiment → target label

Label mapping:

- Positive → 1
- Negative → 0

Neutral reviews were excluded.

## Evaluation Results

Performance on evaluation split:

- Accuracy: 0.8953
- F1-score: 0.9164
- Precision: 0.8886
- Recall: 0.9459

## Usage

Example:

from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="angelhm/distilbert-metacritic-sentiment-classifier"
)

result = classifier("This game is amazing. Great story and gameplay.")
print(result)

## Labels

- Positive → positive review
- Negative → negative review

## Limitations

- Only works with English text
- Trained only on Metacritic video game reviews
- May not generalize well to other domains
- Neutral sentiment is not predicted


## Demo

You can test the model interactively in the Hugging Face Space:

https://huggingface.co/spaces/angelhm/distilbert-metacritic-sentiment-classifier

Write a video game review in English and the model will predict whether the sentiment is Positive or Negative.
