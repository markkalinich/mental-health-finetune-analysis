---
language:
- min
- id
- en
license: mit
library_name: transformers
tags:
- xlm-roberta
- sentiment-analysis
- code-mixing
- explainable-ai
- xai
- low-resource-language
datasets:
- custom-minangkabau-youtube-comments
metrics:
- f1
- accuracy
---

# Explainable XLM-R for Code-Mixed Minangkabau Sentiment Analysis

## Model Description
This model is a fine-tuned version of **XLM-RoBERTa (XLM-R)** specifically designed to handle the complexities of **Code-Mixed Minangkabau** sentiment analysis. Social media data in Indonesia, particularly from regional areas like West Sumatra, often features a heavy mix of Minangkabau, Indonesian, and English. 

Traditional models often struggle with this "low-resource gap" and "non-standard orthography." This model bridge those gaps while prioritizing **Explainability (XAI)** to demystify the "black-box" nature of Deep Learning.

### Key Features:
- **Multilingual Support:** Optimized for Indonesian, Minangkabau, and English code-mixing.
- **Robustness:** Handles informal spelling, unique affixations, and phonetic typing common in YouTube comments.
- **XAI-Ready:** Designed to be interpreted using feature attribution methods like **SHAP** or **LIME** to provide local and global explanations.

## Intended Uses & Limitations
- **Primary Use:** Sentiment classification (Positive, Neutral, Negative) for regional Indonesian languages.
- **Limitations:** Performance might vary on purely formal Minang literature as the training data is derived from social media (YouTube) contexts.

## How to Use
You can use this model directly with the `transformers` library:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "bimobirra/explainable-xlmr-code-mixed-low-resource-lang"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "Rancak bana videonya, tapi agak sedikit nge-lag loadingnya."
inputs = tokenizer(text, return_tensors="pt")

with torch.no_grad():
    logits = model(**inputs).logits

predicted_class_id = logits.argmax().item()
print(f"Predicted class ID: {predicted_class_id}")