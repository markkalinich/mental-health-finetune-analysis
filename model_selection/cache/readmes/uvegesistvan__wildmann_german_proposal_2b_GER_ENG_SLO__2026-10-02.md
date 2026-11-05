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

# Model Card for uvegesistvan/wildmann_german_proposal_2b_GER_ENG_SLO

## Model Overview
This model is a multi-class emotion classifier trained on German-to-English-to-Slovak machine-translated text data. It identifies nine distinct emotional states in text. The dataset combines synthetic and original German sentences translated sequentially into English and Slovak, presenting unique challenges and opportunities for cross-linguistic emotion classification.

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
The dataset consists of German text first translated into English and then into Slovak. This sequential translation introduces additional linguistic complexity and potential noise. Preprocessing steps included:

- Normalization to reduce noise introduced during translations.
- Undersampling of overrepresented classes, such as "No emotion" and "Anger," to balance the dataset.

### Evaluation Metrics
The model's performance was evaluated using precision, recall, F1-score, and accuracy metrics. Detailed results are as follows:

| Class         | Precision | Recall | F1-Score | Support |
|---------------|-----------|--------|----------|---------|
| Anger (0)     | 0.34      | 0.41   | 0.37     | 777     |
| Fear (1)      | 0.86      | 0.67   | 0.75     | 776     |
| Disgust (2)   | 0.95      | 0.92   | 0.93     | 776     |
| Sadness (3)   | 0.86      | 0.78   | 0.82     | 775     |
| Joy (4)       | 0.84      | 0.73   | 0.78     | 777     |
| Enthusiasm (5)| 0.57      | 0.46   | 0.51     | 776     |
| Hope (6)      | 0.32      | 0.41   | 0.36     | 777     |
| Pride (7)     | 0.84      | 0.60   | 0.70     | 776     |
| No emotion (8)| 0.48      | 0.59   | 0.53     | 1553    |

### Overall Metrics
- **Accuracy**: 0.61
- **Macro Average**: Precision = 0.67, Recall = 0.62, F1-Score = 0.64
- **Weighted Average**: Precision = 0.65, Recall = 0.61, F1-Score = 0.63

### Performance Insights
The model shows strong performance in detecting "Disgust" and "Fear," but struggles with "Anger," "Hope," and "No emotion," likely due to the compounded translation noise and subtle emotional cues being lost in the translation process. These results highlight the challenges of training models on sequentially translated text.

## Model Usage
### Applications
- Emotion analysis of German texts translated sequentially into English and Slovak for sentiment tracking or research.
- Studying cross-linguistic emotion classification in complex multilingual contexts.
- Sentiment analysis for Slovak content derived from German source material through intermediate English translations.

### Limitations
- Sequential translation increases the likelihood of noise and inaccuracies, affecting classification performance for subtle emotional states.
- The model's accuracy is lower compared to models trained on single-step translations, reflecting the challenges introduced by additional linguistic transformations.

### Ethical Considerations
The use of sequentially machine-translated datasets may result in biases or inaccuracies due to compounded linguistic and cultural nuances being lost in translation. Users should carefully evaluate the model for their specific use case, particularly in sensitive applications such as mental health or social studies.

### Citation
For further information, visit: [uvegesistvan/wildmann_german_proposal_2b_GER_ENG_SLO](#)
