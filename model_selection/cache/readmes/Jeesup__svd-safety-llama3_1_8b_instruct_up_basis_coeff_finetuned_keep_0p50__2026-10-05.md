---
license: llama3.1
base_model: meta-llama/Llama-3.1-8B-Instruct
tags:
  - basis-sharing
  - compression
  - low-rank
  - safety
---

# llama3_1_8b_instruct_up_basis_coeff_finetuned_keep_0p50

`meta-llama/Llama-3.1-8B-Instruct` compressed with **Basis Sharing** using the authors' code
([TUDa-HWAI/Basis_Sharing](https://github.com/TUDa-HWAI/Basis_Sharing), `1c021b6ce1d3`),
then recovered by LoRA on the coefficients alone.

- **Parameters removed:** 50% (keeping 50%)
- **Realised parameter fraction:** 0.4998967097355769
- **Groups:** 2 adjacent layers share one basis per weight type
- **Shared types:** `v`, `k`, `q`, `up`, `gate` — **private (per-layer):** `down`, `o`
- **Pipeline:** whitened SVD of each group's horizontally concatenated weights
  (the shared-basis fit) -> LoRA on the coefficients, bases frozen -> merge
  `C' = C + (alpha/r)BA` -> fold `W = C' @ B` to dense
- **Calibration:** 256 WikiText-2 sequences of
  2048 tokens, seed 42
  (upstream hard-codes seed 2023; this project calibrates every method at one seed)
- **Recovery:** LoRA r=8, alpha 16,
  2 epochs, lr 0.0001,
  batch 64, on `yahma/alpaca-cleaned`

**Only the coefficients were trained.** The shared and per-layer bases are frozen and
bit-identical to the compressed model, so every weight keeps rank <= k, each group still
shares one basis, and the parameter budget survives recovery exactly. This is *not*
Basis Sharing's own LoRA (wikitext, batch 1, q/v only): the project's alpaca recipe is
used for every compressor so the recovery data is constant across methods.

> **Rotary embeddings.** The LoRA trains the factored `ShareLlama` model, so its
> positional encoding matters. It uses transformers' own rotary tables built from this
> model's config, verified identical to stock Llama in float64 for base-500000 RoPE,
> llama3 scaling and grouped-query attention (`tests/check_share_llama_exact.py`).

The factors are folded back to dense Llama shapes, so this loads with stock
`transformers` and needs no custom modelling code. It is rank-deficient, not smaller
on disk.

## Results

| Metric | Value |
|---|---:|
| Parameter fraction retained | 0.4999 |
| WikiText-2 perplexity | 22.2115 |
| arc_easy (acc_norm) | 0.5593 |
| arc_challenge (acc_norm) | 0.3473 |
| hellaswag (acc_norm) | 0.5012 |
| winogrande (acc) | 0.6196 |
| openbookqa (acc_norm) | 0.3460 |
| piqa (acc_norm) | 0.6790 |
| mathqa (acc_norm) | 0.2606 |
| AdvBench HarmBench ASR | 0.6173 |
| StrongREJECT HarmBench ASR | 0.4856 |
| Over-refusal rate (XSTest-safe) | 0.1440 |
| Over-refusal rate (OR-Bench-Hard-1K) | 0.1016 |
| Over-refusal macro rate | 0.1228 |

Over-refusal judging is **reliable** for this cell (XSTest-safe scored fraction 0.97; OR-Bench-Hard-1K scored fraction 0.98).

Full per-prompt outputs and raw metric files are in `utility/` and `safety/`.

## Evaluation

WikiText-2 perplexity; ARC-Easy/Challenge, HellaSwag, WinoGrande, OpenBookQA, PIQA and
MathQA zero-shot; AdvBench and StrongREJECT generation judged by
`cais/HarmBench-Llama-2-13b-cls`; over-refusal on XSTest-safe and OR-Bench-Hard-1K judged
by `allenai/wildguard`. All generation uses the chat template, greedy.

## Caveat

Compression at this ratio degrades refusal behaviour, which is what this cell exists to
measure. Safety numbers from a model that has become degenerate are not evidence about
alignment — read the over-refusal reliability line above alongside the ASR.
