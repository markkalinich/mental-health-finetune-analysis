---
language: en
license: mit
tags:
  - emotion-classification
  - text-analysis
metrics:
  - precision
  - recall
  - f1-score
  - accuracy
---

# Model Card for uvegesistvan/wildmann_german_proposal_1

## Model Overview
This model is a multi-class emotion classifier trained to identify nine distinct emotional states in text. The classes and their corresponding labels are as follows:

- **Anger (0)**
- **Fear (1)**
- **Disgust (2)**
- **Sadness (3)**
- **Joy (4)**
- **Enthusiasm (5)**
- **Hope (6)**
- **Pride (7)**
- **No emotion (8)**

### Dataset and Preprocessing
The dataset underwent undersampling to balance the two most frequent classes ("Anger" and "No emotion") with the others. This adjustment aimed to mitigate class imbalance and improve model performance across all labels.

### Evaluation Metrics
The model was evaluated using precision, recall, F1-score, and support for each class. Below are the detailed metrics:

| Class      | Precision | Recall | F1-Score | Support |
|------------|-----------|--------|----------|---------|
| Anger (0)  | 0.62      | 0.63   | 0.62     | 777     |
| Fear (1)   | 0.49      | 0.59   | 0.54     | 317     |
| Disgust (2)| 0.61      | 0.56   | 0.59     | 105     |
| Sadness (3)| 0.65      | 0.61   | 0.63     | 333     |
| Joy (4)    | 0.65      | 0.71   | 0.68     | 427     |
| Enthusiasm (5) | 0.45  | 0.42   | 0.44     | 544     |
| Hope (6)   | 0.53      | 0.57   | 0.55     | 777     |
| Pride (7)  | 0.47      | 0.57   | 0.52     | 354     |
| No emotion (8) | 0.46  | 0.36   | 0.41     | 777     |

### Overall Metrics
- **Accuracy**: 0.54
- **Macro Average**: Precision = 0.55, Recall = 0.56, F1-Score = 0.55
- **Weighted Average**: Precision = 0.54, Recall = 0.54, F1-Score = 0.54

### Performance Insights
The model achieves reasonable accuracy and F1-scores across most classes. However, classes like "Fear" (1) and "No emotion" (8) exhibit lower performance, which may stem from either insufficient training samples or ambiguous cases in the dataset.

## Model Usage
### Applications
- Emotion classification in text-based datasets.
- Analyzing emotional tone in social media, reviews, or other text corpora.

### Limitations
- Performance varies across classes, with some (e.g., "Fear" and "No emotion") showing lower recall.
- The model may not generalize well to domains outside the training data.

### Ethical Considerations
The model's predictions might not always align with human interpretations of emotions, particularly in ambiguous or context-dependent cases. Misclassification could lead to inappropriate conclusions if used in sensitive applications (e.g., mental health monitoring).


