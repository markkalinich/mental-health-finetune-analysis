---
license: cc-by-nc-4.0
language:
- az
pipeline_tag: text-classification
tags:
- sentiment
- analysis
- azerbaijani
widget:
- text: Bu mənim xoşuma gəlir
datasets:
- LocalDoc/sentiments_dataset_azerbaijani
---
# Sentiment Analysis Model for Azerbaijani Text
This repository hosts a fine-tuned XLM-RoBERTa model for sentiment analysis on Azerbaijani text. The model is capable of classifying text into three categories: negative, neutral, and positive.

## Model Description
The model is based on `xlm-roberta-base`, which has been fine-tuned on a diverse dataset of Azerbaijani text samples. It is designed to understand the sentiment expressed in texts and classify them accordingly.

## How to Use
You can use this model directly with a pipeline for text classification, or you can use it with the `transformers` library for more custom usage, as shown in the example below.

### Quick Start
First, install the transformers library if you haven't already:
```bash
pip install transformers
```

```python
from transformers import AutoModelForSequenceClassification, XLMRobertaTokenizer
import torch

# Load the model and tokenizer from Hugging Face Hub
model_name = "LocalDoc/sentiment_analysis_azerbaijani"
tokenizer = XLMRobertaTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

def predict_sentiment(text):
    # Encode the text using the tokenizer
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=128)

    # Get predictions from the model
    with torch.no_grad():
        outputs = model(**inputs)

    # Convert logits to probabilities using softmax
    probs = torch.nn.functional.softmax(outputs.logits, dim=-1)

    # Get the highest probability and corresponding label
    top_prob, top_label = torch.max(probs, dim=-1)
    labels = ["negative", "neutral", "positive"]

    # Return the label with the highest probability
    return labels[top_label], top_prob

# Example text
text = "Bu mənim xoşuma gəlir"

# Get the sentiment
predicted_label, probability = predict_sentiment(text)
print(f"Predicted sentiment: {predicted_label} with a probability of {probability.item():.4f}")

```

## Sentiment Label Information

The model outputs a label for each prediction, corresponding to one of the sentiment categories listed below. Each label is associated with a specific sentiment as detailed in the following table:

| Label | Sentiment |
|-------|-----------|
| 0     | Negative  |
| 1     | Neutral   |
| 2     | Positive  |



License

The dataset is licensed under the Creative Commons Attribution-NonCommercial 4.0 International  license. This license allows you to freely share and redistribute the dataset with attribution to the source but prohibits commercial use and the creation of derivative works.



Contact information

If you have any questions or suggestions, please contact us at [v.resad.89@gmail.com].