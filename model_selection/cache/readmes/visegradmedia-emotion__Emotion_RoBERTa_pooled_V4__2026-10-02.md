---
language: 
- hu
- sk
- pl
- cs
tags:
- emotion-classification
- roberta
- fine-tuned
- multilingual

license: mit
datasets:
- custom

model-index:
- name: Multilingual Fine-tuned RoBERTa for Emotion Classification
  results:
  - task:
      type: text-classification
      name: Multilingual Emotion Classification
    dataset:
      name: Multilingual Custom Dataset (Hungarian, Slovak, Polish, Czech)
      type: text
    metrics:
      - name: Precision (Macro Avg)
        type: precision
        value: 0.86
      - name: Recall (Macro Avg)
        type: recall
        value: 0.86
      - name: F1 Score (Macro Avg)
        type: f1
        value: 0.86
      - name: Accuracy
        type: accuracy
        value: 0.84

---

# Multilingual Fine-tuned RoBERTa Model for Emotion Classification

## Model Description
This model is a multilingual fine-tuned version of the [RoBERTa](https://huggingface.co/roberta-base) model, specifically tailored for emotion classification tasks in Hungarian, Slovak, Polish, and Czech languages. 
The model was trained to classify textual data into six emotional categories (**anger, fear, disgust, sadness, joy,** and **none of them**).

## Intended Use
This model is intended for classifying textual data into emotional categories across multiple languages, including Hungarian, Slovak, Polish, and Czech. 
It can be used in applications such as sentiment analysis, social media monitoring, customer feedback analysis, and similar tasks. 
The model predicts the dominant emotion in a given text among the six predefined categories.

## Metrics

| **Class**       | **Precision (P)** | **Recall (R)** | **F1-Score (F1)** |
|-----------------|-------------------|----------------|-------------------|
| **anger**       | 0.74              | 0.81           | 0.77              |
| **fear**        | 0.98              | 0.98           | 0.98              |
| **disgust**     | 0.94              | 0.95           | 0.95              |
| **sadness**     | 0.87              | 0.87           | 0.87              |
| **joy**         | 0.89              | 0.89           | 0.89              |
| **none of them**| 0.77              | 0.69           | 0.73              |
| **Accuracy**    |                   |                | **0.84**          |
| **Macro Avg**   | 0.86              | 0.86           | 0.86              |
| **Weighted Avg**| 0.84              | 0.84           | 0.84              |

### Overall Performance
- **Accuracy:** 0.84
- **Macro Average Precision:** 0.86
- **Macro Average Recall:** 0.86
- **Macro Average F1-Score:** 0.86

### Class-wise Performance
The model demonstrates strong performance across different emotional categories, with particularly high precision, recall, and F1 scores in the **fear**, **disgust**, and **joy** categories. 
The model performs moderately well in detecting **anger** and **none of them** categories, but still achieves adequate accuracy in these cases.

## Limitations
- **Context Sensitivity:** The model may struggle with recognizing emotions that require deeper contextual understanding.
- **Class Imbalance:** The model's performance on the "none of them" category suggests that further training with more balanced datasets could improve accuracy.
- **Generalization:** The model's performance may vary depending on the text's domain, language style, and length, especially across different languages.

## How to Use
You can use this model directly with the `transformers` library from Hugging Face. Below is an example of how to load and use the model:

```python
from transformers import pipeline

# Load the fine-tuned model
classifier = pipeline("text-classification", model="visegradmedia-emotion/Emotion_RoBERTa_pooled_V4")

# Example usage
result = classifier("Nagyon örömtelinek érzem magam ma!")
print(result)