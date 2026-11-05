---
language: en
tags:
- distilbert
- emotion-classification
- text-classification
datasets:
- dair-ai/emotion
metrics:
- accuracy
---

# Emotion Classification Model

## Model Description
This model fine-tunes DistilBERT for multi-class emotion classification on the `dair-ai/emotion` dataset. 
The model is designed to classify text into one of six emotions: sadness, joy, love, anger, fear, or surprise. 
It can be used in applications requiring emotional analysis in English text.

## Training and Evaluation
- **Training Dataset**: `dair-ai/emotion` (16,000 examples)
- **Training Time**: 8 minutes and 51 seconds
- **Training Hyperparameters**:
  - Learning Rate: `3e-5`
  - Batch Size: `32`
  - Epochs: `4`
  - Weight Decay: `0.01`

### Training results

| Training Loss | Epoch | Step | Validation Loss | Val. Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:     |
| 0.5164        | 1.0   | 500  | 0.1887          | 0.9275        |
| 0.1464        | 2.0   | 1000 | 0.1487          | 0.9345        |
| 0.0994        | 3.0   | 1500 | 0.1389          | 0.94          |
| 0.0701        | 4.0   | 2000 | 0.1479          | 0.94          |

- **Overall Training Loss**: 0.2081
- **Test Accuracy**: 100% accuracy on the 10 examples tested.
  Confidence scores ranged from 90% to 100%.

## Usage
```python
from transformers import pipeline
classifier = pipeline("text-classification", model="Zoopa/emotion-classification-model")

text = "I am so happy today!"
result = classifier(text)
print(result)
```

## Limitations
  - The model only supports English.
  - The training dataset may contain biases, affecting model predictions on test data.
  - Edge Cases like mixed emotions might reduce accuracy.
