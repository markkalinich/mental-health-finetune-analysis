---
license: apache-2.0
base_model: Qwen/Qwen2.5-3B-Instruct
tags:
- mlp-surgery
- finetuned
- reasoning
language:
- en
datasets:
- Malum0x/openhermes2.5-Perplexity_filtered_top30
---

# mlp-surgery — broken baseline (Qwen2.5-3B)

The "broken" baseline used as input for the [mlp-surgery](https://github.com/Malum0x/mlp-surgery) project. **Don't use this model for downstream tasks** — it underperforms the base model on both math and general reasoning. It's published only so the experiment is reproducible.

## What it is

Qwen2.5-3B-Instruct + LoRA fine-tune on the perplexity-filtered top-30% of OpenHermes 2.5 (from the sister project [Perplexity-weighted-selective-finetuning](https://github.com/Malum0x/Perplexity-weighted-selective-finetuning)), merged into the base weights.

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

This model is the "After SFT (broken)" row.

## Companion models

- [mlp-surgery-restored-top5](https://huggingface.co/Malum0x/mlp-surgery-restored-top5) — partial recovery
- [mlp-surgery-restored-top15](https://huggingface.co/Malum0x/mlp-surgery-restored-top15) — partial recovery
- [mlp-surgery-restored-top30](https://huggingface.co/Malum0x/mlp-surgery-restored-top30) — **headline result, crosses base on GSM8K**
- [mlp-surgery-restored-specificity-top10](https://huggingface.co/Malum0x/mlp-surgery-restored-specificity-top10) — negative-result variant

Code: https://github.com/Malum0x/mlp-surgery
