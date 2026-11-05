---
base_model: Qwen/Qwen2.5-VL-7B-Instruct
datasets:
- PolicyShiftBench/PolicyShiftBench
library_name: transformers
license: apache-2.0
pipeline_tag: image-text-to-text
tags:
- vision-language
- safety
- guardrail
- policy-conditioned
- qwen2.5-vl
- policyshiftguard
---

# PolicyShiftGuard-7B-RP-SFT

[\ud83d\udcc3 Paper](https://arxiv.org/abs/2607.05910) | [\ud83c\udf10 Project Page](https://policyshiftguard.github.io/) | [\ud83d\udcbb GitHub](https://github.com/ssmisya/PolicyShiftGuard)

This repository releases the **Stage-1 Randomized Policy SFT (RP-SFT)** checkpoint for the 7B PolicyShiftGuard model.

RP-SFT is the first training stage in PolicyShiftGuard. It trains a Qwen2.5-VL guardrail model to read policy bundles under randomized policy identifiers and randomized policy ordering. This checkpoint is provided for reproducibility and ablation use. The final public model after the second-stage adaptation is available at [`PolicyShiftGuard/PolicyShiftGuard-7B`](https://huggingface.co/PolicyShiftGuard/PolicyShiftGuard-7B).

## Intended Use

Use this checkpoint when you want to reproduce the two-stage training pipeline or compare Stage-1 RP-SFT against the final BP-Adapt model.

For standard evaluation or deployment, use the final model instead:

- [`PolicyShiftGuard/PolicyShiftGuard-7B`](https://huggingface.co/PolicyShiftGuard/PolicyShiftGuard-7B)

## Dataset

The model is trained with PolicyShiftBench supervision:

- [`PolicyShiftBench/PolicyShiftBench`](https://huggingface.co/datasets/PolicyShiftBench/PolicyShiftBench)

## Notes

- This is an intermediate checkpoint, not the final model reported as the main PolicyShiftGuard model.
- This checkpoint corresponds to the randomized-policy no-think Stage-1 SFT setting.
- Training-state files such as optimizer states are intentionally not included.

## Citation

If you find this work helpful, please cite the paper:

```bibtex
@article{song2026policyshiftguard,
  title   = {PolicyShiftGuard: Benchmarking and Improving Policy-Adaptive Image Guardrails},
  author  = {Song, Mingyang and Xu, Luxin and Sun, Haoyu and Pan, Minzhou and Cheng, Yu and Li, Bo},
  journal = {arXiv preprint arXiv:2607.05910},
  year    = {2026}
}
```