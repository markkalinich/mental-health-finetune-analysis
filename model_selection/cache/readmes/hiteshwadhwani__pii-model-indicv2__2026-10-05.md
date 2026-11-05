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
base_model: ai4bharat/IndicBERTv2-MLM-only
pipeline_tag: token-classification
metrics:
  - f1
  - precision
  - recall
model-index:
  - name: pii-model-indicv2
    results:
      - task:
          type: token-classification
          name: Named Entity Recognition
        metrics:
          - name: F1
            type: f1
            value: 0.9497
          - name: Precision
            type: precision
            value: 0.9464
          - name: Recall
            type: recall
            value: 0.9530
---

# PII Detection Model — IndicBERTv2

A token classification model for detecting and redacting **Personally Identifiable Information (PII)** in English, Hindi, Hinglish, and Devanagari text.

Built on [ai4bharat/IndicBERTv2-MLM-only](https://huggingface.co/ai4bharat/IndicBERTv2-MLM-only) — a 278M parameter BERT model pretrained on 20.9B tokens across 24 Indian languages.

## Supported Languages
- **English** — names, addresses, phone numbers, SSN, etc.
- **Hindi (Devanagari)** — राजेश कुमार, मुंबई, बीस हज़ार रुपये, पंद्रह मार्च
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
| DATE | General date | पंद्रह मार्च, March fifteenth |
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
| AMOUNT | Money amount | 50000, बीस हज़ार रुपये |

## Usage

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

model = AutoModelForTokenClassification.from_pretrained("hiteshwadhwani/pii-model-indicv2")
tokenizer = AutoTokenizer.from_pretrained("hiteshwadhwani/pii-model-indicv2")

ner = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="first")

# English
results = ner("Mr John Smith lives at 456 Oak Avenue Boston")

# Hinglish
results = ner("Mera naam Rajesh Kumar hai aur main Mumbai mein rehta hoon")

# Hindi (Devanagari)
results = ner("मेरा नाम राजेश कुमार है और मैं मुंबई में रहता हूं")

# Hindi amounts and dates in words
results = ner("आपके क्रेडिट कार्ड के बीस हज़ार रूपये शुल्क लंबित हैं, जो पंद्रह मार्च को देना था।")

for entity in results:
    if entity["entity_group"] != "O":
        print(f"{entity['word']} → {entity['entity_group']} ({entity['score']:.2f})")
```

### Redaction Example

```python
def redact_pii(text, ner_pipeline, threshold=0.5):
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

print(redact_pii("आपके बीस हज़ार रूपये शुल्क लंबित हैं, जो पंद्रह मार्च को देना था।", ner))
# आपके [AMOUNT] शुल्क लंबित हैं, जो [DATE] को देना था।
```

## Evaluation Results

| Metric | Score |
|--------|-------|
| **Overall F1** | **0.9497** |
| Precision | 0.9464 |
| Recall | 0.9530 |

### Per-Entity F1

| Entity | F1 | Entity | F1 |
|--------|-----|--------|-----|
| FIRSTNAME | 0.99 | LASTNAME | 0.99 |
| CITY | 0.99 | STATE | 0.99 |
| PHONENUMBER | 0.98 | EMAIL | 0.93 |
| DOB | 0.96 | DATE | 0.95 |
| COMPANYNAME | 0.97 | PREFIX | 0.98 |
| CREDITCARDNUMBER | 0.95 | CREDITCARDISSUER | 0.95 |
| URL | 0.99 | USERNAME | 0.99 |
| MIDDLENAME | 1.00 | ACCOUNTNUMBER | 0.91 |
| PASSWORD | 0.91 | ZIPCODE | 0.95 |
| AMOUNT | 0.86 | STREET | 0.91 |

## Why IndicBERTv2?

| | indic-bert (v1) | IndicBERTv2 (this model) |
|---|---|---|
| Parameters | 32M | **278M** |
| Architecture | ALBERT (shared layers) | **BERT (unique layers)** |
| Languages | 12 | **24** |
| Training corpus | ~9B tokens | **20.9B tokens** |
| Devanagari names | Partial subword issues | **Clean detection** |
| Hindi amounts (बीस हज़ार) | Not detected | **Detected** |
| Hindi dates (पंद्रह मार्च) | Not detected | **Detected** |
| Unusual names (Viteshwar) | Broken subword alignment | **Clean detection** |

## Training Details

- **Base model**: ai4bharat/IndicBERTv2-MLM-only (278M params, 24 languages)
- **Task**: Token Classification (NER with BIO tagging)
- **Epochs**: 10
- **Learning rate**: 2e-5
- **Batch size**: 16
- **Optimizer**: AdamW

## Limitations

- SEX entity has low F1 — overlaps with GENDER
- SECONDARYADDRESS detection is weak
- Latency is higher than v1 (~25-40ms vs ~8ms) due to larger model size
- Best suited for Indian and US PII patterns

## License

Apache 2.0
