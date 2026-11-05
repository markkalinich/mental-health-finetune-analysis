---
language: en
tags:
  - medical
  - triage
  - emergency
  - esi
license: mit
---

# ESI Clinical Triage Assistant - ClinicalBERT

Modele fine-tune pour classification ESI (Emergency Severity Index).

Version: 4.0
Base: ClinicalBERT
Dataset: MTSamples

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained('yallou/esi-clinical-triage')
tokenizer = AutoTokenizer.from_pretrained('yallou/esi-clinical-triage')
```
