---
language: ne
license: apache-2.0
tags:
- sentiment-analysis
- nepali
- onnx
- bert
- text-classification
datasets:
- custom-nepali-sentiment
metrics:
- f1
- accuracy
model-index:
- name: mohit4519/nepali-sentiment
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      name: Nepali Sentiment Dataset
      type: custom
    metrics:
    - type: f1
      value: 0.73
      name: Macro F1
---

# Nepali Sentiment Analysis (ONNX)

This model is a fine-tuned BERT model for Nepali sentiment analysis, exported to ONNX format for optimized inference.

## Model Details

- **Base Model**: Shushant/nepaliBERT
- **Task**: Sentiment Classification (3-class)
- **Labels**: 
  - 0: Negative
  - 1: Positive
  - 2: Neutral
- **Format**: ONNX (optimized for fast inference)

## Usage

### Installation

```bash
pip install transformers optimum[onnxruntime]
```

### Inference

```python
from transformers import AutoTokenizer
from optimum.onnxruntime import ORTModelForSequenceClassification
import torch

# Load model and tokenizer
model = ORTModelForSequenceClassification.from_pretrained("mohit4519/nepali-sentiment")
tokenizer = AutoTokenizer.from_pretrained("Shushant/nepaliBERT")

# Predict sentiment
text = "यो धेरै राम्रो छ"
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)
prediction = torch.argmax(outputs.logits, dim=-1).item()

sentiment_map = {0: 'Negative', 1: 'Positive', 2: 'Neutral'}
print(f"Sentiment: {sentiment_map[prediction]}")
```

## Performance on test set

- **Macro F1 Score**: 0.73
- **Accuracy**: 0.76

## Training Data

Trained on Nepali sentiment dataset containing social media text, reviews, and comments.

## Limitations

- Best performance on Nepali text
- May have reduced accuracy on code-mixed or transliterated text
- Performance varies across different domains
