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

# cbg-llama2-7b-step500

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
| beta | 0.1 |
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
| geo/log_eta_k (step 500) | -1.5338230116066822 |
| delta log eta_k | -1.510295288437013 |

## Provenance

| | |
|---|---|
| base model | meta-llama/Llama-2-7b-chat-hf @ f5db02db724555f92da89c216ac04704f23d4590 |
| config sha256 | d8634ab79eb0e306752e7c39d20aa497b1d091f9a6930f40661aae99ada380f0 |
| data manifest sha256 | d08a4023a7c11c4a3d01259356569ec19766bb7d754d194841dff60836d7a898 |
| torch | 2.5.1+cu124 |
| GPUs | NVIDIA H200, NVIDIA H200 |

Training records (config, identity, per-step log, metrics) are in `training/`.

## License

A derivative of Llama 2, distributed under the Llama 2 Community License Agreement; use is subject to its terms and Acceptable Use Policy.
