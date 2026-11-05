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
model-index:
  - name: modernbert-ausmed-pii
    results:
      - task:
          type: token-classification
          name: PII NER (BIO)
        dataset:
          name: pii_datagen synthetic Australian clinical notes
          type: pii_datagen-synthetic
        metrics:
          - type: precision
            value: 0.8252
            name: precision (test split)
          - type: recall
            value: 0.9506
            name: recall (test split)
          - type: f1
            value: 0.8835
            name: f1 (test split)
          - type: accuracy
            value: 0.9673
            name: accuracy (test split)
---

# modernbert-ausmed-pii

Token-classification (NER) model for PII detection in Australian clinical notes,
trained on synthetic data from the pii_datagen pipeline. Labels use the BIO scheme
over these entity types:

- `ABN`
- `ADDRESS`
- `ADVANCE_CARE_DIRECTIVE`
- `AGE`
- `AMBULANCE_MEMBERSHIP_NUMBER`
- `BANKING_FINANCE_DETAILS`
- `CENTRELINK_NUMBER`
- `COUNTRY`
- `DATE`
- `DRIVER_LICENCE_NUMBER`
- `DVA_FILE_NUMBER`
- `EMAIL_ADDRESS`
- `FAX_NUMBER`
- `IHI`
- `LGA`
- `MEDICAL_ENTITY`
- `MEDICAL_PROFESSIONAL_ID`
- `MEDICARE_NUMBER`
- `MRN`
- `NAME`
- `NDIS_NUMBER`
- `OCCUPATION`
- `ORGANISATION_NAME`
- `PASSPORT_NUMBER`
- `PATHOLOGY_ACCESSION_NUMBER`
- `PHONE`
- `POLICE_CORRECTIONS_ID`
- `PRIVATE_HEALTH_INSURANCE_NUMBER`
- `PROVIDER_NUMBER`
- `RADIOLOGY_ACCESSION_NUMBER`
- `SEX_GENDER`
- `TAC_CLAIM_NUMBER`
- `TFN`
- `TIMESTAMP`
- `WORKCOVER_CLAIM`

`MEDICAL_ENTITY` marks eponymous medical terms (Parkinson's disease, Foley catheter);
it is a hard-negative class and must **never** be redacted.

## Metrics (seqeval, entity-level)

| split | precision | recall | f1 |
|---|---|---|---|
| test (model selection) | 0.8252 | 0.9506 | 0.8835 |
| holdout | 0.8239 | 0.9468 | 0.8811 |

## Training

- **data**: 17817 synthetic notes from the pii_datagen pipeline (audited)
- **split**: 13351 train / 3541 test (per-epoch model selection) / 925 untouched holdout — deterministic per-doc_id hash, seed 42
- **selection**: best epoch by test-split F1 (epoch 4 of 7 run), early stopping (patience 3), max 15 epochs
- **context length**: 8192 tokens

## Usage

```python
from transformers import pipeline

ner = pipeline("token-classification", model="Cbezz/modernbert-ausmed-pii", aggregation_strategy="simple")
ner("Patient John Smith, DOB 12/03/1980, MRN 4456219.")
```
