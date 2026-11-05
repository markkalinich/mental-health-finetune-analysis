---
library_name: transformers
license: mit
base_model: microsoft/deberta-v3-base
tags:
- generated_from_trainer
- token-classification
- pii-detection
- indian-pii
---

# deberta-pii-owndlp

Fine-tuned DeBERTa-v3-base model for PII detection, with specific tuning for
Indian identifiers: Aadhaar, PAN, GSTIN, IFSC, and RuPay credit cards, along
with standard PII categories (names, emails, phone numbers, addresses, etc).

## Verified working on:
- Aadhaar numbers
- PAN numbers
- RuPay card numbers
- Person names, organizations, emails

Verified via manual sanity checks on real test sentences containing these
entity types, with confidence scores of 0.90+ across all categories.