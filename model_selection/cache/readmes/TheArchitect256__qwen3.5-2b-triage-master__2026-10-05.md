---
base_model: unsloth/Qwen3.5-2B
tags:
- text-generation-inference
- transformers
- unsloth
- qwen3_5
- tool-routing
- triage
license: apache-2.0
language:
- en
---

# Triage Master - Qwen3.5-2B

A fine-tuned router/triage model that selects the appropriate tool from a given schema based on a user query. Intended for use as a routing node in multi-agent pipelines (e.g. LangGraph, CrewAI) to classify intent and dispatch to the correct downstream tool.

## Model Details

- **Developed by:** TheArchitect256
- **License:** apache-2.0
- **Finetuned from model:** [unsloth/Qwen3.5-2B](https://huggingface.co/unsloth/Qwen3.5-2B)
- **Task:** Tool/intent routing (single-label classification framed as text generation)

## Training Details

- **Method:** LoRA (r=16, alpha=16, dropout=0), target modules: q/k/v/o_proj, gate/up/down_proj
- **Dataset:** ~5,000 custom instruction examples, Alpaca format, covering routing scenarios with 2-4 available tools per prompt
- **Epochs:** 3
- **Batch size:** 32 (A100, bf16)
- **Learning rate:** 2e-4
- **Optimizer:** AdamW 8-bit
- **Framework:** [Unsloth](https://github.com/unslothai/unsloth) + TRL SFTTrainer

## Evaluation

Evaluated on a held-out set of 500 examples (not seen during training):

- **Accuracy: 99.4% (497/500)**
- Remaining errors occur on semantically ambiguous cases where multiple tools are plausible (e.g. routing vs. mapping tools, read vs. update operations on similarly-named systems)

## Usage

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "TheArchitect256/qwen3.5-2b-triage-master"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, dtype=torch.bfloat16, device_map="auto")

alpaca_prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{}

### Input:
{}

### Response:
"""

instruction = """Available tools:
1. [STOCK_CHECK]: Verifies if an item is available in the warehouse inventory.
2. [SHIPPING_CALC]: Calculates delivery rates and times based on postal codes.

User Query: Can you tell me if we still have the RTX 4060 graphics card in our warehouse?"""

prompt = alpaca_prompt.format(instruction, "")
inputs = tokenizer(text=prompt, return_tensors="pt").to(model.device)

outputs = model.generate(**inputs, max_new_tokens=20, do_sample=False, pad_token_id=tokenizer.eos_token_id)
print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))

# **Note:** The model does not reliably emit an EOS token after the tool label, so `generate()` may continue producing text past the intended answer. Always truncate the output to the first `[TOOL_NAME]`-style tag rather than relying on generation length alone:

import re
match = re.search(r"\[[A-Z_]+\]", response)
clean_response = match.group(0) if match else response.strip()
```

This model was trained 2x faster with [Unsloth](https://github.com/unslothai/unsloth) and Hugging Face's TRL library.

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)