---
language:
  - pt
license: apache-2.0
base_model: distilbert/distilbert-base-cased
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
  - portuguese
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
  - name: OpenMed-PII-Portuguese-LiteClinical-Base-66M-v1
    results:
      - task:
          type: token-classification
          name: Named Entity Recognition
        dataset:
          name: AI4Privacy + Synthetic Portuguese PII
          type: ai4privacy/pii-masking-200k
          split: test
        metrics:
          - type: f1
            value: 0.8827
            name: F1 (micro)
          - type: precision
            value: 0.8860
            name: Precision
          - type: recall
            value: 0.8795
            name: Recall
widget:
  - text: "Dr. Pedro Almeida (CPF: 123.456.789-00) pode ser contatado em pedro.almeida@hospital.pt ou +351 912 345 678. Endereço: Rua das Flores 25, 1200-195 Lisboa."
    example_title: Clinical Note with PII (Portuguese)
---

# OpenMed-PII-Portuguese-LiteClinical-Base-66M-v1

**Portuguese PII Detection Model** | 66M Parameters | Open Source

[![F1 Score](https://img.shields.io/badge/F1-88.27%25-brightgreen)]() [![Precision](https://img.shields.io/badge/Precision-88.60%25-blue)]() [![Recall](https://img.shields.io/badge/Recall-87.95%25-orange)]()

## Model Description

**OpenMed-PII-Portuguese-LiteClinical-Base-66M-v1** is a transformer-based token classification model fine-tuned for **Personally Identifiable Information (PII) detection in Portuguese text**. This model identifies and classifies **54 types of sensitive information** including names, addresses, social security numbers, medical record numbers, and more.

### Key Features

- **Portuguese-Optimized**: Specifically trained on Portuguese text for optimal performance
- **High Accuracy**: Achieves strong F1 scores across diverse PII categories
- **Comprehensive Coverage**: Detects 55+ entity types spanning personal, financial, medical, and contact information
- **Privacy-Focused**: Designed for de-identification and compliance with GDPR and other privacy regulations
- **Production-Ready**: Optimized for real-world text processing pipelines

## Performance

Evaluated on the Portuguese test split (AI4Privacy + synthetic data):

| Metric | Score |
|:---|:---:|
| **Micro F1** | **0.8827** |
| Precision | 0.8860 |
| Recall | 0.8795 |
| Macro F1 | 0.5211 |
| Weighted F1 | 0.8730 |
| Accuracy | 0.9330 |

### Top 10 Portuguese PII Models

| Rank | Model | F1 | Precision | Recall |
|:---:|:---|:---:|:---:|:---:|
| 1 | [OpenMed-PII-Portuguese-SnowflakeMed-Large-568M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Portuguese-SnowflakeMed-Large-568M-v1) | 0.8921 | 0.8914 | 0.8928 |
| 2 | [OpenMed-PII-Portuguese-ClinicalBGE-568M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Portuguese-ClinicalBGE-568M-v1) | 0.8905 | 0.8896 | 0.8913 |
| 3 | [OpenMed-PII-Portuguese-NomicMed-Large-395M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Portuguese-NomicMed-Large-395M-v1) | 0.8896 | 0.8927 | 0.8866 |
| 4 | [OpenMed-PII-Portuguese-SuperMedical-Large-355M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Portuguese-SuperMedical-Large-355M-v1) | 0.8889 | 0.8891 | 0.8887 |
| 5 | [OpenMed-PII-Portuguese-SuperClinical-Large-434M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Portuguese-SuperClinical-Large-434M-v1) | 0.8889 | 0.8830 | 0.8948 |
| 6 | [OpenMed-PII-Portuguese-BioClinicalModern-Large-395M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Portuguese-BioClinicalModern-Large-395M-v1) | 0.8871 | 0.8906 | 0.8836 |
| 7 | [OpenMed-PII-Portuguese-mSuperClinical-Base-279M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Portuguese-mSuperClinical-Base-279M-v1) | 0.8865 | 0.8796 | 0.8934 |
| 8 | [OpenMed-PII-Portuguese-mLiteClinical-135M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Portuguese-mLiteClinical-135M-v1) | 0.8862 | 0.8888 | 0.8837 |
| 9 | [OpenMed-PII-Portuguese-SuperMedical-Base-125M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Portuguese-SuperMedical-Base-125M-v1) | 0.8856 | 0.8844 | 0.8868 |
| 10 | [OpenMed-PII-Portuguese-ModernMed-Large-395M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Portuguese-ModernMed-Large-395M-v1) | 0.8856 | 0.8987 | 0.8728 |

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
ner = pipeline("ner", model="OpenMed/OpenMed-PII-Portuguese-LiteClinical-Base-66M-v1", aggregation_strategy="simple")

text = """
Paciente Carlos Mendes (nascido em 15/03/1985, CPF: 987.654.321-00) foi atendido hoje.
Contato: carlos.mendes@email.pt, Telefone: +351 912 345 678.
Endereço: Avenida da Liberdade 42, 1250-096 Lisboa.
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

model_name = "OpenMed/OpenMed-PII-Portuguese-LiteClinical-Base-66M-v1"
model = AutoModelForTokenClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

texts = [
    "Paciente Carlos Mendes (nascido em 15/03/1985, CPF: 987.654.321-00) foi atendido hoje.",
    "Contato: carlos.mendes@email.pt, Telefone: +351 912 345 678.",
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
- **Synthetic Portuguese Data**: ~80K high-quality samples generated with locale-specific formatting (CPF format, +55 phones, Brazilian names, R$ currency)

- **Format**: BIO-tagged token classification
- **Labels**: 76 BIO tags (54 entity types)

### Training Configuration

- **Max Sequence Length**: 512 tokens
- **Epochs**: 3
- **Framework**: Hugging Face Transformers + Trainer API

## Intended Use & Limitations

### Intended Use

- **De-identification**: Automated redaction of PII in Portuguese clinical notes, medical records, and documents
- **Compliance**: Supporting GDPR, and other privacy regulation compliance
- **Data Preprocessing**: Preparing datasets for research by removing sensitive information
- **Audit Support**: Identifying PII in document collections

### Limitations

**Important**: This model is intended as an **assistive tool**, not a replacement for human review.

- **False Negatives**: Some PII may not be detected; always verify critical applications
- **Context Sensitivity**: Performance may vary with domain-specific terminology
- **Language**: Optimized for Portuguese text; may not perform well on other languages

## Citation

```bibtex
@misc{openmed-pii-2026,
  title = {OpenMed-PII-Portuguese-LiteClinical-Base-66M-v1: Portuguese PII Detection Model},
  author = {OpenMed Science},
  year = {2026},
  publisher = {Hugging Face},
  url = {https://huggingface.co/OpenMed/OpenMed-PII-Portuguese-LiteClinical-Base-66M-v1}
}
```

## Links

- **Organization**: [OpenMed](https://huggingface.co/OpenMed)
