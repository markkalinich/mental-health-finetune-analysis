---
base_model: LiquidAI/LFM2.5-230M
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
tags:
  - abliteration
  - directional-ablation
  - uncensored
  - mechanistic-interpretability
  - safety-research
  - ablate
---
# LFM2.5-230M-Uncensored

This is a **directionally-ablated ("abliterated")** version of
[`LiquidAI/LFM2.5-230M`](https://huggingface.co/LiquidAI/LFM2.5-230M), produced with
[**ablate**](https://github.com/) — an activation-engineering toolkit for
mechanistic-interpretability and safety research.

The model's **refusal direction(s)** were identified in the residual stream and
projected out of the weights, reducing the model's tendency to refuse. No weights
were fine-tuned; this is a rank-1 linear edit.

## Method

- **Technique:** single-direction ablation (baked)
- **Direction extraction:** difference-of-means on matched harmful/harmless
  instruction pairs (Arditi et al., 2024, *"Refusal in LLMs is mediated by a
  single direction"*).
- **Intervention:** orthogonalization of every residual-writing matrix
  (embedding, attention output, MLP output) against the refusal subspace, so the
  edit is baked into the weights.

### Ablation configuration

```json
{
  "direction_layer": 12,
  "alpha": 1.2485360790589348,
  "min_layer": 12,
  "max_layer": 13
}
```

## Evaluation

| metric | value |
|---|---|
| refusal_rate | 0.0 |
| mean_kl | 0.101 |
| coherence | 0.9096 |

Refusal rate is measured on held-out harmful prompts; `mean_kl` is the mean KL divergence of next-token distributions vs. the base model on benign prompts (lower ⇒ less capability drift). ASR (if present) is the judged attack-success rate on a harmful benchmark.

## Intended use

Research into how safety behaviour is represented in language models, red-teaming,
and building better defenses. Studying the *robustness* and *locality* of refusal
is the scientific goal; the reduced-refusal behaviour is the measurement
instrument.

## ⚠️ Responsible use

This model has had safety guardrails **deliberately weakened** and will more
readily produce harmful, unsafe, or otherwise objectionable content than the base
model. It is released for research and evaluation. **Do not deploy it in
user-facing products without adding your own safety layer.** You are responsible
for complying with the base model's license and all applicable laws. The authors
of `ablate` accept no liability for misuse.

## Limitations

- Ablation is a blunt linear edit: it can leave residual refusals and may cause
  mild capability drift (see `mean_kl` above).
- Safety is redundantly encoded; a single subspace rarely removes all of it.
- Evaluated only on the benchmarks noted above — behaviour elsewhere may differ.


## Citation

If you use this model or `ablate`, please cite Arditi et al. (2024),
*Refusal in Language Models Is Mediated by a Single Direction*
([arXiv:2406.11717](https://arxiv.org/abs/2406.11717)).
