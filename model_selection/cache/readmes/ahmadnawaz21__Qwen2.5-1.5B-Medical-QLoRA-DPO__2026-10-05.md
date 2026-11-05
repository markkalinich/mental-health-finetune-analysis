---
license: apache-2.0
base_model: unsloth/Qwen2.5-1.5B
tags:
- medical
- healthcare
- qlora
- dpo
- alignment
- text-generation
- unsloth
datasets:
- medalpaca/medical_meadow_medical_flashcards
- argilla/distilabel-intel-orca-dpo-pairs
language:
- en
pipeline_tag: text-generation
library_name: transformers
---

# Qwen2.5-1.5B-Medical-DPO

An end-to-end domain-adapted and preference-aligned LLM for medical decision support and clinical reasoning.

This repository contains the full **16-bit merged weights** of `unsloth/Qwen2.5-1.5B`, fine-tuned using a 2-stage alignment pipeline:
1. **Stage 1 (Domain SFT):** Supervised Fine-Tuning on medical terminology and clinical flashcards via 4-bit QLoRA.
2. **Stage 2 (Preference Alignment):** Direct Preference Optimization (DPO) to maximize helpfulness and mitigate unsafe or non-factual outputs.

---

## Model Details

* **Developed by:** Ahmad Nawaz`
* **Base Model:** `unsloth/Qwen2.5-1.5B`
* **Model Type:** Causal Language Model (Transformer Architecture)
* **Fine-Tuning Method:** QLoRA (4-bit quantization using `bitsandbytes` + PEFT)
* **Alignment Technique:** Direct Preference Optimization (DPO)
* **Target Modules:** `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`
* **Precision:** FP16 (Merged 16-bit floating point weights)

---

## Training Methodology

### Stage 1: Supervised Fine-Tuning (SFT)
* **Dataset:** [`medalpaca/medical_meadow_medical_flashcards`](https://huggingface.co/datasets/medalpaca/medical_meadow_medical_flashcards)
* **Purpose:** Imbues the base model with medical vocabulary, disease symptomatology, and diagnostic logic.
* **Hyperparameters:**
  * Sequence Length: `2048`
  * Micro Batch Size: `2` (Gradient Accumulation: `4`)
  * Learning Rate: `2e-4`
  * Optimizer: `adamw_8bit`
  * Epochs/Steps: `120 steps`

### Stage 2: Direct Preference Optimization (DPO)
* **Dataset:** Subfiltered [`argilla/distilabel-intel-orca-dpo-pairs`](https://huggingface.co/datasets/argilla/distilabel-intel-orca-dpo-pairs)
* **Purpose:** Aligns the model's preferred responses over rejected/hallucinated options.
* **Hyperparameters:**
  * Beta ($\beta$): `0.1`
  * Micro Batch Size: `1` (Gradient Accumulation: `8`)
  * Learning Rate: `5e-6`
  * Optimizer: `adamw_8bit`

---

## How to Use

### Using `transformers`

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "ahmadnawaz21/Qwen2.5-1.5B-Medical-DPO"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto"
)

messages = [
    {"role": "system", "content": "You are a specialized medical AI assistant."},
    {"role": "user", "content": "What are the primary diagnostic indicators and initial management steps for acute pancreatitis?"}
]

prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

outputs = model.generate(
    **inputs,
    max_new_tokens=256,
    temperature=0.3,
    top_p=0.9
)

print(tokenizer.decode(outputs[0][inputs['input_ids'].shape[1]:], skip_special_tokens=True))