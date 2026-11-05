---
license: apache-2.0
library_name: transformers
base_model: openai/privacy-filter
pipeline_tag: token-classification
tags:
- privacy
- pii
- ner
- token-classification
- redaction
- nemotron
- openmed
- openai-privacy-filter
language:
- bg
- cs
- da
- de
- el
- en
- es
- et
- fi
- fr
- hr
- hu
- it
- lt
- lv
- nl
- pl
- pt
- ro
- sk
datasets:
- nvidia/Nemotron-PII
- gretelai/gretel-pii-masking-en-v1
- ai4privacy/pii-masking-openpii-1m
private: true
---

# privacy-filter-nemotron-v2

`OpenMed/privacy-filter-nemotron-v2` is the second-generation Nemotron-schema checkpoint in the OpenMed privacy-filter family. It keeps the same fine-grained 55-category PII vocabulary as `OpenMed/privacy-filter-nemotron`, while using a broader training mix and a more recall-oriented adaptation recipe. In practice, this v2 checkpoint should perform better as a general PII masking and redaction model while preserving the useful typed labels from the original Nemotron model.

The model is based on `openai/privacy-filter`, a 1.4B-parameter MoE token classifier with roughly 50M active parameters per token. It predicts 221 BIOES token classes:

- `O`
- 55 PII categories encoded as `B-*`, `I-*`, `E-*`, and `S-*`

Use this checkpoint when you want the Nemotron fine-grained label schema, but prefer the improved v2 masking behavior.

## Relationship To The Original Nemotron Model

This model is a direct successor to `OpenMed/privacy-filter-nemotron`.

- Same base architecture: `openai/privacy-filter`
- Same core label schema: 55 fine-grained Nemotron-style PII categories
- Same output format: BIOES token classification
- Broader adaptation data: Nemotron-style fine labels plus additional PII
  masking examples from other synthetic PII sources
- Better practical masking behavior for general redaction use cases

The original `OpenMed/privacy-filter-nemotron` remains useful when you want the
cleanest single-dataset Nemotron training lineage. This v2 model is the better
default when you want stronger general-purpose PII masking while keeping the
same fine-grained schema.

## Quick Start

### With OpenMed

```bash
pip install -U "openmed[hf]"
```

```python
from openmed import extract_pii, deidentify

model_name = "OpenMed/privacy-filter-nemotron-v2"
text = (
    "Patient Sarah Johnson (DOB 03/15/1985), MRN 4872910, "
    "phone 415-555-0123, email sarah.johnson@example.com."
)

result = extract_pii(text, model_name=model_name)
for ent in result.entities:
    print(ent.label, ent.text)

masked = deidentify(text, method="mask", model_name=model_name)
print(masked.deidentified_text)
```

### With `opf`

```bash
pip install 'opf @ git+https://github.com/openai/privacy-filter.git'

opf redact \
  --checkpoint OpenMed/privacy-filter-nemotron-v2 \
  --text "Patient Sarah Johnson (DOB 03/15/1985), MRN 4872910, phone 415-555-0123."
```

### With Transformers

```python
from transformers import AutoModelForTokenClassification, AutoTokenizer, pipeline

repo_id = "OpenMed/privacy-filter-nemotron-v2"

tokenizer = AutoTokenizer.from_pretrained(repo_id, trust_remote_code=True)
model = AutoModelForTokenClassification.from_pretrained(
    repo_id,
    trust_remote_code=True,
)

ner = pipeline(
    "token-classification",
    model=model,
    tokenizer=tokenizer,
    aggregation_strategy="simple",
)

text = "Patient Sarah Johnson, MRN 4872910, can be reached at sarah@example.com."
print(ner(text))
```

For best production behavior, use BIOES-aware decoding and merge overlapping or
consecutive spans before masking.

## Label Space

The checkpoint uses 55 fine-grained PII categories:

- Identity and demographic attributes: `first_name`, `last_name`, `age`,
  `gender`, `race_ethnicity`, `sexuality`, `religious_belief`,
  `political_view`, `marital_status`, `nationality`, `education_level`,
  `occupation`, `employment_status`, `language`, `blood_type`,
  `biometric_identifier`
- Contact and web identifiers: `email`, `phone_number`, `fax_number`, `url`
- Address: `street_address`, `city`, `county`, `state`, `country`, `postcode`,
  `coordinate`
- Dates and times: `date`, `date_of_birth`, `date_time`, `time`
- Government and regulated IDs: `ssn`, `national_id`, `tax_id`
- Financial and secret values: `account_number`, `bank_routing_number`,
  `swift_bic`, `credit_debit_card`, `cvv`, `pin`, `password`
- Healthcare identifiers: `medical_record_number`,
  `health_plan_beneficiary_number`
- Enterprise and customer identifiers: `customer_id`, `employee_id`,
  `unique_id`, `certificate_license_number`
- Vehicle identifiers: `license_plate`, `vehicle_identifier`
- Digital identifiers: `ipv4`, `ipv6`, `mac_address`, `device_identifier`,
  `api_key`, `http_cookie`

The full label-space JSON is included as `label_space_fine_v1.json`.

## Training Summary

This checkpoint was initialized from the first-generation OpenMed Nemotron
privacy-filter branch and further adapted with source-balanced typed PII
examples.

- Base model: `openai/privacy-filter`
- First-generation predecessor: `OpenMed/privacy-filter-nemotron`
- Output schema: 55 fine-grained PII labels, 221 BIOES classes
- Training precision: bf16
- Training method: full fine-tuning with OpenAI's `opf train`

The training mix includes synthetic PII examples derived from:

- `nvidia/Nemotron-PII`
- `gretelai/gretel-pii-masking-en-v1`
- `ai4privacy/pii-masking-openpii-1m`

## Limitations And Intended Use

This is an experimental private checkpoint intended for PII detection,
masking, and de-identification workflows. It should be validated on your target
domain before use in high-stakes systems.

For clinical PHI, radiology/DICOM workflows, legal data, or other regulated
settings, use this model as one component inside a broader de-identification
pipeline with deterministic rules, audit logging, and human review where
appropriate.

## Credits

This model builds on:

- OpenAI's `openai/privacy-filter` model and `opf` training tools
- NVIDIA's `nvidia/Nemotron-PII`
- Gretel's `gretelai/gretel-pii-masking-en-v1`
- AI4Privacy's `ai4privacy/pii-masking-openpii-1m`

## Citation

```bibtex
@misc{openmed_privacy_filter_nemotron_v2_2026,
  author       = {OpenMed},
  title        = {{OpenMed/privacy-filter-nemotron-v2}: second-generation Nemotron-schema privacy filter},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/OpenMed/privacy-filter-nemotron-v2}}
}
```