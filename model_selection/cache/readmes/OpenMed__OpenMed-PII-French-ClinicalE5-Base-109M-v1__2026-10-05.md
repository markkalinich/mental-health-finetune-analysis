---
language:
  - fr
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
  - french
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
  - name: OpenMed-PII-French-ClinicalE5-Base-109M-v1
    results:
      - task:
          type: token-classification
          name: Named Entity Recognition
        dataset:
          name: AI4Privacy (French subset)
          type: ai4privacy/pii-masking-400k
          split: test
        metrics:
          - type: f1
            value: 0.9379
            name: F1 (micro)
          - type: precision
            value: 0.9341
            name: Precision
          - type: recall
            value: 0.9416
            name: Recall
widget:
  - text: "Dr. Jean Dupont (NSS: 1 85 12 75 108 123 45) peut être contacté à jean.dupont@hopital.fr ou au 06 12 34 56 78. Il habite au 15 Rue de la Paix, 75002 Paris."
    example_title: Clinical Note with PII (French)
---

# OpenMed-PII-French-ClinicalE5-Base-109M-v1

**French PII Detection Model** | 109M Parameters | Open Source

[![F1 Score](https://img.shields.io/badge/F1-93.79%25-brightgreen)]() [![Precision](https://img.shields.io/badge/Precision-93.41%25-blue)]() [![Recall](https://img.shields.io/badge/Recall-94.16%25-orange)]()

## Model Description

**OpenMed-PII-French-ClinicalE5-Base-109M-v1** is a transformer-based token classification model fine-tuned for **Personally Identifiable Information (PII) detection in French text**. This model identifies and classifies **54 types of sensitive information** including names, addresses, social security numbers, medical record numbers, and more.

### Key Features

- **French-Optimized**: Specifically trained on French text for optimal performance
- **High Accuracy**: Achieves strong F1 scores across diverse PII categories
- **Comprehensive Coverage**: Detects 55+ entity types spanning personal, financial, medical, and contact information
- **Privacy-Focused**: Designed for de-identification and compliance with GDPR and other privacy regulations
- **Production-Ready**: Optimized for real-world text processing pipelines

## Performance

Evaluated on the French subset of AI4Privacy dataset:

| Metric | Score |
|:---|:---:|
| **Micro F1** | **0.9379** |
| Precision | 0.9341 |
| Recall | 0.9416 |
| Macro F1 | 0.9145 |
| Weighted F1 | 0.9325 |
| Accuracy | 0.9916 |

### Top 10 French PII Models

| Rank | Model | F1 | Precision | Recall |
|:---:|:---|:---:|:---:|:---:|
| 1 | [OpenMed-PII-French-SuperClinical-Large-434M-v1](https://huggingface.co/OpenMed/OpenMed-PII-French-SuperClinical-Large-434M-v1) | 0.9797 | 0.9790 | 0.9804 |
| 2 | [OpenMed-PII-French-EuroMed-210M-v1](https://huggingface.co/OpenMed/OpenMed-PII-French-EuroMed-210M-v1) | 0.9762 | 0.9747 | 0.9777 |
| 3 | [OpenMed-PII-French-ClinicalBGE-568M-v1](https://huggingface.co/OpenMed/OpenMed-PII-French-ClinicalBGE-568M-v1) | 0.9733 | 0.9718 | 0.9748 |
| 4 | [OpenMed-PII-French-BigMed-Large-560M-v1](https://huggingface.co/OpenMed/OpenMed-PII-French-BigMed-Large-560M-v1) | 0.9733 | 0.9716 | 0.9749 |
| 5 | [OpenMed-PII-French-SnowflakeMed-Large-568M-v1](https://huggingface.co/OpenMed/OpenMed-PII-French-SnowflakeMed-Large-568M-v1) | 0.9728 | 0.9711 | 0.9745 |
| 6 | [OpenMed-PII-French-SuperMedical-Large-355M-v1](https://huggingface.co/OpenMed/OpenMed-PII-French-SuperMedical-Large-355M-v1) | 0.9728 | 0.9712 | 0.9744 |
| 7 | [OpenMed-PII-French-NomicMed-Large-395M-v1](https://huggingface.co/OpenMed/OpenMed-PII-French-NomicMed-Large-395M-v1) | 0.9722 | 0.9704 | 0.9740 |
| 8 | [OpenMed-PII-French-mClinicalE5-Large-560M-v1](https://huggingface.co/OpenMed/OpenMed-PII-French-mClinicalE5-Large-560M-v1) | 0.9713 | 0.9697 | 0.9729 |
| 9 | [OpenMed-PII-French-mSuperClinical-Base-279M-v1](https://huggingface.co/OpenMed/OpenMed-PII-French-mSuperClinical-Base-279M-v1) | 0.9674 | 0.9662 | 0.9687 |
| 10 | [OpenMed-PII-French-ClinicalBGE-Large-335M-v1](https://huggingface.co/OpenMed/OpenMed-PII-French-ClinicalBGE-Large-335M-v1) | 0.9668 | 0.9644 | 0.9692 |

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
ner = pipeline("ner", model="OpenMed/OpenMed-PII-French-ClinicalE5-Base-109M-v1", aggregation_strategy="simple")

text = """
Patient Jean Martin (né le 15/03/1985, NSS: 1 85 03 75 108 234 67) a été vu aujourd'hui.
Contact: jean.martin@email.fr, Téléphone: 06 12 34 56 78.
Adresse: 123 Avenue des Champs-Élysées, 75008 Paris.
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

model_name = "OpenMed/OpenMed-PII-French-ClinicalE5-Base-109M-v1"
model = AutoModelForTokenClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

texts = [
    "Patient Jean Martin (né le 15/03/1985, NSS: 1 85 03 75 108 234 67) a été vu aujourd'hui.",
    "Contact: jean.martin@email.fr, Téléphone: 06 12 34 56 78.",
]

inputs = tokenizer(texts, return_tensors='pt', padding=True, truncation=True)
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=-1)
```

## Training Details

### Dataset

- **Source**: [AI4Privacy PII Masking 400k](https://huggingface.co/datasets/ai4privacy/pii-masking-400k) (French subset)
- **Format**: BIO-tagged token classification
- **Labels**: 109 total (54 entity types × 2 BIO tags + O)

### Training Configuration

- **Max Sequence Length**: 512 tokens
- **Epochs**: 3
- **Framework**: Hugging Face Transformers + Trainer API

## Intended Use & Limitations

### Intended Use

- **De-identification**: Automated redaction of PII in French clinical notes, medical records, and documents
- **Compliance**: Supporting GDPR, and other privacy regulation compliance
- **Data Preprocessing**: Preparing datasets for research by removing sensitive information
- **Audit Support**: Identifying PII in document collections

### Limitations

**Important**: This model is intended as an **assistive tool**, not a replacement for human review.

- **False Negatives**: Some PII may not be detected; always verify critical applications
- **Context Sensitivity**: Performance may vary with domain-specific terminology
- **Language**: Optimized for French text; may not perform well on other languages

## Citation

```bibtex
@misc{openmed-pii-2026,
  title = {OpenMed-PII-French-ClinicalE5-Base-109M-v1: French PII Detection Model},
  author = {OpenMed Science},
  year = {2026},
  publisher = {Hugging Face},
  url = {https://huggingface.co/OpenMed/OpenMed-PII-French-ClinicalE5-Base-109M-v1}
}
```

## Links

- **Organization**: [OpenMed](https://huggingface.co/OpenMed)
