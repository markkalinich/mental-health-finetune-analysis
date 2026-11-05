---
license: apache-2.0
language:
- en
tags:
- pii
- ner
- token-classification
- privacy
- deberta
datasets:
- ai4privacy/pii-masking-200k
- nvidia/Nemotron-PII
- gretelai/synthetic_pii_finance_multilingual
- gretelai/gretel-pii-masking-en-v1
metrics:
- f1
- precision
- recall
pipeline_tag: token-classification
model-index:
- name: pii-small-en
  results:
  - task:
      type: token-classification
      name: PII NER
    metrics:
    - name: F1
      type: f1
      value: 0.8894
    - name: Precision
      type: precision
      value: 0.8698
    - name: Recall
      type: recall
      value: 0.9098
---

# DataFog PII-Small-EN (v1.4)

A compact PII (Personally Identifiable Information) Named Entity Recognition model for English text.

## Architecture

- **Backbone:** DeBERTa-v3-xsmall (22M params)
- **Head:** CharCNN + CRF
- **Total params:** ~45M
- **Entity types:** 41 PII categories across 4 sensitivity tiers

## Performance (v1.4, Epoch 3)

| Tier | Recall | Target |
|------|--------|--------|
| T1 (Critical: SSN, Credit Card, etc.) | 0.814 | >=0.98 |
| T2 (High: Person, Email, Phone, etc.) | 0.937 | >=0.95 |
| T3 (Moderate: Username, Date, Location, etc.) | 0.945 | >=0.90 |
| T4 (Domain-specific: Employee ID, Crypto, etc.) | 0.937 | >=0.85 |
| **Overall F1** | **0.889** | |

## Training Data

- AI4Privacy (~43K examples, English subset)
- NVIDIA Nemotron-PII (100K examples)
- Gretel Synthetic PII Finance (26K examples)
- Gretel PII Masking EN v1 (50K examples)
- Synthetic data for rare entity types (22K examples)
- **Total: ~241K examples**

## Entity Types (41)

### Tier 1 — Critical PII
SSN, CREDIT_CARD, BANK_ACCOUNT, PASSPORT_NUMBER, DRIVERS_LICENSE, TAX_ID

### Tier 2 — High Sensitivity
PERSON, EMAIL, PHONE, DATE_OF_BIRTH, STREET_ADDRESS, IP_ADDRESS

### Tier 3 — Moderate Sensitivity
USERNAME, DATE, LOCATION, ORGANIZATION, URL, LICENSE_PLATE, AGE, NATIONALITY, GENDER, RELIGION, MARITAL_STATUS

### Tier 4 — Domain-Specific
MEDICAL_RECORD, EMPLOYEE_ID, STUDENT_ID, ACCOUNT_NUMBER, PIN, PASSWORD, BIOMETRIC, VEHICLE_ID, DEVICE_ID, CRYPTO_WALLET, IBAN, SWIFT_CODE, INSURANCE_NUMBER, SALARY, CRIMINAL_RECORD, POLITICAL_AFFILIATION, SEXUAL_ORIENTATION, HEALTH_CONDITION

## License

Apache 2.0
