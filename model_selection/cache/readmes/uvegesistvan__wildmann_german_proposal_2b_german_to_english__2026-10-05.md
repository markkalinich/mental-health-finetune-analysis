---
language: en
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

# Model Card for uvegesistvan/wildmann_german_proposal_2b

## Model Overview
This model is a multi-class emotion classifier trained on German-to-English machine-translated text data. It identifies nine distinct emotional states in text. The model leverages the strengths of a diverse dataset, balancing both synthetic and original German sentences translated into English, emphasizing its ability to generalize across linguistic and cultural variations introduced by machine translation.

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
The dataset consists of German text machine-translated into English and annotated for emotional content. 
It includes both synthetic and original sentences to enhance diversity. P
reprocessing involved:

- Undersampling of overrepresented classes, such as "No emotion" and "Anger," to ensure balanced training across all labels.

### Evaluation Metrics
The model's performance was evaluated using precision, recall, F1-score, and accuracy metrics. Detailed results are as follows:

| Class         | Precision | Recall | F1-Score | Support |
|---------------|-----------|--------|----------|---------|
| Anger (0)     | 0.54      | 0.58   | 0.56     | 777     |
| Fear (1)      | 0.79      | 0.79   | 0.79     | 776     |
| Disgust (2)   | 0.96      | 0.93   | 0.94     | 776     |
| Sadness (3)   | 0.86      | 0.83   | 0.84     | 775     |
| Joy (4)       | 0.82      | 0.82   | 0.82     | 777     |
| Enthusiasm (5)| 0.64      | 0.61   | 0.63     | 776     |
| Hope (6)      | 0.51      | 0.57   | 0.54     | 777     |
| Pride (7)     | 0.71      | 0.82   | 0.76     | 776     |
| No emotion (8)| 0.70      | 0.62   | 0.66     | 1553    |

### Overall Metrics
- **Accuracy**: 0.72
- **Macro Average**: Precision = 0.73, Recall = 0.73, F1-Score = 0.73
- **Weighted Average**: Precision = 0.72, Recall = 0.72, F1-Score = 0.72

### Performance Insights
The model shows high accuracy in detecting "Disgust" and "Fear," while "Hope" and "Enthusiasm" demonstrate slightly lower performance due to subtle nuances or translation noise. These results highlight the trade-offs involved when training on machine-translated text.

## Model Usage
### Applications
- Emotion analysis of German texts by leveraging English machine translation as an intermediary step.
- Research on cross-linguistic emotion classification in multilingual datasets.
- Sentiment analysis for social media or user feedback originally in German.

### Limitations
- The model's performance is influenced by the quality of the machine-translated text. Translation errors or omissions could lead to misclassifications.
- Subtle emotional expressions may not always translate effectively, potentially introducing inaccuracies in classification.

### Ethical Considerations
The use of machine-translated datasets may lead to biases or inaccuracies due to linguistic and cultural nuances being lost during translation. Users should carefully evaluate the model before applying it to sensitive domains such as mental health, social research, or customer sentiment analysis.

### Citation
For further information, visit: [uvegesistvan/wildmann_german_proposal_2b](#)
