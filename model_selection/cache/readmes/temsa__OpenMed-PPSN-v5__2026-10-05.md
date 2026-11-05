---
language:
- en
- ga
license: apache-2.0
library_name: transformers
tags:
- pii
- token-classification
- healthcare
- de-identification
- ireland
- ppsn
base_model:
- OpenMed/OpenMed-PII-SuperClinical-Large-434M-v1
datasets:
- nvidia/Nemotron-PII
- joelniklaus/mapa
model-index:
- name: OpenMed-PPSN-v5
  results:
  - task:
      type: token-classification
      name: PPSN detection (Irish regression set)
    dataset:
      name: irish_ppsn_regression_v5
      type: custom
    metrics:
    - type: f1
      value: 0.8235
      name: Raw model F1
    - type: f1
      value: 1.0000
      name: Hybrid strict F1
---

# OpenMed PPSN v5

Token classification model derived from `OpenMed/OpenMed-PII-SuperClinical-Large-434M-v1` with added `B-PPSN` / `I-PPSN` support for Irish PPS Number detection.

## What this release contains

- Full model weights (`model.safetensors`) with original OpenMed labels + PPSN labels.
- `label_meta.json` with label mapping and provenance.
- Repro/eval artifacts:
  - `irish_ppsn_regression_v5.jsonl`
  - `eval_manual_irish_v5_raw.json`
  - `eval_hybrid_v5_no_plausible.json`
  - `ab_non_ppsn_v5_baseline.json`

## Key results

On `irish_ppsn_regression_v5`:

- Raw model-only PPSN performance: `P=0.7778 R=0.8750 F1=0.8235`.
- Recommended strict hybrid mode (model + checksum + span normalization, no plausible fallback):
  - `P=1.0000 R=1.0000 F1=1.0000`.

Non-PPSN retention check vs base OpenMed (A/B):

- Real-text behavior agreement F1: `1.0000`.
- Entity density unchanged in the sampled real-text proxy set.

## Recommended production usage

For best PPSN reliability, run this model with a strict hybrid post-processor:

1. Keep model detections for all labels.
2. For PPSN specifically, normalize/expand spans to full PPSN candidates.
3. Validate PPSN with checksum.
4. Disable broad "plausible" fallback in production (`no-plausible-ppsn`).

This repository includes only the model artifacts; hybrid scripts are in the companion codebase used to train/evaluate this release.

For a quick local smoke test of the packaged checkpoint, use the bundled `word_aligned` helper:

```bash
python3 inference_word_aligned.py \
  --ppsn-min-score 0.4 \
  --text "My PPSN is 1234567TW and I need help with my housing grant." \
  --json
```

Install dependencies from `pyproject.toml` first if you are not already in an environment with `transformers`, `torch`, and `regex`.

## Limitations

- The Irish regression set is small and targeted; additional domain-specific validation is required before regulated deployment.
- PPSN detection in noisy OCR/ASR or heavily malformed text may require extra hardening.

## License and attribution

- This derivative release is distributed under Apache-2.0, consistent with the base model license tag.
- Base model: `OpenMed/OpenMed-PII-SuperClinical-Large-434M-v1`.
- Training/evaluation used synthetic and augmented data sources, including `nvidia/Nemotron-PII` and `joelniklaus/mapa`.
- See `NOTICE` for attribution details.

## QA quick check

- Load this model as a standard `AutoModelForTokenClassification` checkpoint.
- Run against `irish_ppsn_regression_v5.jsonl`.
- Confirm results in `eval_manual_irish_v5_raw.json` (raw) and `eval_hybrid_v5_no_plausible.json` (strict hybrid).

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
