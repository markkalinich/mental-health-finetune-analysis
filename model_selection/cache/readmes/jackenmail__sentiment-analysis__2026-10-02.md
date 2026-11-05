---
language: en
license: apache-2.0
model_name: Sentiment Analysis with DistilBERT
tags:
- text-classification
- sentiment-analysis
- pytorch
dataset_id: imdb
finetuned_from: distilbert-base-uncased
---

# Sentiment Analysis Model

This is a sentiment analysis model fine-tuned on the IMDB movie review dataset. It classifies text into two categories: 'POSITIVE' and 'NEGATIVE'.

## Model Description

This model utilizes a pre-trained `distilbert-base-uncased` model from Hugging Face Transformers, further fine-tuned for sentiment classification. The base model is a lighter, faster version of BERT, suitable for various NLP tasks.

## Intended Uses

This model is intended for classifying the sentiment of short to medium-length text, such as movie reviews, product feedback, or social media comments. It can be used to:

*   Automatically categorize user feedback.
*   Monitor sentiment trends.
*   Filter content based on sentiment.

## Limitations and Bias

*   **Dataset Bias:** The model was trained on movie reviews (IMDB dataset), which may introduce biases specific to that domain. Its performance might degrade on text from other domains or with different linguistic styles.
*   **Language:** Only English text is supported.
*   **Nuance:** Like most sentiment models, it may struggle with sarcasm, irony, or complex contextual sentiment.
*   **Ethical Considerations:** Ensure responsible deployment, especially in applications that might impact individuals (e.g., automated moderation). Always review critical decisions made by the model.

## Training Data

The model was fine-tuned on a subset of the [IMDB movie review dataset](https://huggingface.co/datasets/imdb).

*   **Training Set Size:** 5,000 samples
*   **Evaluation Set Size:** 1,000 samples

## Training Procedure

The model was trained using the following parameters:

*   **Base Model:** `distilbert-base-uncased`
*   **Number of Epochs:** 3
*   **Batch Size:** 32 (for both training and evaluation)
*   **Optimizer:** AdamW
*   **Mixed Precision Training:** `fp16=True` was used to speed up training.
*   **Evaluation Strategy:** Evaluated at the end of each epoch.
*   **Best Model Selection:** The model with the best evaluation loss was loaded at the end of training.

## Usage

You can use this model directly with the Hugging Face `pipeline`:

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="jackenmail/sentiment-analysis")

text = "I absolutely loved this movie, it was fantastic!"
result = classifier(text)
print(result)
# Output: {'label': 'POSITIVE', 'score': 0.99...}

text = "This was a terrible experience, completely ruined my day."
result = classifier(text)
print(result)
# Output: {'label': 'NEGATIVE', 'score': 0.99...}
```
