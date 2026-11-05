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

# svd-safety-mis7_swift_remove30_swapgapiter_b010

A Mistral-7B-Instruct-v0.2 checkpoint compressed with Swift-SVD with LoRA recovery (base checkpoint `Jeesup/svd-safety-mis7_swift_remove30`) to **70.0% of dense
parameters**, then edited by **10 of 10 rounds** of iterative
parameter-neutral swap selected by the **`gap_iter`** rule (up to 0.1% of dense
parameters per round; the full run's budget is 1.0%).

This is a research artifact from a study of how SVD compression damages safety
behaviour and which component-selection rule best repairs it. It is one cell of a
grid over selection rules and budgets; it is **not** a general-purpose chat model.

## Provenance

| field | value |
|---|---|
| base (uncompressed) | `mistralai/Mistral-7B-Instruct-v0.2` |
| compression | Swift-SVD with LoRA recovery (base checkpoint `Jeesup/svd-safety-mis7_swift_remove30`), 29.97% of parameters removed |
| selection rule | `gap_iter` |
| restore budget | 1.000% of dense parameters |
| components restored | 9835 |
| components swapped out | 9835 |
| resulting parameter fraction | 0.7003 |
| seed | 42 |
| iterative rounds applied | 10 of 10 |
| per-round chunk | 0.100% of dense parameters |
| parameters swapped in | 69,730,304 (1.00% of dense projection parameters) |
| eviction | matrix-local (each insertion evicts a component of the same matrix) |
| swap value | `insert` (insertion value only; sigma-ordered eviction) |

## Measured

| metric | value |
|---|---|
| AdvBench ASR (HarmBench judge) | 0.0288 |
| StrongREJECT ASR (HarmBench judge) | 0.1534 |
| Macro over-refusal (WildGuard) | 0.2052 |
| WikiText-2 perplexity | 9.1118 |


## Intended use and limitations

This checkpoint exists to measure safety/utility trade-offs under compression.
Several arms in the grid are **deliberately safety-degraded** relative to
Mistral-7B-Instruct-v0.2: compression alone raises attack-success rate, and the point of
the study is to quantify that and test recovery. Treat any given cell as an
experimental subject, not as a deployable assistant, and evaluate it yourself
before drawing conclusions from it.

## Licence

Apache License 2.0. The base model's repository ships no licence file to redistribute; the licence above governs this derivative. 
