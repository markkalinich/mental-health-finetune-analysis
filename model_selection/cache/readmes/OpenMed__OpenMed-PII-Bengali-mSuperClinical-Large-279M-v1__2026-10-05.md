---
language:
  - bn
license: apache-2.0
base_model: microsoft/mdeberta-v3-base
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
  - bengali
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
  - name: OpenMed-PII-Bengali-mSuperClinical-Large-279M-v1
    results:
      - task:
          type: token-classification
          name: Named Entity Recognition
        dataset:
          name: AI4Privacy + Synthetic Bengali PII
          type: ai4privacy/pii-masking-200k
          split: test
        metrics:
          - type: f1
            value: 0.8570
            name: F1 (micro)
          - type: precision
            value: 0.8522
            name: Precision
          - type: recall
            value: 0.8619
            name: Recall
widget:
  - text: "ডা. রহিম আহমেদ (NID: 1234567890123) rahman.ahmed@hospital.bd বা +880 1712 345678 এ যোগাযোগ করা যাবে। ঠিকানা: ধানমন্ডি ৪২, ঢাকা ১২০৫।"
    example_title: Clinical Note with PII (Bengali)
---

# OpenMed-PII-Bengali-mSuperClinical-Large-279M-v1

**Bengali PII Detection Model** | 279M Parameters | Open Source

[![F1 Score](https://img.shields.io/badge/F1-85.70%25-brightgreen)]() [![Precision](https://img.shields.io/badge/Precision-85.22%25-blue)]() [![Recall](https://img.shields.io/badge/Recall-86.19%25-orange)]()

## Model Description

**OpenMed-PII-Bengali-mSuperClinical-Large-279M-v1** is a transformer-based token classification model fine-tuned for **Personally Identifiable Information (PII) detection in Bengali text**. This model identifies and classifies **54 types of sensitive information** including names, addresses, social security numbers, medical record numbers, and more.

### Key Features

- **Bengali-Optimized**: Specifically trained on Bengali text for optimal performance
- **High Accuracy**: Achieves strong F1 scores across diverse PII categories
- **Comprehensive Coverage**: Detects 55+ entity types spanning personal, financial, medical, and contact information
- **Privacy-Focused**: Designed for de-identification and compliance with GDPR and other privacy regulations
- **Production-Ready**: Optimized for real-world text processing pipelines

## Performance

Evaluated on the Bengali test split (AI4Privacy + synthetic data):

| Metric | Score |
|:---|:---:|
| **Micro F1** | **0.8570** |
| Precision | 0.8522 |
| Recall | 0.8619 |
| Macro F1 | 0.6587 |
| Weighted F1 | 0.8572 |
| Accuracy | 0.8986 |

### Top 10 Bengali PII Models

| Rank | Model | F1 | Precision | Recall |
|:---:|:---|:---:|:---:|:---:|
| 1 | [OpenMed-PII-Bengali-BigMed-Large-560M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Bengali-BigMed-Large-560M-v1) | 0.8748 | 0.8747 | 0.8750 |
| 2 | [OpenMed-PII-Bengali-ClinicalBGE-Large-568M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Bengali-ClinicalBGE-Large-568M-v1) | 0.8602 | 0.8538 | 0.8667 |
| 3 | [OpenMed-PII-Bengali-SnowflakeMed-Large-568M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Bengali-SnowflakeMed-Large-568M-v1) | 0.8593 | 0.8584 | 0.8603 |
| **4** | **[OpenMed-PII-Bengali-mSuperClinical-Large-279M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Bengali-mSuperClinical-Large-279M-v1)** | **0.8570** | **0.8522** | **0.8619** |
| 5 | [OpenMed-PII-Bengali-BigMed-Large-278M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Bengali-BigMed-Large-278M-v1) | 0.8558 | 0.8448 | 0.8672 |
| 6 | [OpenMed-PII-Bengali-SuperClinical-Large-434M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Bengali-SuperClinical-Large-434M-v1) | 0.8530 | 0.8477 | 0.8585 |
| 7 | [OpenMed-PII-Bengali-mLiteClinical-Base-135M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Bengali-mLiteClinical-Base-135M-v1) | 0.8527 | 0.8434 | 0.8621 |
| 8 | [OpenMed-PII-Bengali-NomicMed-Large-395M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Bengali-NomicMed-Large-395M-v1) | 0.8526 | 0.8476 | 0.8578 |
| 9 | [OpenMed-PII-Bengali-SuperClinical-Small-44M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Bengali-SuperClinical-Small-44M-v1) | 0.8498 | 0.8490 | 0.8506 |
| 10 | [OpenMed-PII-Bengali-ModernMed-Large-395M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Bengali-ModernMed-Large-395M-v1) | 0.8488 | 0.8446 | 0.8531 |

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
ner = pipeline("ner", model="OpenMed/OpenMed-PII-Bengali-mSuperClinical-Large-279M-v1", aggregation_strategy="simple")

text = """
রোগী করিম হোসেন (জন্ম তারিখ: ১৫/০৩/১৯৮৫, NID: 9876543210987) আজ পরীক্ষা করা হয়েছে।
যোগাযোগ: karim.hossain@email.bd, ফোন: +880 1712 345678।
ঠিকানা: গুলশান ৪২, ঢাকা ১২১২।
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

model_name = "OpenMed/OpenMed-PII-Bengali-mSuperClinical-Large-279M-v1"
model = AutoModelForTokenClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

texts = [
    "রোগী করিম হোসেন (জন্ম তারিখ: ১৫/০৩/১৯৮৫, NID: 9876543210987) আজ পরীক্ষা করা হয়েছে।",
    "যোগাযোগ: karim.hossain@email.bd, ফোন: +880 1712 345678।",
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
- **Synthetic Bengali Data**: ~25K high-quality samples generated with locale-specific formatting (NID format, +880 phones, Bengali names, ৳ currency)

- **Format**: BIO-tagged token classification
- **Labels**: 76 BIO tags (54 entity types)

### Training Configuration

- **Max Sequence Length**: 512 tokens
- **Framework**: Hugging Face Transformers + Trainer API

## Intended Use & Limitations

### Intended Use

- **De-identification**: Automated redaction of PII in Bengali clinical notes, medical records, and documents
- **Compliance**: Supporting GDPR, and other privacy regulation compliance
- **Data Preprocessing**: Preparing datasets for research by removing sensitive information
- **Audit Support**: Identifying PII in document collections

### Limitations

**Important**: This model is intended as an **assistive tool**, not a replacement for human review.

- **False Negatives**: Some PII may not be detected; always verify critical applications
- **Context Sensitivity**: Performance may vary with domain-specific terminology
- **Language**: Optimized for Bengali text; may not perform well on other languages

## Citation

```bibtex
@misc{openmed-pii-2026,
  title = {OpenMed-PII-Bengali-mSuperClinical-Large-279M-v1: Bengali PII Detection Model},
  author = {OpenMed Science},
  year = {2026},
  publisher = {Hugging Face},
  url = {https://huggingface.co/OpenMed/OpenMed-PII-Bengali-mSuperClinical-Large-279M-v1}
}
```

## Links

- **Organization**: [OpenMed](https://huggingface.co/OpenMed)
