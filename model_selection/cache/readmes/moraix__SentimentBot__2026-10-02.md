---
tags:
  - sentiment-analysis
  - bert
  - pytorch
  - text-classification
license: mit
---

# SentimentBot: A Sentiment Analysis Chatbot with BERT 🤖

## Overview
SentimentBot is a fine-tuned BERT model (bert-base-uncased) designed for sentiment analysis, trained on the SST-2 (Stanford Sentiment Treebank) dataset. This model predicts whether a given text expresses a positive or negative sentiment with high accuracy, achieving 92.3% accuracy and 92.3% F1 score on the validation set after 2 epochs. It was developed as part of an AI Engineer internship project focusing on NLP.

## Model Details
- Base Model: bert-base-uncased
- Dataset: SST-2 (2 classes: 0 = negative, 1 = positive)
- Training: Fine-tuned for 2 epochs with a batch size of 16
- Performance:
    Eval Loss: 0.311
    Accuracy: 92.3%
    F1 Score: 92.3%

## Usage
To use the SentimentBot model in your Python project, install the required libraries and load the model as follows:
```
pip install transformers torch
```
```
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("moraix/SentimentBot")
model = AutoModelForSequenceClassification.from_pretrained("moraix/SentimentBot").to("cuda")

# Example input
text = "I love this movie so much!"
inputs = tokenizer(text, return_tensors="pt", padding="max_length", truncation=True, max_length=128).to("cuda")

# Predict sentiment
model.eval()
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.softmax(outputs.logits, dim=1)
    predicted_class = torch.argmax(predictions, dim=1).item()
    confidence = predictions[0, predicted_class].item()

label_map = {0: "negative", 1: "positive"}
sentiment = label_map[predicted_class]
print(f"Text: {text}")
print(f"Sentiment: {sentiment} (Confidence: {confidence:.2f})")
```
## Intended Uses
- Primary Use: Analyzing sentiment in English text (e.g., movie reviews, social media posts).
- Out-of-Scope: Multi-class sentiment (e.g., neutral) or non-English text (requires further fine-tuning).
## Limitations
- Trained only on SST-2, so performance may vary on other datasets.
- Limited to binary classification (positive/negative).
## Future Improvements
- dd support for more complex sentiments (e.g., neutral, angry).
- Expand the dataset with custom data.
- Deploy the chatbot as a web app using Flask or Streamlit.
## Contributing
Feel free to fork this repository, open issues, or submit pull requests. Feedback is always welcome! Contact For questions, reach out via mohammadmehdiomidi95@gmail.com or connect with me on LinkedIn.