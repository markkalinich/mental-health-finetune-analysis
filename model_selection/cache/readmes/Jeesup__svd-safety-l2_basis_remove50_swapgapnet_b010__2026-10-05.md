---
license: llama2
base_model: meta-llama/Llama-2-7b-chat-hf
library_name: transformers
pipeline_tag: text-generation
tags:
- llama2
- svd
- compression
- safety
- interpretability
---

# svd-safety-l2_basis_remove50_swapgapnet_b010

A Llama-2-7b-chat checkpoint compressed with Basis Sharing (ICLR 2025; shared bases over groups of 2 adjacent layers) to **50.0% of dense
parameters**, then edited by **10 of 10 rounds** of iterative
parameter-neutral swap selected by the **`swapgapnet_iter`** rule (up to 0.1% of dense
parameters per round; the full run's budget is 1.0%).

This is a research artifact from a study of how SVD compression damages safety
behaviour and which component-selection rule best repairs it. It is one cell of a
grid over selection rules and budgets; it is **not** a general-purpose chat model.

## Provenance

| field | value |
|---|---|
| base (uncompressed) | `meta-llama/Llama-2-7b-chat-hf` |
| compression | Basis Sharing (ICLR 2025; shared bases over groups of 2 adjacent layers), 50.00% of parameters removed |
| selection rule | `swapgapnet_iter` |
| restore budget | 1.000% of dense parameters |
| components restored | 4512 |
| components swapped out | 4512 |
| resulting parameter fraction | 0.4998 |
| seed | 42 |
| recovery | LoRA r=8 on the per-layer coefficients only (bases frozen, budget unchanged), 2 epochs, lr 0.0001, batch 64, alpaca-cleaned |
| iterative rounds applied | 10 of 10 |
| per-round chunk | 0.100% of dense parameters |
| parameters swapped in | 64,723,200 (1.00% of dense projection parameters) |
| swap value | `net` (insertion value + removal value of the sigma-ordered eviction) |

## Measured

| metric | value |
|---|---|
| AdvBench ASR (HarmBench judge) | 0.1231 |
| StrongREJECT ASR (HarmBench judge) | 0.2396 |
| Macro over-refusal (WildGuard) | 0.0751 |


## Intended use and limitations

This checkpoint exists to measure safety/utility trade-offs under compression.
Several arms in the grid are **deliberately safety-degraded** relative to
Llama-2-7b-chat: compression alone raises attack-success rate, and the point of
the study is to quantify that and test recovery. Treat any given cell as an
experimental subject, not as a deployable assistant, and evaluate it yourself
before drawing conclusions from it.

## Licence

Llama 2 Community License. `LICENSE.txt` and `USE_POLICY.md` are included in this
repository, and use of this derivative is bound by both. Built with Llama 2.
