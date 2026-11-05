---
language:
- fr
license: mit
tags:
- token-classification
- ner
- pii
- privacy
- french
- camembert
pipeline_tag: token-classification
base_model: almanach/camembert-base
datasets:
- ai4privacy/pii-masking-200k
metrics:
- f1
- precision
- recall
---

# CamemBERT French PII NER

A fine-tuned [CamemBERT](https://huggingface.co/almanach/camembert-base) model for **French PII (personally identifiable information) detection**, trained to identify 56 entity types for document anonymization / redaction.

## Model description

- **Base model:** `almanach/camembert-base` (RoBERTa-style, French, 111M params)
- **Task:** token classification (BIO NER)
- **Labels:** 56 entity types → 113 BIO labels
- **Language:** French

## Label taxonomy (56 entity types)

| Group | Entity types |
|---|---|
| Names | `FIRSTNAME`, `LASTNAME`, `MIDDLENAME`, `PREFIX`, `USERNAME` |
| Contact | `EMAIL`, `PHONENUMBER`, `PHONEIMEI`, `URL`, `IP`, `IPV4`, `IPV6`, `MAC`, `USERAGENT` |
| Address | `STREET`, `CITY`, `STATE`, `ZIPCODE`, `BUILDINGNUMBER`, `COUNTY`, `SECONDARYADDRESS`, `NEARBYGPSCOORDINATE`, `ORDINALDIRECTION` |
| IDs & numbers | `ACCOUNTNUMBER`, `ACCOUNTNAME`, `IBAN`, `SSN`, `CREDITCARDNUMBER`, `CREDITCARDCVV`, `CREDITCARDISSUER`, `VEHICLEVIN`, `VEHICLEVRM`, `BIC`, `MASKEDNUMBER`, `PIN` |
| Dates | `DATE`, `DOB`, `TIME` |
| Crypto | `BITCOINADDRESS`, `ETHEREUMADDRESS`, `LITECOINADDRESS` |
| Personal attributes | `AGE`, `GENDER`, `SEX`, `EYECOLOR`, `HEIGHT`, `JOBTITLE`, `JOBAREA`, `JOBTYPE`, `COMPANYNAME` |
| Other | `PASSWORD`, `AMOUNT`, `CURRENCY`, `CURRENCYCODE`, `CURRENCYNAME`, `CURRENCYSYMBOL` |

## Training

- **Dataset:** French subset of [`ai4privacy/pii-masking-200k`](https://huggingface.co/datasets/ai4privacy/pii-masking-200k) (61,958 examples)
- **Hyperparameters:** 3 epochs, batch size 16 (gradient accumulation 2), learning rate 5e-5, max sequence length 128, weight decay 0.01
- **Hardware:** single NVIDIA A10G

## Evaluation

**Held-out split (same distribution, synthetic):** F1 0.94, precision 0.94, recall 0.95

**Out-of-distribution — [`TheoDB/french-pii-eval`](https://huggingface.co/datasets/TheoDB/french-pii-eval)** (8-class taxonomy, span-level exact match):

| Metric | Value |
|---|---|
| Precision | 0.51 |
| Recall | 0.87 |
| **F1** | **0.65** |

Per-class F1: `private_email` 0.93, `private_date` 0.82, `private_phone` 0.76, `private_address` 0.72, `account_number` 0.68, `private_person` 0.63, `private_url` 0.37, `secret` 0.33.

> Note: the model favors **recall over precision** (over-detects PII), which is the safer direction for anonymization — better to over-redact than leak PII.

## Usage

```python
from transformers import pipeline

nlp = pipeline("token-classification", model="Spyridon/camembert-base-pii-fr",
               aggregation_strategy="simple")
nlp("Contactez Jean Dupont au 06 12 34 56 78 ou jean.dupont@email.fr")
```

For PDF redaction, see the companion pipeline that maps detected spans back to PDF word boxes and applies redaction annotations.
