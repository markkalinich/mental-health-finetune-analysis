---
license: apache-2.0
library_name: transformers
base_model: openai/privacy-filter
datasets:
  - ai4privacy/pii-masking-200k
  - ai4privacy/pii-masking-400k
  - ai4privacy/open-pii-masking-500k-ai4privacy
pipeline_tag: token-classification
tags:
  - token-classification
  - pii
  - ner
  - privacy
  - redaction
  - multilingual
  - openmed
  - openai-privacy-filter
language:
  - ar
  - bn
  - de
  - en
  - es
  - fr
  - hi
  - it
  - ja
  - ko
  - nl
  - pt
  - te
  - tr
  - vi
  - zh
---

# privacy-filter-multilingual

Fine-tuned [`openai/privacy-filter`](https://huggingface.co/openai/privacy-filter)
for **fine-grained PII extraction** across **54 categories** in **16 languages**.

- **Base model**: [`openai/privacy-filter`](https://huggingface.co/openai/privacy-filter) — 1.4B-parameter MoE (50M active per token), BIOES token-classification head
- **Task**: Token classification for PII detection (BIOES scheme)
- **Languages (16)**: Arabic, Bengali, Chinese, Dutch, English, French, German, Hindi, Italian, Japanese, Korean, Portuguese, Spanish, Telugu, Turkish, Vietnamese
- **Training data**: Multilingual mix from [AI4Privacy](https://huggingface.co/ai4privacy) — `pii-masking-200k`, `pii-masking-400k`, and `open-pii-masking-500k-ai4privacy`, language-balanced
- **Recipe**: `opf train` (OpenAI's official fine-tuning CLI) — full fine-tune, AdamW, balanced language sampling, 5 epochs, bf16
- **Labels**: 54 PII categories → 217 BIOES classes (1 `O` + 54 × B/I/E/S)

The base model ships with 8 coarse PII categories and English-only training. This
model trades that for a **6.75× more granular vocabulary** spanning identity,
contact, address, financial, vehicle, digital, and crypto labels — all evaluated
across 16 languages.

> **Family at a glance.** Same architecture, three runtimes:
> - **PyTorch (this repo)** — CPU + CUDA, anywhere transformers runs.
> - **MLX BF16** — [`OpenMed/privacy-filter-multilingual-mlx`](https://huggingface.co/OpenMed/privacy-filter-multilingual-mlx) — Apple Silicon, full precision.
> - **MLX 8-bit** — [`OpenMed/privacy-filter-multilingual-mlx-8bit`](https://huggingface.co/OpenMed/privacy-filter-multilingual-mlx-8bit) — Apple Silicon, smaller + faster.

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
result = extract_pii(text, model_name="OpenMed/privacy-filter-multilingual")
for ent in result.entities:
    print(f"{ent.label:30s} {ent.text!r}  conf={ent.confidence:.2f}")

# De-identify with any of the supported methods
masked   = deidentify(text, method="mask",   model_name="OpenMed/privacy-filter-multilingual")
removed  = deidentify(text, method="remove", model_name="OpenMed/privacy-filter-multilingual")
hashed   = deidentify(text, method="hash",   model_name="OpenMed/privacy-filter-multilingual")

# Faker-backed locale-aware obfuscation, deterministic with consistent=True+seed
fake = deidentify(
    text,
    method="replace",
    model_name="OpenMed/privacy-filter-multilingual",
    consistent=True,
    seed=42,
)
print(fake.deidentified_text)
```

`OpenMed/privacy-filter-multilingual-mlx*` model names also work in the same
`extract_pii()` / `deidentify()` calls — on a non-Apple-Silicon host they
automatically fall back to **this PyTorch checkpoint** with a one-time warning.
So you can ship MLX names in code and still run on Linux/Windows.

The OpenMed wrapper passes `trust_remote_code=True` for you, runs the model's
own BIOES Viterbi decoder, and skips OpenMed's regex smart-merging (the model
already produces clean spans).

## Label space (54 categories)

| Category | Typical examples |
|---|---|
| **Identity** | `FIRSTNAME`, `MIDDLENAME`, `LASTNAME`, `PREFIX`, `AGE`, `GENDER`, `SEX`, `EYECOLOR`, `HEIGHT`, `USERNAME`, `OCCUPATION`, `JOBTITLE`, `JOBDEPARTMENT`, `ORGANIZATION`, `USERAGENT` |
| **Contact** | `EMAIL`, `PHONE`, `URL` |
| **Address** | `STREET`, `BUILDINGNUMBER`, `SECONDARYADDRESS`, `CITY`, `COUNTY`, `STATE`, `ZIPCODE`, `GPSCOORDINATES`, `ORDINALDIRECTION` |
| **Dates & time** | `DATE`, `DATEOFBIRTH`, `TIME` |
| **Government IDs** | `SSN` |
| **Financial** | `ACCOUNTNAME`, `BANKACCOUNT`, `IBAN`, `BIC`, `CREDITCARD`, `CREDITCARDISSUER`, `CVV`, `PIN`, `MASKEDNUMBER`, `AMOUNT`, `CURRENCY`, `CURRENCYCODE`, `CURRENCYNAME`, `CURRENCYSYMBOL` |
| **Crypto** | `BITCOINADDRESS`, `ETHEREUMADDRESS`, `LITECOINADDRESS` |
| **Vehicle** | `VIN`, `VRM` |
| **Digital** | `IPADDRESS`, `MACADDRESS`, `IMEI` |
| **Auth** | `PASSWORD` |

The output space is `O` plus `B-`, `I-`, `E-`, `S-` for each of the 54 categories
(4 × 54 + 1 = 217). The `id2label` mapping is shipped with the model.

## Limitations & intended use

- **Multilingual but uneven.** Strongest on languages with rich PII training
  data (German, Spanish, French, Italian, Hindi, Telugu, English). CJK languages
  (Japanese, Korean, Chinese) and some morphologically-marked low-resource
  languages remain the main bottleneck on the current training mix.
- **Synthetic training data.** The AI4Privacy datasets are template-synthesized;
  real clinical notes, legal documents, and web text may show different
  surface forms. For high-stakes deployments, collect a domain-specific eval
  set and re-calibrate thresholds.
- **Not a substitute for legal compliance review.** Use alongside a governance
  layer (human review, deterministic regex pre-filters, etc.).
- **Not a clinical PHI model.** Healthcare-specific PHI and clinical entity
  training is planned as a separate branch.

**Head initialization**: `opf`'s default "copy-from-matching-base" head init.
Of the 217 new BIOES classes, the few with exact base-vocabulary matches
(`O`, `B/I/E/S-account_name`, etc.) were copied directly; the rest were copied
from semantically-adjacent coarse rows and fine-tuned end-to-end.

**Router**: base model has 128 MoE experts per layer with top-4 routing.
Routers were kept trainable during full fine-tuning; no collapse was observed.

## Credits & Acknowledgements

This model wouldn't exist without two open-source releases — sincere thanks
to both teams:

- **OpenAI** for [open-sourcing the Privacy Filter](https://huggingface.co/openai/privacy-filter)
  (architecture, modeling code, and `opf` training/eval CLI). Everything in
  this repo is a fine-tune on top of that release.
- **AI4Privacy** for releasing the multilingual PII masking datasets used as
  training data:
  [`pii-masking-200k`](https://huggingface.co/datasets/ai4privacy/pii-masking-200k),
  [`pii-masking-400k`](https://huggingface.co/datasets/ai4privacy/pii-masking-400k),
  [`open-pii-masking-500k-ai4privacy`](https://huggingface.co/datasets/ai4privacy/open-pii-masking-500k-ai4privacy).

Additional thanks to the **HuggingFace** team for the `transformers` /
`huggingface_hub` ecosystem this model ships through.

## License

Apache 2.0.


## Citation

If you use this model, please cite **this model**, the organization behind it
(**OpenMed**), and the upstream base model + datasets:

```bibtex
@misc{openmed_privacy_filter_multilingual_2026,
  author       = {OpenMed},
  title        = {{OpenMed/privacy-filter-multilingual}: multilingual fine-grained PII extraction across 16 languages and 54 categories},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/OpenMed/privacy-filter-multilingual}}
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

@misc{ai4privacy_pii_masking,
  author       = {AI4Privacy},
  title        = {{AI4Privacy PII Masking Datasets}},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/ai4privacy}}
}
```
