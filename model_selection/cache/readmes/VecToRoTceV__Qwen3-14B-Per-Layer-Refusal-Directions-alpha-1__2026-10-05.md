---
license: apache-2.0
base_model: Qwen/Qwen3-14B
library_name: transformers
pipeline_tag: text-generation
inference: false
tags:
  - mechanistic-interpretability
  - model-editing
  - refusal-direction
  - per-layer
  - ablation
  - research
  - not-for-all-audiences
---

# Qwen3-14B Per-Layer Refusal-Direction Edit (alpha=1)

> **Experimental research condition, released for comparison and reuse.** This checkpoint is not
> the preferred result of the associated study. It is published so that researchers can inspect,
> reproduce, and extend the tested per-layer intervention.

## Model summary

| Field | Value |
|---|---|
| Base model | `Qwen/Qwen3-14B` |
| Base revision | `40c069824f4251a91eefaf281ebe4c544efd3e18` |
| Method | One normalized refusal direction per transformer layer |
| Direction position | Fixed post-instruction position `-8` for every layer |
| Strength | `alpha=1` on every supported residual writer |
| Format | BF16 Transformers checkpoint, six sharded safetensors files |
| Validated software | Transformers `4.57.6` |

For layer-specific unit direction `r_l`, each supported output-space weight in layer `l` is edited
as:

```text
W_l,new = W_l - r_l (r_l^T W_l)
```

Each block uses its original `resid_post[l]` direction for its attention `o_proj` and MLP
`down_proj`. The untied embedding uses the block-0 output direction. The unembedding, Q/K/V,
gate/up projections, and RMSNorm tensors are unchanged.

## Evaluation

All comparisons use fixed prompts and matched decoding settings. Prompt and completion bodies are
not distributed with this model.

| Condition | Refusal rate | Proxy usefulness | XSTest safe answer | Capability | Benign KL |
|---|---:|---:|---:|---:|---:|
| Base | 84.39% | 3.82% | 89.20% | 70.60% | 0.00000 |
| Global `alpha=1` | 11.71% | 50.87% | 98.40% | 70.40% | 0.06752 |
| Per-layer `alpha=1` | 11.95% | 49.17% | 98.40% | 69.40% | 0.19770 |

An independent `garak-llm/garak-refusal-detector` classifier measured 51.46% refusal for Base and
0.00% for this checkpoint on the same 410-sample refusal set. It is a binary synthetic-data
classifier, not the official StrongREJECT evaluator, and does not establish response correctness or
safety.

On complete IFEval (541 prompts, 834 instructions), this checkpoint scored 86.32% prompt-strict,
90.53% instruction-strict, 88.54% prompt-loose, and 91.97% instruction-loose.

## Interpretation and known limitations

This experiment does **not** show that Per-layer editing is better than the simpler Global method.
At `alpha=1`, refusal reduction is similar while Per-layer has roughly three times the benign KL
and a 1.0-point lower capability macro score. The paper's main empirical conclusion therefore does
not favor this checkpoint.

The initial refusal evaluation reached its 256-token cap for 94.39% of Per-layer responses. Unlike
Global `alpha=0.75`, this checkpoint did not receive a dedicated 1024-token output-degradation and
relevance rerun. Its long-generation stopping, repetition, and off-topic rates are therefore
uncharacterized, not assumed to be acceptable.

Per-layer directions are statistically stable under 200 bootstrap and 200 half-sample
recomputations, and their pairwise cosine geometry rotates across model depth. Stable geometry does
not by itself imply a superior intervention trade-off.

## Intended use and limitations

This checkpoint is intended for mechanistic-interpretability, model-editing, and controlled
evaluation research. It is not presented as safe, universally "uncensored," capability-preserving
for every task, or suitable for deployment. Reducing refusal behavior does not show that the model
has lost its internal representation of harmfulness.

No public API, Space, managed endpoint, or interactive service is maintained by this project.

## Reproducibility

Code, configurations, aggregate results, plots, and the technical report are available at
[VecToR-1024/qwen3-refusal-direction-removal](https://github.com/VecToR-1024/qwen3-refusal-direction-removal).
The repository excludes extraction prompt bodies and restricted generations.

The serialized checkpoint passed save/reload, six-shard index, activation-versus-weight,
determinism, dtype/device, and tied-weight handling checks before release. Users should perform a
fresh-download load and benign smoke test against the exact Hub revision they consume.

## License

The base model and this derivative checkpoint are distributed under Apache-2.0. The base model's
notices and attribution remain applicable. Dataset licenses remain applicable to their source data;
dataset bodies are not redistributed here.
