---
license: mit
language:
- en
metrics:
- accuracy
- precision
- recall
- f1
- roc_auc
base_model:
- distilbert/distilbert-base-uncased
pipeline_tag: text-classification
library_name: transformers
tags:
- tweet
- sentiment
- nlp
- english
- distilbert
---
# Tweet Sentiment Classifier (DistilBERT)

This model classifies tweets into three sentiment classes: positive, and negative.  
It is fine-tuned from distilbert-base-uncased on a dataset of labeled tweets.

## Training Methodology

The model was fine-tuned using the Hugging Face 🤗 transformers library on the [Sentiment140 dataset](https://www.kaggle.com/datasets/kazanova/sentiment140).

- *Base model*: distilbert-base-uncased
- *Task*: Sentiment classification (positive, negative)
- *Data Preprocessing*:
  - Cleaned tweets from links, mentions, hashtags
  - Removed duplicates and empty samples
- *Split*: 60% training / 20% validation / 20% test
- *Optimizer*: Adam
- *Learning rate*: 2e-6
- *Batch size*: 32
- *Epochs*: 7
- *Loss function*: CrossEntropyLoss
- *Evaluation metrics*: Accuracy, F1, Precision, Recall, ROC-AUC

Training was done on a local machine using GPU.

## Evaluation
- Accuracy: 0.8070
- Precision: 0.7880
- Recall:    0.8400
- F1 Score:  0.8132
- ROC AUC:   0.8910

## Example Usage

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import re

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = AutoModelForSequenceClassification.from_pretrained("KotYrod/tweet-sentiment-distilbert").to(device)
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

def predict_sentiment(text):
    model.eval()
    text = re.sub(r"http\S+|www\S+|\@\w+|\#|\s+", ' ', text).strip()
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding='max_length', max_length=128).to(device)
    with torch.no_grad():
        logits = model(**inputs).logits
        probs = torch.softmax(logits, dim=1)
        pred = torch.argmax(probs, dim=1).item()
    return ("Positive 😊" if pred == 1 else "Negative 😠", probs[0][pred].item())

if _name_ == "_main_":
    label, conf = predict_sentiment("wow im so glad")
    print(f"Prediction: {label} (Confidence: {conf:.2f})")