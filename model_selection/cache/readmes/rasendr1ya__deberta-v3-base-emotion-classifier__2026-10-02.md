---
language: en
tags:
- emotion-classification
- multilabel
- text-classification
- pytorch
- transformers
- deberta-v3-large
license: apache-2.0
metrics:
- f1
---

# Multilabel Emotion Classification Model (DeBERTa-v3-base)

## Model Description
This model is fine-tuned DeBERTa-v3-base for multilabel emotion classification. It can predict multiple emotions simultaneously from text with superior performance using disentangled attention mechanisms.

## Emotions Detected
amusement, anger, annoyance, caring, confusion, disappointment, disgust, embarrassment, excitement, fear, gratitude, joy, love, sadness

## Performance
- **Macro F1 Score**: 0.3913
- **Training Data**: 37164 samples
- **Validation Data**: 9291 samples

## Key Features
- **Disentangled Attention**: Separates content and position representations
- **Enhanced Mask Decoder**: Better handling of masked tokens
- **Relative Position Bias**: Improved positional understanding
- **Multilabel Capability**: Simultaneous prediction of multiple emotions

## Usage

```python
from transformers import AutoTokenizer, AutoModel
import torch

tokenizer = AutoTokenizer.from_pretrained("your-username/emotion-classifier-deberta")
model = AutoModel.from_pretrained("your-username/emotion-classifier-deberta")

# Example usage
text = "I'm so happy and excited about this!"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.sigmoid(outputs.logits)
```

## Training Details
- **Base Model**: microsoft/deberta-v3-base
- **Training Epochs**: 2
- **Learning Rate**: 1e-05
- **Batch Size**: 16
- **Max Length**: 128
- **Memory Optimizations**: Gradient accumulation, FP16, gradient checkpointing

## Model Architecture
- **Total Parameters**: 183,842,318
- **Trainable Parameters**: 183,842,318

## Training Optimizations
- Mixed precision training (FP16)
- Gradient accumulation for memory efficiency
- Gradient checkpointing
- Early stopping based on macro F1 score
