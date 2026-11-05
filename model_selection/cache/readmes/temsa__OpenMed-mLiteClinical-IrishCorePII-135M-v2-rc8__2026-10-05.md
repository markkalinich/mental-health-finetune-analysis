---
language:
- en
- ga
license: apache-2.0
library_name: transformers
pipeline_tag: token-classification
tags:
- pii
- de-identification
- token-classification
- ireland
- irish
- gaelic
- raw-only
- ppsn
- eircode
- passport
- phone-number
- onnx
- int8
- dynamic-quantization
base_model:
- OpenMed/OpenMed-PII-mLiteClinical-Base-135M-v1
datasets:
- temsa/OpenMed-Irish-CorePII-TrainMix-v1
- temsa/OpenMed-Irish-PPSN-Eircode-Spec-v1
- joelniklaus/mapa
- gretelai/synthetic_pii_finance_multilingual
---

# OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc8

Raw-only Irish core PII release derived from `OpenMed/OpenMed-PII-mLiteClinical-Base-135M-v1`.

This repo does **not** require the scanner / validator layer used by `temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc7`.
Both the full checkpoint and the ONNX q8 artifact use the same learned score-only decoder over token-presence and typed boundary heads.

## Coverage

- `PPSN`
- `ACCOUNT_NUMBER`
- `BANK_ROUTING_NUMBER`
- `CREDIT_DEBIT_CARD`
- `PASSPORT_NUMBER`
- `POSTCODE`
- `PHONE_NUMBER`
- `EMAIL`
- `FIRST_NAME`
- `LAST_NAME`
- `SWIFT_BIC`

## Included Variants

- Full `transformers` checkpoint in the repo root
- Unquantized ONNX export in `onnx/model.onnx`
- Dynamic q8 ONNX artifact in `onnx/model_quantized.onnx`
- `inference_mask.py` for the full checkpoint
- `inference_mask_onnx.py` for the ONNX q8 artifact
- `common.py`, `model.py`, and `multitask_model.py` implementing the raw-only decoder
- benchmark files in `eval/`

Artifact sizes:

- Full checkpoint: `515 MB` (`model.safetensors`)
- Dynamic q8 ONNX: `393 MB` (`onnx/model_quantized.onnx`)

## What Changed From rc7

`rc7` achieves its public quality with a bundled scanner / validator inference stack.

`rc8` removes that layer completely:

- no regex-based candidate extraction
- no checksum validator dependency at inference time
- no separate scanner spec or generated scanner code
- same compact `mLiteClinical` encoder family, but with a raw-only multi-head decoder

The tradeoff is explicit:

- `rc7` is still stronger on the broad manual Irish core suite
- `rc8` is easier to embed, simpler to maintain, and its ONNX q8 path stays very close to the full checkpoint

## Architecture

`rc8` keeps the DistilBERT-size encoder class of the 135M `mLiteClinical` base and adds:

- a token-presence head for each released label
- a typed start-boundary head
- a typed end-boundary head
- a score-only decoder that uses model scores, token offsets, continuity priors, and minimum-length priors from config

There is no scanner or external validator in the release path.

Design references that informed this direction:

- Split-NER: https://aclanthology.org/2023.acl-short.36/
- SpanNER: https://aclanthology.org/2021.acl-long.558/
- Boundary Smoothing for Named Entity Recognition: https://aclanthology.org/2022.acl-long.490/
- TinyBERT: https://aclanthology.org/2020.findings-emnlp.372/

## How To Use It

Full checkpoint:

```bash
uv run python inference_mask.py \
  --model temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc8 \
  --min-score 0.5 \
  --text "My PPSN is 1234567TW, my Eircode is D02 X285, and my phone is 087 123 4567." \
  --json
```

Dynamic q8 ONNX:

```bash
uv run python inference_mask_onnx.py \
  --model temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc8 \
  --min-score 0.5 \
  --text "Please provide your passport NN5123456 and call me on 0851234567." \
  --json
```

## Benchmarks

Main comparison:

| Model | Irish core F1 | Edge F1 | Finance F1 | Finance-boundary F1 | User PPSN F1 | GA weak PPSN F1 | Multilingual PPSN F1 | Core CPU ex/s | Multilingual CPU ex/s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Base OpenMed | 0.3743 | 0.0556 | - | - | - | - | 0.0000 | 15.1811 | 37.4666 |
| Previous public `rc7` full | 1.0000 | - | 1.0000 | 1.0000 | - | 1.0000 | - | 3.5394 | - |
| Previous public `rc7` ONNX q8 | 0.9934 | - | 1.0000 | 1.0000 | - | 1.0000 | - | 12.1653 | - |
| `rc8` full | 0.9737 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.9176 | 2.2965 | 6.3095 |
| `rc8` ONNX q8 | 0.9737 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.9176 | 46.1420 | 99.7166 |

Irish core label breakdown:

| Label | `rc8` full | `rc8` ONNX q8 |
|---|---:|---:|
| PPSN | 1.0000 | 1.0000 |
| PHONE_NUMBER | 0.9565 | 0.9565 |
| POSTCODE | 1.0000 | 1.0000 |
| ACCOUNT_NUMBER | 0.8000 | 0.8000 |
| PASSPORT_NUMBER | 1.0000 | 1.0000 |
| EMAIL | 1.0000 | 1.0000 |
| FIRST_NAME | 0.9744 | 0.9744 |
| LAST_NAME | 0.9744 | 0.9744 |

## Dynamic q8 Artifact

Artifact paths:

- unquantized: `onnx/model.onnx`
- preprocessed: `onnx/model.preprocessed.onnx`
- quantized: `onnx/model_quantized.onnx`

Quantization recipe used here:

- ONNX pre-processing before quantization
- ONNX Runtime dynamic int8
- `qint8`
- `per_channel=true`
- `op_types=MatMul,Gemm,Attention`

For CPU deployment, the ONNX q8 artifact is the recommended default.

## Limits

- `rc8` is raw-only. It intentionally gives up the scanner/validator stack used by `rc7`, so its broad manual-suite ceiling is lower.
- The current remaining local misses are a bare 8-digit account-number case and one Gaelic phone-number case in the manual core suite.
- If you need the exact `rc8` behavior, use the bundled inference scripts or import `decode_token_presence_segments` from `common.py`.

## License And Attribution

- Release license: Apache-2.0
- Base model: `OpenMed/OpenMed-PII-mLiteClinical-Base-135M-v1`
- See `NOTICE` and `training_sources.json` for attribution and training details.

<!-- portfolio-comparison:start -->
## Portfolio Comparison

Updated: `2026-03-16`.

Use this section for the fastest public comparison across the `temsa` PII masking portfolio.

- The first core table only includes public checkpoints that ship both comparable q8 accuracy and q8 CPU throughput.
- The first PPSN table only includes public artifacts that ship comparable PPSN accuracy and CPU throughput.
- Missing cells in the archive tables mean the older release did not ship that metric in its public bundle.
- DiffMask rows use the reconciled `clean_single_pass` harness that matches the deployed runtime.
- GlobalPointer rows use the public raw-only span-matrix release bundle and its packaged q8 ONNX artifact.
- The same content is shipped as `PORTFOLIO_COMPARISON.md` inside each public model repo.

### Irish Core PII: Comparable Public Checkpoints

| Repo | Stack | Full Core F1 | Q8 Core F1 | Q8 Multilingual PPSN F1 | Q8 Core ex/s |
|---|---|---:|---:|---:|---:|
| [`temsa/IrishCore-GlobalPointer-ContextPII-4L-122M-v1-rc4`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-4L-122M-v1-rc4) | 4-layer GlobalPointer distilled fast student | 1.0000 | 1.0000 | 0.9333 | 299.0 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-4L-122M-v1-rc3`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-4L-122M-v1-rc3) | 4-layer GlobalPointer distilled fast student | 1.0000 | 1.0000 | 0.9333 | 317.9 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-4L-122M-v1-rc2`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-4L-122M-v1-rc2) | 4-layer GlobalPointer distilled fast student | 1.0000 | 1.0000 | 0.9333 | 292.5 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-4L-122M-v1-rc1`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-4L-122M-v1-rc1) | 4-layer GlobalPointer distilled fast student | 1.0000 | 1.0000 | 0.9333 | 337.3 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc27`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc27) | GlobalPointer raw-only + context labels | 1.0000 | 1.0000 | 0.9333 | 270.0 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc25`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc25) | GlobalPointer raw-only + context labels | 1.0000 | 1.0000 | 0.9333 | 212.1 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc24`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc24) | GlobalPointer raw-only + context labels | 1.0000 | 1.0000 | 0.9333 | 278.9 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc23`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc23) | GlobalPointer raw-only + context labels | 1.0000 | 1.0000 | 0.9333 | 237.6 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc22`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc22) | GlobalPointer raw-only + context labels | 1.0000 | 1.0000 | 0.9333 | 106.8 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc21`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc21) | GlobalPointer raw-only + context labels | 1.0000 | 1.0000 | 0.9333 | 150.8 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc20`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc20) | GlobalPointer raw-only + context labels | 1.0000 | 1.0000 | 0.9333 | 181.9 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc19`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc19) | GlobalPointer raw-only + context labels | 1.0000 | 1.0000 | 0.9333 | 73.1 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc18`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc18) | GlobalPointer raw-only + context labels | 1.0000 | 1.0000 | 0.9333 | 126.2 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc17`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc17) | GlobalPointer raw-only + context labels | 1.0000 | 1.0000 | 0.9333 | 125.5 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc16`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc16) | GlobalPointer raw-only + context labels | 1.0000 | 1.0000 | 0.9333 | 125.5 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc15`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc15) | GlobalPointer raw-only + context labels | 1.0000 | 1.0000 | 0.9333 | 125.5 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc14`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc14) | GlobalPointer raw-only + context labels | 1.0000 | 1.0000 | 0.9333 | 119.2 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc13`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc13) | GlobalPointer raw-only + context labels | 1.0000 | 1.0000 | 0.9333 | 126.1 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc12`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc12) | GlobalPointer raw-only + context labels | 1.0000 | 1.0000 | 0.9333 | 73.6 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc11`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc11) | GlobalPointer raw-only + context labels | 1.0000 | 1.0000 | 0.9333 | 94.1 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc10`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc10) | GlobalPointer raw-only + context labels | 1.0000 | 1.0000 | 0.9333 | 125.8 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc9`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc9) | GlobalPointer raw-only + context labels | 1.0000 | 1.0000 | 0.9333 | 119.8 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc8`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc8) | GlobalPointer raw-only + context labels | 1.0000 | 1.0000 | 0.9333 | 128.9 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc7`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc7) | GlobalPointer raw-only + context labels | 1.0000 | 1.0000 | 0.9333 | 89.0 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc6`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc6) | GlobalPointer raw-only + context labels | 1.0000 | 1.0000 | 0.9333 | 89.0 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc5`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc5) | GlobalPointer raw-only + context labels | 1.0000 | 1.0000 | 0.9333 | 84.5 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc4`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc4) | GlobalPointer raw-only + context labels | 0.9935 | 0.9935 | 0.9333 | 61.5 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc3`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc3) | GlobalPointer raw-only + context labels | 0.9935 | 0.9935 | 0.9333 | 61.5 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc2`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc2) | GlobalPointer raw-only + context labels | 0.9935 | 0.9935 | 0.9222 | 61.5 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc1`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc1) | GlobalPointer raw-only + context labels | 0.9935 | 0.9935 | 0.9222 | 61.5 |
| [`temsa/IrishCore-GlobalPointer-135M-v1-rc4`](https://huggingface.co/temsa/IrishCore-GlobalPointer-135M-v1-rc4) | GlobalPointer raw-only span-matrix | 1.0000 | 1.0000 | 0.9333 | 221.6 |
| [`temsa/IrishCore-GlobalPointer-135M-v1-rc3`](https://huggingface.co/temsa/IrishCore-GlobalPointer-135M-v1-rc3) | GlobalPointer raw-only span-matrix | 1.0000 | 1.0000 | 0.9213 | 204.9 |
| [`temsa/IrishCore-GlobalPointer-135M-v1-rc2`](https://huggingface.co/temsa/IrishCore-GlobalPointer-135M-v1-rc2) | GlobalPointer raw-only span-matrix | 0.9934 | 0.9934 | 0.9326 | 231.2 |
| [`temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc8`](https://huggingface.co/temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc8) | Raw-only token-span | 0.9737 | 0.9737 | 0.9176 | 46.1 |
| [`temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc7`](https://huggingface.co/temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc7) | Hybrid classifier + generated scanner spec | 1.0000 | 0.9934 | 1.0000 | 30.0 |
| [`temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc6`](https://huggingface.co/temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc6) | Hybrid classifier + repair decoders | 1.0000 | 0.9934 | 1.0000 | 29.5 |
| [`temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc5`](https://huggingface.co/temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc5) | Hybrid classifier + repair decoders | 0.9737 | 0.9669 | 0.9333 | 34.4 |
| [`temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc4`](https://huggingface.co/temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc4) | Hybrid classifier + repair decoders | 0.9870 | 0.9740 | 0.9600 | 114.2 |
| [`temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc3`](https://huggingface.co/temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc3) | Hybrid classifier + repair decoders | 0.9806 | 0.9677 | 0.9333 | 44.9 |
| [`temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc2`](https://huggingface.co/temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc2) | Hybrid classifier + repair decoders | 0.9554 | 0.9615 | 0.7887 | 119.1 |
| [`temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v1`](https://huggingface.co/temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v1) | Hybrid classifier baseline | 0.9530 | 0.9333 | 0.9882 | 103.3 |
| [`temsa/IrishCore-DiffMask-135M-v1-rc6`](https://huggingface.co/temsa/IrishCore-DiffMask-135M-v1-rc6) | DiffMask token-span, scanner-free | 0.9801 | 0.9733 | 0.9274 | 130.3 |
| [`temsa/IrishCore-DiffMask-135M-v1-rc5`](https://huggingface.co/temsa/IrishCore-DiffMask-135M-v1-rc5) | DiffMask token-span, scanner-free | 0.9733 | 0.9733 | 0.9379 | 249.2 |
| [`temsa/IrishCore-DiffMask-135M-v1-rc4`](https://huggingface.co/temsa/IrishCore-DiffMask-135M-v1-rc4) | DiffMask token-span, scanner-free | 0.9733 | 0.9733 | 0.9371 | 29.5 |
| [`temsa/IrishCore-DiffMask-135M-v1-rc3`](https://huggingface.co/temsa/IrishCore-DiffMask-135M-v1-rc3) | DiffMask token-span, scanner-free | 0.9664 | 0.9664 | 0.9591 | 30.0 |
| [`temsa/IrishCore-DiffMask-135M-v1-rc2`](https://huggingface.co/temsa/IrishCore-DiffMask-135M-v1-rc2) | DiffMask token-span, scanner-free | 0.9664 | 0.9664 | 0.9212 | 247.1 |
| [`temsa/IrishCore-DiffMask-135M-v1-rc1`](https://huggingface.co/temsa/IrishCore-DiffMask-135M-v1-rc1) | DiffMask token-span, scanner-free | 0.9801 | 0.9934 | 0.9412 | 251.2 |

### Irish Core PII: Other Public Checkpoints

| Repo | Stack | Full Core F1 | Q8 Core F1 | Q8 Multilingual PPSN F1 | Notes |
|---|---|---:|---:|---:|---|
| [`temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc1`](https://huggingface.co/temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc1) | Hybrid classifier prototype | 0.9487 | — | — | Predates the public q8 artifact. |

Finance-boundary q8 F1 is `1.0000` for `OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc6`, `OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc7`, `OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc8`, and all public `IrishCore-DiffMask` releases from `rc1` to `rc6`. `OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc5` ships `0.8750` on that public q8 suite.

### PPSN-Only: Comparable Public Artifacts

| Repo | Artifact | Irish Large F1 | Multilingual PPSN F1 | User Raw F1 | QA v8 F1 | CPU ex/s |
|---|---|---:|---:|---:|---:|---:|
| [`temsa/OpenMed-mLiteClinical-IrishPPSN-135M-v1`](https://huggingface.co/temsa/OpenMed-mLiteClinical-IrishPPSN-135M-v1) | fp32 canonical checkpoint | 0.8979 | 0.9704 | 0.8000 | 0.7385 | 57.4 |
| [`temsa/OpenMed-mLiteClinical-IrishPPSN-135M-v1-fp16`](https://huggingface.co/temsa/OpenMed-mLiteClinical-IrishPPSN-135M-v1-fp16) | fp16 CPU/GPU artifact | — | 0.9704 | 0.8000 | 0.7385 | 45.8 |
| [`temsa/OpenMed-mLiteClinical-IrishPPSN-135M-v1-q8`](https://huggingface.co/temsa/OpenMed-mLiteClinical-IrishPPSN-135M-v1-q8) | dynamic int8 CPU artifact | — | 0.9040 | — | — | 132.1 |

### PPSN-Only: Historical Public Checkpoints

| Repo | Main Published Metrics | Notes |
|---|---|---|
| [`temsa/OpenMed-PPSN-mLiteClinical-v1`](https://huggingface.co/temsa/OpenMed-PPSN-mLiteClinical-v1) | same as canonical fp32 repo: multilingual 0.9704, user raw 0.8000 | Legacy alias; prefer `temsa/OpenMed-mLiteClinical-IrishPPSN-135M-v1`. |
| [`temsa/OpenMed-PPSN-v6-raw-rc2`](https://huggingface.co/temsa/OpenMed-PPSN-v6-raw-rc2) | irish_reg_v5 0.8750; user_raw 0.8000; qa_v8 0.7385 | Raw PPSN-only research checkpoint; no packaged multilingual CPU benchmark row. |
| [`temsa/OpenMed-PPSN-v5_1`](https://huggingface.co/temsa/OpenMed-PPSN-v5_1) | irish_large_v2 raw 0.9285; qa_v6 hybrid strict 1.0000 | Hybrid PPSN-only checkpoint; predates the canonical multilingual suite packaging. |
| [`temsa/OpenMed-PPSN-v5`](https://huggingface.co/temsa/OpenMed-PPSN-v5) | irish_reg_v5 raw 0.8235; irish_reg_v5 hybrid strict 1.0000 | Hybrid PPSN-only checkpoint; predates the canonical multilingual suite packaging. |
| [`temsa/OpenMed-PPSN-v4`](https://huggingface.co/temsa/OpenMed-PPSN-v4) | synthetic non-PPSN drift check only | Predates the current PPSN eval suite; no packaged apples-to-apples multilingual CPU row. |

If you need the strongest current raw-only Irish core model, start with `IrishCore-GlobalPointer-135M-v1-rc4`. If you need the fastest CPU-first raw-only line, compare it against `IrishCore-DiffMask-135M-v1-rc6`. If you need a PPSN-only artifact, compare the canonical `fp32`, `fp16`, and `q8` variants of `OpenMed-mLiteClinical-IrishPPSN-135M-v1` directly in the table above.
<!-- portfolio-comparison:end -->
