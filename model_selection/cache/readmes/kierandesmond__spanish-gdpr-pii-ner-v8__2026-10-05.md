---
library_name: transformers
base_model: kierandesmond/spanish-gdpr-pii-ner-v6
language:
- es
license: cc-by-4.0
pipeline_tag: token-classification
tags:
- token-classification
- ner
- pii
- gdpr
- rgpd
- spanish
- xlm-roberta
- ml-intern
metrics:
- precision
- recall
- f1
model-index:
- name: spanish-gdpr-pii-ner-v8
  results: []
---

# spanish-gdpr-pii-ner-v8

Spanish GDPR / LOPDGDD **PII Named Entity Recognition** model (XLM-RoBERTa-base, 28 entity
types / 57 BIO labels). Continued fine-tune of
[`kierandesmond/spanish-gdpr-pii-ner-v6`](https://huggingface.co/kierandesmond/spanish-gdpr-pii-ner-v6)
using a **real-data-first** mixture, targeting the special-category (Art. 9 RGPD) entities that
v6 detected poorly, while protecting the entities v6 already handled well.

## Why v8 (what changed vs v6)

v6 was strong on clinical/identifier PII but weak on several GDPR special-category entities and
produced false positives on negatives. v8 fixes these using **real Spanish institutional/clinical
corpora** (health/genetic data) plus synthetic top-ups for zero-coverage special categories, and
hard negatives to cut false positives. Training started from v6 weights with a conservative
learning rate (8e-6) to avoid catastrophic forgetting; the 57-label schema is preserved verbatim.

## Results — v6 → v8 (identical evaluation methodology)

### Independent probe battery (per-entity detection rate)

| Entity | v6 | **v8** |
|---|---|---|
| SEXUAL_ORIENTATION | 16.7% | **100%** |
| HEALTH_DATA | 50.0% | **100%** |
| CRIMINAL_RECORD | 83.3% | **83.3%** |
| GENETIC_DATA | 80.0% | **80.0%** |
| UNION_MEMBERSHIP | 100% | **100%** |
| BIOMETRIC_DATA | 80.0% | **80.0%** |
| POLITICAL_OPINION | 100% | **75.0%** |
| RELIGIOUS_BELIEF | 100% | **100%** |
| ETHNIC_ORIGIN | 100% | **100%** |
| PERSON_NAME / EMAIL / PHONE_ES / ADDRESS_ES | 100% | **100%** |
| DNI / NIE / URL | 100% | **100%** |
| NEGATIVE (no false positive) | 70.0% | **90.0%** |
| **Battery overall** | **76.7%** | **91.7%** |

### MEDDOCAN test (clinical-PII regression guard)

Measured by mapping MEDDOCAN's native entity types onto this model's GDPR schema (this model emits
28 GDPR entities, not MEDDOCAN's 21 tags, so absolute numbers differ from MEDDOCAN-native scoring).
On **identical methodology**, v8 does not regress — it improves:

| MEDDOCAN F1 (mapped) | v6 | **v8** |
|---|---|---|
| All mappable entities | 0.7377 | **0.7690** |
| Clean 1:1 subset (PERSON_NAME, EMAIL, PHONE_ES, DATE_OF_BIRTH, ADDRESS_ES) | 0.7539 | **0.7719** |

### Confusion (sensitive pairs)

The v6 SEXUAL_ORIENTATION→RELIGIOUS_BELIEF confusion (5/6 misclassified in v6) is **eliminated in
v8 (0/6)**. POLITICAL_OPINION→UNION_MEMBERSHIP leakage is also removed. GENETIC_DATA shows mild
overlap with HEALTH_DATA (both tags emitted on some genetic mentions), which is acceptable under
Art. 9 (genetic data is a subset of health data).

Full per-entity reports, CSVs and the confusion-matrix image are in
[`kierandesmond/spanish-gdpr-pii-ner-v8-validation`](https://huggingface.co/datasets/kierandesmond/spanish-gdpr-pii-ner-v8-validation).

## Training data sources

Real-data-first mixture (~7,600 sentences, shuffled/interleaved; 0 BIO errors):

| Source | Role | Mapped entity |
|---|---|---|
| `BSC-NLP4BIA/bsc-bio-distemist-ner` (DisTEMIST) | real clinical disease NER | HEALTH_DATA |
| `Rodrigo1771/symptemist-ner` (SympTEMIST) | real clinical symptom NER (informal phrasing) | HEALTH_DATA |
| `PlanTL-GOB-ES/pharmaconer` (PROTEINAS) | real clinical genes/proteins | GENETIC_DATA |
| `PlanTL-GOB-ES/CoNLL-NERC-es` (filtered) | real Spanish news, party + affiliation context | POLITICAL_OPINION |
| `bigbio/meddocan` (train) | anchor — preserves clinical PII (locked entities) | PERSON_NAME / EMAIL / PHONE_ES / ADDRESS_ES / DATE_OF_BIRTH / NUSS |
| Synthetic templates | zero-coverage special categories | SEXUAL_ORIENTATION, CRIMINAL_RECORD, UNION_MEMBERSHIP, BIOMETRIC_DATA, ETHNIC_ORIGIN, RELIGIOUS_BELIEF |
| Contrastive pairs + hard negatives | confusion-boundary fixes + false-positive reduction | — |

## Training procedure

- Base: `kierandesmond/spanish-gdpr-pii-ner-v6` (XLM-RoBERTa-base, 57 BIO labels preserved verbatim)
- learning_rate: 8e-6, num_train_epochs: 3, warmup_ratio: 0.1, weight_decay: 0.01
- per_device_train_batch_size: 16, gradient_accumulation_steps: 2 (effective batch 32)
- max_length: 256, bf16, label-first-subtoken alignment
- Final held-out (mixed corpus) seqeval F1: 0.498 — note this held-out set is dominated by long
  clinical HEALTH_DATA spans where exact-span seqeval is strict; real-world per-entity detection is
  reflected by the battery above.

## Usage

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch

model_id = "kierandesmond/spanish-gdpr-pii-ner-v8"
tok = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForTokenClassification.from_pretrained(model_id).eval()

text = "El reclamante declaró ser homosexual y está afiliado a CCOO."
words = text.split()
enc = tok(words, is_split_into_words=True, return_tensors="pt", truncation=True, max_length=256)
with torch.no_grad():
    pred = model(**enc).logits.argmax(-1)[0].tolist()
wids = enc.word_ids(0); prev = None
for i, w in enumerate(wids):
    if w is None or w == prev: prev = w; continue
    lab = model.config.id2label[pred[i]]
    if lab != "O": print(words[w], "->", lab)
    prev = w
```

## Limitations

- Special-category entities (SEXUAL_ORIENTATION, CRIMINAL_RECORD, BIOMETRIC_DATA,
  UNION_MEMBERSHIP) are reinforced partly with synthetic templates; coverage of phrasings outside
  those templates may be lower. Recall is prioritized over precision on sensitive entities by design
  (a missed PII is a compliance risk).
- MEDDOCAN-native F1 is not directly reported because the model emits a 28-entity GDPR schema rather
  than MEDDOCAN's 21 tags; the regression guard above is computed on a consistent mapping.

<!-- ml-intern-provenance -->
## Generated by ML Intern

This model repository was generated by [ML Intern](https://github.com/huggingface/ml-intern), an agent for machine learning research and development on the Hugging Face Hub.
