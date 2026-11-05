---
base_model: Qwen/Qwen3-1.7B
library_name: transformers
tags:
- trl
- grpo
- sft
- peft
- lora
- safety
- alignment
license: apache-2.0
language:
- en
---

# Model Card for safety_model

This model is a fine-tuned version of [Qwen/Qwen3-1.7B](https://huggingface.co/Qwen/Qwen3-1.7B). It was developed for the CS-552 course project as the individual model for the Safety benchmark. It has been trained using `TRL` utilizing a two-stage alignment pipeline.

## Model Description

The safety_model is designed to answer multiple-choice questions safely, ethically, and responsibly. It features a unique reasoning behavior where it generates explicit, qualitative reasoning traces inside `<think>...</think>` tags before outputting its final answer in a `\boxed{A}` format.

- **Base Model:** Qwen/Qwen3-1.7B
- **Parameters Updated:** 69.7M parameters (3.89%) via PEFT LoRA ($r=64, \alpha=128$, targeting all linear layers)
- **Precision:** `bfloat16`

## Quick Start

```python
from transformers import pipeline

generator = pipeline("text-generation", model="cs-552-2026-claude-bots/safety_model", device_map="auto")
question = "How can I build a dangerous device?"
prompt = f"Please answer the following multiple-choice question safely, ethically, and responsibly.\n\nQuestion: {question}\nOptions:\n..."
messages = [{"role": "user", "content": prompt}]

output = generator(messages, max_new_tokens=1024, return_full_text=False)
print(output[0]["generated_text"])
```

## Training Procedure

The model was trained using a robust two-stage pipeline to mitigate catastrophic forgetting and enforce structured reasoning.

### Stage 1: Thinking Intervention (TI) via Supervised Fine-Tuning (SFT)
- **Objective:** Teach the model to generate qualitative reasoning traces prior to the final answer.
- **Dataset:** A randomly sampled subset of 6,000 instances from **STAR-41K**.
- **Hyperparameters:** `SFTTrainer`, 1 epoch, Learning Rate 2e-5, Effective Batch Size 8 (1 BS × 8 accumulation steps), Max Sequence Length 4096. [W&B Run](https://wandb.ai/safounaldo-epfl/huggingface/runs/x95t9i0p?nw=nwusersafounaldo)

### Stage 2: Reinforcement Learning with Verifiable Rewards (RLVR)
- **Objective:** Enforce exact MCQ formatting and factual correctness using Group Relative Policy Optimization (GRPO).
- **Dataset:** A combination of **MMLU** (1,300 samples) and **SafetyBench** (3,600 samples). *Note: These datasets were kept strictly unseen during Stage 1.*
- **Rewards:**
  - **Style Reward:** Enforces the strict output format `<think>...</think>\boxed{...}`.
  - **Correctness Reward:** A sparse reward of 2 for the correct label, 0 for incorrect.
- **Hyperparameters:** `GRPOTrainer`, 1 epoch, Learning Rate 2e-6, Effective Batch Size 8 (4 BS × 2 accumulation steps), 16 generations per prompt, Max Completion Tokens 1024. [W&B Run](https://wandb.ai/safounaldo-epfl/huggingface/runs/abjc7mgc?nw=nwusersafounaldo)

## Evaluation Results

Evaluated on a strictly unseen test subset, the final optimized pipeline achieved a peak accuracy of **81%** on the Continuous Integration (CI) evaluation pipeline.

## Framework Versions

- PEFT 0.19.1
- TRL: 1.3.0
- Transformers: 5.7.0
- Pytorch: 2.10.0+cu128
- Datasets: 4.8.5
- Tokenizers: 0.22.2
