---
license: apache-2.0
base_model: Qwen/Qwen2.5-3B-Instruct
tags:
- mlp-surgery
- layer-restoration
- reasoning
language:
- en
datasets:
- openai/gsm8k
- allenai/ai2_arc
---

# mlp-surgery — restore top 10 (spec) on Qwen2.5-3B

Qwen2.5-3B-Instruct that was fine-tuned on perplexity-filtered OpenHermes 2.5 (which damaged its reasoning), then partially restored by copying back the top-10 most-damaged MLP layers from the base model. **No retraining.** Just weight surgery.

## Method (short)

1. Take the broken finetune ([mlp-surgery-broken](https://huggingface.co/Malum0x/mlp-surgery-broken)).
2. Score MLP layer parameters via specificity ratio (error gradient norms / correct gradient norms).
3. Copy the top-10 from base into the broken model. Save.

## Eval

lm-eval, GSM8K flexible-extract 5-shot, ARC Challenge acc_norm 0-shot, no chat template, batch_size 8, single seed (2026-05-07).

| Model | GSM8K | ARC Challenge |
|-------|------:|--------------:|
| Base (Qwen2.5-3B-Instruct) | 63.15% | 48.12% |
| After SFT (broken) | 61.64% | 45.22% |
| Restore top 5 | 63.00% | 45.73% |
| Restore top 15 | 63.46% | 46.50% |
| **Restore top 30** | **64.29%** | **48.55%** |
| Restore specificity top 10 | 61.64% | 45.22% |

This model is the **"Restore specificity top 10"** row.

## Why publish a model that didn't work?

Specificity scoring was supposed to isolate math-specifically-broken layers from generally-important ones. It didn't — restoring the top-10 specificity layers performed worse than restoring the same number of raw-norm-ranked layers. Publishing this is the negative subresult kept open. The Layer 2 case is a clean illustration: it's the top raw-score outlier (84.14 vs 12.96 for #2) but a non-outlier in specificity (1.15), correctly identifying it as a foundation layer that shouldn't be reset.

## Companion models + code

- [mlp-surgery-broken](https://huggingface.co/Malum0x/mlp-surgery-broken) — input baseline
- [mlp-surgery-restored-top5](https://huggingface.co/Malum0x/mlp-surgery-restored-top5)
- [mlp-surgery-restored-top15](https://huggingface.co/Malum0x/mlp-surgery-restored-top15)
- [mlp-surgery-restored-top30](https://huggingface.co/Malum0x/mlp-surgery-restored-top30)
- [mlp-surgery-restored-specificity-top10](https://huggingface.co/Malum0x/mlp-surgery-restored-specificity-top10)
- Code: https://github.com/Malum0x/mlp-surgery

## Caveats

Single seed. Magnitudes are ~1pt. The "no chat template" eval style means absolute numbers are below what you'd see with chat template applied (~78% GSM8K), but relative comparisons across the same setup are meaningful.
