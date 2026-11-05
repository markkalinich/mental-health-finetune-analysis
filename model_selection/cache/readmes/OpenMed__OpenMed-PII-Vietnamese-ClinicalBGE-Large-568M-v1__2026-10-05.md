---
language:
  - vi
license: apache-2.0
base_model: BAAI/bge-m3
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
  - vietnamese
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
  - name: OpenMed-PII-Vietnamese-ClinicalBGE-Large-568M-v1
    results:
      - task:
          type: token-classification
          name: Named Entity Recognition
        dataset:
          name: AI4Privacy + Synthetic Vietnamese PII
          type: ai4privacy/pii-masking-200k
          split: test
        metrics:
          - type: f1
            value: 0.7447
            name: F1 (micro)
          - type: precision
            value: 0.7323
            name: Precision
          - type: recall
            value: 0.7575
            name: Recall
widget:
  - text: "BS. Nguyễn Văn An (CCCD: 012345678901) có thể liên hệ qua nguyen.an@hospital.vn hoặc +84 912 345 678. Địa chỉ: 42 Nguyễn Huệ, Quận 1, TP.HCM."
    example_title: Clinical Note with PII (Vietnamese)
---

# OpenMed-PII-Vietnamese-ClinicalBGE-Large-568M-v1

**Vietnamese PII Detection Model** | 568M Parameters | Open Source

[![F1 Score](https://img.shields.io/badge/F1-74.47%25-brightgreen)]() [![Precision](https://img.shields.io/badge/Precision-73.23%25-blue)]() [![Recall](https://img.shields.io/badge/Recall-75.75%25-orange)]()

## Model Description

**OpenMed-PII-Vietnamese-ClinicalBGE-Large-568M-v1** is a transformer-based token classification model fine-tuned for **Personally Identifiable Information (PII) detection in Vietnamese text**. This model identifies and classifies **54 types of sensitive information** including names, addresses, social security numbers, medical record numbers, and more.

### Key Features

- **Vietnamese-Optimized**: Specifically trained on Vietnamese text for optimal performance
- **High Accuracy**: Achieves strong F1 scores across diverse PII categories
- **Comprehensive Coverage**: Detects 55+ entity types spanning personal, financial, medical, and contact information
- **Privacy-Focused**: Designed for de-identification and compliance with GDPR and other privacy regulations
- **Production-Ready**: Optimized for real-world text processing pipelines

## Performance

Evaluated on the Vietnamese test split (AI4Privacy + synthetic data):

| Metric | Score |
|:---|:---:|
| **Micro F1** | **0.7447** |
| Precision | 0.7323 |
| Recall | 0.7575 |
| Macro F1 | 0.6774 |
| Weighted F1 | 0.7435 |
| Accuracy | 0.8823 |

### Top 10 Vietnamese PII Models

| Rank | Model | F1 | Precision | Recall |
|:---:|:---|:---:|:---:|:---:|
| 1 | [OpenMed-PII-Vietnamese-BigMed-Large-560M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Vietnamese-BigMed-Large-560M-v1) | 0.7545 | 0.7522 | 0.7568 |
| 2 | [OpenMed-PII-Vietnamese-SuperClinical-Large-434M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Vietnamese-SuperClinical-Large-434M-v1) | 0.7457 | 0.7314 | 0.7606 |
| 3 | [OpenMed-PII-Vietnamese-NomicMed-Large-395M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Vietnamese-NomicMed-Large-395M-v1) | 0.7450 | 0.7378 | 0.7523 |
| 4 | [OpenMed-PII-Vietnamese-SnowflakeMed-Large-568M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Vietnamese-SnowflakeMed-Large-568M-v1) | 0.7447 | 0.7327 | 0.7571 |
| **5** | **[OpenMed-PII-Vietnamese-ClinicalBGE-Large-568M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Vietnamese-ClinicalBGE-Large-568M-v1)** | **0.7447** | **0.7323** | **0.7575** |
| 6 | [OpenMed-PII-Vietnamese-mSuperClinical-Large-279M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Vietnamese-mSuperClinical-Large-279M-v1) | 0.7430 | 0.7280 | 0.7586 |
| 7 | [OpenMed-PII-Vietnamese-ModernMed-Large-395M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Vietnamese-ModernMed-Large-395M-v1) | 0.7428 | 0.7341 | 0.7517 |
| 8 | [OpenMed-PII-Vietnamese-BioClinicalModern-Large-395M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Vietnamese-BioClinicalModern-Large-395M-v1) | 0.7418 | 0.7344 | 0.7493 |
| 9 | [OpenMed-PII-Vietnamese-BiomedELECTRA-Large-335M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Vietnamese-BiomedELECTRA-Large-335M-v1) | 0.7382 | 0.7252 | 0.7517 |
| 10 | [OpenMed-PII-Vietnamese-SuperMedical-Large-355M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Vietnamese-SuperMedical-Large-355M-v1) | 0.7370 | 0.7231 | 0.7513 |

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
ner = pipeline("ner", model="OpenMed/OpenMed-PII-Vietnamese-ClinicalBGE-Large-568M-v1", aggregation_strategy="simple")

text = """
Bệnh nhân Trần Minh Đức (sinh ngày 15/03/1985, CCCD: 098765432109) được khám hôm nay.
Liên hệ: tran.duc@email.vn, Điện thoại: +84 912 345 678.
Địa chỉ: 123 Lê Lợi, Quận 1, TP.HCM.
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

model_name = "OpenMed/OpenMed-PII-Vietnamese-ClinicalBGE-Large-568M-v1"
model = AutoModelForTokenClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

texts = [
    "Bệnh nhân Trần Minh Đức (sinh ngày 15/03/1985, CCCD: 098765432109) được khám hôm nay.",
    "Liên hệ: tran.duc@email.vn, Điện thoại: +84 912 345 678.",
]

inputs = tokenizer(texts, return_tensors='pt', padding=True, truncation=True)
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=-1)
```

## Training Details

### Dataset

This model was trained on a combination of:

- **[AI4Privacy PII Masking 200K](https://huggingface.co/datasets/ai4privacy/pii-masking-200k)**: Multilingual base dataset (200K records across 8 languages)
- **[NVIDIA Nemotron-PII](https://huggingface.co/datasets/nvidia/Nemotron-PII)**: Seed dataset for synthetic data generation
- **Synthetic Vietnamese Data**: ~25K high-quality samples generated with locale-specific formatting (CCCD format, +84 phones, Vietnamese names, ₫ currency)

- **Format**: BIO-tagged token classification
- **Labels**: 76 BIO tags (54 entity types)

### Training Configuration

- **Max Sequence Length**: 512 tokens
- **Framework**: Hugging Face Transformers + Trainer API

## Intended Use & Limitations

### Intended Use

- **De-identification**: Automated redaction of PII in Vietnamese clinical notes, medical records, and documents
- **Compliance**: Supporting GDPR, and other privacy regulation compliance
- **Data Preprocessing**: Preparing datasets for research by removing sensitive information
- **Audit Support**: Identifying PII in document collections

### Limitations

**Important**: This model is intended as an **assistive tool**, not a replacement for human review.

- **False Negatives**: Some PII may not be detected; always verify critical applications
- **Context Sensitivity**: Performance may vary with domain-specific terminology
- **Language**: Optimized for Vietnamese text; may not perform well on other languages

## Citation

```bibtex
@misc{openmed-pii-2026,
  title = {OpenMed-PII-Vietnamese-ClinicalBGE-Large-568M-v1: Vietnamese PII Detection Model},
  author = {OpenMed Science},
  year = {2026},
  publisher = {Hugging Face},
  url = {https://huggingface.co/OpenMed/OpenMed-PII-Vietnamese-ClinicalBGE-Large-568M-v1}
}
```

## Links

- **Organization**: [OpenMed](https://huggingface.co/OpenMed)
