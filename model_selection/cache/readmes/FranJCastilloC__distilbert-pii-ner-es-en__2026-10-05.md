---
language:
  - es
  - en
license: mit
library_name: transformers
pipeline_tag: token-classification
base_model: distilbert-base-multilingual-cased
tags:
  - pii
  - ner
  - privacy
  - redaction
  - token-classification
---

# DistilBERT multilingual — PII token classification (ES/EN)

Fine-tuned `distilbert-base-multilingual-cased` for detecting personally
identifiable information in Spanish and English business documents. It is the
learned component of the
[PII Detection & Redaction Pipeline](https://github.com/FranJCastilloC/PII-Detection-Redaction-Pipeline),
where it is combined with a checksum-backed rule engine and Presidio.

## Entity types

10 BIO classes: `PERSON`, `EMAIL`, `PHONE`, `ADDRESS`, `DATE_OF_BIRTH`,
`GOV_ID`, `USERNAME`, `CREDENTIAL`, `IP_ADDRESS`, `DATE_TIME`.

**`CREDIT_CARD` and `BANK_ACCOUNT` are deliberately absent.** The training
corpus annotates a card *issuer* but contains no card numbers and no bank
account numbers at all, so the model cannot learn them. In the parent pipeline
those two classes are handled by the rule engine, where Luhn and the IBAN
mod-97 checksum are arithmetic proofs rather than estimates.

## Results

Validation (seqeval, entity level, 2,000 held-out samples):

| | Precision | Recall | F1 |
|---|---|---|---|
| **micro** | 0.9236 | 0.9468 | **0.9350** |

| Entity | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| `EMAIL` | 0.976 | 0.991 | 0.984 | 669 |
| `GOV_ID` | 0.943 | 0.973 | 0.958 | 2536 |
| `ADDRESS` | 0.954 | 0.941 | 0.948 | 2864 |
| `PHONE` | 0.927 | 0.945 | 0.936 | 526 |
| `PERSON` | 0.887 | 0.953 | 0.919 | 1338 |
| `USERNAME` | 0.928 | 0.909 | 0.918 | 680 |
| `DATE_TIME` | 0.897 | 0.940 | 0.918 | 1450 |
| `DATE_OF_BIRTH` | 0.900 | 0.933 | 0.916 | 510 |
| `IP_ADDRESS` | 0.885 | 0.935 | 0.909 | 585 |
| `CREDENTIAL` | 0.809 | 0.851 | 0.830 | 403 |

On **complete business documents** (out-of-distribution, 250 synthetic invoices,
contracts, emails, tickets and forms) F1 drops to **0.651**, while the
rule baseline reaches 0.712 and the full ensemble 0.765. Formal
documents carry explicit field labels (`Phone:`, `Name:`) that regexes handle
well and that the sentence-level training corpus never contained. Use this model
as one component of an ensemble, not on its own.

## Usage

```python
from transformers import AutoModelForTokenClassification, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("FranJCastilloC/distilbert-pii-ner-es-en")
model = AutoModelForTokenClassification.from_pretrained("FranJCastilloC/distilbert-pii-ner-es-en")
```

For span decoding, sliding windows over long documents, per-span confidence and
redaction, use the pipeline in the linked repository.

## Training data

[`ai4privacy/pii-masking-300k`](https://huggingface.co/datasets/ai4privacy/pii-masking-300k),
filtered to English and Spanish. The corpus is fully synthetic: **no real
person's data was used at any point.** Character offsets were re-aligned to this
model's own tokenisation rather than reusing the corpus's precomputed BIO tags.

Config: 15,057 training windows, batch
16, lr 5e-05,
max length 192, 1 epoch.

## Limitations

- Spanish and English only.
- Trained on synthetic sentences; real documents bring OCR noise, abbreviations
  and inconsistent layout that this evaluation does not capture.
- Degrades on document-style input relative to sentence-style input (see above).
- Should not be the only safeguard in a redaction system. The parent pipeline
  pairs it with deterministic rules, calibrated confidence scores and a human
  review queue for exactly this reason.
