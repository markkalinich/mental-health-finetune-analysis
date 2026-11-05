---
base_model: Qwen/Qwen3-4B-Instruct-2507
datasets:
- u-10bei/sft_alfworld_trajectory_dataset_v5
language:
- en
license: apache-2.0
library_name: peft
pipeline_tag: text-generation
tags:
- lora
- agent
- tool-use
- alfworld
- dbbench
---

# ryo-llm/qwen3-4b-agent-trajectory-lora-alf-guard

This repository provides a **LoRA adapter** fine-tuned from
**Qwen/Qwen3-4B-Instruct-2507** using **LoRA + Unsloth**.

This repository contains **LoRA adapter weights only**.
The base model must be loaded separately.

## Training Objective

This adapter is trained to improve **multi-turn agent task performance**
on ALFWorld (household tasks) and DBBench (database operations).

Loss is applied to **all assistant turns** in the multi-turn trajectory,
enabling the model to learn environment observation, action selection,
tool use, and recovery from errors.

## Training Configuration

- Base model: Qwen/Qwen3-4B-Instruct-2507
- Method: LoRA (full precision base)
- Max sequence length: 2048
- Epochs: 2
- Learning rate: 2e-06
- LoRA: r=64, alpha=128

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import torch

base = "Qwen/Qwen3-4B-Instruct-2507"
adapter = "your_id/your-repo"

tokenizer = AutoTokenizer.from_pretrained(base)
model = AutoModelForCausalLM.from_pretrained(
    base,
    torch_dtype=torch.float16,
    device_map="auto",
)
model = PeftModel.from_pretrained(model, adapter)
```

## Sources & Terms (IMPORTANT)

Training data: u-10bei/sft_alfworld_trajectory_dataset_v5

Dataset License: MIT License. This dataset is used and distributed under the terms of the MIT License.
Compliance: Users must comply with the MIT license (including copyright notice) and the base model's original terms of use.
