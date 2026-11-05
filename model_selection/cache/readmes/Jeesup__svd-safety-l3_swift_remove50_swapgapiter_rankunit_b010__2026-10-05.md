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

# svd-safety-l3_swift_remove50_swapgapiter_rankunit_b010

A Llama-3-8B-Instruct checkpoint compressed with Swift-SVD with LoRA recovery (base checkpoint `Jeesup/svd-safety-l3_swift_remove50`) to **50.0% of dense
parameters**, then edited by **10 of 10 rounds** of iterative
parameter-neutral swap selected by the **`gap_iter`** rule (up to 0.1% of dense
parameters per round; the full run's budget is 1.0%).

This is a research artifact from a study of how SVD compression damages safety
behaviour and which component-selection rule best repairs it. It is one cell of a
grid over selection rules and budgets; it is **not** a general-purpose chat model.

## Provenance

| field | value |
|---|---|
| base (uncompressed) | `meta-llama/Meta-Llama-3-8B-Instruct` |
| compression | Swift-SVD with LoRA recovery (base checkpoint `Jeesup/svd-safety-l3_swift_remove50`), 49.97% of parameters removed |
| selection rule | `gap_iter` |
| restore budget | 1.000% of dense parameters |
| components restored | 5308 |
| components swapped out | 5308 |
| resulting parameter fraction | 0.5003 |
| seed | 42 |
| iterative rounds applied | 10 of 10 |
| per-round chunk | 0.100% of dense parameters |
| parameters swapped in | 69,743,616 (1.00% of dense projection parameters) |
| eviction | matrix-local (each insertion evicts a component of the same matrix) |
| candidate ranking | safety value alone (`--rank-cost unit`) |
| swap value | `insert` (insertion value only; sigma-ordered eviction) |

## Measured

| metric | value |
|---|---|
| AdvBench ASR (HarmBench judge) | 0.0192 |
| StrongREJECT ASR (HarmBench judge) | 0.1246 |
| Macro over-refusal (WildGuard) | 0.2419 |
| WikiText-2 perplexity | 55.3440 |


## Intended use and limitations

This checkpoint exists to measure safety/utility trade-offs under compression.
Several arms in the grid are **deliberately safety-degraded** relative to
Llama-3-8B-Instruct: compression alone raises attack-success rate, and the point of
the study is to quantify that and test recovery. Treat any given cell as an
experimental subject, not as a deployable assistant, and evaluate it yourself
before drawing conclusions from it.

## Licence

Meta Llama 3 Community License. `LICENSE` and `USE_POLICY.md` are included in this repository, and use of this derivative is bound by them. Built with Meta Llama 3.
