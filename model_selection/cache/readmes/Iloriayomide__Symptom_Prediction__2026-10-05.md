---
language: en
pipeline_tag: text-classification
library_name: transformers
tags:
- medical
- classification
- healthcare
- clinicalbert
- symptom-checker
- text-classification
license: apache-2.0
datasets:
- qilex/Symptom2Disease
- niyarrbarman/symptom-disease-dataset
metrics:
- accuracy
model-index:
- name: SymbiPredict-ClinicalBERT
  results:
  - task:
      type: text-classification
      name: Disease Prediction
    metrics:
    - type: loss
      value: 0.2577
base_model:
- emilyalsentzer/Bio_ClinicalBERT
---

# 🏥 SymbiPredict: ClinicalBERT Symptom-to-Disease Classifier

This model is a fine-tuned version of **[Bio_ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT)**, optimized to predict diseases based on natural language descriptions of symptoms.

It has been trained on a massive merged dataset of over **96,000 patient cases** covering **115+ unique medical conditions**.

## 📊 Model Performance

| Epoch | Training Loss | Validation Loss |
|-------|---------------|-----------------|
| 1     | 0.4108        | 0.3452          | 
| 2     | 0.3092        | 0.2852          | 
| 3     | 0.2526        | **0.2577**      | 

The model achieves a final validation loss of **0.2577**, demonstrating high confidence and generalization capabilities across 115 disease classes.

## 🚀 How to Use (Python)

You can use this model directly with the Hugging Face `pipeline`.

```python
from transformers import pipeline

# Load the pipeline
classifier = pipeline("text-classification", model="Iloriayomide/Symptom_Prediction", top_k=3)

# Test with symptoms
symptoms = "I have a severe headache, sensitivity to light, and I feel nauseous."
prediction = classifier(symptoms)

print(prediction)