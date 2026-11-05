---
language:
- en
license: mit
tags:
- ner
- pii
- pci
- token-classification
- roberta
datasets:
- ai4privacy/pii-masking-200k
metrics:
- f1
model-index:
- name: roberta-pii-ner-en
  results:
  - task:
      type: token-classification
      name: Named Entity Recognition
    dataset:
      name: ai4privacy/pii-masking-200k
      type: ai4privacy/pii-masking-200k
    metrics:
    - type: f1
      value: 0.95
      name: Micro F1
---

# roberta-pii-ner-en

Fine-tuned [roberta-base](https://huggingface.co/roberta-base) for detecting Personally Identifiable Information (PII) and Payment Card Industry (PCI) data in English text.

**GitHub:** [rakmohan/pii-ner-en](https://github.com/rakmohan/pii-ner-en)

## Model Performance

| Metric | Score |
|--------|-------|
| Micro avg F1 | **0.95** |
| Macro avg F1 | 0.94 |
| Weighted avg F1 | 0.95 |

Per-entity metrics are available in `classification_report.txt`.

## Usage

```python
from transformers import pipeline

ner = pipeline(
    "token-classification",
    model="rm0013/roberta-pii-ner-en",
    aggregation_strategy="simple"
)

result = ner("Send the invoice to john.smith@acme.com, card 4111-1111-1111-1111 CVV 123.")
for entity in result:
    print(f"{entity['word']:30s} → {entity['entity_group']} ({entity['score']:.2f})")
```

## Supported Entities (54 types)

**PII:** `PERSON_NAME` `EMAIL` `PHONE_NUMBER` `SSN` `ADDRESS` `SECONDARYADDRESS` `DATE_OF_BIRTH` `DATE` `TIME` `AGE` `GENDER` `USERNAME` `PASSWORD` `IP_ADDRESS` `URL` `API_KEY` `PASSPORT_NUMBER` `DRIVER_LICENSE` `ORGANIZATION` `COMPANYNAME` `ACCOUNTNAME` `JOBAREA` `JOBTITLE` `JOBTYPE` `HEIGHT` `EYECOLOR` `ORDINALDIRECTION` `GPS_COORDINATES` `NEARBYGPSCOORDINATE` `USERAGENT` `DEVICE_ID` `VEHICLE_ID` `VEHICLEVIN` `VEHICLEVRM` `PHONEIMEI`

**PCI / Financial:** `CREDIT_CARD` `CREDIT_CARD_CVV` `CREDIT_CARD_EXPIRY` `PIN` `BANK_ACCOUNT` `BANK_ROUTING` `BIC` `AMOUNT` `CURRENCY` `CURRENCYCODE` `CURRENCYNAME` `CURRENCYSYMBOL` `MASKEDNUMBER` `BITCOINADDRESS` `ETHEREUMADDRESS` `LITECOINADDRESS`

## Training Data

1. [ai4privacy/pii-masking-200k](https://huggingface.co/datasets/ai4privacy/pii-masking-200k) — 200k annotated PII examples
2. Synthetic PCI data generated with [Faker](https://faker.readthedocs.io/) for rare entities (CVV, PIN, routing numbers)

## Training Details

| Parameter | Value |
|-----------|-------|
| Base model | roberta-base |
| Epochs | 10 (early stopping patience 3) |
| Batch size | 32 |
| Learning rate | 2e-5 |
| Max sequence length | 256 |
| Mixed precision | FP16 |

## Limitations

- English text only
- Performance varies by entity type — currency-related entities (CURRENCY, CURRENCYNAME) have lower accuracy due to limited training signal
- Not tested on non-standard text formats (code, structured data)

## License

MIT
