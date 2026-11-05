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
- sentiment-analysis
- text-classification
---
# GordonAI

GordonAI is an AI package designed for sentiment analysis, emotion detection, and fact-checking classification. The models are pre-trained on three languages: **Italian**, **English**, and **Spanish**. 

## Features
This model has been trained for text sentiment classification. It is capable of distinguishing into three categories: **positive**, **negative**, and **neutral**

The model is based on the pre-trained version of DeBERTa-v3-large from Microsoft and has been fine-tuned on a sentiment analysis dataset to adapt to recognizing emotions in text.

## Usage

You can use the `GordonAI` to predict the sentiment of a text. The analyzer classifies texts as positive, negative, or neutral.

```python
from transformers import pipeline

# Load the pipeline for text classification
classifier = pipeline("text-classification", model="VinMir/GordonAI-sentiment_analysis")

# Use the model to classify the sentiment of a text
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