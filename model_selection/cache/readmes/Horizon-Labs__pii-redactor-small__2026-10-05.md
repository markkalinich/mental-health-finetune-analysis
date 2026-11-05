---
license: apache-2.0
language:
- multilingual
- en
- de
- fr
- es
- it
- nl
- pt
- pl
- cs
- sk
- sl
- hr
- sr
- bg
- ro
- hu
- el
- da
- sv
- fi
- et
- lv
- lt
- ru
- uk
- tr
- ar
- hi
- zh
- ja
- ko
- vi
- id
- ms
- tl
- th
library_name: transformers
pipeline_tag: token-classification
base_model: jhu-clsp/mmBERT-small
tags:
- pii
- pii-detection
- redaction
- anonymization
- privacy
- secrets-detection
- data-masking
- ner
- presidio
- modernbert
- mmbert
- onnx
- transformers.js
datasets:
- ai4privacy/pii-masking-openpii-1.5m
- nvidia/Nemotron-PII
- gretelai/gretel-pii-masking-en-v1
widget:
- text: Hi, I'm Anna Müller. Mail anna.mueller@posteo.de or call +49 30 1234567. Card
    4111 1111 1111 1111, exp 09/28, CVV 737.
  example_title: Contact + card
- text: Bonjour, je m'appelle Jean Dupont, j'habite 12 rue de la Paix, 75002 Paris.
    IBAN FR76 3000 6000 0112 3456 7890 189.
  example_title: French
- text: DATABASE_URL=postgres://admin:Sup3rS3cret!@10.0.4.17:5432/prod
  example_title: Secrets in config
---

# PII Redactor (small, 141M)

A small, fast, **multilingual PII and secrets detector** for redacting text before it reaches logs, LLM prompts,
training data or a vendor API. It tags 29 entity types: names, contact details, addresses, government IDs,
financial data, credentials and API keys, network and device identifiers, and more.

- **Open**: Apache-2.0, ungated, trained only on permissively licensed data.
- **Multilingual**: 30+ languages, Latin and non-Latin scripts.
- **Small**: 141M parameters, CPU-friendly. ONNX and transformers.js work in the browser and at the edge.
- **Measured honestly**: evaluated on four external benchmarks (plus two held-out sets of our own) that no model below was trained on, against the most
  used open PII models. It is not the best on every benchmark; see the table.

Try it in the browser: [Horizon-Labs/pii-redactor demo](https://huggingface.co/spaces/Horizon-Labs/pii-redactor).

Part of [Agent I/O Guards](https://huggingface.co/collections/Horizon-Labs/agent-i-o-guards-6ab403c49494bc2b71ca7669),
alongside [Prompt Injection Guard](https://huggingface.co/Horizon-Labs/prompt-injection-guard-base).

Source code (data, training, evaluation): [github.com/horizon-ai-labs/agent-io-guards](https://github.com/horizon-ai-labs/agent-io-guards).

## Quick start

```python
from transformers import pipeline

ner = pipeline("token-classification", model="Horizon-Labs/pii-redactor-small", aggregation_strategy="simple")
ner("Hi, I'm Anna Müller. Mail anna.mueller@posteo.de, key sk-proj-9fQ2x7LmA1bC3dE4")
```

For redaction, use `redact.py` from this repo. It merges sub-word pieces, trims whitespace, and handles long
documents with overlapping windows:

```python
from huggingface_hub import hf_hub_download
import importlib.util, sys
spec = importlib.util.spec_from_file_location("redact", hf_hub_download("Horizon-Labs/pii-redactor-small", "redact.py"))
redact = importlib.util.module_from_spec(spec); spec.loader.exec_module(redact)

r = redact.PIIRedactor("Horizon-Labs/pii-redactor-small")
r.redact("Bonjour, je m'appelle Jean Dupont, j'habite 12 rue de la Paix, 75002 Paris.")
# "Bonjour, je m'appelle [PERSON], j'habite [STREET_ADDRESS], [POSTCODE] [LOCATION]."
```

### Presidio

```python
from presidio_analyzer import AnalyzerEngine
analyzer = AnalyzerEngine()
analyzer.registry.add_recognizer(redact.presidio_recognizer("Horizon-Labs/pii-redactor-small"))
analyzer.analyze(text="Call me at (415) 555-0132", language="en")
```

### LLM Guard (Anonymize scanner)

`llm_guard_conf.py` in this repo maps the labels to Presidio / LLM Guard entities. It is a permissive, multilingual
alternative to the default Anonymize models:

```python
spec = importlib.util.spec_from_file_location("conf", hf_hub_download("Horizon-Labs/pii-redactor-small", "llm_guard_conf.py"))
conf = importlib.util.module_from_spec(spec); spec.loader.exec_module(conf)

from llm_guard.vault import Vault
from llm_guard.input_scanners import Anonymize
scanner = Anonymize(Vault(), recognizer_conf=conf.horizon_pii_conf("small"), language="en")
scanner.scan("Hi, I'm Anna Müller, email anna.mueller@posteo.de, IBAN DE89370400440532013000.")[0]
# "Hi, I'm [REDACTED_PERSON_1], email [REDACTED_EMAIL_ADDRESS_1], IBAN [REDACTED_IBAN_CODE_1]."
```

## Entity types

`ACCOUNT_ID`, `AGE`, `BANK_ACCOUNT`, `COORDINATE`, `CREDIT_CARD`, `CREDIT_CARD_CVV`, `DATE`, `DATE_OF_BIRTH`, `DEVICE_ID`, `DRIVER_LICENSE`, `EMAIL`, `IP_ADDRESS`, `LICENSE_NUMBER`, `LOCATION`, `MAC_ADDRESS`, `MEDICAL_ID`, `NATIONAL_ID`, `ORGANIZATION`, `PASSPORT`, `PASSWORD`, `PERSON`, `PHONE`, `POSTCODE`, `SECRET`, `STREET_ADDRESS`, `TAX_ID`, `URL`, `USERNAME`, `VEHICLE_ID`

`ORGANIZATION` means an employer or company linked to a person. `SECRET` covers API keys, tokens, private keys,
connection strings and session cookies. Gender and other sensitive attributes (religion, health conditions) are
**not** tagged in this version.

## Evaluation

### External benchmarks

None of the models below were trained on these benchmarks. Every model uses its own label set, so the comparison
ignores entity types. It measures what matters for redaction: **redaction recall**, the share of must-redact
characters that get masked, and **redaction precision**, the share of masked characters that are PII. All models ran
through the same `transformers` token-classification pipeline (`code/pii/evaluate_pii.py`), with at most 600 documents
per benchmark.

Redaction recall / precision:

| Benchmark | **this model** | base (308M) | OpenAI Privacy Filter (1.5B) | gravitee bert-small | OpenMed PII Small 44M |
|---|---|---|---|---|---|
| RedactionBench (real-world style forms, letters, syllabi; 'mandatory' spans) | 0.23 / 0.74 | 0.19 / 0.74 | 0.10 / 0.85 | 0.07 / 0.76 | 0.12 / 0.76 |
| TonicAI Privacy-Bench (corporate email threads) | 0.76 / 0.95 | 0.81 / 0.94 | 0.78 / 0.96 | 0.88 / 0.76 | 0.86 / 0.82 |
| TAB: ECHR court judgments (DIRECT identifiers) | 0.60 / 0.84 | 0.74 / 0.88 | 0.38 / 0.97 | 0.53 / 0.71 | 0.45 / 0.71 |
| Russian PII benchmark (redmadrobot) | 0.75 / 0.89 | 0.71 / 0.90 | 0.67 / 0.76 | 0.64 / 0.54 | 0.71 / 0.81 |
| Secrets, code, configs, chats in 36 languages (our held-out synthetic set) * | 0.77 / 0.74 | 0.76 / 0.73 | 0.78 / 0.72 | 0.46 / 0.50 | 0.65 / 0.61 |
| Card numbers, expiry dates, CVVs, IBANs in 12 languages (our held-out templates) ** | 1.00 / 0.99 | 0.93 / 0.97 | 0.90 / 0.92 | 0.93 / 0.88 | 0.90 / 0.95 |

Redaction F1 (harmonic mean of the two):

| Benchmark | **this model** | base (308M) | OpenAI Privacy Filter (1.5B) | gravitee bert-small | OpenMed PII Small 44M |
|---|---|---|---|---|---|
| RedactionBench (real-world style forms, letters, syllabi; 'mandatory' spans) | **0.351** | 0.306 | 0.186 | 0.120 | 0.200 |
| TonicAI Privacy-Bench (corporate email threads) | 0.846 | **0.870** | 0.865 | 0.812 | 0.844 |
| TAB: ECHR court judgments (DIRECT identifiers) | 0.700 | **0.804** | 0.544 | 0.607 | 0.554 |
| Russian PII benchmark (redmadrobot) | **0.816** | 0.797 | 0.709 | 0.582 | 0.756 |
| Secrets, code, configs, chats in 36 languages (our held-out synthetic set) * | **0.753** | 0.741 | 0.748 | 0.476 | 0.626 |
| Card numbers, expiry dates, CVVs, IBANs in 12 languages (our held-out templates) ** | **0.996** | 0.951 | 0.908 | 0.906 | 0.920 |

Reading this table:
- RedactionBench marks a lot as mandatory (form field values, course codes, IDs), so every model's recall is low.
  Relative order is the useful signal.
- Privacy-Bench (email threads): gravitee and OpenMed catch more PII but mask much more non-PII.
  OpenAI's much larger model is the most precise.
- \* The last row is a held-out set we generated with Qwen3.8-27B: secrets in code, config files and logs, plus
  chat and email threads, in 36 languages. This model was **not** trained on any of that generator's output, but we
  built the set ourselves, so read it as supporting evidence only.
- \*\* Payment snippets from our own template generator (`code/pii/build_pii_v3.py`) with held-out templates and
  keywords. This v1.1 model was trained on other templates from the same generator, so this row is partly in-distribution for it.
- TAB counts DIRECT identifiers in court judgments, such as names and case-application numbers. Case numbers are not a
  type any of these models were trained for.

### v1.0 → v1.1

v1.1 (this version) adds 6,000 short, programmatically generated payment and bank snippets to the unchanged v1.0
training data: Luhn-valid test card numbers in several groupings, expiry dates, CVV/CVC codes with keywords in 12
languages, and IBAN/BIC codes (none are real accounts). v1.0 missed expiry dates without the word "date" and CVVs after
words like "security code" or "cryptogramme". On the payment set v1.1 masks 1.00 of must-redact characters
(v1.0: 0.88), with the external mean redaction F1 unchanged (0.678 vs 0.678). The same data did **not** help the base
model (external mean 0.683 and 0.666 over two seeds vs 0.694), so pii-redactor-base stays at v1.0. To pin the previous
small model, load it with `revision="v1.0"`.

### In-distribution held-out sets

These come from the same generators as the training data, so they overstate real-world quality.

| Held-out set | entity F1 (exact span + type) | redaction recall | redaction precision |
|---|---|---|---|
| OpenPII validation (30 languages) | 0.971 | 0.999 | 0.998 |
| Nemotron-PII test (en) | 0.946 | 0.943 | 0.992 |
| Gretel PII test (en) | 0.938 | 0.996 | 0.989 |

## Limitations

- Most training text is synthetic (OpenPII, Nemotron-PII, Gretel, plus Qwen3.8-generated documents in later versions).
  Real documents are messier, so expect lower recall on unusual formats, and review before relying on it for compliance.
- It is not a guarantee of anonymization. Quasi-identifiers (job title plus town plus age) and free-text descriptions
  can still identify people.
- Dates are tagged whether or not they are personal, which over-redacts public dates.
- Languages outside the training set, and unusual numeric formats, are weaker. v1.1 fixed most payment-card misses
  (expiry dates, CVVs), but other long ID numbers with unusual grouping can still be only partly masked.

## Training

- Backbone: [jhu-clsp/mmBERT-small](https://huggingface.co/jhu-clsp/mmBERT-small) (MIT), BIO token classification, max length 512
  with stride windows, bf16, 1 epoch.
- Data (about 400k documents): [OpenPII 1.5M](https://huggingface.co/datasets/ai4privacy/pii-masking-openpii-1.5m)
  (CC-BY-4.0, ai4privacy; language-balanced 256k sample), [Nemotron-PII](https://huggingface.co/datasets/nvidia/Nemotron-PII)
  (CC-BY-4.0, NVIDIA), and [Gretel PII masking EN v1](https://huggingface.co/datasets/gretelai/gretel-pii-masking-en-v1)
  (Apache-2.0). Their label sets were mapped to one Presidio-aligned taxonomy (`code/pii/build_pii_v0.py`).
- v1.1: plus 6,000 programmatic payment and bank snippets (`code/pii/build_pii_v3.py`; exact labels, card expiry
  labelled `DATE`, amounts and times left unlabelled).
- Attribution: this model is trained on CC-BY-4.0 data from ai4privacy and NVIDIA. Please keep this notice when
  redistributing derivatives.

## Citation

```bibtex
@misc{horizonlabs2026piiredactor,
  title  = {PII Redactor: small multilingual PII and secrets detection},
  author = {Horizon Labs},
  year   = {2026},
  url    = {https://huggingface.co/Horizon-Labs/pii-redactor-small}
}
```
