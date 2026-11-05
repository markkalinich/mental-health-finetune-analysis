---
language:
- en
- ru
- uk
tags:
- token-classification
- ner
- pii
- xlm-roberta
- transformers
library_name: transformers
license: apache-2.0
base_model: xlm-roberta-large
pipeline_tag: token-classification
model-index:
- name: pii-ner-nemotron
  results:
  - task:
      type: token-classification
      name: Named Entity Recognition
    metrics:
    - type: f1
      value: 0.9768405285513023
---

# pii-ner-nemotron

## Model summary

PII NER model trained on nemotron dataset for multilingual PII entity extraction.

- **Base model:** `xlm-roberta-large`
- **Repository:** `scanpatch/pii-ner-nemotron`
- **Training run name:** `pii-ner-nemotron`
- **Export timestamp (UTC):** `2025-12-29T12:06:13.731145+00:00`

## Labels

### Entity types
- `address`
- `address_apartment`
- `address_building`
- `address_city`
- `address_country`
- `address_district`
- `address_geolocation`
- `address_house`
- `address_postal_code`
- `address_region`
- `address_street`
- `date`
- `document_number`
- `email`
- `first_name`
- `ip`
- `last_name`
- `middle_name`
- `military_individual_number`
- `mobile_phone`
- `name`
- `name_initials`
- `nickname`
- `organization`
- `snils`
- `tin`
- `vehicle_number`

## Evaluation

| Metric | Value |
|---|---:|
| `test_f1` | `0.9768405285513023` |
| `test_precision` | `0.9734942064790006` |
| `test_recall` | `0.9802099354987895` |
| `test_accuracy` | `0.9977181928808507` |
| `train_runtime` | `1693.5057` |
| `train_samples_per_second` | `238.116` |

## How to use

```python
from transformers import pipeline

ner = pipeline(
    "token-classification",
    model="scanpatch/pii-ner-nemotron",
    aggregation_strategy="simple",
)

text = "Contact me at test@example.com and my phone is +380 67 123 45 67."
print(ner(text))
```
