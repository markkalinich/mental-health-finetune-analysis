---
language: es
task_ids:
- token-classification
tags:
- clinical, medical, ner, healthcare, cardiology, spanish, symptom, multiclass
---

## Model Card for Cardio-Ner-Es-Symptom-Roberta-Biomedical-Multiclass

### Description

Spanish cardiology multiclass NER model for symptom recognition, fine-tuned on roberta-biomedical.

### Model Details

- **Language**: ES
- **Task**: token-classification
- **Framework**: pytorch

### How to Use

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification

model_name = "DT4H/cardio-ner-es-symptom-roberta-biomedical-multiclass"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

```

### Acknowledgments
This work received funding from the European Union’s Horizon Europe research and innovation programme under Grant Agreement No. 101057849 (DataTools4Heart project).
