---
language: pl
license: mit
tags:
  - emotion-classification
  - text-analysis
  - machine-translation
metrics:
  - precision
  - recall
  - f1-score
  - accuracy
---

# Model Card for uvegesistvan/wildmann_german_proposal_2b_german_to_polish

## Model Overview
This model is a multi-class emotion classifier trained on German-to-Polish machine-translated text data. It identifies nine distinct emotional states in text. By leveraging a dataset that combines synthetic and original German sentences translated into Polish, the model demonstrates its capability to generalize across linguistic variations introduced by machine translation.

### Emotion Classes
The model classifies the following emotional states:

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
The dataset consists of German text machine-translated into Polish and annotated for emotional content. It includes a mix of synthetic and original sentences to ensure diversity. Preprocessing steps included:

- Normalization to reduce noise from machine translation.
- Undersampling of overrepresented classes, such as "No emotion" and "Anger," to balance the dataset.

### Evaluation Metrics
The model's performance was evaluated using precision, recall, F1-score, and accuracy metrics. Detailed results are as follows:

| Class         | Precision | Recall | F1-Score | Support |
|---------------|-----------|--------|----------|---------|
| Anger (0)     | 0.52      | 0.61   | 0.56     | 777     |
| Fear (1)      | 0.89      | 0.74   | 0.81     | 776     |
| Disgust (2)   | 0.91      | 0.94   | 0.93     | 776     |
| Sadness (3)   | 0.88      | 0.83   | 0.85     | 775     |
| Joy (4)       | 0.82      | 0.81   | 0.81     | 777     |
| Enthusiasm (5)| 0.64      | 0.63   | 0.63     | 776     |
| Hope (6)      | 0.51      | 0.52   | 0.52     | 777     |
| Pride (7)     | 0.74      | 0.80   | 0.77     | 776     |
| No emotion (8)| 0.66      | 0.64   | 0.65     | 1553    |

### Overall Metrics
- **Accuracy**: 0.72
- **Macro Average**: Precision = 0.73, Recall = 0.73, F1-Score = 0.73
- **Weighted Average**: Precision = 0.72, Recall = 0.72, F1-Score = 0.72

### Performance Insights
The model performs well across most classes, with strong results for "Disgust" and "Fear." However, classes like "Hope" and "Anger" exhibit slightly lower precision and recall, reflecting challenges in distinguishing more subtle or overlapping emotional states in the Polish translation.

## Model Usage
### Applications
- Emotion analysis of German texts translated into Polish for sentiment tracking or social research.
- Research on cross-linguistic emotion classification using Polish datasets derived from German text.
- Sentiment analysis for customer feedback or user-generated content in Polish.

### Limitations
- The model's performance may vary depending on the quality of the machine-translated text. Errors in translation can introduce misclassifications.
- Subtle or culturally specific emotional expressions may not translate accurately, impacting classification outcomes.

### Ethical Considerations
The use of machine-translated datasets introduces potential biases or inaccuracies due to linguistic and cultural nuances being lost in translation. Users should evaluate the model's suitability for specific applications, especially in sensitive domains like mental health or social research.

### Citation
For further information, visit: [uvegesistvan/wildmann_german_proposal_2b_german_to_polish](#)
