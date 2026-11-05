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
---

# temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc2

Second QA release candidate for Irish core PII detection with OpenMed mLiteClinical.

This repository should be evaluated against the public release and the previous RC:

- current public release: `temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v1`
- previous RC: `temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc1`
- this repository: `temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc2`

The purpose of this RC is specific: keep the `v2-rc1` weak-context PPSN recovery and improve the QA regressions reported afterwards for:

- passport numbers like `PA1234567`, `NN5123456`, and some Irish Gaelic passport phrasing
- Irish sort codes like `90-00-17`, `90 01 18`, and `900118`
- broader Irish-core stability relative to the public `v1` release

This repo now also includes a bundled dynamic int8 ONNX export for CPU inference in `onnx/model_quantized.onnx`.

## Included Variants

| Variant | Artifact | Backend | Intended Use |
|---|---|---|---|
| Full checkpoint | repo root | `transformers` | highest-fidelity evaluation and deployment |
| Quantized checkpoint | `onnx/model_quantized.onnx` | ONNX Runtime dynamic int8 | CPU-oriented deployment with a smaller/faster artifact |

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

## Recommended Inference

Full checkpoint:

```bash
python3 inference_mask.py \
  --model temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc2 \
  --ppsn-min-score 0.5 \
  --other-min-score 0.35 \
  --text "My sort code is 90-00-17 for AIB." \
  --json
```

Fast CPU path with the bundled ONNX q8 artifact:

```bash
python3 inference_mask_onnx.py \
  --model temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc2 \
  --ppsn-min-score 0.5 \
  --other-min-score 0.35 \
  --text "Please provide your passport: NN5123456." \
  --json
```

## Quantized Artifact

The bundled quantized artifact is:

- `onnx/model_quantized.onnx`

It was benchmarked against the full `v2-rc2` checkpoint and the public baselines at the same release thresholds.

Short reading:

- exact QA: ONNX q8 is below the full checkpoint on passport boundary cases, but it keeps the routing and phone gains
- English/Irish core suite: ONNX q8 is slightly higher overall than the full checkpoint on this suite
- multilingual PPSN suite: ONNX q8 is below the full checkpoint and far below the public `v1` PPSN-focused release
- CPU throughput: ONNX q8 is much faster on the Irish core and edge suites, but not on every workload

## Comparison To Public `v1`, `v2-rc1`, And ONNX q8

Exact QA suites:

| Model | Numeric v2 | Passport | Routing | Phone | Gap | Passport | Routing | Phone |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v1` | 0.3000 | 0.5000 | 0.3333 | 0.0000 | 0.2667 | 0.3333 | 0.4000 | 0.0000 |
| `temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc1` | 0.2105 | 0.0000 | 0.0000 | 0.5000 | 0.1333 | 0.0000 | 0.0000 | 0.3333 |
| `temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc2` | 0.8966 | 0.9091 | 1.0000 | 0.7500 | 0.8696 | 0.8889 | 1.0000 | 0.6667 |
| `temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc2` ONNX q8 | 0.8387 | 0.7692 | 1.0000 | 0.7500 | 0.8333 | 0.8000 | 1.0000 | 0.6667 |

Broader CPU benchmarks:

| Model | User PPSN | Core | Edge | Multilingual PPSN | Core PPSN | Edge PPSN |
|---|---:|---:|---:|---:|---:|---:|
| `OpenMed/OpenMed-PII-mLiteClinical-Base-135M-v1` | 0.0000 | 0.5409 | 0.0513 | 0.0000 | 0.0000 | 0.0000 |
| `temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v1` | 0.5000 | 0.9530 | 0.5714 | 0.9940 | 0.8000 | 0.5000 |
| `temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc1` | 1.0000 | 0.9487 | 0.8205 | 0.7568 | 0.8571 | 0.8571 |
| `temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc2` | 1.0000 | 0.9554 | 0.9500 | 0.8038 | 0.8571 | 0.8571 |
| `temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc2` ONNX q8 | 1.0000 | 0.9615 | 0.9500 | 0.7887 | 0.8571 | 0.8571 |

CPU throughput:

| Model | Core ex/s | Edge ex/s | Multilingual PPSN ex/s |
|---|---:|---:|---:|
| `temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc2` | 27.4796 | 30.1890 | 131.0956 |
| `temsa/OpenMed-mLiteClinical-IrishCorePII-135M-v2-rc2` ONNX q8 | 119.0614 | 69.9669 | 86.9493 |

## Practical Reading Of The ONNX q8 Results

- The ONNX q8 artifact keeps the RC's user PPSN regression score at `1.0000` and the edge-suite overall score at `0.9500`.
- On the exact QA suites, ONNX q8 is still strong on bank routing and phone, but the full checkpoint is better on passport boundary cases.
- On the English/Irish core suite used for this release, ONNX q8 is slightly better overall than the full checkpoint at the same thresholds.
- The main quality cost of ONNX q8 in this release line is multilingual PPSN precision: `0.7887` for ONNX q8 vs `0.8038` for the full checkpoint, and both are below the public `v1` PPSN-focused release (`0.9940`).

## Known Limits

This is still a raw-model-only release candidate. QA should still test these carefully:

- standalone compact Irish mobile numbers such as `0851234567`
- compact Irish mobiles in short contexts such as `Call me on 0851234567 tomorrow.`
- passport values written as prefix + space + digits, such as `Passport PA 1234567 was used to board the flight.`

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
- synthetic Irish training data created in this workspace

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
| [`temsa/IrishCore-GlobalPointer-ContextPII-4L-122M-v1-rc6`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-4L-122M-v1-rc6) | 4-layer GlobalPointer distilled fast student | 1.0000 | 1.0000 | 0.9333 | 282.9 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-4L-122M-v1-rc5`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-4L-122M-v1-rc5) | 4-layer GlobalPointer distilled fast student | 1.0000 | 1.0000 | 0.9333 | 282.9 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-4L-122M-v1-rc3`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-4L-122M-v1-rc3) | 4-layer GlobalPointer distilled fast student | 1.0000 | 1.0000 | 0.9333 | 317.9 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-4L-122M-v1-rc2`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-4L-122M-v1-rc2) | 4-layer GlobalPointer distilled fast student | 1.0000 | 1.0000 | 0.9333 | 292.5 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-4L-122M-v1-rc1`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-4L-122M-v1-rc1) | 4-layer GlobalPointer distilled fast student | 1.0000 | 1.0000 | 0.9333 | 337.3 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc29`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc29) | GlobalPointer raw-only + context labels | 1.0000 | 1.0000 | 0.9333 | 232.7 |
| [`temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc28`](https://huggingface.co/temsa/IrishCore-GlobalPointer-ContextPII-135M-v1-rc28) | GlobalPointer raw-only + context labels | 1.0000 | 1.0000 | 0.9333 | 232.7 |
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
