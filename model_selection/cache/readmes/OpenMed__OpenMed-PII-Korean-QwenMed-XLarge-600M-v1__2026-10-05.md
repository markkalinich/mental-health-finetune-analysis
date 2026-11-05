---
language:
  - ko
license: apache-2.0
base_model: Qwen/Qwen3-Embedding-0.6B
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
  - korean
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
  - name: OpenMed-PII-Korean-QwenMed-600M-v1
    results:
      - task:
          type: token-classification
          name: Named Entity Recognition
        dataset:
          name: AI4Privacy + Synthetic Korean PII
          type: ai4privacy/pii-masking-200k
          split: test
        metrics:
          - type: f1
            value: 0.7326
            name: F1 (micro)
          - type: precision
            value: 0.7113
            name: Precision
          - type: recall
            value: 0.7553
            name: Recall
widget:
  - text: "김철수 의사 (주민등록번호: 850315-1234567) 연락처: kim.cs@hospital.kr 또는 +82 10-1234-5678. 주소: 서울시 강남구 테헤란로 42."
    example_title: Clinical Note with PII (Korean)
---

# OpenMed-PII-Korean-QwenMed-600M-v1

**Korean PII Detection Model** | 600M Parameters | Open Source

[![F1 Score](https://img.shields.io/badge/F1-73.26%25-brightgreen)]() [![Precision](https://img.shields.io/badge/Precision-71.13%25-blue)]() [![Recall](https://img.shields.io/badge/Recall-75.53%25-orange)]()

## Model Description

**OpenMed-PII-Korean-QwenMed-600M-v1** is a transformer-based token classification model fine-tuned for **Personally Identifiable Information (PII) detection in Korean text**. This model identifies and classifies **54 types of sensitive information** including names, addresses, social security numbers, medical record numbers, and more.

### Key Features

- **Korean-Optimized**: Specifically trained on Korean text for optimal performance
- **High Accuracy**: Achieves strong F1 scores across diverse PII categories
- **Comprehensive Coverage**: Detects 55+ entity types spanning personal, financial, medical, and contact information
- **Privacy-Focused**: Designed for de-identification and compliance with GDPR and other privacy regulations
- **Production-Ready**: Optimized for real-world text processing pipelines

## Performance

Evaluated on the Korean test split (AI4Privacy + synthetic data):

| Metric | Score |
|:---|:---:|
| **Micro F1** | **0.7326** |
| Precision | 0.7113 |
| Recall | 0.7553 |
| Macro F1 | 0.4212 |
| Weighted F1 | 0.7423 |
| Accuracy | 0.8838 |

### Top 10 Korean PII Models

| Rank | Model | F1 | Precision | Recall |
|:---:|:---|:---:|:---:|:---:|
| 1 | [OpenMed-PII-Korean-NomicMed-Large-395M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Korean-NomicMed-Large-395M-v1) | 0.7709 | 0.7576 | 0.7848 |
| 2 | [OpenMed-PII-Korean-SuperClinical-Large-434M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Korean-SuperClinical-Large-434M-v1) | 0.7700 | 0.7484 | 0.7929 |
| 3 | [OpenMed-PII-Korean-BioClinicalModern-Large-395M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Korean-BioClinicalModern-Large-395M-v1) | 0.7684 | 0.7519 | 0.7858 |
| 4 | [OpenMed-PII-Korean-ClinicalBGE-568M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Korean-ClinicalBGE-568M-v1) | 0.7656 | 0.7453 | 0.7871 |
| 5 | [OpenMed-PII-Korean-SnowflakeMed-Large-568M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Korean-SnowflakeMed-Large-568M-v1) | 0.7643 | 0.7469 | 0.7827 |
| 6 | [OpenMed-PII-Korean-BigMed-Large-560M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Korean-BigMed-Large-560M-v1) | 0.7642 | 0.7461 | 0.7832 |
| 7 | [OpenMed-PII-Korean-ModernMed-Large-395M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Korean-ModernMed-Large-395M-v1) | 0.7616 | 0.7459 | 0.7779 |
| 8 | [OpenMed-PII-Korean-SuperMedical-Large-355M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Korean-SuperMedical-Large-355M-v1) | 0.7597 | 0.7359 | 0.7850 |
| 9 | [OpenMed-PII-Korean-BigMed-Base-278M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Korean-BigMed-Base-278M-v1) | 0.7596 | 0.7434 | 0.7766 |
| 10 | [OpenMed-PII-Korean-SuperClinical-Base-184M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Korean-SuperClinical-Base-184M-v1) | 0.7595 | 0.7347 | 0.7859 |

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
ner = pipeline("ner", model="OpenMed/OpenMed-PII-Korean-QwenMed-600M-v1", aggregation_strategy="simple")

text = """
환자 이영희 (생년월일: 1985/03/15, 주민등록번호: 850315-9876543) 오늘 진료함.
연락처: lee.yh@email.kr, 전화: +82 10-1234-5678.
주소: 서울시 서초구 반포대로 123.
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

model_name = "OpenMed/OpenMed-PII-Korean-QwenMed-600M-v1"
model = AutoModelForTokenClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

texts = [
    "환자 이영희 (생년월일: 1985/03/15, 주민등록번호: 850315-9876543) 오늘 진료함.",
    "연락처: lee.yh@email.kr, 전화: +82 10-1234-5678.",
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
- **Synthetic Korean Data**: ~25K high-quality samples generated with locale-specific formatting (주민등록번호 format, +82 phones, Korean names, ₩ currency)

- **Format**: BIO-tagged token classification
- **Labels**: 76 BIO tags (54 entity types)

### Training Configuration

- **Max Sequence Length**: 512 tokens
- **Epochs**: 3
- **Framework**: Hugging Face Transformers + Trainer API

## Intended Use & Limitations

### Intended Use

- **De-identification**: Automated redaction of PII in Korean clinical notes, medical records, and documents
- **Compliance**: Supporting GDPR, and other privacy regulation compliance
- **Data Preprocessing**: Preparing datasets for research by removing sensitive information
- **Audit Support**: Identifying PII in document collections

### Limitations

**Important**: This model is intended as an **assistive tool**, not a replacement for human review.

- **False Negatives**: Some PII may not be detected; always verify critical applications
- **Context Sensitivity**: Performance may vary with domain-specific terminology
- **Language**: Optimized for Korean text; may not perform well on other languages

## Citation

```bibtex
@misc{openmed-pii-2026,
  title = {OpenMed-PII-Korean-QwenMed-600M-v1: Korean PII Detection Model},
  author = {OpenMed Science},
  year = {2026},
  publisher = {Hugging Face},
  url = {https://huggingface.co/OpenMed/OpenMed-PII-Korean-QwenMed-600M-v1}
}
```

## Links

- **Organization**: [OpenMed](https://huggingface.co/OpenMed)
