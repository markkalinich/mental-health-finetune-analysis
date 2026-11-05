---
library_name: transformers
tags:
- medical
- xnet
- qwen
license: apache-2.0
datasets:
- FreedomIntelligence/medical-o1-reasoning-SFT
language:
- en
base_model:
- Qwen/Qwen3-32B
pipeline_tag: text-generation
---

# Intro

This is https://huggingface.co/kingabzpro/Qwen-3-32B-Medical-Reasoning applied to https://huggingface.co/Qwen/Qwen3-32B
[Original model card](https://huggingface.co/kingabzpro/Qwen-3-32B-Medical-Reasoning) created by [@kingabzpro](https://huggingface.co/kingabzpro)

---

# Original model card from @kingabzpro

## Fine-tuning Qwen3-32B in 4-bit Quantization for Medical Reasoning

This project fine-tunes the [`Qwen/Qwen3-32B`](https://huggingface.co/Qwen/Qwen3-32B) model using a medical reasoning dataset (`FreedomIntelligence/medical-o1-reasoning-SFT`) with **4-bit quantization** for memory-efficient training.

---

## Setup

1. Install the required libraries:

```bash
pip install -U datasets accelerate peft trl bitsandbytes
pip install -U transformers
pip install huggingface_hub[hf_xet]
```

2. Authenticate with Hugging Face Hub:

Make sure your Hugging Face token is stored in an environment variable:

```bash
export HF_TOKEN=your_huggingface_token
```

The notebook will automatically log you in using this token.

---

## How to Run

1. **Load the Model and Tokenizer**  
   The script downloads the Qwen3-32B model and applies 4-bit quantization with `BitsAndBytesConfig` for efficient memory usage.

2. **Prepare the Dataset**  
   - The notebook uses `FreedomIntelligence/medical-o1-reasoning-SFT` (first 500 samples).
   - It formats each example into an **instruction-following prompt** with step-by-step chain-of-thought reasoning.

3. **Fine-tuning**  
   - Fine-tuning is set up with PEFT (LoRA / Adapter Tuning style) to modify a small subset of model parameters.
   - TRL (Transformer Reinforcement Learning) is used to fine-tune efficiently.

4. **Push Fine-tuned Model**  
   - After training, the fine-tuned model and tokenizer are pushed back to your Hugging Face account.

---

>> Here is the training notebook: [Fine_tuning_Qwen-3-32B](https://huggingface.co/kingabzpro/Qwen-3-32B-Medical-Reasoning/blob/main/fine-tuning-qwen-3.ipynb)

## Model Configuration

- **Base Model**: `Qwen/Qwen3-32B`
- **Quantization**: 4-bit (NF4)
- **Training**: PEFT + TRL
- **Dataset**: 2000 examples from medical reasoning dataset

---

## Notes

- **GPU Required**: Make sure you have access to 1X A100s. Get it from RunPod for an hours. Training took only 50 minutes.
- **Environment**: The notebook expects an environment where NVIDIA CUDA drivers are available (`nvidia-smi` check is included).
- **Memory Efficiency**: 4-bit loading greatly reduces memory footprint.

---

## Example Prompt Format

```
Below is an instruction that describes a task, paired with an input that provides further context. 
Write a response that appropriately completes the request. 
Before answering, think carefully about the question and create a step-by-step chain of thoughts to ensure a logical and accurate response.

### Instruction:
You are a medical expert with advanced knowledge in clinical reasoning, diagnostics, and treatment planning. 
Please answer the following medical question.

### Question:
{}

### Response:
<think>
{}
</think>
{}
```

---
## Usage Script (not-tested)

```python
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import PeftModel
import torch

# Base model (original model from Meta)
base_model_id = "Qwen/Qwen3-32B"

# Your fine-tuned LoRA adapter repository
lora_adapter_id = "kingabzpro/Qwen-3-32B-Medical-Reasoning"

# Load the model in 4-bit
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=False,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
)

# Load base model
base_model = AutoModelForCausalLM.from_pretrained(
    base_model_id,
    device_map="auto",
    torch_dtype=torch.bfloat16,
    quantization_config=bnb_config,
    trust_remote_code=True,
)

# Attach the LoRA adapter
model = PeftModel.from_pretrained(
    base_model,
    lora_adapter_id,
    device_map="auto",
    trust_remote_code=True,
)

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(base_model_id, trust_remote_code=True)

# Inference example
prompt = """Below is an instruction that describes a task, paired with an input that provides further context. 
Write a response that appropriately completes the request. 
Before answering, think carefully about the question and create a step-by-step chain of thoughts to ensure a logical and accurate response.

### Instruction:
You are a medical expert with advanced knowledge in clinical reasoning, diagnostics, and treatment planning. 
Please answer the following medical question.

### Question:
What is the initial management for a patient presenting with diabetic ketoacidosis (DKA)?

### Response:
<think>
"""

inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=1200)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(response)



```


