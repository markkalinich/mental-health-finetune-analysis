---
library_name: transformers
pipeline_tag: text-classification
tags:
- sentiment-analysis
- text-classification
- video-game-reviews
- distilbert
base_model: distilbert-base-uncased
model-index:
- name: video-game-review-final-project
  results: []
---
# Video Game Review Final Project

## Model Description

This model is a fine-tuned DistilBERT model for video game review sentiment classification. The model predicts whether a video game review is positive or negative based on the language used in the review.

## Developed By

QJ Greer

## Model Type

Text classification model

## Base Model

- distilbert-base-uncased

## Task

Binary sentiment classification:

- Negative
- Positive

## Dataset

This model was trained using the `auphong2707/game-reviews-sentiment` dataset from Hugging Face. The dataset contains video game review text and sentiment labels.

Dataset link: https://huggingface.co/datasets/auphong2707/game-reviews-sentiment

## Training Details

The model was fine-tuned using the Hugging Face Transformers `Trainer`. The review text was tokenized with the DistilBERT tokenizer. Reviews were padded and truncated to a maximum length of 128 tokens.

Training setup:

- Base model: distilbert-base-uncased
- Task: binary text classification
- Epochs: 3
- Learning rate: 2e-5
- Batch size: 8
- Weight decay: 0.01
- Train/test split: 80/20

## Evaluation

The model was evaluated using:

- Accuracy
- Macro F1-score
- Classification report
- Confusion matrix
- Sample prediction testing

The goal of evaluation was to measure how well the model classified positive and negative video game reviews.

## Intended Uses

This model can be used for educational purposes and basic video game review sentiment analysis. It could help students, game developers, review websites, or gaming companies quickly understand whether player feedback is mostly positive or negative.

Example uses:

- Classifying one video game review
- Analyzing multiple reviews at once
- Summarizing player feedback
- Supporting a review dashboard or feedback tool

## Limitations

This model may struggle with sarcasm, mixed reviews, slang, short unclear comments, or reviews that include both positive and negative opinions. Since it is trained on a specific video game review dataset, it may not generalize perfectly to every gaming platform, genre, or review style.

The model should not be used as the only source for serious business decisions. Human review is still important, especially for unclear or mixed feedback.

## How to Use

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="qjgreer/video-game-review-final-project"
)

classifier("The gameplay was fun and the graphics were amazing.")