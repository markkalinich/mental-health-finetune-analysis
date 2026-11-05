---
language: 
- hu
tags:
- emotion-classification
- roberta
- fine-tuned
- hungarian

license: mit
datasets:
- custom

model-index:
- name: Fine-tuned RoBERTa for Emotion Classification in Hungarian
  results:
  - task:
      type: text-classification
      name: Emotion Classification in Hungarian
    dataset:
      name: Hungarian Custom Dataset
      type: text
    metrics:
      - name: Precision (Macro Avg)
        type: precision
        value: 0.85
      - name: Recall (Macro Avg)
        type: recall
        value: 0.84
      - name: F1 Score (Macro Avg)
        type: f1
        value: 0.85
      - name: Accuracy
        type: accuracy
        value: 0.81

---

# Fine-tuned RoBERTa Model for Emotion Classification in Hungarian

## Model Description
This model is a fine-tuned version of the [RoBERTa](https://huggingface.co/roberta-base) model, specifically tailored for emotion classification tasks in Hungarian. 
The model was trained to classify textual data into six emotional categories (**anger, fear, disgust, sadness, joy,** and **none of them**).

## Intended Use
This model is intended for classifying textual data into emotional categories in the Hungarian language. 
It can be used in applications such as sentiment analysis, social media monitoring, customer feedback analysis, and similar tasks. 
The model predicts the dominant emotion in a given text among the six predefined categories.

## Metrics

| **Class**       | **Precision (P)** | **Recall (R)** | **F1-Score (F1)** |
|-----------------|-------------------|----------------|-------------------|
| **anger**       | 0.69              | 0.79           | 0.74              |
| **fear**        | 0.95              | 0.99           | 0.97              |
| **disgust**     | 0.96              | 0.95           | 0.96              |
| **sadness**     | 0.88              | 0.83           | 0.86              |
| **joy**         | 0.91              | 0.85           | 0.88              |
| **none of them**| 0.72              | 0.65           | 0.69              |
| **Accuracy**    |                   |                | **0.81**          |
| **Macro Avg**   | 0.85              | 0.84           | 0.85              |
| **Weighted Avg**| 0.82              | 0.81           | 0.81              |

### Overall Performance
- **Accuracy:** 0.81
- **Macro Average Precision:** 0.85
- **Macro Average Recall:** 0.84
- **Macro Average F1-Score:** 0.85

### Class-wise Performance
The model demonstrates strong performance in the **fear**, **disgust**, and **joy** categories, with particularly high precision, recall, and F1 scores. 
The model performs moderately well in detecting **anger** and **none of them** categories, indicating potential areas for improvement.

## Limitations
- **Context Sensitivity:** The model may struggle with recognizing emotions that require deeper contextual understanding.
- **Class Imbalance:** The model's performance on the "none of them" category suggests that further training with more balanced datasets could improve accuracy.
- **Generalization:** The model's performance may vary depending on the text's domain, language style, and length, especially across different languages.

## Training Data
The model was fine-tuned on a custom Hungarian dataset containing textual samples labeled across six emotional categories. 
The dataset's distribution was considered during training to ensure balanced performance across classes.

## How to Use
You can use this model directly with the `transformers` library from Hugging Face. Below is an example of how to load and use the model:

```python
from transformers import pipeline

# Load the fine-tuned model
classifier = pipeline("text-classification", model="visegradmedia-emotion/Emotion_RoBERTa_hungarian6")

# Example usage
result = classifier("Ma nagyon boldognak érzem magam!")
print(result)
