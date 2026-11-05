---
language:
  - te
license: apache-2.0
base_model: intfloat/e5-base-v2
tags:
  - token-classification
  - ner
  - pii
  - pii-detection
  - de-identification
  - privacy
  - healthcare
  - medical
  - clinical
  - phi
  - telugu
  - pytorch
  - transformers
  - openmed
pipeline_tag: token-classification
library_name: transformers
metrics:
  - f1
  - precision
  - recall
model-index:
  - name: OpenMed-PII-Telugu-ClinicalE5-Base-109M-v1
    results:
      - task:
          type: token-classification
          name: Named Entity Recognition
        dataset:
          name: AI4Privacy (Telugu subset)
          type: ai4privacy/pii-masking-400k
          split: test
        metrics:
          - type: f1
            value: 0.8879
            name: F1 (micro)
          - type: precision
            value: 0.9072
            name: Precision
          - type: recall
            value: 0.8694
            name: Recall
widget:
  - text: "డా. రాజేష్ శర్మ (ఆధార్: 1234 5678 9012) ను rajesh.sharma@hospital.in లేదా +91 98765 43210 లో సంప్రదించవచ్చు. చిరునామా: 42 గాంధీ రోడ్, 500001 హైదరాబాద్."
    example_title: Clinical Note with PII (Telugu)
---

# OpenMed-PII-Telugu-ClinicalE5-Base-109M-v1

**Telugu PII Detection Model** | 109M Parameters | Open Source

[![F1 Score](https://img.shields.io/badge/F1-88.79%25-brightgreen)]() [![Precision](https://img.shields.io/badge/Precision-90.72%25-blue)]() [![Recall](https://img.shields.io/badge/Recall-86.94%25-orange)]()

## Model Description

**OpenMed-PII-Telugu-ClinicalE5-Base-109M-v1** is a transformer-based token classification model fine-tuned for **Personally Identifiable Information (PII) detection in Telugu text**. This model identifies and classifies **54 types of sensitive information** including names, addresses, social security numbers, medical record numbers, and more.

### Key Features

- **Telugu-Optimized**: Specifically trained on Telugu text for optimal performance
- **High Accuracy**: Achieves strong F1 scores across diverse PII categories
- **Comprehensive Coverage**: Detects 55+ entity types spanning personal, financial, medical, and contact information
- **Privacy-Focused**: Designed for de-identification and compliance with GDPR and other privacy regulations
- **Production-Ready**: Optimized for real-world text processing pipelines

## Performance

Evaluated on the Telugu subset of AI4Privacy dataset:

| Metric | Score |
|:---|:---:|
| **Micro F1** | **0.8879** |
| Precision | 0.9072 |
| Recall | 0.8694 |
| Macro F1 | 0.8801 |
| Weighted F1 | 0.8854 |
| Accuracy | 0.9555 |

### Top 10 Telugu PII Models

| Rank | Model | F1 | Precision | Recall |
|:---:|:---|:---:|:---:|:---:|
| 1 | [OpenMed-PII-Telugu-SuperClinical-Large-434M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Telugu-SuperClinical-Large-434M-v1) | 0.9525 | 0.9521 | 0.9528 |
| 2 | [OpenMed-PII-Telugu-SnowflakeMed-Large-568M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Telugu-SnowflakeMed-Large-568M-v1) | 0.9507 | 0.9508 | 0.9507 |
| 3 | [OpenMed-PII-Telugu-BigMed-Large-560M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Telugu-BigMed-Large-560M-v1) | 0.9505 | 0.9504 | 0.9507 |
| 4 | [OpenMed-PII-Telugu-SuperMedical-Large-355M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Telugu-SuperMedical-Large-355M-v1) | 0.9494 | 0.9492 | 0.9495 |
| 5 | [OpenMed-PII-Telugu-ClinicalBGE-568M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Telugu-ClinicalBGE-568M-v1) | 0.9485 | 0.9485 | 0.9485 |
| 6 | [OpenMed-PII-Telugu-mClinicalE5-Large-560M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Telugu-mClinicalE5-Large-560M-v1) | 0.9474 | 0.9468 | 0.9480 |
| 7 | [OpenMed-PII-Telugu-NomicMed-Large-395M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Telugu-NomicMed-Large-395M-v1) | 0.9417 | 0.9417 | 0.9416 |
| 8 | [OpenMed-PII-Telugu-SuperClinical-Base-184M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Telugu-SuperClinical-Base-184M-v1) | 0.9414 | 0.9413 | 0.9416 |
| 9 | [OpenMed-PII-Telugu-mSuperClinical-Base-279M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Telugu-mSuperClinical-Base-279M-v1) | 0.9414 | 0.9418 | 0.9410 |
| 10 | [OpenMed-PII-Telugu-ModernMed-Large-395M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Telugu-ModernMed-Large-395M-v1) | 0.9361 | 0.9357 | 0.9365 |

## Supported Entity Types

This model detects **54 PII entity types** organized into categories:

<details>
<summary><strong>Identifiers</strong> (22 types)</summary>

| Entity | Description |
|:---|:---|
| `ACCOUNTNAME` | Accountname |
| `BANKACCOUNT` | Bankaccount |
| `BIC` | Bic |
| `BITCOINADDRESS` | Bitcoinaddress |
| `CREDITCARD` | Creditcard |
| `CREDITCARDISSUER` | Creditcardissuer |
| `CVV` | Cvv |
| `ETHEREUMADDRESS` | Ethereumaddress |
| `IBAN` | Iban |
| `IMEI` | Imei |
| ... | *and 12 more* |

</details>

<details>
<summary><strong>Personal Info</strong> (11 types)</summary>

| Entity | Description |
|:---|:---|
| `AGE` | Age |
| `DATEOFBIRTH` | Dateofbirth |
| `EYECOLOR` | Eyecolor |
| `FIRSTNAME` | Firstname |
| `GENDER` | Gender |
| `HEIGHT` | Height |
| `LASTNAME` | Lastname |
| `MIDDLENAME` | Middlename |
| `OCCUPATION` | Occupation |
| `PREFIX` | Prefix |
| ... | *and 1 more* |

</details>

<details>
<summary><strong>Contact Info</strong> (2 types)</summary>

| Entity | Description |
|:---|:---|
| `EMAIL` | Email |
| `PHONE` | Phone |

</details>

<details>
<summary><strong>Location</strong> (9 types)</summary>

| Entity | Description |
|:---|:---|
| `BUILDINGNUMBER` | Buildingnumber |
| `CITY` | City |
| `COUNTY` | County |
| `GPSCOORDINATES` | Gpscoordinates |
| `ORDINALDIRECTION` | Ordinaldirection |
| `SECONDARYADDRESS` | Secondaryaddress |
| `STATE` | State |
| `STREET` | Street |
| `ZIPCODE` | Zipcode |

</details>

<details>
<summary><strong>Organization</strong> (3 types)</summary>

| Entity | Description |
|:---|:---|
| `JOBDEPARTMENT` | Jobdepartment |
| `JOBTITLE` | Jobtitle |
| `ORGANIZATION` | Organization |

</details>

<details>
<summary><strong>Financial</strong> (5 types)</summary>

| Entity | Description |
|:---|:---|
| `AMOUNT` | Amount |
| `CURRENCY` | Currency |
| `CURRENCYCODE` | Currencycode |
| `CURRENCYNAME` | Currencyname |
| `CURRENCYSYMBOL` | Currencysymbol |

</details>

<details>
<summary><strong>Temporal</strong> (2 types)</summary>

| Entity | Description |
|:---|:---|
| `DATE` | Date |
| `TIME` | Time |

</details>

## Usage

### Quick Start

```python
from transformers import pipeline

# Load the PII detection pipeline
ner = pipeline("ner", model="OpenMed/OpenMed-PII-Telugu-ClinicalE5-Base-109M-v1", aggregation_strategy="simple")

text = """
రోగి రాజేష్ కుమార్ (పుట్టిన తేదీ: 15/03/1985, ఆధార్: 9876 5432 1098) ను నేడు పరీక్షించారు.
సంప్రదింపు: rajesh.kumar@email.in, ఫోన్: +91 98765 43210.
చిరునామా: 123 విజయ రోడ్, 500034 హైదరాబాద్.
"""

entities = ner(text)
for entity in entities:
    print(f"{entity['entity_group']}: {entity['word']} (score: {entity['score']:.3f})")
```

### De-identification Example

```python
def redact_pii(text, entities, placeholder='[REDACTED]'):
    """Replace detected PII with placeholders."""
    # Sort entities by start position (descending) to preserve offsets
    sorted_entities = sorted(entities, key=lambda x: x['start'], reverse=True)
    redacted = text
    for ent in sorted_entities:
        redacted = redacted[:ent['start']] + f"[{ent['entity_group']}]" + redacted[ent['end']:]
    return redacted

# Apply de-identification
redacted_text = redact_pii(text, entities)
print(redacted_text)
```

### Batch Processing

```python
from transformers import AutoModelForTokenClassification, AutoTokenizer
import torch

model_name = "OpenMed/OpenMed-PII-Telugu-ClinicalE5-Base-109M-v1"
model = AutoModelForTokenClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

texts = [
    "రోగి రాజేష్ కుమార్ (పుట్టిన తేదీ: 15/03/1985, ఆధార్: 9876 5432 1098) ను నేడు పరీక్షించారు.",
    "సంప్రదింపు: rajesh.kumar@email.in, ఫోన్: +91 98765 43210.",
]

inputs = tokenizer(texts, return_tensors='pt', padding=True, truncation=True)
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=-1)
```

## Training Details

### Dataset

- **Source**: [AI4Privacy PII Masking 400k](https://huggingface.co/datasets/ai4privacy/pii-masking-400k) (Telugu subset)
- **Format**: BIO-tagged token classification
- **Labels**: 109 total (54 entity types × 2 BIO tags + O)

### Training Configuration

- **Max Sequence Length**: 512 tokens
- **Epochs**: 3
- **Framework**: Hugging Face Transformers + Trainer API

## Intended Use & Limitations

### Intended Use

- **De-identification**: Automated redaction of PII in Telugu clinical notes, medical records, and documents
- **Compliance**: Supporting GDPR, and other privacy regulation compliance
- **Data Preprocessing**: Preparing datasets for research by removing sensitive information
- **Audit Support**: Identifying PII in document collections

### Limitations

**Important**: This model is intended as an **assistive tool**, not a replacement for human review.

- **False Negatives**: Some PII may not be detected; always verify critical applications
- **Context Sensitivity**: Performance may vary with domain-specific terminology
- **Language**: Optimized for Telugu text; may not perform well on other languages

## Citation

```bibtex
@misc{openmed-pii-2026,
  title = {OpenMed-PII-Telugu-ClinicalE5-Base-109M-v1: Telugu PII Detection Model},
  author = {OpenMed Science},
  year = {2026},
  publisher = {Hugging Face},
  url = {https://huggingface.co/OpenMed/OpenMed-PII-Telugu-ClinicalE5-Base-109M-v1}
}
```

## Links

- **Organization**: [OpenMed](https://huggingface.co/OpenMed)
