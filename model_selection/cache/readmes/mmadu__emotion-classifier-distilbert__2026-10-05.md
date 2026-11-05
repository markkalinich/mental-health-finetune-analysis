---
language: en
license: apache-2.0
library_name: transformers
tags:
- emotion-classification
- distilbert
- text-classification
- fine-tuned
datasets:
- go_emotions
---

# Emotion Classification with DistilBERT

This model is a fine-tuned version of distilbert-base-uncased for emotion classification. It classifies text into 6 emotions:

- 0: admiration
- 1: amusement
- 2: anger
- 3: annoyance
- 4: approval
- 5: caring

## Training Data
The model was fine-tuned on the Go Emotions dataset, filtered to these 6 emotion categories.

## Performance
- **Accuracy: 78.3%**
- **F1 Score: 77.9%**
- **Training Loss: 0.45** (from 0.93)

## Usage
```python
from transformers import pipeline

classifier = pipeline('text-classification', model='your-username/emotion-classifier-distilbert')
result = classifier('I love this amazing product!')
print(f"Emotion: {result[0]['label']}, Confidence: {result[0]['score']:.3f}")
```

## Example Predictions
- 'I love this so much!' → admiration (confidence: ~0.85)
- 'This is so frustrating!' → anger (confidence: ~0.82)
- 'That's hilarious!' → amusement (confidence: ~0.88)
- 'This is annoying me' → annoyance (confidence: ~0.79)
- 'Great job on this!' → approval (confidence: ~0.81)
- 'I'm here to support you' → caring (confidence: ~0.83)

## Training Details
- **Base Model**: distilbert-base-uncased
- **Epochs**: 3
- **Batch Size**: 16
- **Learning Rate**: 2e-5
- **Dataset**: Go Emotions (filtered)

## Intended Use
This model is suitable for emotion analysis in text, customer feedback analysis, sentiment-aware chatbots, and social media monitoring.