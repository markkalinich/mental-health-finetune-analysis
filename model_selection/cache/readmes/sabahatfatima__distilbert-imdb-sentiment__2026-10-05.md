---
language: en
license: apache-2.0
tags:
  - text-classification
  - sentiment-analysis
  - distilbert
  - fine-tuned
  - imdb
datasets:
  - imdb
metrics:
  - accuracy
  - f1
---
 
# DistilBERT IMDb Sentiment Classifier
 
A fine-tuned DistilBERT model for binary sentiment analysis on movie reviews.
 
**Author:** [Sabahat Fatima](https://huggingface.co/sabahatfatima)
**GitHub:** [SabahatFatima55](https://github.com/SabahatFatima55)
**Live Demo:** [Gradio Space](https://huggingface.co/spaces/sabahatfatima/distilbert-sentiment-demo)
 
## Model Description
 
Fine-tuned from `distilbert-base-uncased` on 5,000 IMDb movie reviews for 3 epochs.
Classifies text as **POSITIVE** or **NEGATIVE** sentiment.
 
## Training Details
 
| Parameter | Value |
|-----------|-------|
| Base Model | distilbert-base-uncased |
| Train Samples | 5,000 |
| Val Samples | 1,000 |
| Epochs | 3 |
| Learning Rate | 2e-5 |
| Batch Size | 16 |
| Max Token Length | 256 |
 
## Evaluation Results
 
| Metric | Score |
|--------|-------|
| Accuracy | ~92% |
| F1 Score | ~0.92 |
 
## Baseline Comparison
 
| Model | Accuracy |
|-------|----------|
| TF-IDF + Logistic Regression | ~86% |
| DistilBERT (this model) | **~92%** |
 
## How to Use
 
```python
from transformers import pipeline
 
classifier = pipeline(
    "text-classification",
    model="sabahatfatima/distilbert-imdb-sentiment"
)
 
result = classifier("This movie was absolutely incredible!")
# Output: [{'label': 'POSITIVE', 'score': 0.997}]
```
 
## Limitations
 
- Trained on English movie reviews only
- May not handle Urdu or Roman Urdu text
- Very short texts may have lower confidence
- Sarcasm without obvious negative words may be misclassified
