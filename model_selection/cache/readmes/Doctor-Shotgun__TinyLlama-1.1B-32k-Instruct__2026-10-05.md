---
inference: false
language:
- en
library_name: transformers
pipeline_tag: text-generation
tags:
- llama
datasets:
- LDJnr/Capybara
- jondurbin/airoboros-3.2
- unalignment/toxic-dpo-v0.1
- LDJnr/Verified-Camel
- HuggingFaceH4/no_robots
- Doctor-Shotgun/no-robots-sharegpt
- Doctor-Shotgun/capybara-sharegpt
---

# Norobara-ZLoss-8x7B

This is an instruct-tuned [TinyLlama-1.1B-32k](https://huggingface.co/Doctor-Shotgun/TinyLlama-1.1B-32k) on several open-source instruct datasets, intended primarily for speculative decoding.

## Usage:
The intended prompt format is a modified multi-turn Alpaca instruction format:
```
### Instruction:
{system prompt}

### Input:
{user message}

### Response:
{model response}

### Input:
{user message}

### Response:
{model response}

(etc.)
```

## Bias, Risks, and Limitations
The model will show biases present in the base model. No ethical alignment was applied to prevent the generation of toxic or harmful outputs (in fact the opposite, with examples from toxic-DPO included), so generate at your own risk.
## Training Details
This model was trained as a full finetune for 3 epochs using a single A100 GPU for around 3.5 hours.