---
license: mit
language:
- en
- it
- es
base_model:
- microsoft/mdeberta-v3-base
pipeline_tag: text-classification
metrics:
- accuracy
library_name: transformers
tags:
- emotion-detection
- text-classification
---
# GordonAI

GordonAI is an AI package designed for sentiment analysis, emotion detection, and fact-checking classification. The models are pre-trained on three languages: **Italian**, **English**, and **Spanish**. 

## Features

This model has been trained for emotion detection and can categorize text into one of the six basic the six basic emotions defined by Paul Ekman (1992): **Joy**, **Sadness**, **Fear**, **Anger**, **Surprise**, **Disgust**, and **Neutral**.

The model is based on the pre-trained version of mdeberta-v3-base from Microsoft and has been fine-tuned on an emotion detection dataset to adapt to recognizing emotional expressions in text..

## Usage

You can use `GordonAI` to predict the emotion of a text.

```python
from transformers import pipeline

# Load the pipeline for text classification
classifier = pipeline("text-classification", model="VinMir/GordonAI-emotion_detection")

# Use the model to classify the emotion of a text
result = classifier("I love this!")
print(result)
```

## Requirements
Python >= 3.9
transformers
torch

You can install the dependencies using:
```bash
pip install transformers torch
```
## Limitations and bias
Please consult the original DeBERTa paper and literature on different NLI datasets for potential biases.

## Acknowledgments

This package is part of the work for my doctoral thesis. I would like to thank **NeoData** and **Università di Catania** for their valuable contributions to the development of this project.