---
license: mit
language:
  - en
  - it
  - de
  - fr
tags:
  - token-classification
  - ner
  - pii
  - anonymization
  - switzerland
pipeline_tag: token-classification
base_model: microsoft/mdeberta-v3-base
datasets: []
metrics: []
---

# sandsiv-278-pii-ch

Multilingual **PII named-entity recognition** model for Swiss-domain texts,
fine-tuned from [microsoft/mdeberta-v3-base](https://huggingface.co/microsoft/mdeberta-v3-base)
(278M parameters, fp32).

Detects 19 PII entity types in **English, Italian, German and French**, with a
focus on Swiss-specific identifiers:

`AHVNUMBER` (Swiss social security), `IBAN`, `CREDITCARD`, `PHONE`, `EMAIL`,
`FULLNAME`, `ADDRESS`, `ZIPCODE`, `CITY`, `CANTON`, `DATEOFBIRTH`, `DATE`,
`TIME`, `AGE`, `GENDER`, `ORG`, `DOCID`, `PLATE`, `LANDREGISTRY`

## Used in production

This model powers the PII detection engine of [**anonymo.io**](https://anonymo.io) —
a local-first desktop app for document sanitization built for Swiss FADP/GDPR
compliance. All inference runs on-device; no document content ever leaves the
machine. Built by [SandSIV](https://sandsiv.com).

## Intended use

PII detection as a building block for anonymization pipelines on Swiss
texts (e.g. customer feedback, support tickets, administrative documents).

## Usage

```python
from transformers import pipeline

ner = pipeline(
    "token-classification",
    model="sandsiv/sandsiv-278-pii-ch",
    aggregation_strategy="simple",
)
ner("Il numero AVS di Anna Bianchi è 756.1234.5678.97.")
# -> FULLNAME 'Anna Bianchi', AHVNUMBER '756.1234.5678.97'
```

Note: the model is stored in **fp32**. Do not load it with `dtype="auto"`
from code paths that would cast to fp16 before inference on CPU/MPS.

## ONNX export (production deployment)

The `onnx/` folder contains the exported model, verified to match the PyTorch
reference (see evaluation below):

| File | Size | Entity-level F1 (val subset) |
|---|---|---|
| `onnx/model.onnx` (fp32) | 1.11 GB | 0.9991 (identical to PyTorch) |
| `onnx/model-int8.onnx` (dynamic int8) | 338 MB | 0.9978 (−0.0013 vs PyTorch) |

Inference requires only `onnxruntime` + `tokenizers` (no PyTorch/transformers).
Session inputs: `input_ids`, `attention_mask`. Outputs: per-token `logits`
(39 BIO labels — see `config.json` `id2label`).

```python
import numpy as np
import onnxruntime as ort
from tokenizers import Tokenizer

tok = Tokenizer.from_file("tokenizer.json")  # from onnx/ or the repo root
tok.enable_truncation(128)
tok.enable_padding()

sess = ort.InferenceSession("onnx/model-int8.onnx")
enc = tok.encode_batch(["Il numero AVS di Anna Bianchi è 756.1234.5678.97."],
                       is_pretokenized=False)
logits = sess.run(["logits"], {
    "input_ids": np.array([e.ids for e in enc], dtype=np.int64),
    "attention_mask": np.array([e.attention_mask for e in enc], dtype=np.int64),
})[0]
```

Post-processing hint: merge adjacent same-label spans and trim boundary
punctuation for clean entity strings.

## Training data

100% **synthetic** data (generator `ch-pii-synth-0.3.0` + targeted supplement),
no real personal data was used. 29'000 examples, balanced across the 4
languages (7'250 each), 232+ templates, split 90/5/5 stratified by language.

## Evaluation

| Metric | Value |
|---|---|
| Test set entity-level F1 (seqeval) | **0.9988** |
| — per language: de / en / fr / it | 1.0000 / 0.9988 / 0.9988 / 0.9975 |
| Hand-written out-of-template realistic set (26 sentences) | F1 **0.964** (P 0.947, R 0.982) |

Cross-generator robustness (8'000 samples from
[ai4privacy/pii-masking-200k](https://huggingface.co/datasets/ai4privacy/pii-masking-200k),
binary char-level PII detection): P 0.905 / R 0.552 / F1 0.685 overall —
recall **0.891 on entity types covered by training** (EMAIL, names, dates,
addresses, phones, companies), 0.32 on types never trained (user-agent
strings, crypto addresses, IPs, job titles). Precision is a lower bound:
ai4privacy masks only a subset of PII per text.

## Limitations

- Trained on synthetic data only: expect a quality gap on real-world text
  whose style differs from the generator's templates.
- Known weakness: document IDs with a letter prefix (e.g. `S1234567A`) may be
  split or partially mislabeled as `PLATE`.
- Entities spanning multiple SentencePiece subwords can occasionally be
  returned as adjacent fragments when using `aggregation_strategy="simple"`;
  merging adjacent same-label spans fixes this.
- `AGE` is the weakest entity type (test F1 ≈ 0.95).

## Training configuration

lr 2e-5 · batch 16 · 4 epochs · weight decay 0.01 · warmup 10% · max length
128 · best checkpoint on validation entity-level F1 · Apple Silicon (MPS)

## License

MIT (same as the base model).
