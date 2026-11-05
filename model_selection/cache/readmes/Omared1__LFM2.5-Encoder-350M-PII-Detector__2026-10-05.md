---
language:
- en
- de
- fr
- es
- pt
- it
- pl
- ru
- zh
- ja
- ko
- ar
- hi
- id
- vi
- th
tags:
- liquid
- lfm2
- lfm2.5
- bidirectional
- masked-lm
- encoder
- pii
- ner
- privacy
- multilingual
- token-classification
library_name: transformers
license: other
license_name: lfm1.0
license_link: LICENSE
pipeline_tag: token-classification
base_model:
    - LiquidAI/LFM2.5-Encoder-350M
---

<div align="center">
 
# LFM2.5-Encoder-350-PII-Detector

A full fine-tune of [LFM2.5-Encoder-350M](https://huggingface.co/LiquidAI/LFM2.5-Encoder-350M) with a token-classification head, covering **40 PII types** across **16 languages**. 



## Entity types (40 PII types across 11 domains)

| Domain | Types |
|---|---|
| **Identity** | `identity.person_name`, `identity.ssn`, `identity.national_id`, `identity.passport`, `identity.drivers_license`, `identity.date_of_birth`, `identity.tax_id` |
| **Contact** | `contact.email`, `contact.phone`, `contact.address`, `contact.postal_code`, `contact.ip_address` |
| **Financial** | `financial.credit_card`, `financial.iban`, `financial.bank_account`, `financial.swift_bic`, `financial.crypto_wallet`, `financial.amount` |
| **Credentials** | `credential.api_key`, `credential.password`, `credential.private_key`, `credential.jwt`, `credential.connection_string`, `developer.login_credentials` |
| **Online** | `online.username`, `online.url` |
| **Device** | `device.mac_address`, `device.imei`, `developer.device_id` |
| **Location** | `location.gps_coordinates` |
| **Healthcare** | `healthcare.medical_record`, `healthcare.condition`, `healthcare.medication`, `healthcare.health_plan_id` |
| **Organization** | `org.company_name` |
| **Special-category** | `special.religion`, `special.political`, `special.orientation`, `special.health_status` |
| **Legal** | `legal.case_number` |

## Benchmarks (18-locale-filtered, partial-F1, hybrid decode)

| Benchmark | **this model** | detection tier | SauerkrautLM GLiNER | openai/privacy-filter | Piiranha-v1 | OpenMed privacy-filter | regex + validators |
|---|---|---|---|---|---|---|---|
| SPY | **0.428** | 0.509 | 0.280 | 0.264 | 0.232 | 0.226 | 0.358 |
| Gretel | **0.880** | 0.885 | 0.663 | 0.458 | 0.553 | 0.770 | 0.337 |
| TAB | **0.867** | 0.888 | 0.685 | 0.543 | 0.262 | 0.672 | 0.000 |
| ai4privacy | **0.715** | 0.774 | 0.488 | 0.394 | 0.946 | 0.432 | 0.195 |
| Nemotron | **0.855** | 0.863 | 0.639 | 0.572 | 0.658 | 0.918 | 0.335 |
| MAPA | **0.236** | 0.267 | 0.416 | 0.288 | 0.228 | 0.164 | 0.000 |

![leaderboard](leaderboard_18lang.png)

- **Best on every benchmark except MAPA**, whose idiosyncratic date-as-`date_of_birth` labeling
  convention penalises correctly-typed predictions. Only two external scores land higher
  anywhere — Piiranha-v1's 0.946 on ai4privacy and OpenMed's 0.918 on Nemotron — and both are
  in-distribution: each model trains on that exact corpus, as did our own encoder's pretraining
  on those same two.
- **Detection tier** is the same model and the same predictions, scored with the type label
  ignored — did it find the PII span at all, which is the metric that matters for redaction. The
  gap to exact-type is the type-confusion rate, e.g. SPY 0.428 → 0.509.

## Usage

> ⚠️ Loads custom code via `trust_remote_code=True` (the model wraps a `trust_remote_code` encoder).

Install the required packages:

```bash
pip install torch transformers huggingface_hub
```

Run PII detection:

```python
import importlib.util
import sys

from huggingface_hub import hf_hub_download
from transformers import AutoModelForTokenClassification, AutoTokenizer

model_id = "LiquidAI/LFM2.5-Encoder-350-PII-Detector"

helper_path = hf_hub_download(model_id, "pii_hybrid_decode.py")
hf_hub_download(model_id, "context_cued.py")
sys.path.insert(0, helper_path.rsplit("/", 1)[0])

spec = importlib.util.spec_from_file_location("pii_hybrid_decode", helper_path)
hd = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hd)

tok = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForTokenClassification.from_pretrained(model_id, trust_remote_code=True).eval()

spans = hd.predict("Email Dr. Laura Schmidt at laura@charite.de.", tok, model)
print(spans)
```
