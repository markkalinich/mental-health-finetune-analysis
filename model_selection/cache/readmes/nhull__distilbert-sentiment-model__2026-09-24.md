---
license: apache-2.0
datasets:
- nhull/tripadvisor-split-dataset-v2
language:
- en
base_model:
- distilbert/distilbert-base-uncased
tags:
- nlp
- hotels
- reviews
- sentiment-analysis
- transformers
---
# DistilBERT Sentiment Analysis Model

## Overview

This repository contains a fine-tuned **DistilBERT** model trained for sentiment analysis on TripAdvisor reviews. The model predicts sentiment scores on a scale of 1 to 5 based on review text.

- **Base Model**: `distilbert-base-uncased`
- **Trained Dataset**: [nhull/tripadvisor-split-dataset-v2](https://huggingface.co/datasets/nhull/tripadvisor-split-dataset-v2)
- **Use Case**: Sentiment classification for customer reviews to derive insights into customer satisfaction.
- **Output**: Sentiment labels (1-5).

---

## Model Details

- **Learning Rate**: `3e-05`
- **Batch Size**: `64`
- **Epochs**: `10` (with early stopping)
- **Patience**: `5` (epochs without improvement)
- **Tokenizer**: `distilbert-base-uncased`
- **Framework**: PyTorch + Hugging Face Transformers

## Intended Use

This model is designed to classify hotel reviews based on their sentiment. It assigns a star rating between 1 and 5 to a review, indicating the sentiment expressed in the review.

---

### Dataset

The dataset used for training, validation, and testing is [nhull/tripadvisor-split-dataset-v2](https://huggingface.co/datasets/nhull/tripadvisor-split-dataset-v2). It consists of:

- **Training Set**: 30,400 reviews
- **Validation Set**: 1,600 reviews
- **Test Set**: 8,000 reviews

All splits are balanced across five sentiment labels.

---

### Test Performance

Model predicts too high on average by `0.3934`.

| Metric     | Value  |
|------------|--------|
| Accuracy   | 0.6391 |
| Precision  | 0.6416 |
| Recall     | 0.6391 |
| F1-Score   | 0.6400 |

#### Classification Report (Test Set)

| Label | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 1     | 0.7483    | 0.6856 | 0.7156   | 1600    |
| 2     | 0.5445    | 0.5544 | 0.5494   | 1600    |
| 3     | 0.6000    | 0.6281 | 0.6137   | 1600    |
| 4     | 0.5828    | 0.5894 | 0.5861   | 1600    |
| 5     | 0.7326    | 0.7381 | 0.7354   | 1600    |

### Confusion Matrix (Test Set)

| True \\ Predicted | 1    | 2    | 3    | 4    | 5    |
|-------------------|------|------|------|------|------|
| **1**            | 1097 | 437  | 60   | 3    | 3    |
| **2**            | 327  | 887  | 344  | 34   | 8    |
| **3**            | 37   | 278  | 1005 | 254  | 26   |
| **4**            | 3    | 21   | 239  | 943  | 394  |
| **5**            | 2    | 6    | 27   | 384  | 1181 |

---

## Files Included

- **`validation_results_distilbert.csv`**: Contains correctly classified reviews with their real and predicted labels.

---

## Limitations

1. Domain-Specific: The model was trained on TripAdvisor reviews, so it may not generalize to other types of reviews or domains without further fine-tuning.
2. Subjectivity: Sentiment annotations are subjective and may not fully represent every user's perception.
3. Performance: Mid-range sentiment labels (2 and 3) have lower precision and recall compared to extreme sentiment labels (1 and 5).