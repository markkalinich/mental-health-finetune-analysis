---
language:
- ar 
- en
license: mit
pipeline_tag: text-classification
tags:
- text-classification
- sentiment-analysis
- arabic
- egyptian-arabic
- bert
datasets:
- custom
metrics:
- accuracy
---

# Sentiment Analyzer (Egyptian Arabic)

## Model description

This model is fine-tuned for sentiment classification on Egyptian Arabic text.

It predicts one of the following labels:
- Positive
- Negative
- Neutral

## Intended use

This model is designed for:
- Social media sentiment analysis
- Customer feedback analysis
- Chatbot emotional tone detection

## Limitations

- Trained on Egyptian dialect only
- Performance may degrade on MSA or other dialects