---
language: hu
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

## Model Overview
This model is a multi-class emotion classifier trained on German text translated equally into Hungarian, Polish, Slovak, and Czech. It identifies nine distinct emotional states in text. The dataset combines synthetic and original German sentences translated into four target languages, offering insights into multilingual emotion classification in a cross-linguistic setting.

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
The dataset comprises German text translated equally into Hungarian, Polish, Slovak, and Czech, ensuring balanced representation of target languages. Preprocessing steps included:

- Normalization to address linguistic variations across translations.
- Undersampling of overrepresented classes, such as "No emotion" and "Anger," to balance the dataset.

### Evaluation Metrics
The model's performance was evaluated using precision, recall, F1-score, and accuracy metrics. Detailed results are as follows:

| Class         | Precision | Recall | F1-Score | Support |
|---------------|-----------|--------|----------|---------|
| Anger (0)     | 0.50      | 0.66   | 0.57     | 3108    |
| Fear (1)      | 0.84      | 0.76   | 0.80     | 3104    |
| Disgust (2)   | 0.93      | 0.93   | 0.93     | 3104    |
| Sadness (3)   | 0.89      | 0.82   | 0.85     | 3100    |
| Joy (4)       | 0.76      | 0.85   | 0.80     | 3108    |
| Enthusiasm (5)| 0.63      | 0.60   | 0.62     | 3104    |
| Hope (6)      | 0.49      | 0.55   | 0.52     | 3108    |
| Pride (7)     | 0.76      | 0.78   | 0.77     | 3104    |
| No emotion (8)| 0.71      | 0.58   | 0.64     | 6212    |

### Overall Metrics
- **Accuracy**: 0.71
- **Macro Average**: Precision = 0.72, Recall = 0.73, F1-Score = 0.72
- **Weighted Average**: Precision = 0.72, Recall = 0.71, F1-Score = 0.71

### Performance Insights
The model performs well in identifying "Disgust," "Fear," and "Joy," while "Anger," "Hope," and "No emotion" present challenges due to the subtlety of these emotions and the potential noise introduced during translation. Balancing across four target languages adds complexity, yet the model demonstrates robust cross-linguistic classification capabilities.

## Model Usage
### Applications
- Multilingual emotion analysis for texts originating in German and translated into Hungarian, Polish, Slovak, or Czech.
- Sentiment tracking or research in cross-linguistic contexts.
- Studying emotion classification across multiple languages with machine-translated datasets.

### Limitations
- Sequential translation into multiple target languages may introduce noise or biases, affecting performance for nuanced emotional states.
- While effective, the model's accuracy may be limited compared to models trained on single-language or single-step translations.

### Ethical Considerations
This model's reliance on machine-translated data means it may inherit biases or inaccuracies from the translation process. Users should carefully evaluate its applicability to sensitive use cases such as mental health assessments or social research.

### Citation
For further information, visit: [uvegesistvan/wildmann_german_proposal_multilingual_HU_PL_SK_CS](#)
