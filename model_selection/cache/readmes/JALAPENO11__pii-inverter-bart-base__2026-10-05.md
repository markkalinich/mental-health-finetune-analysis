---
language: en
license: mit
tags:
  - text2text-generation
  - model-inversion
  - pii
  - bart
  - seq2seq
base_model: facebook/bart-base
---

# PII Model-Inversion Inverter — BART-base

**Repo:** `JALAPENO11/pii-inverter-bart-base`

This model is a **model-inversion attack** against a PII anonymisation system.
It was trained to reverse the output of a BART-base anonymiser:

> anonymised text → (inverter) → recovered original text

---

## Training Details

| Parameter | Value |
|---|---|
| Base model | `facebook/bart-base` |
| Checkpoint epoch | 8 |
| Global step | 12479 |
| Saved at | 2026-04-06T01:42:04.473556 |
| Train loss | 0.3834 |
| Eval loss | 0.4518 |
| Perplexity | 1.57 |
| Token accuracy | 0.4206 |
| ERR exact | 0.2925 |
| ERR partial | 0.0282 |
| Eval samples | 1918 |

---

## Evaluation Metrics

### Attack B — Inverter Model (best checkpoint)

| Metric | Value |
|---|---|
| ERR exact | 0.2925 (29.2% entities recovered verbatim) |
| ERR partial | 0.0282 |
| Token accuracy | 0.4206 |
| Exact sentence match | 0.1528 |
| Corpus BLEU | 0.6466 |

### ERR by adversarial strategy

| Strategy | Samples | ERR exact |
|---|---|---|
| S2_combinatorial_pii | 424 | 0.1958 |
| S3_paraphrase_consistency | 261 | 0.4521 |
| S4_rarity_spectrum | 311 | 0.2990 |
| S1_entity_consistency | 556 | 0.2878 |
| S6_edge_cases | 186 | 0.3548 |
| S5_cross_entity_correlation | 180 | 0.2278 |

### ERR by name rarity

| Rarity | Samples | ERR exact |
|---|---|---|
| unknown | 1051 | 0.2931 |
| common | 128 | 0.3750 |
| rare | 249 | 0.2088 |
| very_rare | 134 | 0.3134 |
| medium | 356 | 0.3118 |

---

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

tokenizer = AutoTokenizer.from_pretrained("JALAPENO11/pii-inverter-bart-base")
model     = AutoModelForSeq2SeqLM.from_pretrained("JALAPENO11/pii-inverter-bart-base")
model.eval()

anonymized = "Dear Ms. Anya Sharma, please update your account details."

inputs = tokenizer(anonymized, return_tensors="pt",
                   max_length=128, truncation=True)
with torch.no_grad():
    out = model.generate(**inputs, max_new_tokens=128, num_beams=4)
print(tokenizer.decode(out[0], skip_special_tokens=True))
# → "Dear Amyna Tharathip, please update your account details."
```

---

## Disclaimer

This model is published for **research purposes only** to study the
robustness of PII anonymisation systems.  It should not be used to
de-anonymise real personal data.

See `attack_report.txt` in the repo Files tab for the full evaluation report.
