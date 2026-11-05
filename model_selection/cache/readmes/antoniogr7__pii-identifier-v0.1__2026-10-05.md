---
license: apache-2.0
datasets:
- nvidia/Nemotron-PII
language:
- en
base_model:
- answerdotai/ModernBERT-base
pipeline_tag: token-classification
library_name: transformers
tags:
- pii
- nemotron
- privacy
- ner
- token-classification
- modernbert
metrics:
- precision
- recall
- f1
model-index:
- name: pii-identifier-v0.1
  results:
  - task:
      type: token-classification
      name: Token Classification (PII detection)
    dataset:
      name: nvidia/Nemotron-PII
      type: nvidia/Nemotron-PII
      split: test
    metrics:
    - type: f1
      value: 0.9628
      name: PIIMB F1
    - type: precision
      value: 0.9513
      name: PIIMB Precision
    - type: recall
      value: 0.9747
      name: PIIMB Recall
---

# pii-identifier-v0.1

`pii-identifier-v0.1` is a token-classification model that detects and labels **Personally Identifiable Information (PII)** in English text. It is a fine-tune of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on the [nvidia/Nemotron-PII](https://huggingface.co/datasets/nvidia/Nemotron-PII) dataset, covering **55 PII entity types** with BIO tagging.

On the [PII Masking Benchmark (PIIMB)](https://huggingface.co/datasets/piimb) it ranks **#2 of 30 evaluated models** on the `nvidia/Nemotron-PII` task, with an F2 (recall-weighted) main score of **0.970**.

## Model details

| | |
|---|---|
| **Base model** | [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) |
| **Architecture** | `ModernBertForTokenClassification` |
| **Parameters** | ~ 149.7M total (~ 111M active, ~ 38.7M embeddings) |
| **Max context length** | 8192 tokens |
| **Language** | English |
| **Task** | Token classification / NER (BIO scheme) |
| **Entity types** | 55 |
| **Labels** | 111 (`O` + `B-`/`I-` for each entity type) |
| **Weights precision** | float32 |
| **License** | Apache 2.0 |

### Supported entity types

```
account_number, age, api_key, bank_routing_number, biometric_identifier,
blood_type, certificate_license_number, city, company_name, coordinate,
country, county, credit_debit_card, customer_id, cvv, date, date_of_birth,
date_time, device_identifier, education_level, email, employee_id,
employment_status, fax_number, first_name, gender, health_plan_beneficiary_number,
http_cookie, ipv4, ipv6, language, last_name, license_plate, mac_address,
medical_record_number, national_id, occupation, password, phone_number, pin,
political_view, postcode, race_ethnicity, religious_belief, sexuality, ssn,
state, street_address, swift_bic, tax_id, time, unique_id, url, user_name,
vehicle_identifier
```

## Usage

```python
from transformers import pipeline

text = """
HR Internal Note: Please update the personnel file for Antonio Grimaldi. He was born in Naples at the Inventino Clinic on 04/12/1993. He currently works as a Lead Engineer for Invented Corp SPA. If you need to reach him regarding his onboarding paperwork, his corporate mobile number is +39 333 555 1234 and his official email address is antonio.grimaldi@inventedcorp.it. For payroll processing, please verify that his Italian tax code (Codice Fiscale) is registered as GRMMNT93D12F839W before releasing the direct deposit.
"""

pii = pipeline(
    "token-classification",
    model="antoniogr7/pii-identifier-v0.1",
    aggregation_strategy="simple",   # group B-/I- subtokens into spans
)

for ent in pii(text):
    print(f"{ent['entity_group']:>15}  {ent['score']:.2f}  {ent['word']!r}")
```

```text
     first_name  1.00  ' Antonio'
      last_name  1.00  ' Grimaldi'
           city  0.84  ' Naples'
           city  0.48  ' Invent'
           date  0.81  ' 04/12/1993'
     occupation  0.99  ' Lead Engineer'
   company_name  0.65  ' In'
   company_name  0.55  ' Corp SPA'
   phone_number  0.97  ' +39 333 555 1234'
          email  1.00  ' antonio.grimaldi@inventedcorp.it'
         tax_id  0.94  ' GRMMNT93D12F839W'
```

For lower-level control:

```python
import torch
from transformers import AutoTokenizer, AutoModelForTokenClassification

tok = AutoTokenizer.from_pretrained("antoniogr7/pii-identifier-v0.1")
model = AutoModelForTokenClassification.from_pretrained("antoniogr7/pii-identifier-v0.1")


text = """
"HR Internal Note: Please update the personnel file for Antonio Grimaldi. He was born in Naples at the Inventino Clinic on 04/12/1993. He currently works as a Lead Engineer for Invented Corp SPA. If you need to reach him regarding his onboarding paperwork, his corporate mobile number is +39 333 555 1234 and his official email address is antonio.grimaldi@inventedcorp.it. For payroll processing, please verify that his Italian tax code (Codice Fiscale) is registered as GRMMNT93D12F839W before releasing the direct deposit.
"""

inputs = tok(text, return_tensors="pt")
with torch.no_grad():
    logits = model(**inputs).logits

preds = logits.argmax(-1)[0]
labels = [model.config.id2label[i.item()] for i in preds]
tokens = tok.convert_ids_to_tokens(inputs["input_ids"][0])

# FIX: Call the method on 'tok', passing the token IDs as a list
special_tokens_mask = tok.get_special_tokens_mask(
    inputs["input_ids"][0].tolist(), 
    already_has_special_tokens=True
)

# Filter out the special tokens
for token, label, is_special in zip(tokens, labels, special_tokens_mask):
    if not is_special:
        print(f"{token}: {label}")
```

## Training

The model was fine-tuned on the `nvidia/Nemotron-PII` dataset (English, synthetic PII). The `spans` annotations were converted to a BIO token-classification target over the `answerdotai/ModernBERT-base` tokenizer.

**Preprocessing**

| Setting | Value |
|---|---|
| Tokenizer | `answerdotai/ModernBERT-base` |
| Max sequence length | 8192 |
| Stride (overflow) | 128 |
| Label all subtokens | true |

**Hyperparameters**

| Setting | Value |
|---|---|
| Epochs | 2 |
| Per-device batch size | 32 |
| Gradient accumulation | 2 (effective batch size 64) |
| Learning rate | 3e-5 |
| LR scheduler | linear |
| Warmup steps | 169 |
| Weight decay | 0.01 |
| Optimizer | `adamw_torch_fused` |
| Mixed precision | fp16 |
| Max grad norm | 1.0 |
| Seed | 42 |
| Best-model metric | f1 |

## Evaluation

### Token-level (seqeval, held-out test split during training)

| Metric | Value |
|---|---|
| Precision | 0.9543 |
| Recall | 0.9482 |
| F1 | 0.9512 |
| Accuracy | 0.9934 |

### PII Masking Benchmark (PIIMB v0.2.0) — `nvidia/Nemotron-PII` test

The model was evaluated with the [PII Masking Benchmark](https://huggingface.co/datasets/piimb) harness. The primary leaderboard metric is **F2** (recall-weighted), since missing PII is generally costlier than over-flagging it.

| Metric | Value |
|---|---|
| **Main score (F2)** | **0.9699** |
| F1 | 0.9628 |
| Precision | 0.9513 |
| Recall | 0.9747 |

Span-level NER (strict matching): P 0.868 / R 0.938 / F1 0.902.

**Leaderboard position:** #2 of 30 models evaluated on this task, behind `OpenMed/OpenMed-PII-SuperClinical-Small-44M-v1` (0.9717) and ahead of `OpenMed/OpenMed-PII-SuperClinical-Large-434M-v1` (0.9631).

#### Per-entity highlights (strict F1)

**Strongest:** `email` (0.99), `ipv6` (0.99), `mac_address` (0.98), `date_of_birth` (0.98), `biometric_identifier` (0.98), `ipv4` (0.98), `bank_routing_number` (0.98), `medical_record_number` (0.98).

**Weakest:** `occupation` (0.51), `unique_id` (0.65), `blood_type` (0.65), `time` (0.74), `race_ethnicity` (0.80), `political_view` (0.81), `password` (0.81).

## Intended use & limitations

**Intended use.** PII detection, redaction, and anonymization pipelines for English text; pre-processing before LLM ingestion; data-governance and compliance tooling.

**Limitations.**
- **English only.** Trained exclusively on English data; performance on other languages is not evaluated and likely poor.
- **Synthetic training data.** `nvidia/Nemotron-PII` is synthetically generated. Real-world text — especially noisy, OCR'd, or domain-specific data — may differ from the training distribution.
- **Weak categories.** Semantically fuzzy entity types (`occupation`, `time`, `blood_type`, `unique_id`) have noticeably lower F1 and should not be relied on in isolation.
- **Not a guarantee.** No PII detector is perfect. Do **not** treat outputs as a complete safety guarantee for sensitive data; combine with deterministic rules (regex/validators), human review, and defense-in-depth where the stakes warrant it.
- **Potential bias.** Detection of `gender`, `race_ethnicity`, `religious_belief`, `political_view`, and `sexuality` may reflect biases in the training data; use with care.

## Citation

If you use this model, please also credit the base model and dataset:

```bibtex
@misc{modernbert2024,
  title  = {Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder},
  author = {Answer.AI and LightOn},
  year   = {2024},
  url    = {https://huggingface.co/answerdotai/ModernBERT-base}
}
```

- **Dataset:** [nvidia/Nemotron-PII](https://huggingface.co/datasets/nvidia/Nemotron-PII)
- **Benchmark:** [PII Masking Benchmark (PIIMB)](https://huggingface.co/datasets/piimb)
