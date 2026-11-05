---
language:
  - de
license: apache-2.0
base_model: intfloat/e5-large-v2
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
  - german
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
  - name: OpenMed-PII-German-ClinicalE5-Large-335M-v1
    results:
      - task:
          type: token-classification
          name: Named Entity Recognition
        dataset:
          name: AI4Privacy (German subset)
          type: ai4privacy/pii-masking-400k
          split: test
        metrics:
          - type: f1
            value: 0.9646
            name: F1 (micro)
          - type: precision
            value: 0.9620
            name: Precision
          - type: recall
            value: 0.9672
            name: Recall
widget:
  - text: "Dr. Hans Müller (Sozialversicherungsnummer: 12 150385 M 123) ist erreichbar unter hans.mueller@krankenhaus.de oder 0171 234 5678. Er wohnt in der Hauptstraße 42, 10115 Berlin."
    example_title: Clinical Note with PII (German)
---

# OpenMed-PII-German-ClinicalE5-Large-335M-v1

**German PII Detection Model** | 335M Parameters | Open Source

[![F1 Score](https://img.shields.io/badge/F1-96.46%25-brightgreen)]() [![Precision](https://img.shields.io/badge/Precision-96.20%25-blue)]() [![Recall](https://img.shields.io/badge/Recall-96.72%25-orange)]()

## Model Description

**OpenMed-PII-German-ClinicalE5-Large-335M-v1** is a transformer-based token classification model fine-tuned for **Personally Identifiable Information (PII) detection in German text**. This model identifies and classifies **54 types of sensitive information** including names, addresses, social security numbers, medical record numbers, and more.

### Key Features

- **German-Optimized**: Specifically trained on German text for optimal performance
- **High Accuracy**: Achieves strong F1 scores across diverse PII categories
- **Comprehensive Coverage**: Detects 55+ entity types spanning personal, financial, medical, and contact information
- **Privacy-Focused**: Designed for de-identification and compliance with GDPR and other privacy regulations
- **Production-Ready**: Optimized for real-world text processing pipelines

## Performance

Evaluated on the German subset of AI4Privacy dataset:

| Metric | Score |
|:---|:---:|
| **Micro F1** | **0.9646** |
| Precision | 0.9620 |
| Recall | 0.9672 |
| Macro F1 | 0.9460 |
| Weighted F1 | 0.9622 |
| Accuracy | 0.9941 |

### Top 10 German PII Models

| Rank | Model | F1 | Precision | Recall |
|:---:|:---|:---:|:---:|:---:|
| 1 | [OpenMed-PII-German-SuperClinical-Large-434M-v1](https://huggingface.co/OpenMed/OpenMed-PII-German-SuperClinical-Large-434M-v1) | 0.9761 | 0.9744 | 0.9778 |
| 2 | [OpenMed-PII-German-SnowflakeMed-Large-568M-v1](https://huggingface.co/OpenMed/OpenMed-PII-German-SnowflakeMed-Large-568M-v1) | 0.9724 | 0.9705 | 0.9743 |
| 3 | [OpenMed-PII-German-ClinicalBGE-568M-v1](https://huggingface.co/OpenMed/OpenMed-PII-German-ClinicalBGE-568M-v1) | 0.9724 | 0.9702 | 0.9745 |
| 4 | [OpenMed-PII-German-BigMed-Large-560M-v1](https://huggingface.co/OpenMed/OpenMed-PII-German-BigMed-Large-560M-v1) | 0.9714 | 0.9696 | 0.9732 |
| 5 | [OpenMed-PII-German-NomicMed-Large-395M-v1](https://huggingface.co/OpenMed/OpenMed-PII-German-NomicMed-Large-395M-v1) | 0.9713 | 0.9690 | 0.9735 |
| 6 | [OpenMed-PII-German-SuperMedical-Large-355M-v1](https://huggingface.co/OpenMed/OpenMed-PII-German-SuperMedical-Large-355M-v1) | 0.9701 | 0.9684 | 0.9719 |
| 7 | [OpenMed-PII-German-EuroMed-210M-v1](https://huggingface.co/OpenMed/OpenMed-PII-German-EuroMed-210M-v1) | 0.9683 | 0.9667 | 0.9699 |
| 8 | [OpenMed-PII-German-ClinicalBGE-Large-335M-v1](https://huggingface.co/OpenMed/OpenMed-PII-German-ClinicalBGE-Large-335M-v1) | 0.9652 | 0.9624 | 0.9680 |
| **9** | **[OpenMed-PII-German-ClinicalE5-Large-335M-v1](https://huggingface.co/OpenMed/OpenMed-PII-German-ClinicalE5-Large-335M-v1)** | **0.9646** | **0.9620** | **0.9672** |
| 10 | [OpenMed-PII-German-BiomedELECTRA-Large-335M-v1](https://huggingface.co/OpenMed/OpenMed-PII-German-BiomedELECTRA-Large-335M-v1) | 0.9638 | 0.9598 | 0.9677 |

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
ner = pipeline("ner", model="OpenMed/OpenMed-PII-German-ClinicalE5-Large-335M-v1", aggregation_strategy="simple")

text = """
Patient Hans Schmidt (geboren am 15.03.1985, SVN: 12 150385 M 234) wurde heute untersucht.
Kontakt: hans.schmidt@email.de, Telefon: 0171 234 5678.
Adresse: Mozartstraße 15, 80336 München.
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

model_name = "OpenMed/OpenMed-PII-German-ClinicalE5-Large-335M-v1"
model = AutoModelForTokenClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

texts = [
    "Patient Hans Schmidt (geboren am 15.03.1985, SVN: 12 150385 M 234) wurde heute untersucht.",
    "Kontakt: hans.schmidt@email.de, Telefon: 0171 234 5678.",
]

inputs = tokenizer(texts, return_tensors='pt', padding=True, truncation=True)
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=-1)
```

## Training Details

### Dataset

- **Source**: [AI4Privacy PII Masking 400k](https://huggingface.co/datasets/ai4privacy/pii-masking-400k) (German subset)
- **Format**: BIO-tagged token classification
- **Labels**: 109 total (54 entity types × 2 BIO tags + O)

### Training Configuration

- **Max Sequence Length**: 512 tokens
- **Epochs**: 3
- **Framework**: Hugging Face Transformers + Trainer API

## Intended Use & Limitations

### Intended Use

- **De-identification**: Automated redaction of PII in German clinical notes, medical records, and documents
- **Compliance**: Supporting GDPR, and other privacy regulation compliance
- **Data Preprocessing**: Preparing datasets for research by removing sensitive information
- **Audit Support**: Identifying PII in document collections

### Limitations

**Important**: This model is intended as an **assistive tool**, not a replacement for human review.

- **False Negatives**: Some PII may not be detected; always verify critical applications
- **Context Sensitivity**: Performance may vary with domain-specific terminology
- **Language**: Optimized for German text; may not perform well on other languages

## Citation

```bibtex
@misc{openmed-pii-2026,
  title = {OpenMed-PII-German-ClinicalE5-Large-335M-v1: German PII Detection Model},
  author = {OpenMed Science},
  year = {2026},
  publisher = {Hugging Face},
  url = {https://huggingface.co/OpenMed/OpenMed-PII-German-ClinicalE5-Large-335M-v1}
}
```

## Links

- **Organization**: [OpenMed](https://huggingface.co/OpenMed)
