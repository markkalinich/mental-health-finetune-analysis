---
license: llama2
base_model: meta-llama/Llama-2-7b-chat-hf
tags:
  - basis-sharing
  - compression
  - low-rank
  - safety
---

# llama2_7b_chat_up_basis_coeff_jbbmix_finetuned_keep_0p50

`meta-llama/Llama-2-7b-chat-hf` compressed with **Basis Sharing** using the authors' code
([TUDa-HWAI/Basis_Sharing](https://github.com/TUDa-HWAI/Basis_Sharing), `1c021b6ce1d3`),
then recovered by LoRA on the coefficients alone.

- **Parameters removed:** 50% (keeping 50%)
- **Realised parameter fraction:** 0.49982796308290156
- **Groups:** 2 adjacent layers share one basis per weight type
- **Shared types:** `v`, `k`, `q`, `up`, `gate` — **private (per-layer):** `down`, `o`
- **Pipeline:** whitened SVD of each group's horizontally concatenated weights
  (the shared-basis fit) -> LoRA on the coefficients, bases frozen -> merge
  `C' = C + (alpha/r)BA` -> fold `W = C' @ B` to dense
- **Calibration:** 256 WikiText-2 sequences of
  2048 tokens, seed 42
  (upstream hard-codes seed 2023; this project calibrates every method at one seed)
  **plus 2 packed sequence(s) of JailbreakBench's 100 harmful behaviours** (`jbb_harmful:2`, prompt + assistant header only, no response; 0.78% of the calibration tokens)
- **Recovery:** LoRA r=8, alpha 16,
  2 epochs, lr 0.0001,
  batch 64, on `yahma/alpaca-cleaned`

> **Safety-data baseline arm (`calibration_mix`).** This cell differs from the plain
> Basis Sharing cell at the same ratio only in the calibration set: JailbreakBench harmful
> behaviours were mixed in to test whether safety data at that stage preserves
> refusal. 11 of AdvBench's 520 prompts are verbatim JailbreakBench behaviours.

**Only the coefficients were trained.** The shared and per-layer bases are frozen and
bit-identical to the compressed model, so every weight keeps rank <= k, each group still
shares one basis, and the parameter budget survives recovery exactly. This is *not*
Basis Sharing's own LoRA (wikitext, batch 1, q/v only): the project's alpaca recipe is
used for every compressor so the recovery data is constant across methods.

> **Rotary embeddings.** The LoRA trains the factored `ShareLlama` model, so its
> positional encoding matters. It uses transformers' own rotary tables built from this
> model's config, verified identical to stock Llama in float64 across every setting the
> published families use: RoPE base 1e4 / 5e5 / 1e6, llama3 scaling, grouped-query
> attention and q/k/v biases (`tests/check_share_llama_exact.py`).

The factors are folded back to dense Llama shapes, so this loads with stock
`transformers` and needs no custom modelling code. It is rank-deficient, not smaller
on disk.

## Results

| Metric | Value |
|---|---:|
| Parameter fraction retained | 0.4998 |
| WikiText-2 perplexity | 13.0826 |
| arc_easy (acc_norm) | 0.5093 |
| arc_challenge (acc_norm) | 0.3148 |
| hellaswag (acc_norm) | 0.5216 |
| winogrande (acc) | 0.5959 |
| openbookqa (acc_norm) | 0.3420 |
| piqa (acc_norm) | 0.6627 |
| mathqa (acc_norm) | 0.2412 |
| AdvBench HarmBench ASR | 0.0769 |
| StrongREJECT HarmBench ASR | 0.0831 |
| Over-refusal rate (XSTest-safe) | 0.3279 |
| Over-refusal rate (OR-Bench-Hard-1K) | 0.4111 |
| Over-refusal macro rate | 0.3695 |

Over-refusal judging is **reliable** for this cell (XSTest-safe scored fraction 0.99; OR-Bench-Hard-1K scored fraction 1.00).

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
