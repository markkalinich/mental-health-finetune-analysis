---
language:
  - zh
license: apache-2.0
base_model: lightonai/modernbert-embed-large
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
  - chinese
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
  - name: OpenMed-PII-Chinese-NomicMed-Large-395M-v1
    results:
      - task:
          type: token-classification
          name: Named Entity Recognition
        dataset:
          name: AI4Privacy + Synthetic Chinese PII
          type: ai4privacy/pii-masking-200k
          split: test
        metrics:
          - type: f1
            value: 0.7572
            name: F1 (micro)
          - type: precision
            value: 0.7641
            name: Precision
          - type: recall
            value: 0.7505
            name: Recall
widget:
  - text: "张医生（身份证号：110101198503151234）联系方式：zhang.yi@hospital.cn 或 +86 138 1234 5678。地址：北京市朝阳区建国路42号。"
    example_title: Clinical Note with PII (Chinese)
---

# OpenMed-PII-Chinese-NomicMed-Large-395M-v1

**Chinese PII Detection Model** | 395M Parameters | Open Source

[![F1 Score](https://img.shields.io/badge/F1-75.72%25-brightgreen)]() [![Precision](https://img.shields.io/badge/Precision-76.41%25-blue)]() [![Recall](https://img.shields.io/badge/Recall-75.05%25-orange)]()

## Model Description

**OpenMed-PII-Chinese-NomicMed-Large-395M-v1** is a transformer-based token classification model fine-tuned for **Personally Identifiable Information (PII) detection in Chinese text**. This model identifies and classifies **54 types of sensitive information** including names, addresses, social security numbers, medical record numbers, and more.

### Key Features

- **Chinese-Optimized**: Specifically trained on Chinese text for optimal performance
- **High Accuracy**: Achieves strong F1 scores across diverse PII categories
- **Comprehensive Coverage**: Detects 55+ entity types spanning personal, financial, medical, and contact information
- **Privacy-Focused**: Designed for de-identification and compliance with GDPR and other privacy regulations
- **Production-Ready**: Optimized for real-world text processing pipelines

## Performance

Evaluated on the Chinese test split (AI4Privacy + synthetic data):

| Metric | Score |
|:---|:---:|
| **Micro F1** | **0.7572** |
| Precision | 0.7641 |
| Recall | 0.7505 |
| Macro F1 | 0.4755 |
| Weighted F1 | 0.7476 |
| Accuracy | 0.8896 |

### Top 10 Chinese PII Models

| Rank | Model | F1 | Precision | Recall |
|:---:|:---|:---:|:---:|:---:|
| 1 | [OpenMed-PII-Chinese-SnowflakeMed-Large-568M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Chinese-SnowflakeMed-Large-568M-v1) | 0.7592 | 0.7662 | 0.7523 |
| 2 | [OpenMed-PII-Chinese-BigMed-Large-560M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Chinese-BigMed-Large-560M-v1) | 0.7589 | 0.7662 | 0.7517 |
| **3** | **[OpenMed-PII-Chinese-NomicMed-Large-395M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Chinese-NomicMed-Large-395M-v1)** | **0.7572** | **0.7641** | **0.7505** |
| 4 | [OpenMed-PII-Chinese-BioClinicalModern-Large-395M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Chinese-BioClinicalModern-Large-395M-v1) | 0.7543 | 0.7577 | 0.7508 |
| 5 | [OpenMed-PII-Chinese-ModernMed-Large-395M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Chinese-ModernMed-Large-395M-v1) | 0.7534 | 0.7589 | 0.7479 |
| 6 | [OpenMed-PII-Chinese-SuperClinical-Large-434M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Chinese-SuperClinical-Large-434M-v1) | 0.7531 | 0.7508 | 0.7554 |
| 7 | [OpenMed-PII-Chinese-ClinicalBGE-568M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Chinese-ClinicalBGE-568M-v1) | 0.7528 | 0.7553 | 0.7504 |
| 8 | [OpenMed-PII-Chinese-SuperClinical-Base-184M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Chinese-SuperClinical-Base-184M-v1) | 0.7449 | 0.7432 | 0.7465 |
| 9 | [OpenMed-PII-Chinese-mLiteClinical-135M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Chinese-mLiteClinical-135M-v1) | 0.7446 | 0.7498 | 0.7396 |
| 10 | [OpenMed-PII-Chinese-BioClinicalModern-Base-149M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Chinese-BioClinicalModern-Base-149M-v1) | 0.7442 | 0.7490 | 0.7395 |

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
ner = pipeline("ner", model="OpenMed/OpenMed-PII-Chinese-NomicMed-Large-395M-v1", aggregation_strategy="simple")

text = """
患者李明（出生日期：1985/03/15，身份证号：310101198503159876）今日就诊。
联系方式：li.ming@email.cn，电话：+86 138 1234 5678。
地址：上海市浦东新区陆家嘴路123号。
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

model_name = "OpenMed/OpenMed-PII-Chinese-NomicMed-Large-395M-v1"
model = AutoModelForTokenClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

texts = [
    "患者李明（出生日期：1985/03/15，身份证号：310101198503159876）今日就诊。",
    "联系方式：li.ming@email.cn，电话：+86 138 1234 5678。",
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
- **Synthetic Chinese Data**: ~25K high-quality samples generated with locale-specific formatting (身份证号 format, +86 phones, Chinese names, ¥ currency)

- **Format**: BIO-tagged token classification
- **Labels**: 76 BIO tags (54 entity types)

### Training Configuration

- **Max Sequence Length**: 512 tokens
- **Epochs**: 3
- **Framework**: Hugging Face Transformers + Trainer API

## Intended Use & Limitations

### Intended Use

- **De-identification**: Automated redaction of PII in Chinese clinical notes, medical records, and documents
- **Compliance**: Supporting GDPR, and other privacy regulation compliance
- **Data Preprocessing**: Preparing datasets for research by removing sensitive information
- **Audit Support**: Identifying PII in document collections

### Limitations

**Important**: This model is intended as an **assistive tool**, not a replacement for human review.

- **False Negatives**: Some PII may not be detected; always verify critical applications
- **Context Sensitivity**: Performance may vary with domain-specific terminology
- **Language**: Optimized for Chinese text; may not perform well on other languages

## Citation

```bibtex
@misc{openmed-pii-2026,
  title = {OpenMed-PII-Chinese-NomicMed-Large-395M-v1: Chinese PII Detection Model},
  author = {OpenMed Science},
  year = {2026},
  publisher = {Hugging Face},
  url = {https://huggingface.co/OpenMed/OpenMed-PII-Chinese-NomicMed-Large-395M-v1}
}
```

## Links

- **Organization**: [OpenMed](https://huggingface.co/OpenMed)
