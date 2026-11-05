---
language:
  - it
license: apache-2.0
base_model: FacebookAI/roberta-large
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
  - italian
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
  - name: OpenMed-PII-Italian-SuperMedical-Large-355M-v1
    results:
      - task:
          type: token-classification
          name: Named Entity Recognition
        dataset:
          name: AI4Privacy (Italian subset)
          type: ai4privacy/pii-masking-400k
          split: test
        metrics:
          - type: f1
            value: 0.9663
            name: F1 (micro)
          - type: precision
            value: 0.9640
            name: Precision
          - type: recall
            value: 0.9686
            name: Recall
widget:
  - text: "Dr. Marco Rossi (Codice Fiscale: RSSMRC85C15H501Z) può essere contattato a marco.rossi@ospedale.it o al +39 333 123 4567. Abita in Via Roma 25, 00184 Roma."
    example_title: Clinical Note with PII (Italian)
---

# OpenMed-PII-Italian-SuperMedical-Large-355M-v1

**Italian PII Detection Model** | 355M Parameters | Open Source

[![F1 Score](https://img.shields.io/badge/F1-96.63%25-brightgreen)]() [![Precision](https://img.shields.io/badge/Precision-96.40%25-blue)]() [![Recall](https://img.shields.io/badge/Recall-96.86%25-orange)]()

## Model Description

**OpenMed-PII-Italian-SuperMedical-Large-355M-v1** is a transformer-based token classification model fine-tuned for **Personally Identifiable Information (PII) detection in Italian text**. This model identifies and classifies **54 types of sensitive information** including names, addresses, social security numbers, medical record numbers, and more.

### Key Features

- **Italian-Optimized**: Specifically trained on Italian text for optimal performance
- **High Accuracy**: Achieves strong F1 scores across diverse PII categories
- **Comprehensive Coverage**: Detects 55+ entity types spanning personal, financial, medical, and contact information
- **Privacy-Focused**: Designed for de-identification and compliance with GDPR and other privacy regulations
- **Production-Ready**: Optimized for real-world text processing pipelines

## Performance

Evaluated on the Italian subset of AI4Privacy dataset:

| Metric | Score |
|:---|:---:|
| **Micro F1** | **0.9663** |
| Precision | 0.9640 |
| Recall | 0.9686 |
| Macro F1 | 0.9577 |
| Weighted F1 | 0.9653 |
| Accuracy | 0.9950 |

### Top 10 Italian PII Models

| Rank | Model | F1 | Precision | Recall |
|:---:|:---|:---:|:---:|:---:|
| 1 | [OpenMed-PII-Italian-SuperClinical-Large-434M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Italian-SuperClinical-Large-434M-v1) | 0.9728 | 0.9707 | 0.9750 |
| 2 | [OpenMed-PII-Italian-EuroMed-210M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Italian-EuroMed-210M-v1) | 0.9685 | 0.9663 | 0.9707 |
| 3 | [OpenMed-PII-Italian-ClinicalBGE-568M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Italian-ClinicalBGE-568M-v1) | 0.9678 | 0.9653 | 0.9703 |
| 4 | [OpenMed-PII-Italian-SnowflakeMed-Large-568M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Italian-SnowflakeMed-Large-568M-v1) | 0.9678 | 0.9653 | 0.9702 |
| 5 | [OpenMed-PII-Italian-BigMed-Large-560M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Italian-BigMed-Large-560M-v1) | 0.9671 | 0.9645 | 0.9697 |
| **6** | **[OpenMed-PII-Italian-SuperMedical-Large-355M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Italian-SuperMedical-Large-355M-v1)** | **0.9663** | **0.9640** | **0.9686** |
| 7 | [OpenMed-PII-Italian-mClinicalE5-Large-560M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Italian-mClinicalE5-Large-560M-v1) | 0.9659 | 0.9633 | 0.9684 |
| 8 | [OpenMed-PII-Italian-NomicMed-Large-395M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Italian-NomicMed-Large-395M-v1) | 0.9656 | 0.9631 | 0.9682 |
| 9 | [OpenMed-PII-Italian-ClinicalBGE-Large-335M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Italian-ClinicalBGE-Large-335M-v1) | 0.9605 | 0.9575 | 0.9635 |
| 10 | [OpenMed-PII-Italian-SuperClinical-Base-184M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Italian-SuperClinical-Base-184M-v1) | 0.9596 | 0.9573 | 0.9620 |

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
ner = pipeline("ner", model="OpenMed/OpenMed-PII-Italian-SuperMedical-Large-355M-v1", aggregation_strategy="simple")

text = """
Paziente Marco Bianchi (nato il 15/03/1985, CF: BNCMRC85C15H501Z) è stato visitato oggi.
Contatto: marco.bianchi@email.it, Telefono: +39 333 123 4567.
Indirizzo: Via Garibaldi 42, 20121 Milano.
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

model_name = "OpenMed/OpenMed-PII-Italian-SuperMedical-Large-355M-v1"
model = AutoModelForTokenClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

texts = [
    "Paziente Marco Bianchi (nato il 15/03/1985, CF: BNCMRC85C15H501Z) è stato visitato oggi.",
    "Contatto: marco.bianchi@email.it, Telefono: +39 333 123 4567.",
]

inputs = tokenizer(texts, return_tensors='pt', padding=True, truncation=True)
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=-1)
```

## Training Details

### Dataset

- **Source**: [AI4Privacy PII Masking 400k](https://huggingface.co/datasets/ai4privacy/pii-masking-400k) (Italian subset)
- **Format**: BIO-tagged token classification
- **Labels**: 109 total (54 entity types × 2 BIO tags + O)

### Training Configuration

- **Max Sequence Length**: 512 tokens
- **Epochs**: 3
- **Framework**: Hugging Face Transformers + Trainer API

## Intended Use & Limitations

### Intended Use

- **De-identification**: Automated redaction of PII in Italian clinical notes, medical records, and documents
- **Compliance**: Supporting GDPR, and other privacy regulation compliance
- **Data Preprocessing**: Preparing datasets for research by removing sensitive information
- **Audit Support**: Identifying PII in document collections

### Limitations

**Important**: This model is intended as an **assistive tool**, not a replacement for human review.

- **False Negatives**: Some PII may not be detected; always verify critical applications
- **Context Sensitivity**: Performance may vary with domain-specific terminology
- **Language**: Optimized for Italian text; may not perform well on other languages

## Citation

```bibtex
@misc{openmed-pii-2026,
  title = {OpenMed-PII-Italian-SuperMedical-Large-355M-v1: Italian PII Detection Model},
  author = {OpenMed Science},
  year = {2026},
  publisher = {Hugging Face},
  url = {https://huggingface.co/OpenMed/OpenMed-PII-Italian-SuperMedical-Large-355M-v1}
}
```

## Links

- **Organization**: [OpenMed](https://huggingface.co/OpenMed)
