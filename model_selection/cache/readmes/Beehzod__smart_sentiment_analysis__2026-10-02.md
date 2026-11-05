---
license: apache-2.0
language: en
tags:
  - sentiment-analysis
  - distilbert
  - transformers
datasets:
  - imdb
metrics:
  - accuracy
  - f1
  - precision
  - recall
model_type: distilbert
---

# Fine-tuned DistilBERT for Sentiment Analysis

## Model Description
This model is a fine-tuned version of DistilBERT for sentiment analysis tasks. It was trained on the IMDB dataset to classify movie reviews as **positive** or **negative**. It can be used in applications where text sentiment analysis is needed, such as social media monitoring or customer feedback analysis.

- **Model Architecture**: DistilBERT (transformer-based model)
- **Task**: Sentiment Analysis
- **Labels**: 
  - **Positive**
  - **Negative**

## Training Details
- **Dataset**: IMDB movie reviews dataset
- **Training Data Size**: 20,000 samples for training and 5,000 samples for evaluation
- **Epochs**: 3
- **Batch Size**: 16
- **Learning Rate**: 2e-5
- **Optimizer**: AdamW with weight decay

## Evaluation Metrics
The model was evaluated on a held-out test set using the following metrics:
- **Accuracy**: 0.95
- **F1 Score**: 0.94
- **Precision**: 0.93
- **Recall**: 0.92

## Usage

### Example Code
To use this sentiment analysis model with the Hugging Face Transformers library:

```python
from transformers import pipeline

# Load the model from the Hugging Face Hub
sentiment_pipeline = pipeline("sentiment-analysis", model="Beehzod/smart_sentiment_analysis")

# Example predictions
text = "This movie was fantastic! I really enjoyed it."
results = sentiment_pipeline(text)

for result in results:
    print(f"Label: {result['label']}, Score: {result['score']:.4f}")
