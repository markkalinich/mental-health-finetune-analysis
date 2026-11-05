---
language:
  - nl
license: apache-2.0
base_model: microsoft/deberta-v3-large
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
  - dutch
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
  - name: OpenMed-PII-Dutch-SuperClinical-Large-434M-v1
    results:
      - task:
          type: token-classification
          name: Named Entity Recognition
        dataset:
          name: AI4Privacy (Dutch subset)
          type: ai4privacy/pii-masking-400k
          split: test
        metrics:
          - type: f1
            value: 0.9419
            name: F1 (micro)
          - type: precision
            value: 0.9390
            name: Precision
          - type: recall
            value: 0.9448
            name: Recall
widget:
  - text: "Dr. Jan de Vries (BSN: 123456789) is bereikbaar via jan.devries@ziekenhuis.nl of +31 6 12345678. Hij woont op Keizersgracht 42, 1015 CS Amsterdam."
    example_title: Clinical Note with PII (Dutch)
---

# OpenMed-PII-Dutch-SuperClinical-Large-434M-v1

**Dutch PII Detection Model** | 434M Parameters | Open Source

[![F1 Score](https://img.shields.io/badge/F1-94.19%25-brightgreen)]() [![Precision](https://img.shields.io/badge/Precision-93.90%25-blue)]() [![Recall](https://img.shields.io/badge/Recall-94.48%25-orange)]()

## Model Description

**OpenMed-PII-Dutch-SuperClinical-Large-434M-v1** is a transformer-based token classification model fine-tuned for **Personally Identifiable Information (PII) detection in Dutch text**. This model identifies and classifies **54 types of sensitive information** including names, addresses, social security numbers, medical record numbers, and more.

### Key Features

- **Dutch-Optimized**: Specifically trained on Dutch text for optimal performance
- **High Accuracy**: Achieves strong F1 scores across diverse PII categories
- **Comprehensive Coverage**: Detects 54 entity types spanning personal, financial, medical, and contact information
- **Privacy-Focused**: Designed for de-identification and compliance with GDPR and other privacy regulations
- **Production-Ready**: Optimized for real-world text processing pipelines

## Performance

Evaluated on the Dutch subset of AI4Privacy dataset:

| Metric | Score |
|:---|:---:|
| **Micro F1** | **0.9419** |
| Precision | 0.9390 |
| Recall | 0.9448 |
| Macro F1 | 0.9421 |
| Weighted F1 | 0.9417 |
| Accuracy | 0.9949 |

### Top 10 Dutch PII Models

| Rank | Model | F1 | Precision | Recall |
|:---:|:---|:---:|:---:|:---:|
| **1** | **[OpenMed-PII-Dutch-SuperClinical-Large-434M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Dutch-SuperClinical-Large-434M-v1)** | **0.9419** | **0.9390** | **0.9448** |
| 2 | [OpenMed-PII-Dutch-BigMed-Large-560M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Dutch-BigMed-Large-560M-v1) | 0.9336 | 0.9336 | 0.9336 |
| 3 | [OpenMed-PII-Dutch-SnowflakeMed-Large-568M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Dutch-SnowflakeMed-Large-568M-v1) | 0.9243 | 0.9206 | 0.9280 |
| 4 | [OpenMed-PII-Dutch-ClinicalBGE-568M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Dutch-ClinicalBGE-568M-v1) | 0.9235 | 0.9210 | 0.9259 |
| 5 | [OpenMed-PII-Dutch-mSuperClinical-Base-279M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Dutch-mSuperClinical-Base-279M-v1) | 0.9204 | 0.9095 | 0.9315 |
| 6 | [OpenMed-PII-Dutch-mClinicalE5-Large-560M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Dutch-mClinicalE5-Large-560M-v1) | 0.9201 | 0.9111 | 0.9292 |
| 7 | [OpenMed-PII-Dutch-SuperMedical-Large-355M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Dutch-SuperMedical-Large-355M-v1) | 0.9189 | 0.9149 | 0.9230 |
| 8 | [OpenMed-PII-Dutch-NomicMed-Large-395M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Dutch-NomicMed-Large-395M-v1) | 0.9181 | 0.9212 | 0.9150 |
| 9 | [OpenMed-PII-Dutch-EuroMed-210M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Dutch-EuroMed-210M-v1) | 0.9143 | 0.9171 | 0.9115 |
| 10 | [OpenMed-PII-Dutch-BioClinicalModern-Large-395M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Dutch-BioClinicalModern-Large-395M-v1) | 0.9073 | 0.9161 | 0.8988 |

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

### Using OpenMed

```bash
uv pip install "openmed[hf]"
```

```python
from openmed import extract_pii

result = extract_pii(
    "Patiënt: Eva de Vries, geboortedatum: 15 januari 1984, BSN: 123456782, telefoon: +31 6 12345678",
    lang="nl",
    model_name="OpenMed/OpenMed-PII-Dutch-SuperClinical-Large-434M-v1",
    use_smart_merging=True,
)

print([(e.label, e.text) for e in result.entities])
```

### Quick Start

```python
from transformers import pipeline

# Load the PII detection pipeline
ner = pipeline("ner", model="OpenMed/OpenMed-PII-Dutch-SuperClinical-Large-434M-v1", aggregation_strategy="simple")

text = """
Patiënt Jan Jansen (geboren 15-03-1985, BSN: 987654321) is vandaag gezien.
Contact: jan.jansen@email.nl, Telefoon: +31 6 12345678.
Adres: Herengracht 42, 1015 BN Amsterdam.
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

model_name = "OpenMed/OpenMed-PII-Dutch-SuperClinical-Large-434M-v1"
model = AutoModelForTokenClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

texts = [
    "Patiënt Jan Jansen (geboren 15-03-1985, BSN: 987654321) is vandaag gezien.",
    "Contact: jan.jansen@email.nl, Telefoon: +31 6 12345678.",
]

inputs = tokenizer(texts, return_tensors='pt', padding=True, truncation=True)
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=-1)
```

## Training Details

### Dataset

- **Source**: [AI4Privacy PII Masking 400k](https://huggingface.co/datasets/ai4privacy/pii-masking-400k) (Dutch subset)
- **Format**: BIO-tagged token classification
- **Labels**: 76 total (54 B-tags + 21 I-tags + O)

### Training Configuration

- **Max Sequence Length**: 512 tokens
- **Epochs**: 3
- **Framework**: Hugging Face Transformers + Trainer API

## Intended Use & Limitations

### Intended Use

- **De-identification**: Automated redaction of PII in Dutch clinical notes, medical records, and documents
- **Compliance**: Supporting GDPR, and other privacy regulation compliance
- **Data Preprocessing**: Preparing datasets for research by removing sensitive information
- **Audit Support**: Identifying PII in document collections

### Limitations

**Important**: This model is intended as an **assistive tool**, not a replacement for human review.

- **False Negatives**: Some PII may not be detected; always verify critical applications
- **Context Sensitivity**: Performance may vary with domain-specific terminology
- **Language**: Optimized for Dutch text; may not perform well on other languages

## Citation

```bibtex
@misc{openmed-pii-2026,
  title = {OpenMed-PII-Dutch-SuperClinical-Large-434M-v1: Dutch PII Detection Model},
  author = {OpenMed Science},
  year = {2026},
  publisher = {Hugging Face},
  url = {https://huggingface.co/OpenMed/OpenMed-PII-Dutch-SuperClinical-Large-434M-v1}
}
```

## Links

- **Organization**: [OpenMed](https://huggingface.co/OpenMed)
