---
license: mit
language: en
tags:
- text-classification
- sentiment-analysis
- finance
---

# FinBERT for Financial Sentiment Analysis

This is a `bert-base-uncased` model fine-tuned on the Financial PhraseBank dataset for sentiment analysis of financial news.

This model was trained as part of the project available at [https://github.com/jp-marques/financial-sentiment-analysis](https://github.com/jp-marques/financial-sentiment-analysis).

## Model Description

This model is a fine-tuned version of `ProsusAI/finbert` for financial sentiment analysis. It classifies financial headlines into three categories: `positive`, `negative`, or `neutral`. The model achieves an accuracy of **80.8%** on the test set, with a particularly strong F1-score of **50%** for the `negative` class, which is crucial for risk detection.

## Intended Uses & Limitations

This model is intended for analyzing the sentiment of financial news headlines, articles, and social media posts. It can be used to generate trading signals, assess market sentiment, or perform risk analysis.

**Limitations:**
* The model is trained on English financial news and may not generalize well to other languages or domains.
* The training data is from a specific time period and may not capture the nuances of new financial jargon or market conditions.

## How to Use

You can use this model directly with a `pipeline` from the `transformers` library.

```python
from transformers import pipeline

classifier = pipeline('sentiment-analysis', model="peejm/finbert-financial-sentiment")

text = "Stocks are soaring after the positive earnings report."
result = classifier(text)
print(result)
# [{'label': 'positive', 'score': 0.99...}]
```

## Training Data

The model was fine-tuned on a Kaggle dataset, which contains sentences from financial news categorized by sentiment.

- **Source:** [Financial Sentiment Analysis on Kaggle](https://www.kaggle.com/datasets/sbhatti/financial-sentiment-analysis)
- **License:** CC0 1.0 Universal Public Domain Dedication.

The data was split into training, validation, and test sets as detailed in the EDA notebook of the original project.

## Training Procedure

The model was fine-tuned using the `Trainer` API from the Hugging Face `transformers` library. The hyperparameters and training script can be found in the notebook `03_finetune_finbert.ipynb` in the project repository.

## Evaluation Results

| Metric              | Value |
|---------------------|-------|
| Accuracy            | 80.8% |
| F1 Score (Negative) | 50%   |

These results represent a significant improvement over baseline models, as detailed in the project's main `README.md`.
