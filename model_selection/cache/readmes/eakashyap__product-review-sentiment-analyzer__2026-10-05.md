---
license: mit
datasets:
- Yelp/yelp_review_full
language:
- en
metrics:
- accuracy
base_model:
- distilbert/distilbert-base-uncased
pipeline_tag: text-classification
library_name: transformers
tags:
- sentiment-analysis
---


# Product Review Sentiment Analyzer

This model classifies product reviews as positive, negative, or neutral. It was fine-tuned on the IMDB dataset using DistilBERT as the base model.

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("yourusername/product-review-sentiment-analyzer")
model = AutoModelForSequenceClassification.from_pretrained("arpitk/product-review-sentiment-analyzer")

text = "This product exceeded my expectations!"
inputs = tokenizer(text, return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs)
    
probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
prediction = torch.argmax(probabilities, dim=-1).item()

labels = ["Negative", "Positive", "Neutral"]  # Adjust based on your model's output order
print(f"Sentiment: {labels[prediction]}")
```

This project demonstrates how to build and deploy a sentiment analysis model for product reviews using free resources.

## Project Overview
- Fine-tuned a DistilBERT model on Yelp product reviews
- Classifies reviews as Positive, Negative, or Neutral
- Achieved XX% accuracy on the evaluation dataset

## Live Demo
Try the model yourself: [Hugging Face Space](https://huggingface.co/spaces/arpitk/product-review-sentiment-analyzer)

## Technologies Used
- Google Colab (free GPU)
- Hugging Face Transformers
- PyTorch
- Gradio for the web interface

## Project Structure
- `notebooks/`: Contains the Jupyter notebook for model development
- `app/`: Contains the Gradio app for deployment
- `src/`: Contains source code for data processing and model training

## How to Use
1. Clone this repository
2. Run the notebook to train your own model
3. Or use the pre-trained model: `arpitk/product-review-sentiment-analyzer`

## Results
The model achieves 90% accuracy on the test set. Here are some example predictions:
- "This product exceeded my expectations!" → Positive (0.95)
- "It broke after two days of use." → Negative (0.89)
- "The product is okay, but a bit overpriced." → Neutral (0.78)