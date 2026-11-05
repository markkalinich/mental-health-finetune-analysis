---
language: en
license: apache-2.0
tags:
- text-classification
- medical
- distilbert
- transformers
datasets:
- openlifescienceai/medmcqa
metrics:
- accuracy
- f1
model-index:
- name: medical-question-classifier
  results:
  - task:
      type: text-classification
    dataset:
      name: MedMCQA
      type: openlifescienceai/medmcqa
    metrics:
    - type: accuracy
      value: 0.824
---

# Medical Question Category Classifier (DistilBERT)

## Model Description
This model is a fine-tuned version of `distilbert-base-uncased` trained to classify medical and health-related questions into 20 distinct medical specialties (e.g., Cardiology, Pediatrics, Psychiatry, Surgery).

## Intended Use
- **Primary Use Case:** Triage systems and automatic tag generation for medical Q&A platforms.
- **Safety Notice:** This model is designed strictly for categorization and routing purposes. It **does not** provide medical diagnosis or treatment advice.

## Dataset Information
- **Dataset:** `openlifescienceai/medmcqa`
- **License:** Apache 2.0
- **Classes (20):** Anaesthesia, Anatomy, Biochemistry, Dental, ENT, Forensic Medicine, Gynaecology & Obstetrics, Medicine, Microbiology, Ophthalmology, Orthopaedics, Pathology, Pediatrics, Pharmacology, Physiology, Psychiatry, Radiology, Skin, Social & Preventive Medicine, Surgery.

## Training Hyperparameters
- **Base Model:** `distilbert-base-uncased`
- **Epochs:** 3
- **Batch Size:** 16
- **Learning Rate:** 2e-5
- **Optimizer:** AdamW

## Evaluation Metrics
- **Accuracy:** ~82.4%
- **Weighted F1-Score:** ~0.821

## How to Use

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "mahmoodulhassan23/medical-question-classifier"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

question = "Child presenting with high grade fever, rash, and cough."
inputs = tokenizer(question, return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs)
    pred_class = torch.argmax(outputs.logits, dim=-1).item()

print(f"Predicted Class ID: {pred_class}")