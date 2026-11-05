---
language: en
license: mit
library_name: transformers
tags:
  - text-classification
  - sentiment-analysis
  - emotion-detection
  - bert
  - pytorch
datasets:
  - dair-ai/emotion
metrics:
  - accuracy
  - f1
pipeline_tag: text-classification
model-index:
  - name: twitter-emotion-bert
    results:
      - task:
          type: text-classification
          name: Emotion Classification
        dataset:
          name: dair-ai/emotion
          type: dair-ai/emotion
        metrics:
          - type: accuracy
            value: 0.9385
          - type: f1
            value: 0.9399
            name: Weighted F1
---

# Twitter Emotion BERT

A fine-tuned `bert-base-cased` model for classifying emotions in text
into six categories: sadness, joy, love, anger, fear, and surprise.

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="gabe-zhang/twitter-emotion-bert",
)

classifier("I am so happy today!")
# [{'label': 'joy', 'score': 0.95}]

classifier("This makes me really angry")
# [{'label': 'anger', 'score': 0.89}]
```

## Labels

| ID | Emotion  |
|----|----------|
| 0  | sadness  |
| 1  | joy      |
| 2  | love     |
| 3  | anger    |
| 4  | fear     |
| 5  | surprise |

## Performance

**Overall:** Accuracy 0.9385 | Weighted F1 0.9399

| Emotion  | Precision | Recall | F1-Score |
|----------|-----------|--------|----------|
| Sadness  | 0.94      | 0.93   | 0.93     |
| Joy      | 0.95      | 0.96   | 0.95     |
| Love     | 0.86      | 0.89   | 0.87     |
| Anger    | 0.93      | 0.90   | 0.91     |
| Fear     | 0.91      | 0.89   | 0.90     |
| Surprise | 0.85      | 0.82   | 0.83     |

## Training

- **Base model:** `bert-base-cased`
- **Dataset:** [dair-ai/emotion](https://huggingface.co/datasets/dair-ai/emotion)
  (~20,000 English Twitter messages)
- **Optimizer:** AdamW, learning rate 1e-5
- **Dropout:** 0.5
- **Max sequence length:** 512
- **Early stopping:** patience 5
- **Class balancing:** Random oversampling for minority classes
- **Framework:** PyTorch Lightning

## Limitations

- Trained on English Twitter text only; may not generalize well to
  other languages or formal writing styles.
- "Love" and "surprise" have lower F1 scores due to smaller
  representation in the training data and overlap with other emotions.
- Short, informal text with slang or emojis may affect predictions.

## Source Code

Full training code, notebooks, and baseline comparisons:
[github.com/gabe-zhang/twitter-emotion-classification](https://github.com/gabe-zhang/twitter-emotion-classification)
