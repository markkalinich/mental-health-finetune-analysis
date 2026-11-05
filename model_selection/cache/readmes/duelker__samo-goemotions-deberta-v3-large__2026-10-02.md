---
license: apache-2.0
tags:
- deberta-v3-large
- goemotions
- emotion-detection
- multi-label-classification
- text-classification
- transformers
- pytorch
pipeline_tag: text-classification
model-index:
- name: GoEmotions DeBERTa v3 Large
  results:
  - task:
      type: text-classification
      name: Multi-label Emotion Classification
    dataset:
      type: go_emotions
      name: GoEmotions
    metrics:
    - type: f1_macro
      value: 0.518
      name: F1 Macro
    - type: f1_micro
      value: 0.598
      name: F1 Micro
    - type: f1_weighted
      value: 0.603
      name: F1 Weighted
datasets:
- google-research-datasets/go_emotions
metrics:
- f1
base_model:
- microsoft/deberta-v3-large
---

# SAMO GoEmotions DeBERTa v3 Large

A multi-label emotion classification model fine-tuned on the GoEmotions dataset using Microsoft's DeBERTa v3 Large architecture.

## Model Description

This model is based on `microsoft/deberta-v3-large` and fine-tuned for multi-label emotion classification on the GoEmotions dataset. It achieves **51.8% F1 Macro** and **59.8% F1 Micro** performance, significantly outperforming baseline models.

### Key Features

- **Architecture**: DeBERTa v3 Large (24 layers, 1024 hidden size, 16 attention heads)
- **Task**: Multi-label emotion classification (27 emotions + neutral)
- **Training**: 3 epochs with BCE loss and class imbalance handling

## Performance Metrics

- **F1 Macro**: 51.8% 
- **F1 Micro**: 59.8% 
- **F1 Weighted**: 60.3% (accounts for class imbalance)

## How to Use

```python
from transformers import pipeline

# Load the model
clf = pipeline(
    "text-classification",
    model="duelker/samo-goemotions-deberta-v3-large",
    tokenizer="duelker/samo-goemotions-deberta-v3-large",
    top_k=None,  # Return all emotions with scores
    truncation=True
)

# Example predictions
texts = [
    "I am feeling really happy today!",
    "I'm frustrated but hopeful about the future.",
    "Thank you so much for your help!"
]

results = clf(texts)
print(results)
```

## Advanced Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("duelker/samo-goemotions-deberta-v3-large")
model = AutoModelForSequenceClassification.from_pretrained("duelker/samo-goemotions-deberta-v3-large")

# Emotion labels
emotion_labels = [
    'admiration', 'amusement', 'anger', 'annoyance', 'approval', 'caring',
    'confusion', 'curiosity', 'desire', 'disappointment', 'disapproval',
    'disgust', 'embarrassment', 'excitement', 'fear', 'gratitude', 'grief',
    'joy', 'love', 'nervousness', 'optimism', 'pride', 'realization',
    'relief', 'remorse', 'sadness', 'surprise', 'neutral'
]

def predict_emotions(text, threshold=0.4):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=256)
    
    with torch.no_grad():
        logits = model(**inputs).logits
        probabilities = torch.sigmoid(logits).squeeze(0)
    
    predictions = {}
    for i, emotion in enumerate(emotion_labels):
        predictions[emotion] = {
            'probability': float(probabilities[i]),
            'predicted': probabilities[i] > threshold
        }
    
    return predictions

# Example usage
text = "I'm so grateful for this opportunity!"
results = predict_emotions(text)
print(results)
```

## Intended Use

- **Journaling Apps**: Analyze emotional content in personal entries
- **Content Moderation**: Detect emotional tone in user-generated content
- **UX Research**: Understand user sentiment and emotional responses
- **Mental Health Apps**: Track emotional patterns and well-being

## Limitations

- **Not Medical Device**: Do not use for clinical diagnosis or high-risk decisions
- **Rare Emotions**: May struggle with very rare emotions
- **Context Length**: Optimized for short to medium-length texts (up to 256 tokens)

## Citation

If you use this model, please cite.

```bibtex


## License

This model is licensed under the Apache 2.0 License.