---
language: en
tags:
- sentiment-analysis
- game-reviews
- text-classification
- roberta
license: mit
datasets:
- game-reviews
metrics:
- accuracy
- f1
- precision
- recall
---

# Roberta - Game Review Sentiment Analysis

## Model Description

This model performs sentiment analysis on game reviews, classifying them into three categories:
- **Positive**: Favorable reviews
- **Mixed**: Neutral or mixed sentiment reviews
- **Negative**: Unfavorable reviews

**Model Type**: Roberta

**Training Date**: 2025-11-03

## Performance

### Test Set Metrics

| Metric | Score |
|--------|-------|
| Accuracy | 0.8810 |
| F1-Score | 0.8790 |
| Precision | 0.8776 |
| Recall | 0.8810 |

### Training Information

- **Training Time**: 669.81 seconds
- **Training Samples**: 629,884
- **Validation Samples**: 78,735
- **Test Samples**: 78,737

## Model Configuration

```json
{
  "model_name": "FacebookAI/roberta-base",
  "max_length": 256,
  "batch_size": 32,
  "learning_rate": 2e-05,
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
| Positive | 0.9359 | 0.9489 | 0.9423 | 45859 |
| Mixed | 0.6820 | 0.6166 | 0.6476 | 12697 |
| Negative | 0.8683 | 0.8932 | 0.8806 | 20181 |


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
  url = {https://huggingface.co/roberta}
}
```
