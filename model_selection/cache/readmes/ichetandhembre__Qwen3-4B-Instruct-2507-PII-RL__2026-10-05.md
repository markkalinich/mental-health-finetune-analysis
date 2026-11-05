---
base_model: Qwen/Qwen3-4B-Instruct-2507
license: apache-2.0
tags:
  - pii
  - privacy
  - grpo
  - lora
  - rl
---

# Qwen3-4B-Instruct-2507 PII Masking (GRPO RL)

Fine-tuned from [Qwen/Qwen3-4B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507) using GRPO reinforcement learning on the [AdamLucek/open-pii-masking-en-us-30k](https://huggingface.co/datasets/AdamLucek/open-pii-masking-en-us-30k) dataset.

## Training

- **Framework:** verl v0.7.1 + FSDP2 + vLLM
- **Algorithm:** GRPO + CISPO (asymmetric clip)
- **LoRA:** r=8, α=16, all-linear modules
- **Steps:** 90
- **KL coefficient:** 0.01

## Eval (matched leaderboard split, seed=42, 5919 examples)

| Metric | Value |
|--------|-------|
| exact_match | 0.818 |
| pii_count_match | 0.838 |
| format_compliance | 1.000 |
| mean_reward (normalized) | 0.836 |
| raw reward | 1.337 / 1.6 |

## Usage

```python
from transformers import pipeline

pipe = pipeline("text-generation", model="ichetandhembre/Qwen3-4B-Instruct-2507-PII-RL")
result = pipe([
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": "Call John Smith at 555-123-4567"},
], max_new_tokens=256)
```

System prompt: replace all PII with `[PII]` tags, return output in `<masked_output>...</masked_output>` XML tags.
