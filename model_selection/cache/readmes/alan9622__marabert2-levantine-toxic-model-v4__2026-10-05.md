---
language:
- ar
pipeline_tag: text-classification
tags:
- text-classification
- sentiment
- levantine
- marbert
metrics:
- accuracy
- f1
model-index:
- name: Levantine Hate Classifier
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: L-HSAB Custom
      type: alan9622/marabert2-levantine-toxic-model-v4-dataset
    metrics:
    - type: accuracy
      value: 0.9128205128205128
    - type: f1
      value: 0.908218073979278
license: apache-2.0
base_model:
- UBC-NLP/MARBERTv2
datasets:
- alan9622/marabert2-levantine-toxic-model-v4-dataset
---

# Levantine Hate Speech Classifier

This model identifies **Hate Speech** and **Abusive Language** in Levantine Arabic tweets.
It was fine-tuned on the dataset: [**alan9622/marabert2-levantine-toxic-model-v4-dataset**](https://huggingface.co/datasets/alan9622/marabert2-levantine-toxic-model-v4-dataset).

## 📊 Evaluation
| Metric | Score |
| :--- | :--- |
| **Accuracy** | **0.9128205128205128** |
| **F1 Score** | **0.908218073979278** |

## 📖 Labels
| ID | Label | Definition |
| :--- | :--- | :--- |
| **0** | **normal** | Safe text. | **Abusive** | Insults/Vulgarity not directed at identity. |
| **1** | **toxic** | abusive or hate Insults/Vulgarity not directed at identity or Attacks based on religion, sect, gender, or nationality.

### Usage
```python
from transformers import pipeline
classifier = pipeline("text-classification", model="alan9622/marabert2-levantine-toxic-model-v4")
classifier("يا زلمة حل عني")