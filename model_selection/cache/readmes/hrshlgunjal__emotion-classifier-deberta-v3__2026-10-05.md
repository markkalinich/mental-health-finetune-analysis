---
language: en
license: apache-2.0
tags:
- text-classification
- multi-label-classification
- emotion-classification
- deberta-v3
- pytorch
---

# Emotion Classification Model

This model classifies text into 5 emotion categories: **anger**, **fear**, **joy**, **sadness**, and **surprise**.

## Model Description

- **Base Model:** microsoft/deberta-v3-base
- **Task:** Multi-label text classification
- **Labels:** anger, fear, joy, sadness, surprise
- **Training Strategy:** 5-Fold Cross-Validation
- **Framework:** PyTorch + Transformers

## Performance

### Overall Metrics
- **Macro F1:** N/A
- **Cross-Validation:** 0.7989 +/- 0.0121

### Per-Label Performance
N/A

### Optimized Thresholds
N/A

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np

# Load model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("hrshlgunjal/emotion-classifier-deberta-v3")
tokenizer = AutoTokenizer.from_pretrained("hrshlgunjal/emotion-classifier-deberta-v3")

# Optimized thresholds (use these for best results)
thresholds = np.array([0.5, 0.5, 0.5, 0.5, 0.5])
labels = ['anger', 'fear', 'joy', 'sadness', 'surprise']

# Predict emotions
def predict_emotions(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
    with torch.no_grad():
        outputs = model(**inputs)
    probs = torch.sigmoid(outputs.logits).cpu().numpy()[0]
    predictions = (probs >= thresholds).astype(int)
    return {label: (pred, prob) for label, pred, prob in zip(labels, predictions, probs)}

# Example
text = "I am so excited about this amazing opportunity!"
result = predict_emotions(text)
print(result)
```

## Training Details

- **Optimizer:** AdamW with differential weight decay
- **Learning Rate:** 1.5e-05
- **Batch Size:** 16
- **Epochs:** 4
- **Max Sequence Length:** 128
- **Warmup Ratio:** 0.1
- **Weight Decay:** 0.01
- **Mixed Precision:** Enabled (FP16)
- **Gradient Clipping:** 1.0

## Training Infrastructure

- **Device:** GPU
- **Training Time:** ~300 minutes (approximate)
- **Framework Versions:**
  - PyTorch: 2.6.0+cu124
  - Transformers: 4.53.3

## Model Card Authors

hrshlgunjal

## Model Card Contact

For questions or feedback, please open an issue in the model repository.
