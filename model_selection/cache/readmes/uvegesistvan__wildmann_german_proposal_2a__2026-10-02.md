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

# Model Card for uvegesistvan/wildmann_german_proposal_2a

## Model Overview
This model is a multi-class emotion classifier trained to identify nine distinct emotional states in text. The classes and their corresponding labels are as follows:

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
The dataset combines original and synthetic data to improve class balance and performance. Synthetic data augmentation was applied to classes with lower representation in the original dataset, specifically "Fear," "Disgust," "Sadness," "Joy," and "Pride." The following table summarizes the distribution of original and synthetic data across training, testing, and validation sets:

#### Training Data:
| Label       | Original Count | Original (%) | Synthetic Count | Synthetic (%) |
|-------------|----------------|--------------|------------------|----------------|
| Anger       | 6210           | 100.00       | 0                | 0.00           |
| Fear        | 2534           | 40.81        | 3676             | 59.19          |
| Disgust     | 845            | 13.60        | 5366             | 86.40          |
| Sadness     | 2670           | 42.99        | 3541             | 57.01          |
| Joy         | 3420           | 55.07        | 2790             | 44.93          |
| Enthusiasm  | 4347           | 70.00        | 1863             | 30.00          |
| Hope        | 6210           | 100.00       | 0                | 0.00           |
| Pride       | 2834           | 45.63        | 3377             | 54.37          |
| No emotion  | 6210           | 100.00       | 0                | 0.00           |

#### Testing Data:
| Label       | Original Count | Original (%) | Synthetic Count | Synthetic (%) |
|-------------|----------------|--------------|------------------|----------------|
| Anger       | 777            | 100.00       | 0                | 0.00           |
| Fear        | 317            | 40.85        | 459              | 59.15          |
| Disgust     | 106            | 13.66        | 670              | 86.34          |
| Sadness     | 333            | 42.97        | 442              | 57.03          |
| Joy         | 428            | 55.08        | 349              | 44.92          |
| Enthusiasm  | 543            | 69.97        | 233              | 30.03          |
| Hope        | 777            | 100.00       | 0                | 0.00           |
| Pride       | 354            | 45.62        | 422              | 54.38          |
| No emotion  | 777            | 100.00       | 0                | 0.00           |

#### Validation Data:
| Label       | Original Count | Original (%) | Synthetic Count | Synthetic (%) |
|-------------|----------------|--------------|------------------|----------------|
| Anger       | 776            | 100.00       | 0                | 0.00           |
| Fear        | 317            | 40.80        | 460              | 59.20          |
| Disgust     | 105            | 13.53        | 671              | 86.47          |
| Sadness     | 334            | 42.99        | 443              | 57.01          |
| Joy         | 427            | 55.03        | 349              | 44.97          |
| Enthusiasm  | 544            | 70.01        | 233              | 29.99          |
| Hope        | 776            | 100.00       | 0                | 0.00           |
| Pride       | 354            | 45.62        | 422              | 54.38          |
| No emotion  | 776            | 100.00       | 0                | 0.00           |

### Evaluation Metrics
The model was evaluated using precision, recall, F1-score, and support for each class. Below are the detailed metrics:

| Class      | Precision | Recall | F1-Score | Support |
|------------|-----------|--------|----------|---------|
| Anger (0)  | 0.57      | 0.64   | 0.61     | 777     |
| Fear (1)   | 0.84      | 0.77   | 0.80     | 776     |
| Disgust (2)| 0.91      | 0.95   | 0.93     | 776     |
| Sadness (3)| 0.84      | 0.85   | 0.85     | 775     |
| Joy (4)    | 0.78      | 0.85   | 0.81     | 777     |
| Enthusiasm (5)| 0.63   | 0.63   | 0.63     | 777     |
| Hope (6)   | 0.51      | 0.55   | 0.53     | 777     |
| Pride (7)  | 0.77      | 0.77   | 0.77     | 776     |
| No emotion (8) | 0.47 | 0.34   | 0.39     | 777     |

### Overall Metrics
- **Accuracy**: 0.71
- **Macro Average**: Precision = 0.70, Recall = 0.71, F1-Score = 0.70
- **Weighted Average**: Precision = 0.70, Recall = 0.71, F1-Score = 0.70

### Performance Insights
The model achieves strong performance across most classes, particularly for "Disgust" and "Sadness." However, the "No emotion" class shows lower recall, which could indicate challenges in distinguishing neutral text from emotional expressions. Additional fine-tuning or data augmentation may help address this limitation.

## Model Usage
### Applications
- Emotion classification in text-based datasets.
- Analyzing emotional tone in social media, reviews, or other text corpora.

### Limitations
- Performance varies across classes, with some (e.g., "Hope" and "No emotion") showing lower recall.
- The model may not generalize well to domains outside the training data.

### Ethical Considerations
The model's predictions might not always align with human interpretations of emotions, particularly in ambiguous or context-dependent cases. Misclassification could lead to inappropriate conclusions if used in sensitive applications (e.g., mental health monitoring).

