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

# svd-safety-l2_swift_remove40_swapgapiter_b010

A Llama-2-7b-chat checkpoint compressed with Swift-SVD with LoRA recovery (base checkpoint `Jeesup/svd-safety-l2_swift_remove40`) to **60.0% of dense
parameters**, then edited by **10 of 10 rounds** of iterative
parameter-neutral swap selected by the **`gap_iter`** rule (up to 0.1% of dense
parameters per round; the full run's budget is 1.0%).

This is a research artifact from a study of how SVD compression damages safety
behaviour and which component-selection rule best repairs it. It is one cell of a
grid over selection rules and budgets; it is **not** a general-purpose chat model.

## Provenance

| field | value |
|---|---|
| base (uncompressed) | `meta-llama/Llama-2-7b-chat-hf` |
| compression | Swift-SVD with LoRA recovery (base checkpoint `Jeesup/svd-safety-l2_swift_remove40`), 40.02% of parameters removed |
| selection rule | `gap_iter` |
| restore budget | 1.000% of dense parameters |
| components restored | 6502 |
| components swapped out | 6502 |
| resulting parameter fraction | 0.5998 |
| seed | 42 |
| iterative rounds applied | 10 of 10 |
| per-round chunk | 0.100% of dense parameters |
| parameters swapped in | 64,717,568 (1.00% of dense projection parameters) |
| eviction | matrix-local (each insertion evicts a component of the same matrix) |
| swap value | `insert` (insertion value only; sigma-ordered eviction) |

## Measured

| metric | value |
|---|---|
| AdvBench ASR (HarmBench judge) | 0.0558 |
| StrongREJECT ASR (HarmBench judge) | 0.1342 |
| Macro over-refusal (WildGuard) | 0.1442 |
| WikiText-2 perplexity | 11.7512 |


## Intended use and limitations

This checkpoint exists to measure safety/utility trade-offs under compression.
Several arms in the grid are **deliberately safety-degraded** relative to
Llama-2-7b-chat: compression alone raises attack-success rate, and the point of
the study is to quantify that and test recovery. Treat any given cell as an
experimental subject, not as a deployable assistant, and evaluate it yourself
before drawing conclusions from it.

## Licence

Llama 2 Community License. `LICENSE.txt` and `USE_POLICY.md` are included in this repository, and use of this derivative is bound by them. Built with Llama 2.
