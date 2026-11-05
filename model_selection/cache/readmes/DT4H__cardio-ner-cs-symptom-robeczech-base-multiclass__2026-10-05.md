---
language: cs
task_ids:
- token-classification
tags:
- clinical, medical, ner, healthcare, cardiology, cs, Czech, symptom
---

## Model Card for Cardio-Ner-Cs-Symptom-Robeczech-Base-Multiclass

### Description

Czech cardiology NER model for symptom recognition

### Model Details

- **Language**: CS
- **Task**: token-classification
- **Framework**: pytorch

### How to Use

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification

model_name = "DT4H/cardio-ner-cs-symptom-robeczech-base-multiclass"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

```

### Acknowledgments
This work received funding from the European Union’s Horizon Europe research and innovation programme under Grant Agreement No. 101057849 (DataTools4Heart project).
