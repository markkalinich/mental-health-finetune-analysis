---
language: en
tags:
- sentiment-analysis
- imdb
- distilbert
- transformers
license: apache-2.0
datasets:
- imdb
---

# DistilBERT Sentiment Analysis Model

This model is a fine-tuned version of `distilbert-base-uncased` for binary sentiment classification on the IMDB movie reviews dataset.

## Model Details

### Model Description
- **Model type**: DistilBERT (transformer-based)
- **Task**: Binary sentiment classification (positive/negative)
- **Base Model**: `distilbert-base-uncased`
- **Language**: English

### Training Details

#### Training Data
- **Dataset**: IMDB Movie Reviews
- **Training Samples**: 16,000
- **Validation Samples**: 4,000
- **Test Samples**: 5,000
- **Class Distribution**: 50% positive, 50% negative

#### Training Procedure
- **Epochs**: 3
- **Batch Size**: 16
- **Learning Rate**: 2e-05
- **Max Sequence Length**: 512
- **Optimizer**: AdamW with weight decay (0.01)
- **Scheduler**: Linear with 10% warmup

#### Evaluation Results
- **Test Accuracy**: 0.9460
- **Test F1 Score**: 0.9723
- **Best Validation Accuracy**: 0.9300
- **Training Time**: ~6 minutes on Google Colab T4 GPU

## How to Use

### Direct Inference
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
model_name = "Hums003/distilbert-imdb-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Prepare text
text = "This movie was absolutely fantastic! I loved every minute of it."
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)

# Get predictions
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)

# Interpret results
sentiment = "positive" if predictions[0][1] > 0.5 else "negative"
confidence = predictions[0][1].item() if predictions[0][1] > 0.5 else predictions[0][0].item()
print(f"Sentiment: {sentiment} (confidence: {confidence:.2%})")
```
