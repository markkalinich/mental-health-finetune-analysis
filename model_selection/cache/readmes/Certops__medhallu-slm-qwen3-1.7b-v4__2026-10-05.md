---
library_name: mlx
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3-1.7B/blob/main/LICENSE
pipeline_tag: text-generation
base_model: mlx-community/Qwen3-1.7B-bf16
datasets:
- Certops/medhallu-twins-rewritten-v3
tags:
- mlx
- hallucination-detection
- medical
---

# medhallu-slm-qwen3-1.7b-v4

Qwen3-1.7B, fine-tuned with LoRA and merged (bf16). Given a context and an answer,
it splits the answer into claims and returns, per claim, a reason and a verdict
(`yes` = supported by the context, `no` = not supported). An answer is flagged as
hallucinated if any claim gets `no`.

Weights use standard Hugging Face names, so they load in MLX, transformers and vLLM.

## Training

| | |
|---|---|
| training run | `train-45058cc8` (Unsloth Studio, MLX) |
| data | `Certops/medhallu-twins-rewritten-v3` @ `d775afd8`, train split |
| prompt | `claims-reason-first-v3` (fingerprint `b4098877f027cc0e`) |
| method | LoRA r=16, alpha=16, all linear layers, lr 2e-4, 1 epoch, 288 steps |
| inference | chat template with `enable_thinking=False` |

## Scores

| set | rows | accuracy | precision | recall | F1 |
|---|---|---|---|---|---|
| dev (held out from train) | 256 | 90.6% | 94.1 | 86.7 | 90.2 |
| RAGTruth QA (test, fixed sample) | 200 | 62.5% | 72.1 | 46.8 | 56.8 |

The dataset's test split is locked and has not been scored.
