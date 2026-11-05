---
license: apache-2.0
language:
  - en
  - hi
  - bn
  - ta
base_model: google/muril-base-cased
pipeline_tag: token-classification
tags:
  - ner
  - pii
  - india
  - dpdp
  - hinglish
  - code-mixed
  - governance
---

# sakshi-pii-in

Token-classification model (MuRIL-base fine-tune) detecting Indian PII in
unstructured text: `PERSON`, `ADDRESS`, `DOB` — including inside
**code-mixed Hinglish** and Devanagari/Bengali/Tamil content.

Built by [RotaVision](https://www.rotavision.com) as Layer 2 of the Sakshi
agent-governance platform's ingest tokenization. Structured identifiers
(Aadhaar, PAN, IFSC, mobile, account numbers) are handled by a
deterministic regex+checksum layer upstream and are deliberately **out of
scope** for this model — pair it with checksum detectors, don't ask it to
find Aadhaar numbers.

## Training data

100% synthetic: templated sentences, JSON records, and chat transcripts
across English, Hindi (Devanagari), Hinglish, Bengali, and Tamil, populated
from public-knowledge name/place gazetteers. No scraped data, no real
persons, no customer data. Hard negatives include order/ticket/invoice
identifiers and checksum-valid synthetic Aadhaar numbers (unlabeled — the
deterministic layer owns those).

## Evaluation (frozen 2,000-example set, disjoint names/places/templates)

| Metric | Result |
|---|---|
| PERSON F1 | 0.988 (P 0.989 / R 0.988) |
| ADDRESS F1 | 0.956 (P 0.957 / R 0.959) |
| DOB F1 | 0.998 |
| Micro F1 / recall | 0.979 / 0.981 |
| CPU batch latency (B=16) | p50 5.7 / p95 6.2 ms per record |

**Operating threshold: 0.25.** Confidence scores are diffuse (correct spans
score 0.28–0.6); calibration is a v1 item. Selection was recall-prioritized
(F-beta, β=2): a missed identity is a liability, a false positive is a
tokenized order id.

```python
from transformers import pipeline

ner = pipeline("token-classification", model="rotalabs/sakshi-pii-in",
               aggregation_strategy="first")
spans = [s for s in ner("Priya Sharma, DOB 14/03/1991, Andheri West se hai")
         if s["score"] >= 0.25]
```

## Limitations

- Five language settings in training; other Indic scripts (Malayalam,
  Telugu, Kannada, Odia…) are best-effort — expect lower recall.
- Synthetic-only training under-represents OCR noise and SMS shorthand.
- Finds PII in text; does not decide lawfulness of processing. Not a
  consent-management or data-discovery tool.
- Machine identifiers (fingerprints, digests, version strings) should be
  exempted from NER at the application layer — see the Sakshi source for
  the pattern.

## Provenance

Base model [google/muril-base-cased](https://huggingface.co/google/muril-base-cased)
(Apache-2.0). Training data fully synthetic, generator and frozen eval set
maintained in the Sakshi repository. Released by RotaVision under the
rotalabs open-source commons, Apache-2.0.
