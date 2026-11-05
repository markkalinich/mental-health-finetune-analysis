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

# svd-safety-mistral_remove50_swapgapiter_rankunit_b010

A Mistral-7B-Instruct-v0.2 checkpoint compressed with SVD-LLM to **50.0% of dense
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
| compression | SVD-LLM, 50.03% of parameters removed |
| selection rule | `gap_iter` |
| restore budget | 1.000% of dense parameters |
| components restored | 5331 |
| components swapped out | 5331 |
| resulting parameter fraction | 0.4997 |
| seed | 42 |
| iterative rounds applied | 10 of 10 |
| per-round chunk | 0.100% of dense parameters |
| parameters swapped in | 69,739,520 (1.00% of dense projection parameters) |
| swap value | `insert` (insertion value only; sigma-ordered eviction) |

## Measured

| metric | value |
|---|---|
| AdvBench ASR (HarmBench judge) | 0.1942 |
| StrongREJECT ASR (HarmBench judge) | 0.3419 |
| Macro over-refusal (WildGuard) | 0.1319 |
| WikiText-2 perplexity | 13.5122 |


## Intended use and limitations

This checkpoint exists to measure safety/utility trade-offs under compression.
Several arms in the grid are **deliberately safety-degraded** relative to
Mistral-7B-Instruct-v0.2: compression alone raises attack-success rate, and the point of
the study is to quantify that and test recovery. Treat any given cell as an
experimental subject, not as a deployable assistant, and evaluate it yourself
before drawing conclusions from it.

## Licence

Apache License 2.0. The base model's repository ships no licence file to redistribute; the licence above governs this derivative. 
