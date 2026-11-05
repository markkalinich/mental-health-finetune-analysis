---
license: apache-2.0
base_model: mistralai/Mistral-7B-Instruct-v0.2
library_name: transformers
pipeline_tag: text-generation
tags:
- mistral
- svd
- compression
- safety
- interpretability
---

# svd-safety-mis7_basis_jbbsftx1_remove50

A Mistral-7B-Instruct-v0.2 checkpoint compressed with Basis Sharing (ICLR 2025; shared bases over groups of 2 adjacent layers) to **50.0% of dense
parameters**, then recovered with a coefficient-only LoRA fine-tune that keeps both the
parameter budget and the shared bases exactly.

This is a research artifact from a study of how SVD compression damages safety
behaviour and which component-selection rule best repairs it. It is one cell of a
grid over selection rules and budgets; it is **not** a general-purpose chat model.

## Provenance

| field | value |
|---|---|
| base (uncompressed) | `mistralai/Mistral-7B-Instruct-v0.2` |
| compression | Basis Sharing (ICLR 2025; shared bases over groups of 2 adjacent layers), 50.00% of parameters removed |
| resulting parameter fraction | 0.4999 |
| seed | 42 |
| recovery | LoRA r=8 on the per-layer coefficients only (bases frozen, budget unchanged), 2 epochs, lr 0.0001, batch 64, alpaca-cleaned |

## Measured

| metric | value |
|---|---|
| AdvBench ASR (HarmBench judge) | 0.1250 |
| StrongREJECT ASR (HarmBench judge) | 0.1917 |
| Macro over-refusal (WildGuard) | 0.2112 |
| WikiText-2 perplexity | 11.6250 |


## Intended use and limitations

This checkpoint exists to measure safety/utility trade-offs under compression.
Several arms in the grid are **deliberately safety-degraded** relative to
Mistral-7B-Instruct-v0.2: compression alone raises attack-success rate, and the point of
the study is to quantify that and test recovery. Treat any given cell as an
experimental subject, not as a deployable assistant, and evaluate it yourself
before drawing conclusions from it.

## Licence

Apache License 2.0. The base model's repository ships no licence file to redistribute; the licence above governs this derivative. 
