---
language: cs
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

# Model Card for uvegesistvan/wildmann_german_proposal_2b_GER_ENG_CZ

## Model Overview
This model is a multi-class emotion classifier trained on German text that was first machine-translated into English as an intermediary language and then into Czech. It identifies nine distinct emotional states in text. The training process explores the impact of multi-step machine translation on emotion classification accuracy and robustness.

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
The dataset was created using a three-step machine translation process: German → English → Czech. Emotional annotations were applied after the final translation to ensure consistency. Preprocessing steps included:

- Balancing the dataset through undersampling overrepresented classes like "No emotion" and "Anger."
- Normalizing text to mitigate noise introduced by multi-step translations.

### Evaluation Metrics
The model's performance was evaluated using standard classification metrics. Results are detailed below:

| Class         | Precision | Recall | F1-Score | Support |
|---------------|-----------|--------|----------|---------|
| Anger (0)     | 0.55      | 0.53   | 0.54     | 777     |
| Fear (1)      | 0.85      | 0.75   | 0.80     | 776     |
| Disgust (2)   | 0.90      | 0.95   | 0.92     | 776     |
| Sadness (3)   | 0.86      | 0.83   | 0.85     | 775     |
| Joy (4)       | 0.85      | 0.80   | 0.82     | 777     |
| Enthusiasm (5)| 0.67      | 0.59   | 0.63     | 776     |
| Hope (6)      | 0.52      | 0.49   | 0.51     | 777     |
| Pride (7)     | 0.75      | 0.79   | 0.77     | 776     |
| No emotion (8)| 0.60      | 0.69   | 0.64     | 1553    |

### Overall Metrics
- **Accuracy**: 0.71
- **Macro Average**: Precision = 0.73, Recall = 0.71, F1-Score = 0.72
- **Weighted Average**: Precision = 0.71, Recall = 0.71, F1-Score = 0.71

### Performance Insights
The model performs well in classes such as "Disgust" and "Fear." However, "Hope" and "Enthusiasm" classes show slightly lower performance, likely due to complexities introduced by the multi-step translation process. Overall, the model demonstrates strong performance across most classes.

## Model Usage
### Applications
- Emotion analysis of German texts via machine-translated Czech representations.
- Sentiment analysis for Czech-language datasets derived from multilingual sources.
- Research on the effects of multi-step machine translation in emotion classification.

### Limitations
- The multi-step translation process introduces additional noise, potentially impacting classification accuracy for subtle or ambiguous emotions.
- Emotional nuances and cultural context might be lost during translation.

### Ethical Considerations
The reliance on multi-step machine translation can amplify biases or inaccuracies introduced at each stage. Careful validation is recommended before applying the model in sensitive areas such as mental health, social research, or customer feedback analysis.

### Citation
For further information, visit: [uvegesistvan/wildmann_german_proposal_2b_GER_ENG_CZ](#)
