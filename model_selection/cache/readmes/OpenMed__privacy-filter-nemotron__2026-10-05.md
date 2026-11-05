---
license: apache-2.0
library_name: transformers
base_model: openai/privacy-filter
datasets:
  - nvidia/Nemotron-PII
pipeline_tag: token-classification
tags:
  - token-classification
  - pii
  - ner
  - privacy
  - redaction
  - nemotron
  - privacy-filter
  - openmed
language:
  - en
---

# privacy-filter-nemotron

Fine-tuned [`openai/privacy-filter`](https://huggingface.co/openai/privacy-filter)
for **fine-grained PII extraction** across **55 categories** from
[`nvidia/Nemotron-PII`](https://huggingface.co/datasets/nvidia/Nemotron-PII).

- **Base model**: [`openai/privacy-filter`](https://huggingface.co/openai/privacy-filter) — 1.4B-parameter MoE (50M active per token), BIOES token-classification head
- **Task**: Token classification for PII detection (BIOES scheme)
- **Training data**: Full 100K rows of `nvidia/Nemotron-PII` train split
- **Held-out val**: 10K label-stratified rows from the Nemotron `test` split (every label has ≥229 entities)
- **Recipe**: `opf train` (OpenAI's official fine-tuning CLI) — full fine-tune, AdamW, lr=1e-4, 5 epochs, bf16, weight decay 0.0
- **Labels**: 55 fine-grained PII categories → 221 BIOES classes (1 `O` + 55 × B/I/E/S)

The base model ships with 8 coarse PII categories (`private_person`,
`private_email`, etc.). This model trades that coarse vocabulary for a
**5× more granular one** — `first_name`, `last_name`, `medical_record_number`,
`credit_debit_card`, `ssn`, and so on — matching what downstream redaction
and masking pipelines typically need.

> **Family at a glance.** Same architecture, three runtimes:
> - **PyTorch (this repo)** — CPU + CUDA, anywhere transformers runs.
> - **MLX BF16** — [`OpenMed/privacy-filter-nemotron-mlx`](https://huggingface.co/OpenMed/privacy-filter-nemotron-mlx) — Apple Silicon, full precision.
> - **MLX 8-bit** — [`OpenMed/privacy-filter-nemotron-mlx-8bit`](https://huggingface.co/OpenMed/privacy-filter-nemotron-mlx-8bit) — Apple Silicon, ~1.7× faster.

## Quick start

### With [OpenMed](https://github.com/maziyarpanahi/openmed) — recommended

OpenMed gives you `extract_pii()` / `deidentify()` with built-in BIOES Viterbi
decoding, span refinement, and a Faker-backed obfuscation engine. Same call
on every host — Apple Silicon picks up MLX automatically; everywhere else uses
this PyTorch checkpoint.

```bash
pip install -U "openmed[hf]"
```

```python
from openmed import extract_pii, deidentify

text = (
    "Patient Sarah Johnson (DOB 03/15/1985), MRN 4872910, "
    "phone 415-555-0123, email sarah.johnson@example.com."
)

# Extract grouped entity spans
result = extract_pii(text, model_name="OpenMed/privacy-filter-nemotron")
for ent in result.entities:
    print(f"{ent.label:30s} {ent.text!r}  conf={ent.confidence:.2f}")

# De-identify with any of the supported methods
masked   = deidentify(text, method="mask",   model_name="OpenMed/privacy-filter-nemotron")
removed  = deidentify(text, method="remove", model_name="OpenMed/privacy-filter-nemotron")
hashed   = deidentify(text, method="hash",   model_name="OpenMed/privacy-filter-nemotron")

# Faker-backed locale-aware obfuscation, deterministic with consistent=True+seed
fake = deidentify(
    text,
    method="replace",
    model_name="OpenMed/privacy-filter-nemotron",
    consistent=True,
    seed=42,
)
print(fake.deidentified_text)
```

`OpenMed/privacy-filter-nemotron-mlx*` model names also work in the same
`extract_pii()` / `deidentify()` calls — on a non-Apple-Silicon host they
automatically fall back to **this PyTorch checkpoint** with a one-time
warning. So you can ship MLX names in code and still run on Linux/Windows.

The OpenMed wrapper passes `trust_remote_code=True` for you, runs the
model's own BIOES Viterbi decoder, and skips OpenMed's regex
smart-merging (the model already produces clean spans).

### With `opf` — OpenAI's official CLI

```bash
pip install 'opf @ git+https://github.com/openai/privacy-filter.git'

opf redact \
  --checkpoint OpenMed/privacy-filter-nemotron \
  --text "Patient Sarah Johnson (DOB 03/15/1985), MRN 4872910, phone 415-555-0123."
```

### With `transformers` directly

```python
import torch
from transformers import AutoModelForTokenClassification, AutoTokenizer

model_id = "OpenMed/privacy-filter-nemotron"
tok = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForTokenClassification.from_pretrained(
    model_id, trust_remote_code=True, dtype=torch.bfloat16
).to("cuda")
model.eval()

text = "Patient Sarah Johnson (DOB 03/15/1985), MRN 4872910, phone 415-555-0123."
enc = tok(text, return_tensors="pt").to("cuda")
with torch.no_grad():
    out = model(**enc).logits.argmax(-1).cpu()[0].tolist()

id2label = {int(k): v for k, v in model.config.id2label.items()}
tokens = tok.convert_ids_to_tokens(enc["input_ids"][0].cpu().tolist())
for t, l in zip(tokens, out):
    if l != 0:
        print(f"{t}\t{id2label[l]}")
```

For best results use Viterbi decoding (not argmax) — both `opf` and OpenMed
do this by default. If you're doing argmax with the HF transformers API, you'll
see slightly more boundary errors but still excellent label accuracy.

## Performance

Evaluated with `opf eval --decode-mode viterbi --eval-mode typed --span-metrics-space char`
on the 10K label-stratified held-out val from `nvidia/Nemotron-PII:test`.

### Headline

| Metric | Value |
|---|---:|
| **Macro B-F1** (across 55 labels) | **0.9533** |
| **Token accuracy** | **0.9910** |
| Strong labels (F1 ≥ 0.90) | 46 / 55 |
| Acceptable (F1 0.70–0.89) | 7 / 55 |
| Weak (F1 < 0.70) | 0 / 55 |

### Per-label F1 (B-tag, sorted)

| Label | Precision | Recall | F1 |
|---|---:|---:|---:|
| 🟢 `mac_address` | 1.000 | 1.000 | **1.000** |
| 🟢 `biometric_identifier` | 0.999 | 0.998 | **0.999** |
| 🟢 `bank_routing_number` | 0.995 | 0.999 | **0.997** |
| 🟢 `credit_debit_card` | 0.999 | 0.993 | **0.996** |
| 🟢 `ipv6` | 0.992 | 1.000 | **0.996** |
| 🟢 `health_plan_beneficiary_number` | 1.000 | 0.990 | **0.995** |
| 🟢 `coordinate` | 0.994 | 0.996 | **0.995** |
| 🟢 `ipv4` | 0.993 | 0.996 | **0.994** |
| 🟢 `url` | 0.989 | 0.999 | **0.994** |
| 🟢 `email` | 0.994 | 0.993 | **0.994** |
| 🟢 `date_of_birth` | 0.992 | 0.994 | **0.993** |
| 🟢 `medical_record_number` | 0.997 | 0.989 | **0.993** |
| 🟢 `street_address` | 0.996 | 0.989 | **0.993** |
| 🟢 `vehicle_identifier` | 0.986 | 0.996 | **0.991** |
| 🟢 `license_plate` | 0.987 | 0.993 | **0.990** |
| 🟢 `customer_id` | 0.995 | 0.984 | **0.990** |
| 🟢 `http_cookie` | 0.992 | 0.983 | **0.988** |
| 🟢 `employee_id` | 0.987 | 0.988 | **0.988** |
| 🟢 `account_number` | 0.992 | 0.982 | **0.987** |
| 🟢 `certificate_license_number` | 0.989 | 0.984 | **0.987** |
| 🟢 `swift_bic` | 0.975 | 0.998 | **0.987** |
| 🟢 `postcode` | 0.991 | 0.981 | **0.986** |
| 🟢 `api_key` | 0.980 | 0.990 | **0.985** |
| 🟢 `password` | 0.999 | 0.968 | **0.983** |
| 🟢 `tax_id` | 1.000 | 0.965 | **0.982** |
| 🟢 `device_identifier` | 0.974 | 0.988 | **0.981** |
| 🟢 `national_id` | 0.991 | 0.961 | **0.976** |
| 🟢 `last_name` | 0.977 | 0.975 | **0.976** |
| 🟢 `date_time` | 0.982 | 0.967 | **0.974** |
| 🟢 `first_name` | 0.962 | 0.978 | **0.970** |
| 🟢 `pin` | 0.973 | 0.967 | **0.970** |
| 🟢 `phone_number` | 0.948 | 0.992 | **0.970** |
| 🟢 `county` | 0.986 | 0.946 | **0.965** |
| 🟢 `employment_status` | 0.960 | 0.968 | **0.964** |
| 🟢 `user_name` | 0.959 | 0.964 | **0.961** |
| 🟢 `date` | 0.967 | 0.955 | **0.961** |
| 🟢 `blood_type` | 0.922 | 0.954 | **0.938** |
| 🟢 `country` | 0.955 | 0.918 | **0.936** |
| 🟢 `ssn` | 0.926 | 0.945 | **0.935** |
| 🟢 `education_level` | 0.961 | 0.908 | **0.934** |
| 🟢 `sexuality` | 0.908 | 0.956 | **0.931** |
| 🟢 `company_name` | 0.967 | 0.894 | **0.929** |
| 🟢 `religious_belief` | 0.912 | 0.941 | **0.926** |
| 🟢 `unique_id` | 0.910 | 0.922 | **0.916** |
| 🟢 `political_view` | 0.939 | 0.872 | **0.905** |
| 🟢 `fax_number` | 0.978 | 0.841 | **0.904** |
| 🟡 `city` | 0.917 | 0.876 | **0.896** |
| 🟡 `time` | 0.933 | 0.802 | **0.863** |
| 🟡 `race_ethnicity` | 0.821 | 0.906 | **0.861** |
| 🟡 `gender` | 0.967 | 0.744 | **0.841** |
| 🟡 `state` | 0.878 | 0.785 | **0.829** |
| 🟡 `language` | 0.889 | 0.735 | **0.804** |
| 🟡 `occupation` | 0.799 | 0.667 | **0.727** |

## Label space (55 categories)

| Category | Typical examples |
|---|---|
| **Identity** | `first_name`, `last_name`, `user_name`, `age`, `gender`, `race_ethnicity`, `sexuality`, `religious_belief`, `political_view`, `marital_status`, `nationality`, `education_level`, `occupation`, `employment_status`, `language`, `blood_type`, `biometric_identifier` |
| **Contact** | `email`, `phone_number`, `fax_number`, `url` |
| **Address** | `street_address`, `city`, `county`, `state`, `country`, `postcode`, `coordinate` |
| **Dates** | `date`, `date_of_birth`, `date_time`, `time` |
| **Government IDs** | `ssn`, `national_id`, `tax_id` |
| **Financial** | `account_number`, `bank_routing_number`, `swift_bic`, `credit_debit_card`, `cvv`, `pin`, `password` |
| **Healthcare** | `medical_record_number`, `health_plan_beneficiary_number` |
| **Enterprise IDs** | `customer_id`, `employee_id`, `unique_id`, `certificate_license_number` |
| **Vehicle** | `license_plate`, `vehicle_identifier` |
| **Digital** | `ipv4`, `ipv6`, `mac_address`, `device_identifier`, `api_key`, `http_cookie` |


**Head initialization**: `opf`'s default "copy-from-matching-base" head init.
Of the 221 new BIOES classes, 5 had exact matches in the base
(`O`, `B/I/E/S-account_number`); the other 216 were copied from
semantically-adjacent coarse rows and fine-tuned end-to-end.

**Router**: base model has 128 MoE experts per layer with top-4 routing.
Routers were kept trainable during full fine-tuning; no collapse was
observed.

## Limitations & intended use

- **English-only training data.** Nemotron-PII is predominantly English
  with a 50/50 US/international locale split. Performance on non-English
  text is not guaranteed.
- **`occupation`, `language`, `gender`, `state`, `race_ethnicity`,
  `political_view`, `education_level` are fuzzier categories** than the
  strict identifiers — F1 lands in 0.65–0.89 vs 0.95+ for formatted
  identifiers. If your downstream only cares about strict PII, you can
  ignore low-confidence predictions on these.
- **Synthetic training data.** Nemotron-PII is a synthesized dataset; real
  clinical notes, legal documents, and web text may show different
  surface forms. For high-stakes deployments, collect a domain-specific
  eval set and re-calibrate thresholds.
- **Not a substitute for legal compliance review.** Use alongside a
  governance layer (human review, deterministic regex pre-filters, etc.).

## Credits & Acknowledgements

This model wouldn't exist without two open-source releases — sincere thanks
to both teams:

- **OpenAI** for [open-sourcing the Privacy Filter](https://huggingface.co/openai/privacy-filter)
  (architecture, modeling code, and `opf` training/eval CLI). Everything in
  this repo is a fine-tune on top of that release.
- **NVIDIA** for releasing the [Nemotron-PII dataset](https://huggingface.co/datasets/nvidia/Nemotron-PII)
  with its 100K-row train split and 55 fine-grained PII labels.

Additional thanks to the **HuggingFace** team for the `transformers` /
`huggingface_hub` ecosystem this model ships through.

## License

Apache 2.0, same as the base model.

## Citation

If you use this model, please cite **this model**, the organization behind
it (**OpenMed**), and the upstream base model + dataset:

```bibtex
@misc{openmed_privacy_filter_nemotron_2026,
  author       = {OpenMed},
  title        = {{OpenMed/privacy-filter-nemotron}: fine-grained PII extraction with 55 categories},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/OpenMed/privacy-filter-nemotron}}
}

@misc{openmed_2026,
  author       = {OpenMed},
  title        = {{OpenMed}: open models and resources for healthcare NLP},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/OpenMed}}
}

@misc{openai_privacy_filter_2025,
  author       = {OpenAI},
  title        = {{openai/privacy-filter}},
  year         = {2025},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/openai/privacy-filter}}
}

@misc{nemotron_pii_2025,
  author       = {NVIDIA},
  title        = {{Nemotron-PII}},
  year         = {2025},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/nvidia/Nemotron-PII}}
}
```
