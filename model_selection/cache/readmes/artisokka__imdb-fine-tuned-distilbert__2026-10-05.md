---
library_name: transformers
tags:
- sentiment-analysis
- distilbert
- fine-tuned
- imdb
license: apache-2.0
language:
- en
base_model:
- distilbert/distilbert-base-uncased
pipeline_tag: text-classification
---

# Model Card for imdb-fine-tuned-distilbert

This model is a fine-tuned DistilBERT model for sentiment analysis of movie reviews from the IMDB dataset. It classifies reviews as either positive or negative.

## Model Details

### Model Description

This model is a fine-tuned version of `distilbert-base-uncased` specifically trained on the IMDB dataset for sentiment analysis. It takes movie reviews as input and predicts whether the sentiment is positive (1) or negative (0).

- **Developed by:** artisokka
- **Model type:** DistilBERT for Sequence Classification
- **Language(s) (NLP):** English
- **License:** Apache 2.0
- **Finetuned from model:** [distilbert-base-uncased](https://huggingface.co/distilbert/distilbert-base-uncased)

### Model Sources

- **Repository:** [IMDB fine-tuned DistilBERT](https://huggingface.co/artisokka/imdb-fine-tuned-distilbert)

## Training Details

### Training Data

The model was fine-tuned on the IMDB Dataset of 50k Movie Reviews. This dataset originated from Kaggle and was accessed via the [IMDB Dataset of 50k Movie Reviews](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews) on Kaggle Datasets. The dataset consists of 50,000 highly polar movie reviews, with 25,000 for training and 25,000 for testing. The reviews are labeled as positive or negative, making it suitable for binary sentiment classification.

The dataset was chosen due to its widespread use in sentiment analysis tasks and its clear labeling, which facilitated the fine-tuning process.

## Uses

### Direct Use

This model can be directly used for sentiment analysis of movie reviews. Input a text review, and the model will output a prediction of positive or negative sentiment.

### Downstream Use

This model can be used as a component in larger applications that require sentiment analysis, such as customer feedback analysis for movie streaming platforms or social media monitoring.

### Out-of-Scope Use

This model is specifically fine-tuned for movie reviews. It may not perform well on other types of text, such as news articles, legal documents, or social media posts from other domains. It should not be used for any harmful or unethical purposes, such as generating misleading or biased content.

## Bias, Risks, and Limitations

The model's performance is limited to the domain of movie reviews. It may inherit biases present in the IMDB dataset. Additionally, the model's accuracy may vary depending on the complexity and style of the input reviews.

### Recommendations

Users should be aware of the model's domain-specific nature and potential biases. It is recommended to evaluate the model's performance on a representative dataset before deploying it in a production environment.

## How to Get Started with the Model

Use the code below to get started with the model.

```python
from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis", model="artisokka/imdb-fine-tuned-distilbert")
result = sentiment_pipeline("This movie was amazing!")
print(result)