---
language: en
license: other
tags:
- sentiment-analysis
- fine-tuned
- sentiment-classification
- transformers
model_name: Fine-Tuned Sentiment Model
model_type: Roberta
datasets:
- custom-dataset
- rohittamidapati11/training_data
- rohittamidapati11/validation_data
metrics:
- micro precision and recall
- macro precision and recall
---

# Fine-Tuned Sentiment Model
    This model is fine-tuned for Sentiment Analysis task, the model classifies a customer ticket into 5-categories of sentiments, namely:
        - "Strong Negative"
        - "Mild Negative"
        - "Neutral"
        - "Mild Positive"
        - "Strong Positive"

    *Point To Note*: The Customers are from these specific industries only:
        - Food
        - Cars
        - Pet Food
        - Furniture
        - Beauty

## Model Details
    - **Model Architecture**: This fine-tuned model was built on a pre-trained model, "IDEA-CCNL/Erlangshen-Roberta-110M-Sentiment"
    - **Training Dataset**: The Dataset was generated using the model, "meta-llama/Llama-3.2-1B-Instruct"

## Example Usage-
    To use this model for Sentiment Analysis:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("rohittamidapati11/fine_tuned_sentiment_model_rt2")
model = AutoModelForSequenceClassification.from_pretrained("rohittamidapati11/fine_tuned_sentiment_model_rt2")

# Example input
inputs = tokenizer("The food was a bit bland, but the portion sizes were generous. I was looking forward to trying it, but it didn't quite live up to my expectations.", return_tensors='pt')
outputs = model(**inputs)
predicted_class = torch.argmax(outputs.logits, dim = 1).item()
print("Predicted Sentiment:", predicted_class)