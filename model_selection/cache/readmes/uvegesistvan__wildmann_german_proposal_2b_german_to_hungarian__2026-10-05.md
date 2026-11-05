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

# Model Card for uvegesistvan/wildmann_german_proposal_2b_german_to_english

## Model Overview
This model is a multi-class emotion classifier trained on German-to-English machine-translated text data. It identifies nine distinct emotional states in text. The model's performance reflects the impact of training on machine-translated datasets, emphasizing its ability to generalize across linguistic variations. 

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
The dataset consists of German text that has been machine-translated into English and annotated for emotional content. Preprocessing included normalization of translated text to reduce noise introduced by translation errors. Undersampling was applied to balance the most frequent classes ("Anger" and "No emotion") with less frequent ones to ensure equitable learning across all labels.

### Evaluation Metrics
The model was evaluated using precision, recall, F1-score, and accuracy metrics. Below are the detailed performance metrics:

| Class      | Precision | Recall | F1-Score | Support |
|------------|-----------|--------|----------|---------|
| Anger (0)  | 0.54      | 0.58   | 0.56     | 777     |
| Fear (1)   | 0.88      | 0.73   | 0.80     | 776     |
| Disgust (2)| 0.93      | 0.94   | 0.94     | 776     |
| Sadness (3)| 0.86      | 0.84   | 0.85     | 775     |
| Joy (4)    | 0.82      | 0.81   | 0.82     | 777     |
| Enthusiasm (5) | 0.61  | 0.62   | 0.62     | 776     |
| Hope (6)   | 0.52      | 0.52   | 0.52     | 777     |
| Pride (7)  | 0.75      | 0.80   | 0.77     | 776     |
| No emotion (8) | 0.64  | 0.65   | 0.65     | 1553    |

### Overall Metrics
- **Accuracy**: 0.71
- **Macro Average**: Precision = 0.73, Recall = 0.72, F1-Score = 0.72
- **Weighted Average**: Precision = 0.72, Recall = 0.71, F1-Score = 0.72

### Performance Insights
The model demonstrates strong performance in most emotion classes, especially for "Fear" and "Disgust." However, classes like "Hope" and "Enthusiasm" exhibit slightly lower scores, likely due to inherent challenges in identifying subtle emotions within machine-translated text.

## Model Usage
### Applications
- Emotion analysis of German texts via machine-translated English representations.
- Detecting emotional tone in multilingual datasets where German-English translations are present.

### Limitations
- Performance depends on the quality of the machine-translated text. Errors in translation could propagate and affect classification results.
- Subtle or ambiguous emotional states may be misclassified due to translation noise or lack of context.

### Ethical Considerations
As the dataset is machine-translated, cultural and linguistic nuances might be lost, leading to potential biases or misinterpretations. Users should exercise caution when applying the model to sensitive domains such as mental health or social research.
