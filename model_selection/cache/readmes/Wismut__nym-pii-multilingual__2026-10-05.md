---
license: mit
base_model: jhu-clsp/mmBERT-base
tags:
  - token-classification
  - pii
  - de-identification
  - anonymization
  - onnx
  - modernbert
  - multilingual
language:
  - en
  - de
  - fr
  - es
  - it
  - pt
  - nl
  - pl
  - sv
  - cs
  - ro
  - tr
  - fi
  - da
  - el
  - ru
  - uk
  - ja
  - zh
  - ko
  - ar
  - hi
datasets:
  - Wismut/nym-pii-multilingual-data
pipeline_tag: token-classification
---

# nym-pii-multilingual

Multilingual PII token-classification model for the
[nym](https://github.com/byteowlz/nym) anonymization CLI — a fine-tune of
[`jhu-clsp/mmBERT-base`](https://huggingface.co/jhu-clsp/mmBERT-base)
(ModernBERT architecture, 1,800-language pretraining). **v3**: trained with
self-distillation + recall tilt on synthetic + LLM-teacher-labeled real text.

**40 entity types / 81 BIO labels** across ~23 languages and 6 scripts
(Latin, Cyrillic, CJK, Korean, Arabic, Devanagari): names, dates of birth,
emails, phones, street addresses, cities, government/medical/financial IDs,
credit cards, IBANs, API keys, passwords, and more. Trained with OCR-style
corruption (`o→0`, `rn→m`, typos, spacing) and structured-document formats
(JSON/CSV/tables/key-value/EDI), so field names and delimiters aren't mistaken
for PII and scanned text still parses.

## Files

| File | Size | Use |
|------|------|-----|
| `model.safetensors` | 1.2 GB | PyTorch / transformers (fine-tuning, GPU inference; full 256k vocab, matches root `tokenizer.json`) |
| `model.onnx` | 1.2 GB | ONNX fp32 — **nym's default** (accuracy-first) |
| `int8/` | 359 MB | vocab-pruned + embedding-int8 + fp16 body weights (compute stays fp32). **Measured lossless** on the full battery — see below. `token_model = "Wismut/nym-pii-multilingual/int8"` (has its own pruned `tokenizer.json`) |

The previous `int8/` (full dynamic int8, 309 MB) cost a real, initially unnoticed
accuracy loss off-distribution. The v3 `int8/` uses a different stack whose every
step was individually re-benchmarked.

## Benchmarks

Same harness for every row (span-level, label-agnostic; OOD sets never trained on):

| Model | Size | Real-text F1 | ai4privacy OOD | Non-Latin char-F1 |
|-------|------|--------------|----------------|-------------------|
| **v3 fp32 (this)** | 1.2 GB | **79.1** | **69.8** | **73.1** |
| **v3 int8/** | 359 MB | 78.9 | 69.9 | 73.0 |
| v2 fp32 (previous artifact) | 1.2 GB | 73.3 | 51.8 | 50.9 |
| v2 int8 (previous artifact) | 309 MB | 68.3 | 38.2 | 36.1 |
| small v3 (companion repo) | 429 MB | 76.4 | 67.7 | 71.8 |
| OpenMed-PII-mSuperClinical (279M, their best) | 1.1 GB | 81.4 | 55.0 | 60.4 |
| OpenMed-PII-SnowflakeMed (568M) | 2.3 GB | 80.9 | 54.2 | 54.2 |
| OpenMed-PII-SuperClinical-Large (434M) | 1.7 GB | 77.4 | 53.2 | 43.9 |
| OpenMed-PII-SuperClinical-Small (44M) | 172 MB | 78.1 | 44.6 | 46.3 |
| piiranha-v1 | ~600 MB | 60.6 | 62.9 | 43.2 |

OpenMed's clinical-corpus models win the curated real-text F1 column (their
multilingual 279M: 81.4). Off-distribution this model leads their best by
+14.8 ai4 and +12.7 non-Latin, and by ~40 points in-distribution (98.5 vs 59.0)
— pick by what your text looks like.

In-distribution (held-out synthetic): 98.5.

On the independent [REDACT benchmark](https://github.com/guneeshvats/REDACT-PII-Benchmark)
(25 languages / 9 scripts / 51 PII types, type-matched partial micro-F1, their
harness): **this model scores 0.515 — above the OpenAI Privacy Filter (0.512)**,
far above GLiNER-multi (0.320) and Presidio (0.195); GPT-4.1 scores 0.597 and
Claude Sonnet 4.6 0.636. A local 277M model, no API.

The v2→v3 jump has two causes: (1) retraining with self-KD + recall tilt, and
(2) a **corrected ONNX export** — v2's export environment silently ran a
different transformers version whose ModernBERT forward differs, so the shipped
v2 artifact lost ~3.5 ai4 vs its own checkpoint. v3 exports are gate-verified
(torch-vs-ONNX ≤1e-3 at 10 sequence lengths + padded batch).

## Use with nym

This is nym's default token-classification model — with NER enabled it is
downloaded and cached automatically. Explicitly:

```toml
[ner]
enabled = true
backend = "tokens"          # or "both" to also run GLiNER
token_model = "Wismut/nym-pii-multilingual"        # fp32
# token_model = "Wismut/nym-pii-multilingual/int8" # 359 MB, measured lossless
threshold = 0.5
# recall_first = true  # decode on total entity mass: +recall at -precision,
#                      # the right mode for redaction
```

For a 3× smaller model with ~97% of the OOD accuracy, see
[`Wismut/nym-pii-multilingual-small`](https://huggingface.co/Wismut/nym-pii-multilingual-small).

## Use with transformers

```python
from transformers import AutoModelForTokenClassification, AutoTokenizer
tok = AutoTokenizer.from_pretrained("Wismut/nym-pii-multilingual")
model = AutoModelForTokenClassification.from_pretrained("Wismut/nym-pii-multilingual")
```

## How it was trained

1. **Synthetic** (724k) from
   [`Wismut/nym-pii-multilingual-data`](https://huggingface.co/datasets/Wismut/nym-pii-multilingual-data)
   including structured-format templates.
2. **Real text** (77.5k): Wikipedia passages auto-labeled by a large LLM teacher
   (gemma-4-26b); weak `O` tokens masked from the loss.
3. **Self-distillation** from the plain-recipe mmBERT-base teacher
   (KL on all attended tokens, α=0.5, T=2) + **recall tilt** (`--o-weight 0.3`).
   At base size this combination *gains* precision (+3) while lifting recall.
4. **Gate-verified export** (`scripts/export_onnx.py`), then for `int8/`:
   vocab prune (0.999 coverage, 27 corpora) → embedding-only int8 → weight-only
   fp16 body; each step re-benchmarked.

Pipeline: [`scripts/`](https://github.com/byteowlz/nym/tree/main/scripts).

## Limitations

- Trained partly on LLM-labeled Wikipedia text (CC-BY-SA source; not
  redistributed here). Those labels are machine-generated.
- Reference-style IDs (ticket/case numbers) are the weakest class on
  out-of-taxonomy benchmarks — pair with nym's regex patterns (the default
  pipeline does).
- No claim of HIPAA/GDPR compliance by itself; it is a detection component.

## License

MIT (inherited from mmBERT-base). The synthetic training data contains no real
personal information; the real-text training corpus is not distributed with this
model.
