---
library_name: transformers
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- sentiment-analysis
- youtube-comments
- text-classification
- distilbert
- fine-tuned
metrics:
- f1
- accuracy
model-index:
- name: distilbert-finetuned-youtube_sentiment_analysis
  results: []
datasets:
- iam-tsr/comments-sentiments
language:
- en
pipeline_tag: text-classification
---

# Finetuned DistilBERT model card

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) post trained on a huge comments corpus for sentiment analysis.

## Model description

The model is based on DistilBERT, a distilled version of BERT that is smaller, faster, and requires less computational resources while maintaining 97% of BERT's performance. This specific model has been fine-tuned to perform sentiment analysis on YouTube comments, classifying them into three categories: POSITIVE, NEUTRAL, and NEGATIVE.

The model is designed to understand the nuanced language used in social media comments, including slang, emojis, and informal speech patterns typically found in YouTube comment sections.

### Model architecture
- **Base model**: DistilBERT (distilbert-base-uncased)
- **Task type**: Text Classification (Sentiment Analysis)
- **Number of labels**: 3 (POSITIVE, NEUTRAL, NEGATIVE)
- **Label mapping**: {"NEUTRAL": 0, "POSITIVE": 1, "NEGATIVE": 2}


## Training and evaluation data

The model was trained on a custom dataset of YouTube comments with sentiment labels:

- **Dataset**: [im-tsr/comments-sentiments](https://huggingface.co/datasets/im-tsr/comments-sentiments)
- **Training set size**: 7,20,977 samples
- **Test set size**: 36,558 samples
- **Maximum sequence length**: 128 tokens

## Training procedure

The model was fine-tuned using the Hugging Face Transformers library with Pytorch.

### Training hyperparameters

The following hyperparameters were used during training:
- **Learning rate**: 5e-05
- **Train batch size**: 64
- **Eval batch size**: 64
- **Weight decay**: 0.01
- **Optimizer**: AdamW
- **Number of epochs**: 3
- **Maximum sequence length**: 128

### Evaluation results

The model was evaluated on a test set of YouTube comments. The evaluation metrics are:
- **Accuracy**: 0.730100
- **F1 Score**: 0.730025

### Using Hugging Face Transformers

```python
import torch
import transformers
from transformers import pipeline

def get_sentiment(text):
    #Set to avoid warning messages.
    transformers.logging.set_verbosity_error()
    sentiment_classifier = pipeline(task="text-classification",
                                    model="iam-tsr/distilbert-finetuned-sentiment-analysis",
                                    tokenizer="iam-tsr/distilbert-finetuned-sentiment-analysis",)

    return sentiment_classifier(text)

get_sentiment("I love programming!")
#[{'label': 'POSITIVE', 'score': 0.9759756326675415}]
```

## Intended uses
This model is intended for analyzing sentiment in YouTube comments and similar social media text. It can be used for:

- Monitoring sentiment in YouTube comment sections
- Content moderation assistance
- Social media sentiment analysis
- User feedback analysis
- Tracking audience reaction to videos or content

### Limitations
- The model is specifically trained on YouTube comments, which may have different characteristics from other text sources
- Performance may vary for comments in languages other than English
- The model may not handle sarcasm, irony, or cultural context effectively
- Limited to three sentiment categories which may not capture the full spectrum of emotions
- May not perform optimally on very short texts or texts with multiple conflicting sentiments

## Links

- [Dataset on Hugging Face](https://huggingface.co/datasets/im-tsr/comments-sentiments)
- [Demo on Hugging Face Spaces](https://huggingface.co/spaces/im-tsr/sentiment-analysis)

## Framework versions
- Transformers 4.53
- Pytorch 2.8.0
- Datasets 3.6.0