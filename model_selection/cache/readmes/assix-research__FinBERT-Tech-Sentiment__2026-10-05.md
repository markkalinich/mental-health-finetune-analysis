---
language: en
license: mit
library_name: transformers
pipeline_tag: text-classification
tags:
- finbert
- finance
- sentiment-analysis
- tech-stocks
base_model: ProsusAI/finbert
datasets:
- financial_phrasebank
metrics:
- accuracy
- f1
---

# FinBERT-Tech-Sentiment

This model is a fine-tuned version of [ProsusAI/finbert](https://huggingface.co/ProsusAI/finbert) for sentiment analysis on financial news related to major technology companies.

## Model Description

This model was fine-tuned on a filtered subset of the `financial_phrasebank` dataset. Specifically, it was trained on sentences from the `Sentences_50Agree.txt` file that contained keywords for major tech companies (Google, Apple, Microsoft, Amazon, Nvidia, etc.).

Due to the very small size of the filtered dataset (58 samples), this model is intended as a proof-of-concept and its performance is limited.

## Evaluation Results

The model achieves the following results on the evaluation set:
* **Loss:** 2.3548
* **Accuracy:** 0.25
* **F1 Score:** 0.2639

## How to Use

You can use this model directly with the `pipeline` function from the `transformers` library.

```python
from transformers import pipeline

sentiment_analyzer = pipeline(
    "text-classification",
    model="esix117/FinBERT-Tech-Sentiment"
)

# Example 1
result = sentiment_analyzer("Nvidia reported record earnings, beating all estimates.")
print(result)
# >> [{'label': 'positive', 'score': 0.8...}]

# Example 2
result = sentiment_analyzer("Apple shares fell after the new product announcement.")
print(result)
# >> [{'label': 'negative', 'score': 0.9...}]