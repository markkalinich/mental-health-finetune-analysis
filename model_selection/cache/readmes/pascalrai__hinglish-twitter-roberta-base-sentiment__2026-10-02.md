---
license: mit
datasets:
- mteb/tweet_sentiment_extraction
language:
- hi
- en
metrics:
- f1
- accuracy
pipeline_tag: text-classification
tags:
- hinglish
- sentiment
- sentiment analysis
widget:
- text: "tu mujhe pasandh heh"
  example_title: "Positive sentiment example 1"
- text: "❤️"
  example_title: "Positive sentiment example 2"
- text: "tu mujhe pasandh heh :( ;("
  example_title: "Negative sentiment example 1"
- text: "I do not like you"
  example_title: "Negative sentiment example 2"
- text: "aj mausam kesa heh?"
  example_title: "Neutral sentiment example 1"
- text: "tum kon ho bhai"
  example_title: "Neutral sentiment example 2"
- text: "How is the weather like"
  example_title: "Neutral sentiment example 2"
---
## Overview

The model is more optimized for hinglish + emojis and emojis seem to take more attention than the hinglish words.
This may be due to the base model being trained for emoji classification and then later trained for sentiment analysis.

This model is better if emojis are to be also included for sentiment analysis.
No Evaluation is done for data with only text and no emojis.

The model was fine-tuned with the dataset: mteb/tweet_sentiment_extraction from hugging face
converted to Hinglish text.

The model has a test loss of 0.6 and an f1 score of 0.74 on the unseen data from the dataset.

## Model Inference using pipeline
```
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-classification", model="pascalrai/hinglish-twitter-roberta-base-sentiment")
pipe("tu mujhe pasandh heh")

[{'label': 'positive', 'score': 0.7615439891815186}]
```
## Model Inference
```
# Load model directly
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("pascalrai/hinglish-twitter-roberta-base-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("pascalrai/hinglish-twitter-roberta-base-sentiment")

inputs = ["tum kon ho bhai","tu mujhe pasandh heh"]
outputs = model(**tokenizer(inputs, return_tensors='pt', padding=True))

p = torch.nn.Softmax(dim = 1)(outputs.logits)
for index, each in enumerate(p.detach().numpy()):
    print(f"Text: {inputs[index]}")
    print(f"Negative: {round(float(each[0]),2)}\nNeutral: {round(float(each[1]),2)}\nPositive: {round(float(each[2]),2)}\n")

Text: tum kon ho bhai
Negative: 0.02
Neutral: 0.91
Positive: 0.07

Text: tu mujhe pasandh heh
Negative: 0.01
Neutral: 0.22
Positive: 0.76
```
Possible Future Direction:

1. Pre-train the Hinglish model with both Hindi, Hinglish, and English datasets. Current tokens for hinlish have very small sizes i.e. low-priority vocabs are used mostly.