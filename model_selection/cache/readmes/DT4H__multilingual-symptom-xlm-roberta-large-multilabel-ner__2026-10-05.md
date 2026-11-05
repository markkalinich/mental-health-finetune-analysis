---
language: multilingual
task_ids:
- token-classification
tags:
- clinical, medical, ner, healthcare
---

## Model Card for Multilingual-Symptom-Xlm-Roberta-Large-Multilabel

### Description

Multilingual clinical NER model for symptom recognition

### Model Details

- **Language**: MULTILINGUAL
- **Task**: token-classification
- **Framework**: pytorch

### How to Use

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification

model_name = "DT4H/multilingual-symptom-xlm-roberta-large-multilabel-ner"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

```

### Citation

```bibtex
@inproceedings{danu2026siemens,
  title={SIEMENS at\# SMM4H--HeaRD 2026: The Impact of Training Strategy and Backbone Selection on BERT-based Multilingual Clinical NER},
  author={Danu, Manuela Daniela},
  booktitle={Proceedings of the 11th Social Media Mining for Health Research and Applications (SMM4H-HeaRD 2026) Workshop and Shared Tasks},
  pages={216--221},
  year={2026}
}
```

### Acknowledgments
This work received funding from the European Union’s Horizon Europe research and innovation programme under Grant Agreement No. 101057849 (DataTools4Heart project).
