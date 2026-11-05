---
language:
  - hi
license: apache-2.0
base_model: distilbert/distilbert-base-multilingual-cased
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
  - hindi
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
  - name: OpenMed-PII-Hindi-mLiteClinical-135M-v1
    results:
      - task:
          type: token-classification
          name: Named Entity Recognition
        dataset:
          name: AI4Privacy (Hindi subset)
          type: ai4privacy/pii-masking-400k
          split: test
        metrics:
          - type: f1
            value: 0.9465
            name: F1 (micro)
          - type: precision
            value: 0.9455
            name: Precision
          - type: recall
            value: 0.9474
            name: Recall
widget:
  - text: "डॉ. राजेश शर्मा (आधार: 1234 5678 9012) से rajesh.sharma@hospital.in या +91 98765 43210 पर संपर्क किया जा सकता है। पता: 42 महात्मा गांधी रोड, 110001 नई दिल्ली।"
    example_title: Clinical Note with PII (Hindi)
---

# OpenMed-PII-Hindi-mLiteClinical-135M-v1

**Hindi PII Detection Model** | 135M Parameters | Open Source

[![F1 Score](https://img.shields.io/badge/F1-94.65%25-brightgreen)]() [![Precision](https://img.shields.io/badge/Precision-94.55%25-blue)]() [![Recall](https://img.shields.io/badge/Recall-94.74%25-orange)]()

## Model Description

**OpenMed-PII-Hindi-mLiteClinical-135M-v1** is a transformer-based token classification model fine-tuned for **Personally Identifiable Information (PII) detection in Hindi text**. This model identifies and classifies **54 types of sensitive information** including names, addresses, social security numbers, medical record numbers, and more.

### Key Features

- **Hindi-Optimized**: Specifically trained on Hindi text for optimal performance
- **High Accuracy**: Achieves strong F1 scores across diverse PII categories
- **Comprehensive Coverage**: Detects 55+ entity types spanning personal, financial, medical, and contact information
- **Privacy-Focused**: Designed for de-identification and compliance with GDPR and other privacy regulations
- **Production-Ready**: Optimized for real-world text processing pipelines

## Performance

Evaluated on the Hindi subset of AI4Privacy dataset:

| Metric | Score |
|:---|:---:|
| **Micro F1** | **0.9465** |
| Precision | 0.9455 |
| Recall | 0.9474 |
| Macro F1 | 0.9553 |
| Weighted F1 | 0.9455 |
| Accuracy | 0.9901 |

### Top 10 Hindi PII Models

| Rank | Model | F1 | Precision | Recall |
|:---:|:---|:---:|:---:|:---:|
| 1 | [OpenMed-PII-Hindi-SuperClinical-Large-434M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Hindi-SuperClinical-Large-434M-v1) | 0.9660 | 0.9650 | 0.9669 |
| 2 | [OpenMed-PII-Hindi-SnowflakeMed-Large-568M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Hindi-SnowflakeMed-Large-568M-v1) | 0.9648 | 0.9635 | 0.9661 |
| 3 | [OpenMed-PII-Hindi-BigMed-Large-560M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Hindi-BigMed-Large-560M-v1) | 0.9641 | 0.9629 | 0.9653 |
| 4 | [OpenMed-PII-Hindi-ClinicalBGE-568M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Hindi-ClinicalBGE-568M-v1) | 0.9635 | 0.9625 | 0.9644 |
| 5 | [OpenMed-PII-Hindi-mClinicalE5-Large-560M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Hindi-mClinicalE5-Large-560M-v1) | 0.9615 | 0.9601 | 0.9630 |
| 6 | [OpenMed-PII-Hindi-mSuperClinical-Base-279M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Hindi-mSuperClinical-Base-279M-v1) | 0.9593 | 0.9577 | 0.9610 |
| 7 | [OpenMed-PII-Hindi-SuperMedical-Large-355M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Hindi-SuperMedical-Large-355M-v1) | 0.9588 | 0.9580 | 0.9596 |
| 8 | [OpenMed-PII-Hindi-NomicMed-Large-395M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Hindi-NomicMed-Large-395M-v1) | 0.9554 | 0.9542 | 0.9565 |
| 9 | [OpenMed-PII-Hindi-BioClinicalModern-Large-395M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Hindi-BioClinicalModern-Large-395M-v1) | 0.9539 | 0.9534 | 0.9544 |
| 10 | [OpenMed-PII-Hindi-EuroMed-210M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Hindi-EuroMed-210M-v1) | 0.9538 | 0.9530 | 0.9547 |

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
ner = pipeline("ner", model="OpenMed/OpenMed-PII-Hindi-mLiteClinical-135M-v1", aggregation_strategy="simple")

text = """
रोगी राजेश कुमार (जन्म तिथि: 15/03/1985, आधार: 9876 5432 1098) की आज जांच हुई।
संपर्क: rajesh.kumar@email.in, फ़ोन: +91 98765 43210।
पता: 123 विकास मार्ग, 110092 नई दिल्ली।
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

model_name = "OpenMed/OpenMed-PII-Hindi-mLiteClinical-135M-v1"
model = AutoModelForTokenClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

texts = [
    "रोगी राजेश कुमार (जन्म तिथि: 15/03/1985, आधार: 9876 5432 1098) की आज जांच हुई।",
    "संपर्क: rajesh.kumar@email.in, फ़ोन: +91 98765 43210।",
]

inputs = tokenizer(texts, return_tensors='pt', padding=True, truncation=True)
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=-1)
```

## Training Details

### Dataset

- **Source**: [AI4Privacy PII Masking 400k](https://huggingface.co/datasets/ai4privacy/pii-masking-400k) (Hindi subset)
- **Format**: BIO-tagged token classification
- **Labels**: 109 total (54 entity types × 2 BIO tags + O)

### Training Configuration

- **Max Sequence Length**: 512 tokens
- **Epochs**: 3
- **Framework**: Hugging Face Transformers + Trainer API

## Intended Use & Limitations

### Intended Use

- **De-identification**: Automated redaction of PII in Hindi clinical notes, medical records, and documents
- **Compliance**: Supporting GDPR, and other privacy regulation compliance
- **Data Preprocessing**: Preparing datasets for research by removing sensitive information
- **Audit Support**: Identifying PII in document collections

### Limitations

**Important**: This model is intended as an **assistive tool**, not a replacement for human review.

- **False Negatives**: Some PII may not be detected; always verify critical applications
- **Context Sensitivity**: Performance may vary with domain-specific terminology
- **Language**: Optimized for Hindi text; may not perform well on other languages

## Citation

```bibtex
@misc{openmed-pii-2026,
  title = {OpenMed-PII-Hindi-mLiteClinical-135M-v1: Hindi PII Detection Model},
  author = {OpenMed Science},
  year = {2026},
  publisher = {Hugging Face},
  url = {https://huggingface.co/OpenMed/OpenMed-PII-Hindi-mLiteClinical-135M-v1}
}
```

## Links

- **Organization**: [OpenMed](https://huggingface.co/OpenMed)
