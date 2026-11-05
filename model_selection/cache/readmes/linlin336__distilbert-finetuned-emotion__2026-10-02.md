---
language: en
license: apache-2.0
tags:
  - emotion
  - sentiment-analysis
  - distilbert
  - twitter
  - text-classification
datasets:
  - emotion
metrics:
  - accuracy
  - f1
model-index:
  - name: distilbert-finetuned-emotion
    results:
      - task:
          type: text-classification
          name: Text Classification
        dataset:
          name: emotion
          type: emotion
        metrics:
          - type: accuracy
            value: 0.92
            name: Accuracy
          - type: f1
            value: 0.92
            name: F1 (weighted)
---

# DistilBERT Fine-Tuned for Emotion Detection

## Model Description

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the [Emotion](https://huggingface.co/datasets/emotion) dataset for detecting emotions in English Twitter text.

The model classifies text into **six basic emotions**:

| Label | Emotion |
|-------|---------|
| 0 | sadness |
| 1 | joy |
| 2 | love |
| 3 | anger |
| 4 | fear |
| 5 | surprise |

## Intended Use

- Detecting emotional states in short English text (tweets, messages, comments)
- Social media monitoring and sentiment analysis
- Customer feedback emotion classification

## Training Details

| Parameter | Value |
|-----------|-------|
| Base Model | distilbert-base-uncased |
| Dataset | emotion (16,000 train / 2,000 validation) |
| Epochs | 1 |
| Learning Rate | 1e-3 |
| Batch Size | 8 |
| Weight Decay | 0.01 |

## Evaluation Results

- **Accuracy**: ~92%
- **F1-Score (weighted)**: ~92%

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="<your-username>/distilbert-finetuned-emotion"
)

result = classifier("I am feeling great today!")
print(result)
# [{'label': 'joy', 'score': 0.98}]
```

## Limitations

- Trained on Twitter data — may not generalize well to formal text
- Class imbalance: `joy` and `sadness` are overrepresented
- `surprise` and `love` are the most challenging categories
- Only 1 epoch of fine-tuning — additional training may improve performance

## License

Apache 2.0
