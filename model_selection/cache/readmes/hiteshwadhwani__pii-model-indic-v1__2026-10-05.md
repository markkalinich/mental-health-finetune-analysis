---
language:
  - en
  - hi
license: apache-2.0
tags:
  - token-classification
  - ner
  - pii
  - indian-languages
  - hindi
  - devanagari
  - hinglish
  - privacy
datasets:
  - custom
base_model: ai4bharat/indic-bert
pipeline_tag: token-classification
metrics:
  - f1
  - precision
  - recall
model-index:
  - name: pii-model-indic-v1
    results:
      - task:
          type: token-classification
          name: Named Entity Recognition
        metrics:
          - name: F1
            type: f1
            value: 0.9649
          - name: Precision
            type: precision
            value: 0.9614
          - name: Recall
            type: recall
            value: 0.9685
---

# PII Detection Model (Indian + US) — IndicBERT

A token classification model for detecting and redacting **Personally Identifiable Information (PII)** in English, Hindi, Hinglish, and Devanagari text.

Built on top of [ai4bharat/indic-bert](https://huggingface.co/ai4bharat/indic-bert) — a multilingual ALBERT model pretrained on 12 Indian languages.

## Supported Languages
- **English** — names, addresses, phone numbers, SSN, etc.
- **Hindi (Devanagari)** — राजेश कुमार, मुंबई, महाराष्ट्र, etc.
- **Hinglish** — "Mera naam Rajesh hai aur main Mumbai mein rehta hoon"
- **Mixed Devanagari + English** — "मेरा phone number 9876543210 है"

## Entity Types (31)

| Entity | Description | Example |
|--------|-------------|---------|
| FIRSTNAME | First name | Rajesh, राजेश, John |
| LASTNAME | Last name | Kumar, कुमार, Smith |
| MIDDLENAME | Middle name | Kumar |
| PREFIX | Title/prefix | Mr, श्री, Dr, श्रीमती |
| GENDER | Gender | male, female |
| SEX | Sex | M, F |
| AGE | Age | 35 |
| DOB | Date of birth | 15/03/1990 |
| DATE | General date | 14/03/2026 |
| EMAIL | Email address | priya@gmail.com |
| PHONENUMBER | Phone number | +91 98765 43210 |
| CITY | City | Mumbai, मुंबई, Boston |
| STATE | State | Maharashtra, महाराष्ट्र |
| COUNTY | County | Cook County |
| ZIPCODE | ZIP/PIN code | 400001, 02101 |
| STREET | Street name | MG Road, Oak Avenue |
| BUILDINGNUMBER | Building number | 42 |
| SECONDARYADDRESS | Apt/Suite | Flat 301 |
| COMPANYNAME | Company | Infosys, टाटा कंसल्टेंसी |
| ACCOUNTNUMBER | Account number | 9876543210 |
| ACCOUNTNAME | Account name | Tata Consultancy |
| CREDITCARDNUMBER | Credit card | 4111-1111-1111-1111 |
| CREDITCARDCVV | CVV | 123 |
| CREDITCARDISSUER | Card issuer | Visa, HDFC |
| SSN | SSN/PAN/Aadhaar | 123-45-6789, ABCDE1234F |
| IBAN | IBAN | IN89UTIB00001234567890 |
| PIN | ATM/Security PIN | 4098 |
| PASSWORD | Password | S3cur3P@ss! |
| USERNAME | Username | mdavis |
| URL | URL | www.example.com |
| AMOUNT | Money amount | 50000 |

## Usage

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

model = AutoModelForTokenClassification.from_pretrained("hiteshwadhwani/pii-model-indic-v1")
tokenizer = AutoTokenizer.from_pretrained("hiteshwadhwani/pii-model-indic-v1")

ner = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="first")

# English
results = ner("Mr John Smith lives at 456 Oak Avenue Boston")

# Hinglish
results = ner("Mera naam Rajesh Kumar hai aur main Mumbai mein rehta hoon")

# Hindi (Devanagari)
results = ner("कृपया प्रिया शर्मा को +91 98765 43210 पर call करें")

# Devanagari names
results = ner("राजेश कुमार का account number 1234567890 है")

for entity in results:
    print(f"{entity['word']} → {entity['entity_group']} ({entity['score']:.2f})")
```

### Redaction Example

```python
def redact_pii(text, ner_pipeline, threshold=0.85):
    results = ner_pipeline(text)
    entities = [r for r in results if r["score"] >= threshold and r["entity_group"] != "O"]
    entities.sort(key=lambda x: x["start"])

    merged = []
    for ent in entities:
        label = ent["entity_group"]
        if merged and merged[-1]["label"] == label and ent["start"] <= merged[-1]["end"] + 1:
            merged[-1]["end"] = max(merged[-1]["end"], ent["end"])
        else:
            merged.append({"label": label, "start": ent["start"], "end": ent["end"]})

    redacted = text
    for span in reversed(merged):
        redacted = redacted[:span["start"]] + f"[{span['label']}]" + redacted[span["end"]:]
    return redacted

print(redact_pii("Shri Rajesh Kumar lives at 42 MG Road Bengaluru Karnataka", ner))
# [PREFIX] [FIRSTNAME] [LASTNAME] lives at [BUILDINGNUMBER] [STREET] [CITY] [STATE]
```

## Evaluation Results

| Metric | Score |
|--------|-------|
| **Overall F1** | **0.9623** |
| Precision | 0.9595 |
| Recall | 0.9651 |
| Latency (avg) | 8.2ms |

### Per-Entity F1

| Entity | F1 | Entity | F1 |
|--------|-----|--------|-----|
| FIRSTNAME | 0.975 | LASTNAME | 0.979 |
| CITY | 0.992 | STATE | 0.985 |
| PHONENUMBER | 0.984 | EMAIL | 0.991 |
| DOB | 0.978 | DATE | 0.976 |
| SSN | 0.928 | COMPANYNAME | 0.933 |
| CREDITCARDNUMBER | 0.926 | PREFIX | 0.989 |
| URL | 1.000 | IBAN | 0.957 |
| AGE | 0.985 | USERNAME | 0.939 |
| PASSWORD | 0.977 | ZIPCODE | 0.914 |
| AMOUNT | 0.793 | STREET | 0.927 |

## Training Details

- **Base model**: ai4bharat/indic-bert (ALBERT, 12 Indian languages)
- **Training data**: ~11,800 synthetic samples
  - English (Indian + US PII): ~4,700 samples
  - Hinglish (Roman script): ~1,000 samples
  - Devanagari + English mix: ~1,000 samples
  - Pure Devanagari: ~5,000 samples
  - Negative samples (no PII): ~3,000 samples
- **Epochs**: 15
- **Learning rate**: 3e-5
- **Batch size**: 32
- **Optimizer**: AdamW

## License

Apache 2.0
