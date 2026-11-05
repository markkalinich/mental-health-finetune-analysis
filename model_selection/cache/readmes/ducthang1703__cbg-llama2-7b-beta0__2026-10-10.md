---
base_model: meta-llama/Llama-2-7b-chat-hf
license: llama2
library_name: transformers
pipeline_tag: text-generation
tags:
- cbg
- safety
- tamper-resistance
---

# cbg-llama2-7b-beta0

Full-parameter CBG v2 defense of `meta-llama/Llama-2-7b-chat-hf`, trained with `src/cbg/train_v2.py` on the SEAM main-run data recipe (RepNoise BeaverTails refusals, 4,000 defense rows; Alpaca, 4,000 benign rows).

Prompt format: `Question: {prompt}\nAnswer:` (no chat template), as in training.

## Training settings

| | |
|---|---|
| steps | 500 |
| lr | 2e-05 |
| scheduler | cosine |
| batch m / n | 8 / 32 |
| alpha | 1.0 |
| beta | 0.0 |
| k | 4 |
| radius r | 1.1e-07 |
| lazy_period | 4 |
| lazy_mode | reuse |
| num_sign_draws | 1 |
| geometry_clip_factor | 3.0 |
| max length (safety / benign) | 256 / 256 |
| weights dtype | bfloat16 |

## Geometry (D_geo)

| | |
|---|---|
| geo/log_eta_k (step 0) | -0.02352772316966905 |
| geo/log_eta_k (step 500) | -0.02482512454428497 |
| delta log eta_k | -0.0012974013746159183 |

## Provenance

| | |
|---|---|
| base model | meta-llama/Llama-2-7b-chat-hf @ f5db02db724555f92da89c216ac04704f23d4590 |
| config sha256 | 000d943023a55fdfc8589476670072caa3c6038f47f716f1c3e476c14527bf71 |
| data manifest sha256 | d08a4023a7c11c4a3d01259356569ec19766bb7d754d194841dff60836d7a898 |
| torch | 2.5.1+cu124 |
| GPUs | NVIDIA H200 NVL, NVIDIA H200 NVL |

Training records (config, identity, per-step log, metrics) are in `training/`.

## License

A derivative of Llama 2, distributed under the Llama 2 Community License Agreement; use is subject to its terms and Acceptable Use Policy.
