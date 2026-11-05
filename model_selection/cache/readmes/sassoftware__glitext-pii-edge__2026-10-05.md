---
license: apache-2.0
datasets:
- urchade/synthetic-pii-ner-mistral-v1
language:
- en
- fr
- de
- es
- pt
- it
tags:
- gliner
- ner
- pii
- glitext
pipeline_tag: token-classification
library_name: glitext
glitext:
  name: pii-edge
  label: GliText PII Recognition (Fast)
  description: An efficient zero-shot named entity recognition model tuned for PII
    extraction with high throughput (speed).
  recognition: true
  classification: false
  association: false
  span_mode: true
  size_gb: 0.62
  hf_repo: sassoftware/glitext-pii-edge
  source_url: vicgalle/gliner-small-pii
---

# GLiNER-small-PII

This model has been trained by fine-tuning gliner-community/gliner_small-v2.5 on the urchade/synthetic-pii-ner-mistral-v1 dataset.

This model is capable of recognizing various types of personally identifiable information (PII), including but not limited to these entity types: person, organization, phone number, address, passport number, email, credit card number, social security number, health insurance id number, date of birth, mobile phone number, bank account number, medication, cpf, driver's license number, tax identification number, medical condition, identity card number, national id number, ip address, email address, iban, credit card expiration date, username, health insurance number, registration number, student id number, insurance number, flight number, landline phone number, blood type, cvv, reservation number, digital signature, social media handle, license plate number, cnpj, postal code, passport_number, serial number, vehicle registration number, credit card brand, fax number, visa number, insurance company, identity document number, transaction number, national health insurance number, cvc, birth certificate number, train ticket number, passport expiration date, and social_security_number.

## Usage

```python
model = GLiNER.from_pretrained("vicgalle/gliner-small-pii", load_tokenizer=True)

text = """
Harilala Rasoanaivo, un homme d'affaires local d'Antananarivo, a enregistré une nouvelle société nommée "Rasoanaivo Enterprises" au Lot II M 92 Antohomadinika. Son numéro est le +261 32 22 345 67, et son adresse électronique est harilala.rasoanaivo@telma.mg. Il a fourni son numéro de sécu 501-02-1234 pour l'enregistrement.
"""

labels = [
    "work",
    "booking number",
    "personally identifiable information",
    "driver licence",
    "person",
    "book",
    "postal address",
    "company",
    "actor",
    "character",
    "email",
    "passport number",
    "SSN",
    "phone number",
]
entities = model.predict_entities(text, labels, threshold=0.1)

for entity in entities:
    print(entity["text"], "=>", entity["label"])
```

```
Harilala Rasoanaivo => person
Rasoanaivo Enterprises => company
Lot II M 92 Antohomadinika => postal address
+261 32 22 345 67 => phone number
harilala.rasoanaivo@telma.mg => email
501-02-1234 => SSN
```

**Note**: it may be beneficial to lower the threshold (see the previous example), to extract all related entities.

## Source Model Repo

This model is derived from [`vicgalle/gliner-small-pii`](https://huggingface.co/vicgalle/gliner-small-pii). See the upstream repository for the original safetensors weights, training data, and the full upstream model card.

## ONNX Weights

ONNX weights added by SAS — converted from the upstream safetensors checkpoint.

File in this repo: `model.onnx`.

## Using this Model with the SAS GLiText API

This repo is consumed by the SAS GLiText product. To download it onto a SAS GLiText server:

```
POST /v1/models/download?name=pii-edge
```

To download and load into memory in one step:

```
PUT /v1/models?name=pii-edge
```

## Security Scan

Scanned with [modelaudit](https://github.com/promptfoo/modelaudit) v0.2.40 on 2026-04-27. 24/24 checks passed. [Full results](modelaudit.json).


| File | Size | SHA-256 |
|------|------|---------|
| `model.onnx` | 664.8 MB | `396edfc891b876b0…` |
