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

# Model Card for uvegesistvan/wildmann_german_proposal_2b_german_to_czech

## Model Overview
This model is a multi-class emotion classifier trained on German-to-Czech machine-translated text data. It identifies nine distinct emotional states in text and demonstrates how machine-translated datasets can support emotion classification tasks across different languages.

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
The dataset includes German text machine-translated into Czech and annotated for emotional content. Both synthetic and original German sentences were translated to create a diverse corpus. Preprocessing steps included:

- Balancing classes through undersampling of overrepresented labels, such as "No emotion" and "Anger."
- Normalization of text to handle inconsistencies from the machine translation process.

### Evaluation Metrics
The model's performance was evaluated using standard classification metrics. Results are summarized below:

| Class         | Precision | Recall | F1-Score | Support |
|---------------|-----------|--------|----------|---------|
| Anger (0)     | 0.50      | 0.63   | 0.56     | 777     |
| Fear (1)      | 0.84      | 0.74   | 0.79     | 776     |
| Disgust (2)   | 0.91      | 0.94   | 0.93     | 776     |
| Sadness (3)   | 0.87      | 0.83   | 0.85     | 775     |
| Joy (4)       | 0.83      | 0.81   | 0.82     | 777     |
| Enthusiasm (5)| 0.61      | 0.61   | 0.61     | 776     |
| Hope (6)      | 0.54      | 0.46   | 0.50     | 777     |
| Pride (7)     | 0.75      | 0.81   | 0.78     | 776     |
| No emotion (8)| 0.66      | 0.64   | 0.65     | 1553    |

### Overall Metrics
- **Accuracy**: 0.71
- **Macro Average**: Precision = 0.72, Recall = 0.72, F1-Score = 0.72
- **Weighted Average**: Precision = 0.72, Recall = 0.71, F1-Score = 0.71

### Performance Insights
The model performs well across most classes, particularly in "Disgust" and "Fear." However, classes such as "Hope" exhibit lower F1-scores, potentially due to translation noise or subtle emotional cues being lost in machine translation.

## Model Usage
### Applications
- Emotion analysis of German texts translated into Czech.
- Sentiment tracking in Czech-language customer feedback derived from German text.
- Research on cross-linguistic emotion classification in multilingual datasets.

### Limitations
- The model's performance is influenced by the quality of the machine-translated text, which may introduce biases or inaccuracies.
- Subtle emotional states like "Hope" may be harder to classify due to translation inconsistencies.

### Ethical Considerations
The reliance on machine-translated datasets means that cultural and linguistic nuances may be lost, potentially impacting classification accuracy. Users should carefully evaluate the model before applying it in sensitive areas, such as mental health or customer sentiment analysis.

### Citation
For further information, visit: [uvegesistvan/wildmann_german_proposal_2b_german_to_czech](#)
