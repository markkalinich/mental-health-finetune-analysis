---
language: ko
license: mit
library_name: transformers
pipeline_tag: token-classification
tags:
- token-classification
- ner
- pii
- korean
datasets:
- custom
widget:
- text: "제 이름은 홍길동이고 전화번호는 010-1234-5678입니다."
---

# Korean PII Masking Model

This model detects and masks personally identifiable information (PII) in Korean text.

## Supported PII Types
- PS_NAME: Person names
- QT_MOBILE/QT_PHONE: Phone numbers
- TMI_EMAIL: Email addresses
- QT_RESIDENT_NUMBER: Resident registration numbers
- QT_CARD_NUMBER: Card numbers

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    "token-classification",
    model="seungkukim/korean-pii-masking",
    aggregation_strategy="simple"
)

text = "제 이름은 홍길동이고 전화번호는 010-1234-5678입니다."
results = classifier(text)
print(results)
```
