---
language:
  - es
license: apache-2.0
base_model: microsoft/deberta-v3-small
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
  - spanish
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
  - name: OpenMed-PII-Spanish-SuperClinical-Small-44M-v1
    results:
      - task:
          type: token-classification
          name: Named Entity Recognition
        dataset:
          name: AI4Privacy (Spanish subset)
          type: ai4privacy/pii-masking-400k
          split: test
        metrics:
          - type: f1
            value: 0.9225
            name: F1 (micro)
          - type: precision
            value: 0.9150
            name: Precision
          - type: recall
            value: 0.9300
            name: Recall
widget:
  - text: "Dr. Carlos García (DNI: 12345678A) puede ser contactado en carlos.garcia@hospital.es o al +34 612 345 678. Vive en Calle Gran Vía 25, 28013 Madrid."
    example_title: Clinical Note with PII (Spanish)
---

# OpenMed-PII-Spanish-SuperClinical-Small-44M-v1

**Spanish PII Detection Model** | 44M Parameters | Open Source

[![F1 Score](https://img.shields.io/badge/F1-92.25%25-brightgreen)]() [![Precision](https://img.shields.io/badge/Precision-91.50%25-blue)]() [![Recall](https://img.shields.io/badge/Recall-93.00%25-orange)]()

## Model Description

**OpenMed-PII-Spanish-SuperClinical-Small-44M-v1** is a transformer-based token classification model fine-tuned for **Personally Identifiable Information (PII) detection in Spanish text**. This model identifies and classifies **54 types of sensitive information** including names, addresses, social security numbers, medical record numbers, and more.

### Key Features

- **Spanish-Optimized**: Specifically trained on Spanish text for optimal performance
- **High Accuracy**: Achieves strong F1 scores across diverse PII categories
- **Comprehensive Coverage**: Detects 55+ entity types spanning personal, financial, medical, and contact information
- **Privacy-Focused**: Designed for de-identification and compliance with GDPR and other privacy regulations
- **Production-Ready**: Optimized for real-world text processing pipelines

## Performance

Evaluated on the Spanish subset of AI4Privacy dataset:

| Metric | Score |
|:---|:---:|
| **Micro F1** | **0.9225** |
| Precision | 0.9150 |
| Recall | 0.9300 |
| Macro F1 | 0.9296 |
| Weighted F1 | 0.9221 |
| Accuracy | 0.9936 |

### Top 10 Spanish PII Models

| Rank | Model | F1 | Precision | Recall |
|:---:|:---|:---:|:---:|:---:|
| 1 | [OpenMed-PII-Spanish-SnowflakeMed-Large-568M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Spanish-SnowflakeMed-Large-568M-v1) | 0.9495 | 0.9501 | 0.9490 |
| 2 | [OpenMed-PII-Spanish-SuperClinical-Large-434M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Spanish-SuperClinical-Large-434M-v1) | 0.9491 | 0.9515 | 0.9468 |
| 3 | [OpenMed-PII-Spanish-BigMed-Large-560M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Spanish-BigMed-Large-560M-v1) | 0.9436 | 0.9447 | 0.9426 |
| 4 | [OpenMed-PII-Spanish-EuroMed-210M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Spanish-EuroMed-210M-v1) | 0.9419 | 0.9443 | 0.9395 |
| 5 | [OpenMed-PII-Spanish-mClinicalE5-Large-560M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Spanish-mClinicalE5-Large-560M-v1) | 0.9405 | 0.9362 | 0.9448 |
| 6 | [OpenMed-PII-Spanish-ClinicalBGE-568M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Spanish-ClinicalBGE-568M-v1) | 0.9391 | 0.9348 | 0.9434 |
| 7 | [OpenMed-PII-Spanish-NomicMed-Large-395M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Spanish-NomicMed-Large-395M-v1) | 0.9379 | 0.9418 | 0.9339 |
| 8 | [OpenMed-PII-Spanish-mSuperClinical-Base-279M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Spanish-mSuperClinical-Base-279M-v1) | 0.9352 | 0.9312 | 0.9392 |
| 9 | [OpenMed-PII-Spanish-SuperMedical-Large-355M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Spanish-SuperMedical-Large-355M-v1) | 0.9346 | 0.9370 | 0.9323 |
| 10 | [OpenMed-PII-Spanish-SuperClinical-Base-184M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Spanish-SuperClinical-Base-184M-v1) | 0.9256 | 0.9208 | 0.9303 |

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
ner = pipeline("ner", model="OpenMed/OpenMed-PII-Spanish-SuperClinical-Small-44M-v1", aggregation_strategy="simple")

text = """
Paciente María López (nacida el 15/03/1985, DNI: 87654321B) fue atendida hoy.
Contacto: maria.lopez@email.es, Teléfono: +34 612 345 678.
Dirección: Calle Serrano 42, 28001 Madrid.
"""

entities = ner(text)
for entity in entities:
    print(f"{entity['entity_group']}: {entity['word']} (score: {entity['score']:.3f})")
```

> **Important — Accent Handling:** This model was trained on text without diacritical marks (accents). For best results, strip accents from your input before inference. Character offsets are preserved, so you can map entities back to the original text.
>
> ```python
> import unicodedata
>
> def strip_accents(text: str) -> str:
>     nfc = unicodedata.normalize("NFC", text)
>     nfd = unicodedata.normalize("NFD", nfc)
>     stripped = "".join(ch for ch in nfd if unicodedata.category(ch) != "Mn")
>     return unicodedata.normalize("NFC", stripped)
>
> text = strip_accents(text)  # call before passing to the pipeline
> entities = ner(text)
> ```

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

model_name = "OpenMed/OpenMed-PII-Spanish-SuperClinical-Small-44M-v1"
model = AutoModelForTokenClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

texts = [
    "Paciente María López (nacida el 15/03/1985, DNI: 87654321B) fue atendida hoy.",
    "Contacto: maria.lopez@email.es, Teléfono: +34 612 345 678.",
]

inputs = tokenizer(texts, return_tensors='pt', padding=True, truncation=True)
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=-1)
```

## Training Details

### Dataset

- **Source**: [AI4Privacy PII Masking 400k](https://huggingface.co/datasets/ai4privacy/pii-masking-400k) (Spanish subset)
- **Format**: BIO-tagged token classification
- **Labels**: 109 total (54 entity types × 2 BIO tags + O)

### Training Configuration

- **Max Sequence Length**: 512 tokens
- **Epochs**: 3
- **Framework**: Hugging Face Transformers + Trainer API

## Intended Use & Limitations

### Intended Use

- **De-identification**: Automated redaction of PII in Spanish clinical notes, medical records, and documents
- **Compliance**: Supporting GDPR, and other privacy regulation compliance
- **Data Preprocessing**: Preparing datasets for research by removing sensitive information
- **Audit Support**: Identifying PII in document collections

### Limitations

**Important**: This model is intended as an **assistive tool**, not a replacement for human review.

- **False Negatives**: Some PII may not be detected; always verify critical applications
- **Context Sensitivity**: Performance may vary with domain-specific terminology
- **Language**: Optimized for Spanish text; may not perform well on other languages

## Citation

```bibtex
@misc{openmed-pii-2026,
  title = {OpenMed-PII-Spanish-SuperClinical-Small-44M-v1: Spanish PII Detection Model},
  author = {OpenMed Science},
  year = {2026},
  publisher = {Hugging Face},
  url = {https://huggingface.co/OpenMed/OpenMed-PII-Spanish-SuperClinical-Small-44M-v1}
}
```

## Links

- **Organization**: [OpenMed](https://huggingface.co/OpenMed)
