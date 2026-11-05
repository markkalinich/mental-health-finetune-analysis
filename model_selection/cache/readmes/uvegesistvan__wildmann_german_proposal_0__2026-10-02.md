---
language: multilingual
tags:
- classification
- emotions
license: apache-2.0
metrics:
- precision
- recall
- f1-score
- accuracy
---

# Emotion Classification Model

## Model Description
This model is a fine-tuned version of `xlm-roberta-large` for multilingual emotion classification tasks. It is trained to classify text into 9 distinct emotion categories:

- **Anger (0)**
- **Fear (1)**
- **Disgust (2)**
- **Sadness (3)**
- **Joy (4)**
- **Enthusiasm (5)**
- **Hope (6)**
- **Pride (7)**
- **No emotion (8)**

The model is designed to analyze input text and predict the corresponding emotion, including the neutral "No emotion" category.

---

## Model Performance
The model was evaluated on a dataset of 12,022 examples (10% of all data). Below is a summary of the performance metrics across all categories:

| Emotion        | Precision | Recall | F1-Score | Support |
|----------------|-----------|--------|----------|---------|
| Anger (0)      | 0.70      | 0.50   | 0.59     | 2936    |
| Fear (1)       | 0.56      | 0.13   | 0.21     | 317     |
| Disgust (2)    | 0.56      | 0.35   | 0.43     | 105     |
| Sadness (3)    | 0.69      | 0.40   | 0.51     | 334     |
| Joy (4)        | 0.58      | 0.56   | 0.57     | 427     |
| Enthusiasm (5) | 0.42      | 0.15   | 0.23     | 544     |
| Hope (6)       | 0.50      | 0.20   | 0.29     | 777     |
| Pride (7)      | 0.57      | 0.32   | 0.41     | 354     |
| No emotion (8) | 0.64      | 0.88   | 0.74     | 6228    |

### Overall Metrics
- **Accuracy**: 64%
- **Macro Average**: Precision: 0.58, Recall: 0.39, F1-Score: 0.44
- **Weighted Average**: Precision: 0.63, Recall: 0.64, F1-Score: 0.61

---

## Usage

### Input
The model expects a text input in UTF-8 format. The input can be a sentence, paragraph, or any textual data.

### Output
The model outputs a predicted emotion label from the predefined categories, along with the associated confidence scores.

### Example
```python
from transformers import pipeline

classifier = pipeline("text-classification", model="uvegesistvan/wildmann_german_proposal_0")

text = "Ich bin so glücklich über die Fortschritte, die ich gemacht habe!"
prediction = classifier(text)

print(prediction)
# Output: [{'label': 'Joy', 'score': 0.85}]
```

## Training Data
The model was trained on a dataset containing labeled examples for 9 emotions. All training data was on german. The "No emotion" category is the most represented in the dataset.

## Limitations and Bias
- The model's performance may vary across languages or cultural contexts not well-represented in the training data.
- The "Fear" and "Enthusiasm" categories have lower recall and F1 scores, indicating potential underperformance in these classes.

