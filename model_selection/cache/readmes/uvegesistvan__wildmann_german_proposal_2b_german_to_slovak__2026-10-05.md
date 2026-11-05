---
language: sk
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

# Model Card for uvegesistvan/wildmann_german_proposal_2b_german_to_slovak

## Model Overview
This model is a multi-class emotion classifier trained on German-to-Slovak machine-translated text data. It identifies nine distinct emotional states in text. The model utilizes a diverse dataset, incorporating both synthetic and original German sentences translated into Slovak, highlighting its ability to generalize across linguistic variations introduced by machine translation.

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
The dataset consists of German text machine-translated into Slovak and annotated for emotional content. It includes both synthetic and original sentences to enhance diversity. Preprocessing involved:

- Undersampling of overrepresented classes, such as "No emotion" and "Anger," to ensure balanced training across all labels.

### Evaluation Metrics
The model's performance was evaluated using precision, recall, F1-score, and accuracy metrics. Detailed results are as follows:

| Class         | Precision | Recall | F1-Score | Support |
|---------------|-----------|--------|----------|---------|
| Anger (0)     | 0.54      | 0.58   | 0.56     | 777     |
| Fear (1)      | 0.84      | 0.78   | 0.81     | 776     |
| Disgust (2)   | 0.93      | 0.94   | 0.93     | 776     |
| Sadness (3)   | 0.85      | 0.84   | 0.84     | 775     |
| Joy (4)       | 0.82      | 0.80   | 0.81     | 777     |
| Enthusiasm (5)| 0.62      | 0.64   | 0.63     | 776     |
| Hope (6)      | 0.53      | 0.54   | 0.54     | 777     |
| Pride (7)     | 0.74      | 0.79   | 0.77     | 776     |
| No emotion (8)| 0.67      | 0.63   | 0.65     | 1553    |

### Overall Metrics
- **Accuracy**: 0.72
- **Macro Average**: Precision = 0.73, Recall = 0.73, F1-Score = 0.73
- **Weighted Average**: Precision = 0.72, Recall = 0.72, F1-Score = 0.72

### Performance Insights
The model demonstrates robust performance in detecting "Fear" and "Disgust," while "Hope" and "Enthusiasm" show slightly lower performance due to subtleties in emotional expression and potential translation noise. These results reflect the complexities of training on machine-translated text.

## Model Usage
### Applications
- Emotion analysis of German texts translated into Slovak for social research or sentiment tracking.
- Research on cross-linguistic emotion classification in multilingual datasets.
- Sentiment analysis for Slovak-language customer feedback derived from German text.

### Limitations
- The model's performance depends on the quality of the machine-translated text. Translation errors or ambiguities may impact classification accuracy.
- Subtle emotional expressions may be misclassified due to linguistic nuances being lost in translation.

### Ethical Considerations
The use of machine-translated datasets introduces the possibility of biases or inaccuracies caused by the loss of cultural and linguistic subtleties during translation. Users should carefully evaluate the model's performance before applying it in sensitive contexts such as mental health, social studies, or customer sentiment analysis.

### Citation
For further information, visit: [uvegesistvan/wildmann_german_proposal_2b_german_to_slovak](#)
