---
language:
- en
- ga
license: apache-2.0
library_name: transformers
pipeline_tag: token-classification
tags:
- pii
- token-classification
- de-identification
- ireland
- irish
- gaelic
- ppsn
- eircode
- phone-number
- iban
- passport
- onnx
- quantized
- release-candidate
base_model:
- OpenMed/OpenMed-PII-mLiteClinical-Base-135M-v1
datasets:
- temsa/OpenMed-Irish-CorePII-TrainMix-v1
- temsa/OpenMed-Irish-PPSN-Eircode-Spec-v1
- joelniklaus/mapa
- gretelai/synthetic_pii_finance_multilingual
model-index:
- name: OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc4
  results:
  - task:
      type: token-classification
      name: Irish core PII detection
    dataset:
      type: custom
      name: irish_core_pii_v1
    metrics:
    - type: f1
      name: Overall F1
      value: 0.9870
  - task:
      type: token-classification
      name: Multilingual PPSN detection
    dataset:
      type: custom
      name: multilingual_ppsn_v1_all
    metrics:
    - type: f1
      name: PPSN-only F1
      value: 0.9545
---

# temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc4

Fourth QA release candidate for Irish core PII detection with OpenMed mLiteClinical.

This repository should be evaluated against:

- current public candidate: `temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc3`
- stable public release: `temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v1`
- this repository: `temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc4`

This RC improves the current public candidate on the main release-gating suites without reopening the PPSN false positives that were addressed after `v2-rc3`.

## Included Variants

| Variant | Artifact | Backend | Recommended Thresholds | Intended Use |
|---|---|---|---|---|
| Full checkpoint | repo root | `transformers` | `ppsn=0.71`, `other=0.50` | highest-fidelity evaluation and deployment |
| Quantized checkpoint | `onnx/model_quantized.onnx` | ONNX Runtime dynamic int8 | `ppsn=0.71`, `other=0.60` | CPU-oriented deployment |

## Coverage

- `PPSN`
- `account_number`
- `bank_routing_number`
- `credit_debit_card`
- `PASSPORT_NUMBER`
- `postcode`
- `phone_number`
- `email`
- `first_name`
- `last_name`
- `swift_bic`

The main focus is English and Irish Gaelic handling for Irish administrative, citizen-support, and HSE-style text.

## Recommended Inference

Full checkpoint:

```bash
uv run python inference_mask.py \
  --model temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc4 \
  --ppsn-min-score 0.71 \
  --other-min-score 0.50 \
  --text "My PPSN is 1234567T and my sort code is 90-00-17." \
  --json
```

Fast CPU path with the bundled ONNX q8 artifact:

```bash
uv run python inference_mask_onnx.py \
  --model temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc4 \
  --ppsn-min-score 0.71 \
  --other-min-score 0.60 \
  --text "Please provide your passport: NN5123456." \
  --json
```

If you prefer plain `python3`, install the dependencies from `pyproject.toml` first.

## What Improved Versus `temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc3`

Full checkpoint:

- core suite F1: `0.9806` -> `0.9870`
- overlap suite F1: `0.9429` -> `1.0000`
- strict remaining IoU=1.0 F1: `0.4444` -> `0.6000`
- multilingual PPSN-only F1: `0.9333` -> `0.9545`
- matches the current public candidate on `edge`, `numeric`, `gap`, and `user` PPSN regression F1

Bundled ONNX q8:

- core suite F1: `0.9677` -> `0.9804`
- multilingual PPSN-only F1: `0.9333` -> `0.9600`
- keeps the overlap and strict remaining gains from `v2-rc3`
- q8 remains weaker than the full checkpoint on the small edge suite: `0.9474` vs `1.0000`

## Benchmark Table

| Variant | Core | Edge | Numeric | Gap | User PPSN | Overlap | Strict Remaining IoU=1.0 | Multilingual PPSN |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc3` full | 0.9806 | 1.0000 | 0.9333 | 0.9167 | 1.0000 | 0.9429 | 0.4444 | 0.9333 |
| `temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc4` full | 0.9870 | 1.0000 | 0.9333 | 0.9167 | 1.0000 | 1.0000 | 0.6000 | 0.9545 |
| `temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc3` ONNX q8 | 0.9677 | 1.0000 | 0.9333 | 0.9167 | 1.0000 | 1.0000 | 0.6667 | 0.9333 |
| `temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc4` ONNX q8 | 0.9804 | 0.9474 | 0.9333 | 0.9167 | 1.0000 | 1.0000 | 0.6667 | 0.9600 |

## Quantized Artifact

The bundled quantized artifact is:

- `onnx/model_quantized.onnx`

For this release line, the promoted q8 recipe remains the standard ONNX Runtime dynamic int8 export with per-channel quantization over `MatMul`, `Gemm`, and `Attention`.

Two alternatives were reviewed and not promoted for this model family:

- QAT in this DistilBERT token-classification stack
- Mezzanine's recent Qwen-focused weight transforms

## Known Limits

This is still a raw token-classification release candidate without hybrid rule logic. QA should still test these carefully:

- `Passport PA 1234567 was used to board the flight.`
- `Usaideadh pas PA 1234567 chun dul ar bord an eitilt.`
- `Call me on 0851234567 tomorrow.`

## Included Files

- full `transformers` checkpoint in the repo root
- dynamic int8 ONNX artifact in `onnx/model_quantized.onnx`
- `inference_mask.py`
- `inference_mask_onnx.py`
- `qa_config.json`
- `training_sources.json`
- benchmark summaries in `eval/`

## License And Attribution

- release license: Apache-2.0
- base model: `OpenMed/OpenMed-PII-mLiteClinical-Base-135M-v1`
- upstream attributed data: `joelniklaus/mapa`, `gretelai/synthetic_pii_finance_multilingual`
- synthetic Irish training and replay data created in this workspace

See `NOTICE` for attribution details.

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
