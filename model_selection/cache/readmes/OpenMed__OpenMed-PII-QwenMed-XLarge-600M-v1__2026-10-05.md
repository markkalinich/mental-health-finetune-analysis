---
language:
  - en
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
  - hipaa
  - pytorch
  - transformers
  - openmed
datasets:
  - nvidia/Nemotron-PII
pipeline_tag: token-classification
library_name: transformers
metrics:
  - f1
  - precision
  - recall
model-index:
  - name: OpenMed-PII-QwenMed-600M-v1
    results:
      - task:
          type: token-classification
          name: Named Entity Recognition
        dataset:
          name: nvidia/Nemotron-PII (test_strat)
          type: nvidia/Nemotron-PII
          split: test
        metrics:
          - type: f1
            value: 0.9124
            name: F1 (micro)
          - type: precision
            value: 0.9075
            name: Precision
          - type: recall
            value: 0.9173
            name: Recall
widget:
  - text: "Dr. Sarah Johnson (SSN: 123-45-6789) can be reached at sarah.johnson@hospital.org or 555-123-4567. She lives at 123 Oak Street, Boston, MA 02108."
    example_title: Clinical Note with PII
---

# OpenMed-PII-QwenMed-600M-v1

**PII Detection Model** | 600M Parameters | Open Source

[![F1 Score](https://img.shields.io/badge/F1-91.24%25-brightgreen)]() [![Precision](https://img.shields.io/badge/Precision-90.75%25-blue)]() [![Recall](https://img.shields.io/badge/Recall-91.73%25-orange)]()

## Model Description

**OpenMed-PII-QwenMed-600M-v1** is a transformer-based token classification model fine-tuned for **Personally Identifiable Information (PII) detection** in text. This model identifies and classifies **54 types of sensitive information** including names, addresses, SSNs, medical record numbers, and more.

### Key Features

- **High Accuracy**: Achieves strong F1 scores across diverse PII categories
- **Comprehensive Coverage**: Detects 50+ entity types spanning personal, financial, medical, and contact information
- **Privacy-Focused**: Designed for de-identification and compliance with HIPAA, GDPR, and other privacy regulations
- **Production-Ready**: Optimized for real-world text processing pipelines

## Performance

Evaluated on a stratified 2,000-sample test set from NVIDIA Nemotron-PII:

| Metric | Score |
|:---|:---:|
| **Micro F1** | **0.9124** |
| Precision | 0.9075 |
| Recall | 0.9173 |
| Macro F1 | 0.9268 |
| Weighted F1 | 0.9121 |
| Accuracy | 0.9913 |

### Top 10 PII Models

| Rank | Model | F1 | Precision | Recall |
|:---:|:---|:---:|:---:|:---:|
| 1 | [OpenMed-PII-SuperClinical-Large-434M-v1](https://huggingface.co/openmed/OpenMed-PII-SuperClinical-Large-434M-v1) | 0.9608 | 0.9685 | 0.9532 |
| 2 | [OpenMed-PII-BigMed-Large-560M-v1](https://huggingface.co/openmed/OpenMed-PII-BigMed-Large-560M-v1) | 0.9604 | 0.9644 | 0.9565 |
| 3 | [OpenMed-PII-EuroMed-210M-v1](https://huggingface.co/openmed/OpenMed-PII-EuroMed-210M-v1) | 0.9600 | 0.9681 | 0.9521 |
| 4 | [OpenMed-PII-SnowflakeMed-568M-v1](https://huggingface.co/openmed/OpenMed-PII-SnowflakeMed-568M-v1) | 0.9594 | 0.9640 | 0.9548 |
| 5 | [OpenMed-PII-SuperMedical-Large-355M-v1](https://huggingface.co/openmed/OpenMed-PII-SuperMedical-Large-355M-v1) | 0.9592 | 0.9632 | 0.9553 |
| 6 | [OpenMed-PII-ClinicalBGE-568M-v1](https://huggingface.co/openmed/OpenMed-PII-ClinicalBGE-568M-v1) | 0.9587 | 0.9636 | 0.9538 |
| 7 | [OpenMed-PII-mClinicalE5-Large-560M-v1](https://huggingface.co/openmed/OpenMed-PII-mClinicalE5-Large-560M-v1) | 0.9582 | 0.9631 | 0.9533 |
| 8 | [OpenMed-PII-ModernMed-Large-395M-v1](https://huggingface.co/openmed/OpenMed-PII-ModernMed-Large-395M-v1) | 0.9579 | 0.9639 | 0.9520 |
| 9 | [OpenMed-PII-BioClinicalModern-Large-395M-v1](https://huggingface.co/openmed/OpenMed-PII-BioClinicalModern-Large-395M-v1) | 0.9579 | 0.9656 | 0.9502 |
| 10 | [OpenMed-PII-ClinicalE5-Large-335M-v1](https://huggingface.co/openmed/OpenMed-PII-ClinicalE5-Large-335M-v1) | 0.9577 | 0.9604 | 0.9550 |

### Best Performing Entities

| Entity | F1 | Precision | Recall | Support |
|:---|:---:|:---:|:---:|:---:|
| `blood_type` | 0.992 | 0.992 | 0.992 | 132 |
| `biometric_identifier` | 0.991 | 0.991 | 0.991 | 224 |
| `swift_bic` | 0.990 | 0.980 | 1.000 | 97 |
| `cvv` | 0.989 | 1.000 | 0.978 | 92 |
| `bank_routing_number` | 0.988 | 0.992 | 0.984 | 128 |

### Challenging Entities

These entity types have lower performance and may benefit from additional post-processing:

| Entity | F1 | Precision | Recall | Support |
|:---|:---:|:---:|:---:|:---:|
| `county` | 0.821 | 0.770 | 0.879 | 313 |
| `company_name` | 0.811 | 0.778 | 0.846 | 857 |
| `time` | 0.784 | 0.778 | 0.789 | 459 |
| `date_time` | 0.642 | 0.583 | 0.714 | 227 |
| `occupation` | 0.567 | 0.609 | 0.530 | 692 |

## Supported Entity Types

This model detects **54 PII entity types** organized into categories:

<details>
<summary><strong>Identifiers</strong> (16 types)</summary>

| Entity | Description |
|:---|:---|
| `account_number` | Account Number |
| `api_key` | Api Key |
| `bank_routing_number` | Bank Routing Number |
| `certificate_license_number` | Certificate License Number |
| `credit_debit_card` | Credit Debit Card |
| `cvv` | Cvv |
| `employee_id` | Employee Id |
| `health_plan_beneficiary_number` | Health Plan Beneficiary Number |
| `mac_address` | Mac Address |
| `medical_record_number` | Medical Record Number |
| ... | *and 6 more* |

</details>

<details>
<summary><strong>Personal Info</strong> (14 types)</summary>

| Entity | Description |
|:---|:---|
| `age` | Age |
| `biometric_identifier` | Biometric Identifier |
| `blood_type` | Blood Type |
| `date_of_birth` | Date Of Birth |
| `education_level` | Education Level |
| `first_name` | First Name |
| `last_name` | Last Name |
| `gender` | Gender |
| `language` | Language |
| `occupation` | Occupation |
| ... | *and 4 more* |

</details>

<details>
<summary><strong>Contact Info</strong> (4 types)</summary>

| Entity | Description |
|:---|:---|
| `email` | Email |
| `phone_number` | Phone Number |
| `fax_number` | Fax Number |
| `url` | Url |

</details>

<details>
<summary><strong>Location</strong> (6 types)</summary>

| Entity | Description |
|:---|:---|
| `city` | City |
| `coordinate` | Coordinate |
| `country` | Country |
| `county` | County |
| `state` | State |
| `street_address` | Street Address |

</details>

<details>
<summary><strong>Network Info</strong> (3 types)</summary>

| Entity | Description |
|:---|:---|
| `device_identifier` | Device Identifier |
| `ipv4` | Ipv4 |
| `ipv6` | Ipv6 |

</details>

<details>
<summary><strong>Temporal</strong> (3 types)</summary>

| Entity | Description |
|:---|:---|
| `date` | Date |
| `date_time` | Date Time |
| `time` | Time |

</details>

<details>
<summary><strong>Organization</strong> (1 types)</summary>

| Entity | Description |
|:---|:---|
| `company_name` | Company Name |

</details>

## Usage

### Quick Start

```python
from transformers import pipeline

# Load the PII detection pipeline
ner = pipeline("ner", model="openmed/OpenMed-PII-QwenMed-600M-v1", aggregation_strategy="simple")

text = """
Patient John Smith (DOB: 03/15/1985, SSN: 123-45-6789) was seen today.
Contact: john.smith@email.com, Phone: (555) 123-4567.
Address: 456 Oak Street, Boston, MA 02108.
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

model_name = "openmed/OpenMed-PII-QwenMed-600M-v1"
model = AutoModelForTokenClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

texts = [
    "Contact Dr. Jane Doe at jane.doe@hospital.org",
    "Patient SSN: 987-65-4321, MRN: 12345678",
]

inputs = tokenizer(texts, return_tensors='pt', padding=True, truncation=True)
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=-1)
```

## Training Details

### Dataset

- **Source**: [NVIDIA Nemotron-PII](https://huggingface.co/datasets/nvidia/Nemotron-PII)
- **Format**: BIO-tagged token classification
- **Labels**: 106 total (53 entity types × 2 BIO tags + O)
- **Splits**: 50K train / 5K validation / 45K test

### Training Configuration

- **Max Sequence Length**: 384 tokens
- **Label Strategy**: First token only (`label_all_tokens=False`)
- **Framework**: Hugging Face Transformers + Trainer API

## Intended Use & Limitations

### Intended Use

- **De-identification**: Automated redaction of PII in clinical notes, medical records, and documents
- **Compliance**: Supporting HIPAA, GDPR, and privacy regulation compliance
- **Data Preprocessing**: Preparing datasets for research by removing sensitive information
- **Audit Support**: Identifying PII in document collections

### Limitations

⚠️ **Important**: This model is intended as an **assistive tool**, not a replacement for human review.

- **False Negatives**: Some PII may not be detected; always verify critical applications
- **Context Sensitivity**: Performance may vary with domain-specific terminology
- **Challenging Categories**: `occupation`, `time`, and `sexuality` have lower F1 scores
- **Language**: Primarily trained on English text

## Citation

```bibtex
@misc{openmed-pii-2026,
  title = {OpenMed-PII-QwenMed-600M-v1: PII Detection Model},
  author = {OpenMed Science},
  year = {2026},
  publisher = {Hugging Face},
  url = {https://huggingface.co/openmed/OpenMed-PII-QwenMed-600M-v1}
}
```

## Links

- **Organization**: [OpenMed](https://huggingface.co/OpenMed)
