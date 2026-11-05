---
language: en
license: apache-2.0
tags:
- text-classification
- sentiment-analysis
library_name: transformers
pipeline_tag: text-classification
model_name: my-first-model
---

# my-first-model

This is my first Hugging Face model.

## Model Description
This model is based on DistilBERT and performs sentiment analysis.

## How to use

from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="ganesh435/my-first-model")
classifier("I love learning AI with Hugging Face!")

## Notes
This model was uploaded for learning purposes.
