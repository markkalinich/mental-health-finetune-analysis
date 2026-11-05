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

# Model Card for uvegesistvan/wildmann_german_proposal_2b

## Model Overview
This model is a multi-class emotion classifier trained to identify nine distinct emotional states in text. The classes and their corresponding labels are as follows:

- **Class 0**: Anger
- **Class 1**: Fear
- **Class 2**: Disgust
- **Class 3**: Sadness
- **Class 4**: Joy
- **Class 5**: Enthusiasm
- **Class 6**: Hope
- **Class 7**: Pride
- **Class 8**: No emotion

### Dataset and Preprocessing
The dataset combines original and synthetic data to improve class balance and performance. Below are the evaluation metrics for the model:

| Class      | Precision | Recall | F1-Score | Support |
|------------|-----------|--------|----------|---------|
| Anger (0)| 0.54      | 0.60   | 0.57     | 777     |
| Fear (1)    | 0.85      | 0.76   | 0.80     | 776     |
| Disgust (2)| 0.91     | 0.95   | 0.93     | 776     |
| Sadness (3)| 0.87      | 0.84   | 0.86     | 775     |
| Joy (4)  | 0.84      | 0.81   | 0.83     | 777     |
| Enthusiasm (5)| 0.64      | 0.62   | 0.63     | 776     |
| Hope (6)   | 0.53      | 0.55   | 0.54     | 777     |
| Pride (7)  | 0.75      | 0.81   | 0.78     | 776     |
| No emotion (8)| 0.67 | 0.65 | 0.66     | 1553    |

### Overall Metrics
- **Accuracy**: 0.72
- **Macro Average**: Precision = 0.73, Recall = 0.73, F1-Score = 0.73
- **Weighted Average**: Precision = 0.73, Recall = 0.72, F1-Score = 0.73

### Performance Insights
The model achieves strong performance across most classes, particularly for "Sadness" and "Disgust." 
However, "Enthusiasm" and "Hope" exhibit lower recall and precision, suggesting potential areas for improvement. 
Future development could include targeted data augmentation or specialized techniques to handle these classes.

## Model Usage
### Applications
- Emotion classification in text-based datasets.
- Analyzing emotional tone in social media, reviews, or other text corpora.
- Understanding emotional context for human-computer interaction.

### Limitations
- Performance varies across classes, with some (e.g., "Enthusiasm" and "Hope") showing lower metrics.
- The model may not generalize well to domains outside the training data.
- Ambiguities in text can lead to misclassification, especially for overlapping emotional states.

### Ethical Considerations
The model's predictions might not always align with human interpretations of emotions, particularly in ambiguous or context-dependent cases. 
Misclassification could lead to inappropriate conclusions if used in sensitive applications (e.g., mental health monitoring or automated decision-making).

### Future Work
- Improving performance on underrepresented classes using advanced augmentation or transfer learning techniques.
- Exploring the model's performance in multi-domain datasets.
- Adding explainability features to enhance trustworthiness in sensitive applications.
