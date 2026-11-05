---
language: 
- pl
tags:
- emotion-classification
- roberta
- fine-tuned
- polish

license: mit
datasets:
- custom

model-index:
- name: Fine-tuned RoBERTa for Emotion Classification in Polish
  results:
  - task:
      type: text-classification
      name: Emotion Classification in Polish
    dataset:
      name: Polish Custom Dataset
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
        value: 0.85
      - name: Accuracy
        type: accuracy
        value: 0.82

---

# Fine-tuned RoBERTa Model for Emotion Classification in Polish

## Model Description
This model is a fine-tuned version of the [RoBERTa](https://huggingface.co/roberta-base) model, specifically tailored for emotion classification tasks in Polish. 
The model was trained to classify textual data into six emotional categories (**anger, fear, disgust, sadness, joy,** and **none of them**).

## Intended Use
This model is intended for classifying textual data into emotional categories in the Polish language. 
It can be used in applications such as sentiment analysis, social media monitoring, customer feedback analysis, and similar tasks. 
The model predicts the dominant emotion in a given text among the six predefined categories.

## Metrics

| **Class**       | **Precision (P)** | **Recall (R)** | **F1-Score (F1)** |
|-----------------|-------------------|----------------|-------------------|
| **anger**       | 0.70              | 0.81           | 0.75              |
| **fear**        | 0.96              | 0.96           | 0.98              |
| **disgust**     | 0.97              | 0.97           | 0.95              |
| **sadness**     | 0.87              | 0.87           | 0.86              |
| **joy**         | 0.91              | 0.91           | 0.89              |
| **none of them**| 0.75              | 0.75           | 0.70              |
| **Accuracy**    |                   |                | **0.82**          |
| **Macro Avg**   | 0.86              | 0.86           | 0.85              |
| **Weighted Avg**| 0.83              | 0.83           | 0.82              |

### Overall Performance
- **Accuracy:** 0.82
- **Macro Average Precision:** 0.86
- **Macro Average Recall:** 0.86
- **Macro Average F1-Score:** 0.85

### Class-wise Performance
The model demonstrates strong performance in the **fear**, **disgust**, and **joy** categories, with particularly high precision, recall, and F1 scores. 
The model performs moderately well in detecting **anger** and **none of them** categories, indicating potential areas for improvement.

## Limitations
- **Context Sensitivity:** The model may struggle with recognizing emotions that require deeper contextual understanding.
- **Class Imbalance:** The model's performance on the "none of them" category suggests that further training with more balanced datasets could improve accuracy.
- **Generalization:** The model's performance may vary depending on the text's domain, language style, and length, especially across different languages.

## Training Data
The model was fine-tuned on a custom Polish dataset containing textual samples labeled across six emotional categories. 
The dataset's distribution was considered during training to ensure balanced performance across classes.

## How to Use
You can use this model directly with the `transformers` library from Hugging Face. Below is an example of how to load and use the model:

```python
from transformers import pipeline

# Load the fine-tuned model
classifier = pipeline("text-classification", model="visegradmedia-emotion/Emotion_RoBERTa_polish6")

# Example usage
result = classifier("Czuję się dziś bardzo szczęśliwy!")
print(result)
