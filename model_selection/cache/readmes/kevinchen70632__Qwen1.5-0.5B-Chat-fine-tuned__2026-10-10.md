---
library_name: transformers
base_model: Qwen/Qwen1.5-0.5B-Chat
tags:
  - dpo
  - qlora
  - lora
  - safety
  - alignment
  - trl
  - peft
---

# Qwen1.5-0.5B-Chat — DPO + QLoRA Safety-Aligned

A safety-aligned fine-tune of `Qwen/Qwen1.5-0.5B-Chat`, trained with **Direct Preference Optimization (DPO)** and **QLoRA** as a resource-efficient alternative to standard RLHF.

Team project by **Kuan-Ting Chen, Lady Infante Acosta, and Tharit Saengsuwan**.
Code, data prep, and full evaluation methodology: [github.com/kc3953/dpo-qlora-alignment](https://github.com/kc3953/dpo-qlora-alignment)

## Motivation

RLHF is the industry-standard approach for aligning LLMs to human safety standards, but it's resource-intensive and hard to tune — typically requiring multiple models loaded into memory at once, which is infeasible on limited compute (e.g. a single consumer GPU). This project uses DPO (no separate reward model needed) combined with QLoRA (4-bit quantized LoRA) to make alignment training feasible on a single free-tier Colab GPU.

## Training

- **Base model:** `Qwen/Qwen1.5-0.5B-Chat`
- **Method:** DPO via `trl`'s `DPOTrainer`, with a LoRA adapter (`r=64`, `alpha=128`) over the attention and MLP projection layers, trained in 4-bit (QLoRA, via `bitsandbytes`)
- **Hardware:** single Tesla T4 (~14.7 GB), peak reserved memory under 2 GB
- **Training data:** a combined pool of 306,387 prompt/chosen/rejected preference triples from `Anthropic/hh-rlhf`, `Intel/orca_dpo_pairs`, and `Dahoas/full-hh-rlhf`; the DPO run itself trained on a 1,224-example subsample (307 held out for evaluation), given the compute budget

This repo contains the **merged** model (base weights + LoRA adapter folded in) — load and use it directly, no separate adapter loading required.

## Evaluation

Generations from the base model and the fine-tuned model were scored by a separate LLM judge (`Qwen/Qwen2.5-3B-Instruct`, chain-of-thought reasoning) on the held-out test set:

| Metric | Base model | DPO + QLoRA fine-tuned | Δ |
|---|---|---|---|
| Safe rate | 86.64% | 87.95% | **+1.31 pp** |
| Over-refusal rate | 13.96% | 11.70% | **−2.26 pp** (lower is better) |
| Helpfulness rate | 84.91% | 87.17% | **+2.26 pp** |

All three metrics moved in the right direction at once — safer, fewer unnecessary refusals on benign prompts, and more helpful, rather than trading safety off against usefulness.

## How to use

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "kevinchen70632/Qwen1.5-0.5B-Chat-fine-tuned"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")

messages = [{"role": "user", "content": "How do I safely store household chemicals?"}]
inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to(model.device)
output = model.generate(inputs, max_new_tokens=256)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

## Limitations

- The base model is small (0.5B parameters) and the DPO run trained on a compute-constrained subsample (1,224 examples) — this is a proof-of-concept for the DPO+QLoRA approach on limited hardware, not a production-scale alignment run.
- Safety evaluation relies on an LLM judge rather than human review; judge errors are possible.
- License: inherited from the base model, `Qwen/Qwen1.5-0.5B-Chat`.
