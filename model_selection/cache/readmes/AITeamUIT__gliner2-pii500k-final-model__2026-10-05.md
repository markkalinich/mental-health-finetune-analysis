---
language:
  - en
  - de
  - vi
license: apache-2.0
library_name: gliner2
tags:
  - ner
  - pii
  - information-extraction
  - gliner
datasets:
  - quynong/ontonotes5
---

# gliner2-pii500k-final-model

Fine-tuned [GLiNER2](https://github.com/jackboyla/GLiNER2) for **PII (Personally Identifiable Information)** extraction.  
**Model type:** `extractor`

- **44 entity types** across 8 PII taxonomy groups
- **Languages:** English · German · Vietnamese
- **Uploaded:** 2026-07-20

## Entity Labels

| Group | Labels |
|-------|--------|
| **Identity** | `PREFIX` · `PERSON` · `GENDER` · `AGE` · `BIRTHDATE` |
| **Contact & Location** | `PHONE` · `EMAIL` · `LOCATION` · `ADDRESS` · `ZIP_CODE` · `COORDINATE` |
| **Digital & Network** | `USERNAME` · `ACCOUNT_ID` · `TICKET_ID` · `PASSWORD` · `PIN` · `API_KEY` · `URL` · `IP` |
| **Financial** | `BANK_ACCOUNT` · `MONEY` · `CARD_ISSUER` · `CARD_NUMBER` · `CVV` · `IBAN` · `SWIFT` · `WALLET` |
| **Employment** | `JOB_TITLE` · `ORGANIZATION` · `EMPLOYEE_ID` |
| **Government & Legal** | `NATIONAL_ID` · `PASSPORT` · `LICENSE` · `PLATE` · `TIN` |
| **Time** | `DATE` · `TIME` |
| **Sensitive** | `MARITAL` · `RELIGION` · `ETHNICITY` · `TRADE_UNION` · `NATIONALITY` · `INSURANCE_ID` · `MEDICAL_INFO` |

## Training Configuration

| Parameter | Value |
|-----------|-------|
| Epochs | 6 |
| Batch size | 16 |
| Encoder LR | 1e-05 |
| Task LR | 0.0005 |
| Max seq len | 2048 |
| Precision | fp16 |

## Usage

```python
from gliner2 import GLiNER2

model = GLiNER2.from_pretrained("AITeamUIT/gliner2-pii500k-final-model")

text = "Please contact John Doe at john.doe@example.com or call +1-555-234-5678."
labels = ['PERSON', 'DATE', 'JOB_TITLE', 'TIME', 'LOCATION', 'PREFIX', 'ORGANIZATION', 'EMAIL', 'PHONE', 'ADDRESS', 'GENDER', 'COORDINATE', 'MONEY', 'IP', 'ZIP_CODE', 'NATIONALITY', 'AGE', 'USERNAME', 'URL', 'MARITAL', 'TRADE_UNION', 'BIRTHDATE', 'CARD_ISSUER', 'PIN', 'PASSPORT', 'MEDICAL_INFO', 'IBAN', 'PASSWORD', 'ETHNICITY', 'RELIGION', 'EMPLOYEE_ID', 'INSURANCE_ID', 'TIN', 'SWIFT', 'CARD_NUMBER', 'ACCOUNT_ID', 'WALLET', 'NATIONAL_ID', 'CVV', 'BANK_ACCOUNT', 'LICENSE', 'TICKET_ID', 'PLATE', 'API_KEY']
label_descriptions = {'PERSON': 'Person names', 'DATE': 'Calendar dates', 'JOB_TITLE': 'Job titles', 'TIME': 'Time values', 'LOCATION': 'General locations', 'PREFIX': 'Titles before names', 'ORGANIZATION': 'Organization names', 'EMAIL': 'Email addresses', 'PHONE': 'Phone numbers', 'ADDRESS': 'Street addresses', 'GENDER': 'Sex or gender', 'COORDINATE': 'Geographic coordinates', 'MONEY': 'Monetary amounts', 'IP': 'IP addresses', 'ZIP_CODE': 'Postal or ZIP codes', 'NATIONALITY': 'Legal nationality', 'AGE': 'Age values', 'USERNAME': 'Usernames or handles', 'URL': 'Web links or URLs', 'MARITAL': 'Marital status', 'TRADE_UNION': 'Trade union membership', 'BIRTHDATE': 'Date of birth', 'CARD_ISSUER': 'Card brands or issuers', 'PIN': 'Authentication PINs', 'PASSPORT': 'Passport numbers', 'MEDICAL_INFO': 'Health or medical information', 'IBAN': 'International bank account numbers', 'PASSWORD': 'Account passwords', 'ETHNICITY': 'Ethnic or racial group', 'RELIGION': 'Religious affiliation', 'EMPLOYEE_ID': 'Employee identifiers', 'INSURANCE_ID': 'Insurance identifiers', 'TIN': 'Tax identification numbers', 'SWIFT': 'Bank SWIFT or BIC codes', 'CARD_NUMBER': 'Payment card numbers', 'ACCOUNT_ID': 'Account identifiers', 'WALLET': 'Crypto wallet addresses', 'NATIONAL_ID': 'National ID numbers', 'CVV': 'Card security codes', 'BANK_ACCOUNT': 'Bank account numbers', 'LICENSE': 'Driver license numbers', 'TICKET_ID': 'Support or case IDs', 'PLATE': 'Vehicle plate numbers', 'API_KEY': 'API keys or tokens'}

entities = model.extract(text, labels=labels, label_descriptions=label_descriptions, threshold=0.5)
for ent in entities:
    print(ent)
```

## Limitations

- Span boundaries may be imperfect for entities crossing chunking boundaries.
- High-precision structured fields (EMAIL, PHONE, IBAN, etc.) benefit from the
  bundled regex rule-detector as a gap-filler.
