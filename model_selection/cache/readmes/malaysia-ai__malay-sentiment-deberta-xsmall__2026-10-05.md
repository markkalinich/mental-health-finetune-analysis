---
language:
- ms
tags:
- sentiment
---

## Malay-Language Sentiment Classification

# Overview
This model is a fine-tuned checkpoint of [Deberta-V3-xsmall](https://huggingface.co/microsoft/deberta-v3-xsmall). It enables binary sentiment analysis for Malay-language text. For each instance, it predicts either positive (1) or negative (0) sentiment. Model is trained on all data from https://github.com/mesolitica/malaysian-dataset/tree/master/sentiment.



# Use in a Hugging Face pipeline
The easiest way to use the model for single predictions is Hugging Face's [sentiment analysis pipeline](https://huggingface.co/transformers/quicktour.html#getting-started-on-a-task-with-a-pipeline), which only needs a couple lines of code as shown in the following example:
```
from transformers import pipeline
sentiment_analysis = pipeline("sentiment-analysis",model="malaysia-ai/deberta-v3-xsmall-malay-sentiment")
print(sentiment_analysis("saya comel"))
```