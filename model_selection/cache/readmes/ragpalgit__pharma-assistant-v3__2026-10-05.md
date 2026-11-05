
---
title: Pharma Assistant v3
tags:
- medical
- healthcare
- chatbot
- RAG
- fine-tuning
- unsloth
- tinyllama
---

# Pharma Assistant v3

This model is a fine-tuned version of `unsloth/tinyllama-bnb-4bit` for pharmaceutical question answering, developed using a 3-stage fine-tuning pipeline with Unsloth.

## Training Pipeline

The model was trained using the following stages:
1.  **Stage 1: Non-instruction continued pretraining** on PDF documents related to Metformin and Lipid Therapy knowledge.
2.  **Stage 2: Instruction fine-tuning** on a custom `pharma_instruction_dataset.jsonl`.
3.  **Stage 3: DPO (Direct Preference Optimization)** using a `pharma_preference_dataset.jsonl` to align with preferred responses.

## Model Details

- **Base Model**: `unsloth/tinyllama-bnb-4bit`
- **Fine-tuning Framework**: Unsloth
- **Architecture**: Llama-based, 4-bit quantized

## Usage

To use this model for inference, you can load it using the Hugging Face Transformers library and Unsloth:

```python
from unsloth import FastLanguageModel
import torch

# Load model
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "ragpalgit/pharma-assistant-v3", # YOUR MODEL_ID
    max_seq_length = 512,
    dtype = None,
    load_in_4bit = True,
)

# Example inference (using generate_answer helper from notebook)
instruction = "Explain metformin in simple language."
prompt = f"### Instruction:
{instruction}

### Response:
"

inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

with torch.inference_mode():
    output = model.generate(
        **inputs,
        max_new_tokens=150,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.1,
        pad_token_id=tokenizer.eos_token_id,
        eos_token_id=tokenizer.eos_token_id,
    )

input_tokens = inputs["input_ids"].shape[-1]
generated_tokens = output[0][input_tokens:]
print(tokenizer.decode(generated_tokens, skip_special_tokens=True).strip())
```
