---
license: apache-2.0
datasets:
- stanfordnlp/imdb
language:
- en
metrics:
- accuracy
library_name: transformers
tags:
- sentiment-analysis
- movie-analysis
- sentiment
- distilbert
- movie-reviews
---

## Model Description
This model is a `distilbert-base-uncased` fine-tuned for sentiment analysis on the IMDb movie review dataset. The model is trained to classify movie reviews into positive or negative sentiment.

## Intended Use
The model is intended for sentiment analysis tasks, specifically to classify the sentiment of English-language movie reviews. It can be used by developers or data scientists who wish to include sentiment analysis features in their applications.

## Training Data
The model was fine-tuned on the IMDb movie review dataset available from the Hugging Face datasets library. The dataset consists of 50,000 movie reviews from IMDb, labeled as positive or negative.

## Training Procedure
The model was fine-tuned for 2 epochs with a batch size of 8, Adam optimizer with a learning rate of 2e-5.

## Ethical Considerations
This model may inherit biases present in the IMDb dataset, and its predictions should be reviewed with critical consideration, especially if used in sensitive contexts.

## Sample Usage in Python
Here's how you can use this model in Python:

```python
from transformers import pipeline

# Load the sentiment analysis pipeline
classifier = pipeline('sentiment-analysis', model='sarahai/movie-sentiment-analysis')

# Analyze sentiment
review = "I really enjoyed this movie from start to finish!"
result = classifier(review)

print(result)

```