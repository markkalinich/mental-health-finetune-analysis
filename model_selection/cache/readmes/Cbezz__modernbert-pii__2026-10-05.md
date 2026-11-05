---
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
  - token-classification
  - named-entity-recognition
  - pii
  - modernbert
language:
  - en
pipeline_tag: token-classification
---

# modernbert-pii

ModernBERT fine-tuned for token classification (NER) to detect PII in
Australian clinical notes. Labels use the BIO scheme over these entity types:

- `ACD`
- `ADDRESS`
- `AGE`
- `ATTENDING_NURSE`
- `COUNTRY_OF_BIRTH`
- `DATE_OF_BIRTH`
- `DVA_NUMBER`
- `EMAIL`
- `FULL_NAME`
- `GUARDIANSHIP`
- `IHI`
- `MEDICARE_NUMBER`
- `MRN`
- `NEXT_OF_KIN`
- `OCCUPATION`
- `OTHER_CLINICAL_STAFF`
- `PHONE_NUMBER`
- `PREFERRED_NAME`
- `PRIVATE_HEALTH_NUMBER`
- `REFERRING_GP`
- `SEX_GENDER`
- `TREATING_CLINICIAN`
- `WORKCOVER`

## Usage

```python
from transformers import pipeline

ner = pipeline("token-classification", model="Cbezz/modernbert-pii", aggregation_strategy="simple")
ner("Patient John Smith, DOB 12/03/1980, MRN 4456219.")
```
