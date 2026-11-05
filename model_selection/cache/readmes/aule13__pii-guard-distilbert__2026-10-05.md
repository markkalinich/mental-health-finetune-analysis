---
language: ["ru", "en"]
license: mit
library_name: transformers
tags:
  - pii
  - privacy
  - russian
  - token-classification
  - distilbert
  - 152-fz
metrics:
  - f1
  - precision
  - recall
---

# PII Guard DistilBERT

Fine-tuned DistilBERT-multilingual for Russian PII detection.
21 entity types in BIO format. F1=0.9938 on pii_benchmark.

## Usage

```python
from transformers import AutoModelForTokenClassification, AutoTokenizer
model = AutoModelForTokenClassification.from_pretrained("astralinux/pii-guard-distilbert")
tokenizer = AutoTokenizer.from_pretrained("astralinux/pii-guard-distilbert")
```

## Entity Types

| Tag | Description |
|---|---|
| B-FIRST_NAME | First name |
| B-LAST_NAME | Last name |
| B-MIDDLE_NAME | Middle name / patronymic |
| B-PHONE | Phone number |
| B-EMAIL | Email address |
| B-CITY | City |
| B-STREET | Street |
| B-HOUSE | House number |
| B-COUNTRY | Country |
| B-REGION | Region |
| B-DISTRICT | District |
| B-PASSPORT | Passport number |
| B-SNILS | SNILS |
| B-INN | INN (tax ID) |
| B-OMS | Medical insurance |
| B-CREDIT_CARD | Credit card / bank account |
| B-DRIVER_LICENSE | Driver license |
| B-MILITARY_ID | Military ID |
| B-BIRTH_CERTIFICATE | Birth certificate |
| B-URL | URL |
| B-IP_ADDRESS | IP address |

## Part of PII Guard

[github.com/astralinux/pii-guard](https://github.com/astralinux/pii-guard)

Designed for 152-ФЗ compliance. Self-hosted. No data leaves your perimeter.
