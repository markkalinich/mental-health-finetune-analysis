---
language: sv
task_ids:
- token-classification
tags:
- clinical, medical, ner, healthcare, cardiology, swedish
base_model:
- KBLab/bert-base-swedish-cased
---

## Model Card for Cardio-Ner-Sv-Symptom-Bert-Base-Swedish-Cased-Multiclass

### Description

Swedish cardiology NER model for symptom recognition

### Model Details

- **Language**: SV
- **Task**: token-classification
- **Framework**: pytorch

### How to Use

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification

model_name = "DT4H/cardio-ner-sv-symptom-bert-base-swedish-cased-multiclass"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

```

### Acknowledgments
This work received funding from the European Union’s Horizon Europe research and innovation programme under Grant Agreement No. 101057849 (DataTools4Heart project).