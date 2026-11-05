---
license: llama3
base_model: meta-llama/Meta-Llama-3-8B-Instruct
library_name: transformers
pipeline_tag: text-generation
tags:
- llama3
- svd
- compression
- safety
- interpretability
---

# svd-safety-l3_basis_jbbsftx1_remove40

A Llama-3-8B-Instruct checkpoint compressed with Basis Sharing (ICLR 2025; shared bases over groups of 2 adjacent layers) to **60.0% of dense
parameters**, then recovered with a coefficient-only LoRA fine-tune that keeps both the
parameter budget and the shared bases exactly.

This is a research artifact from a study of how SVD compression damages safety
behaviour and which component-selection rule best repairs it. It is one cell of a
grid over selection rules and budgets; it is **not** a general-purpose chat model.

## Provenance

| field | value |
|---|---|
| base (uncompressed) | `meta-llama/Meta-Llama-3-8B-Instruct` |
| compression | Basis Sharing (ICLR 2025; shared bases over groups of 2 adjacent layers), 40.00% of parameters removed |
| resulting parameter fraction | 0.5999 |
| seed | 42 |
| recovery | LoRA r=8 on the per-layer coefficients only (bases frozen, budget unchanged), 2 epochs, lr 0.0001, batch 64, alpaca-cleaned |

## Measured

| metric | value |
|---|---|
| AdvBench ASR (HarmBench judge) | 0.0654 |
| StrongREJECT ASR (HarmBench judge) | 0.0639 |
| Macro over-refusal (WildGuard) | 0.2999 |
| WikiText-2 perplexity | 18.1062 |


## Intended use and limitations

This checkpoint exists to measure safety/utility trade-offs under compression.
Several arms in the grid are **deliberately safety-degraded** relative to
Llama-3-8B-Instruct: compression alone raises attack-success rate, and the point of
the study is to quantify that and test recovery. Treat any given cell as an
experimental subject, not as a deployable assistant, and evaluate it yourself
before drawing conclusions from it.

## Licence

Meta Llama 3 Community License. `LICENSE` and `USE_POLICY.md` are included in this repository, and use of this derivative is bound by them. Built with Meta Llama 3.
