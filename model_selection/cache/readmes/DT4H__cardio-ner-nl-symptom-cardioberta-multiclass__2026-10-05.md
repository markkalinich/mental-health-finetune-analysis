---
language: nl
task_ids:
- token-classification
tags:
- clinical, medical, ner, healthcare, cardiology, dutch
base_model:
- CLTL/MedRoBERTa.nl
---

## Model Card for Cardio-Ner-Nl-Symptom-Cardioberta-Multiclass

### Description

Dutch cardiology NER model for symptom recognition

### Model Details

- **Language**: NL
- **Task**: token-classification
- **Framework**: pytorch

### How to Use

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification

model_name = "DT4H/cardio-ner-nl-symptom-cardioberta-multiclass"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

```

### Acknowledgments
This work received funding from the European Union’s Horizon Europe research and innovation programme under Grant Agreement No. 101057849 (DataTools4Heart project).