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

# Model Card for uvegesistvan/wildmann_german_proposal_2b_pooled_english

## Model Overview
This model is a multi-class emotion classifier trained on German text translated into English as an intermediate step, followed by translations into Czech, Polish, Slovak, and Hungarian. The model identifies nine distinct emotional states in text, leveraging a pooled dataset designed to capture multilingual and cross-linguistic variations in emotion expression.

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
The dataset consists of German text first translated into English, then subsequently into Czech, Polish, Slovak, and Hungarian. Preprocessing steps included:

- Normalization to mitigate noise introduced during sequential translations.
- Balancing of the dataset through undersampling of overrepresented classes such as "No emotion" and "Anger."

### Evaluation Metrics
The model's performance was evaluated using precision, recall, F1-score, and accuracy metrics. Detailed results are as follows:

| Class         | Precision | Recall | F1-Score | Support |
|---------------|-----------|--------|----------|---------|
| Anger (0)     | 0.57      | 0.50   | 0.53     | 3108    |
| Fear (1)      | 0.82      | 0.76   | 0.79     | 3104    |
| Disgust (2)   | 0.94      | 0.94   | 0.94     | 3104    |
| Sadness (3)   | 0.84      | 0.85   | 0.85     | 3100    |
| Joy (4)       | 0.72      | 0.86   | 0.78     | 3108    |
| Enthusiasm (5)| 0.67      | 0.57   | 0.61     | 3104    |
| Hope (6)      | 0.48      | 0.55   | 0.51     | 3108    |
| Pride (7)     | 0.74      | 0.78   | 0.76     | 3104    |
| No emotion (8)| 0.65      | 0.63   | 0.64     | 6212    |

### Overall Metrics
- **Accuracy**: 0.71
- **Macro Average**: Precision = 0.71, Recall = 0.71, F1-Score = 0.71
- **Weighted Average**: Precision = 0.71, Recall = 0.71, F1-Score = 0.70

### Performance Insights
The model performs strongly on classes such as "Disgust," "Fear," and "Sadness," but struggles with "Anger," "Hope," and "Enthusiasm," likely due to translation noise and the complexity of subtle emotional states across multiple linguistic transformations. The intermediate English step adds consistency to the translations but also introduces its own challenges in emotion classification.

## Model Usage
### Applications
- Emotion analysis of texts originating in German and translated into English and subsequently into Czech, Polish, Slovak, or Hungarian.
- Sentiment tracking and research in complex multilingual contexts.
- Cross-linguistic studies of emotion expression across multiple languages.

### Limitations
- Sequential translations introduce cumulative noise and may obscure subtle emotional states.
- Performance may vary across different languages due to differences in linguistic structures and cultural expressions of emotion.

### Ethical Considerations
The reliance on sequential translations may amplify biases or inaccuracies from the machine translation systems. Users should validate the model for their specific use cases, especially in sensitive domains such as mental health or cultural studies.

### Citation
For further information, visit: [uvegesistvan/wildmann_german_proposal_2b_pooled_english](#)
