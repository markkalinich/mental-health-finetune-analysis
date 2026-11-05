---
language: en
tags:
- sentiment-analysis
- game-reviews
- text-classification
- wm-grsa-roberta-softmax
license: mit
datasets:
- game-reviews
metrics:
- accuracy
- f1
- precision
- recall
---

# Wm-Grsa-Roberta-Softmax - Game Review Sentiment Analysis

## Model Description

This model performs sentiment analysis on game reviews, classifying them into three categories:
- **Positive**: Favorable reviews
- **Mixed**: Neutral or mixed sentiment reviews
- **Negative**: Unfavorable reviews

**Model Type**: Wm-Grsa-Roberta-Softmax

**Training Date**: 2025-12-25

## Performance

### Test Set Metrics

| Metric | Score |
|--------|-------|
| Accuracy | 0.8827 |
| F1-Score | 0.8278 |
| Precision | 0.8313 |
| Recall | 0.8247 |

### Training Information

- **Training Time**: 13961.28 seconds
- **Training Samples**: 629,884
- **Validation Samples**: 78,735
- **Test Samples**: 78,737

## Model Configuration

```json
{
  "model_name": "FacebookAI/roberta-base",
  "max_length": 256,
  "batch_size": 64,
  "learning_rate": 1e-05,
  "num_epochs": 5,
  "warmup_steps": 0,
  "weight_decay": 0.01,
  "subset": 1.0
}
```

## Usage

### Loading the Model

```python
from pathlib import Path
import pickle

# Load the model components
model_dir = Path("path/to/model")

with open(model_dir / 'vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

with open(model_dir / 'classifier.pkl', 'rb') as f:
    classifier = pickle.load(f)

with open(model_dir / 'label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)
```

### Making Predictions

```python
# Example reviews
reviews = [
    "This game is absolutely amazing! Best game I've played this year.",
    "It's okay, nothing special but not terrible either.",
    "Terrible game, waste of money and time."
]

# Transform and predict
X = vectorizer.transform(reviews)
predictions_encoded = classifier.predict(X)
predictions = label_encoder.inverse_transform(predictions_encoded)

print(predictions)
# Output: ['positive', 'mixed', 'negative']

# Get probabilities
probabilities = classifier.predict_proba(X)
print(probabilities)
```

## Per-Class Performance


| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|----------|
| Positive | 0.9379 | 0.9494 | 0.9436 | 45859 |
| Mixed | 0.6791 | 0.6417 | 0.6599 | 12697 |
| Negative | 0.8770 | 0.8830 | 0.8800 | 20181 |


## Feature Importance

The model identifies important words/phrases for each sentiment class. See `results.json` for the complete feature importance analysis.

## Limitations

- The model is trained specifically on game reviews and may not generalize well to other domains
- Performance may vary on reviews with sarcasm or nuanced sentiments
- The model treats text as bag-of-words and doesn't capture word order

## Training Details

This model was trained as part of a game review sentiment analysis project. For more information, see the project repository.

## Files

- `vectorizer.pkl`: TF-IDF vectorizer
- `classifier.pkl`: Trained classifier
- `label_encoder.pkl`: Label encoder for sentiment classes
- `config.json`: Model configuration
- `results.json`: Complete training results and metrics

## Citation

If you use this model, please cite:

```
@misc{game_review_sentiment,
  author = {Game Review Sentiment Analysis Project},
  title = {Sentiment Analysis Model for Game Reviews},
  year = {2025},
  url = {https://huggingface.co/wm-grsa-roberta-softmax}
}
```
