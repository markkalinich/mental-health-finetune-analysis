---
language: es
license: cc-by-4.0
base_model: kierandesmond/spanish-gdpr-pii-ner-v8
pipeline_tag: token-classification
library_name: transformers
tags:
- token-classification
- ner
- spanish
- gdpr
- pii
- privacy
- xlm-roberta
---

# Spanish GDPR PII NER — v9

Token-classification (NER) model that detects GDPR / LOPDGDD-regulated personal data in
Spanish text, including standard identifiers and **GDPR Art. 9 special-category** data
(health, genetic, biometric, ethnic, political, religious, union membership, sexual
orientation, criminal records).

- **Base model:** [`kierandesmond/spanish-gdpr-pii-ner-v8`](https://huggingface.co/kierandesmond/spanish-gdpr-pii-ner-v8) (continued fine-tuning, NOT trained from scratch)
- **Architecture:** `XLMRobertaForTokenClassification` (xlm-roberta-base, ~277M params)
- **Labels:** 57 BIO tags / 28 entity types (schema identical to v6/v8 — preserved verbatim)
- **Max length:** 256

## What's new in v9

v9 was driven by a **large, statistically-meaningful held-out evaluation set** (7,304 examples,
200–336 per entity, with hard negatives) — replacing the tiny n=1–6 battery used for v6/v8 that
masked real weaknesses. Re-scoring v8 on this honest eval exposed gaps (e.g. SIP_CARD 0.5%,
ETHNIC_ORIGIN 40%, GENETIC_DATA 70%) that the old battery rated as 80–100%.

v9 adds targeted real + synthetic training data for the weak entities and hard negatives for the
false-positive traps, while preserving locked entities.

## Evaluation (large held-out eval set, span-level pass-rate)

| Metric | v8 | **v9** |
|---|---|---|
| **Macro positive pass-rate** (avg over 28 entities) | 87.3% | **99.55%** |
| **Macro negative pass-rate** (hard negatives + false-positive guards) | 76.6% | **100%** |
| Lowest single entity | 0.5% (SIP_CARD) | **94.6% (GENETIC_DATA)** |

**Every one of the 28 entity types scores ≥ 90%.** Biggest gains vs v8:
SIP_CARD 0.5%→100%, ETHNIC_ORIGIN 40%→100%, GENETIC_DATA 70%→94.6%, CREDIT_CARD 71%→100%,
BANK_ACCOUNT 80%→100%, POLITICAL_OPINION 81%→97.6%, UNION_MEMBERSHIP 82%→100%,
BIOMETRIC_DATA 82%→100%, USERNAME 85%→100%, SEXUAL_ORIENTATION 88%→100%, PERSON_NAME 90%→100%.
(One minor trade-off: HEALTH_DATA 99.4%→97.0%, still well above bar.)

Confusion guards are clean: SEXUAL_ORIENTATION↔RELIGIOUS_BELIEF = 0 confusion;
POLITICAL_OPINION↔UNION_MEMBERSHIP = 0 confusion.

Full per-entity numbers, comparison CSV, and confusion matrix:
[`kierandesmond/spanish-gdpr-pii-ner-v9-validation`](https://huggingface.co/datasets/kierandesmond/spanish-gdpr-pii-ner-v9-validation).

## Training data sources (v9)

Real corpora (parquet-native, no script execution):
- **HEALTH_DATA** — [`BSC-NLP4BIA/bsc-bio-distemist-ner`](https://huggingface.co/datasets/BSC-NLP4BIA/bsc-bio-distemist-ner) (ENFERMEDAD, train split)
- **GENETIC_DATA** — [`PlanTL-GOB-ES/pharmaconer`](https://huggingface.co/datasets/PlanTL-GOB-ES/pharmaconer) (PROTEINAS, train split)
- **Anchor / locked entities** (PERSON_NAME, ADDRESS_ES, DATE_OF_BIRTH, EMAIL, PHONE_ES, NUSS) — [`bigbio/meddocan`](https://huggingface.co/datasets/bigbio/meddocan) (char-offset → BIO, train split) for catastrophic-forgetting protection

Synthetic (special categories have no labeled Spanish corpus) — register-varied templates
(legal / informal / clinical), contrastive minimal pairs for confusion guards, hard negatives,
and regex-generated structured identifiers (DNI/NIE/NIF/CIF/IBAN/SIP/credit-card/etc.).
**Anti-leakage:** synthetic eval uses template families disjoint from training; real-corpus eval
uses validation/test splits never seen in training.

## Training configuration

- Continued from v8 weights; LR 1e-5, 3 epochs, effective batch 32 (16×2), warmup 0.1,
  weight_decay 0.01, bf16, max_length 256.
- Final token-level seqeval on held-out eval: precision 0.965, recall 0.976, **F1 0.971**.

## Entity types (28)

PERSON_NAME, EMAIL, PHONE_ES, ADDRESS_ES, DATE_OF_BIRTH, IP_ADDRESS, URL, USERNAME, DNI, NIE,
NIF, CIF, NUSS, IBAN_ES, SIP_CARD, PASSPORT_ES, VEHICLE_PLATE_ES, CREDIT_CARD, BANK_ACCOUNT,
HEALTH_DATA, GENETIC_DATA, BIOMETRIC_DATA, ETHNIC_ORIGIN, POLITICAL_OPINION, RELIGIOUS_BELIEF,
UNION_MEMBERSHIP, SEXUAL_ORIENTATION, CRIMINAL_RECORD.

## Usage

```python
from transformers import pipeline
ner = pipeline("token-classification", model="kierandesmond/spanish-gdpr-pii-ner-v9",
               aggregation_strategy="simple")
ner("El trabajador está afiliado a CCOO y fue diagnosticado de diabetes mellitus tipo 2 .")
```

## Limitations & honest caveats

- **Special-category recall partly depends on phrasing patterns.** Although v9 uses
  register-varied, template-family-disjoint synthetic data (so eval measures generalization,
  not memorization), production free-text will be more varied than any synthetic set. Treat
  special-category detection as **assistive** (flag-for-review), not fully autonomous redaction,
  until validated on real production documents.
- **No real labeled corpus exists for Art. 9 special categories in Spanish** — those entities are
  synthetic-trained, grounded in researched real-world phrasings.
- The eval set, while large (200–336/label), is built from public corpora + synthetic generation;
  a production-grade acceptance test would add human-labeled documents from the target domain.
- This model is a privacy/compliance aid and does not guarantee complete PII removal.
