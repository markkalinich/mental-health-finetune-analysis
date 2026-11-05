---
library_name: transformers
pipeline_tag: text-classification
language: en
tags:
- sentiment-analysis
- roberta
- restaurant-reviews
---

# Restaurant Review RoBERTa Classifier

## Model Description
This is a fine-tuned version of `roberta-base` trained specifically to analyze the sentiment of restaurant and hospitality reviews. It was trained to understand the specific nuances, slang, and context of food service feedback.

- **Developed by:** Almashtouly
- **Model type:** RoBERTa Sequence Classification
- **Language:** English
- **License:** MIT

## Uses
This model is intended for analyzing customer feedback in the restaurant and hospitality industry. 

### Direct Use
Pass raw text reviews into the model to classify them into three categories:
* **LABEL_0:** Negative (e.g., "The steak was completely undercooked.")
* **LABEL_1:** Neutral (e.g., "The food was okay, nothing special.")
* **LABEL_2:** Positive (e.g., "The ambiance and service were absolutely incredible!")

### How to Get Started with the Model
You can easily use this model in your own applications via the Hugging Face pipeline:
```python
from transformers import pipeline

# Load the model
analyzer = pipeline("text-classification", model="Almashtouly/Restaurant_RoBERTa_Model")

# Test a review
prediction = analyzer("The waitstaff was incredibly friendly, but the food took way too long.")
print(prediction)