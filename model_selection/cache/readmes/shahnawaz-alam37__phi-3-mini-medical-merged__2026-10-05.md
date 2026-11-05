---
base_model: unsloth/phi-3-mini-4k-instruct-bnb-4bit
library_name: peft
pipeline_tag: text-generation
tags:
- base_model:adapter:unsloth/phi-3-mini-4k-instruct-bnb-4bit
- lora
- peft
- transformers
- pytorch
- unsloth
- healthcare
license: apache-2.0
datasets:
- OpenMed/MedDialog
language:
- en
---

# Description
This repository contains the fully merged version of Phi-3-mini-4k-instruct, fine-tuned on medical dialogues by [Shahnawaz Alam](https://huggingface.co/shahnawaz-alam37).

Unlike the adapter version, this model has the base weights and the QLoRA adapters mathematically combined into a single, standalone model (~5 GB). You do not need the peft library or a separate base model to run this. It is ready for direct deployment in production environments, local inference engines (like Ollama, LM Studio, vLLM), or standard transformers pipelines. It excels at understanding patient symptoms and maintaining a professional healthcare conversational tone, trained on the MedDialog dataset.


# Testing / Inference Code
Because this is a merged model, you can load and test it using standard transformers code just like any other foundational model
```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
model_id = "shahnawaz-alam37/phi-3-mini-medical-merged"

# 1. Load the tokenizer and merged model directly
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,    
    torch_dtype=torch.float16,    
    device_map="auto")

# 2. Format your medical prompt using the built-in chat template
messages = [{
    "role": "system", "content": "You are a helpful and professional medical assistant trained on doctor-patient dialogues."},    
    {"role": "user", "content": "I have been having a persistent headache for three days. What could be causing it and what should I do?"}] # Apply the Phi-3 chat template
inputs = tokenizer.apply_chat_template(
    messages,    
    add_generation_prompt=True,    
    return_tensors="pt").to("cuda")

# 3. Generate the response
outputs = model.generate(
    inputs,    
    max_new_tokens=256,    
    temperature=0.3,    
    top_p=0.9,    
    do_sample=True
)

# 4. Decode and print only the new response (skip the input prompt)
response = outputs[0][inputs.shape[-1]:]
print(tokenizer.decode(response, skip_special_tokens=True))
```


# Training Details
## Frameworks & Libraries
Library: Unsloth & Hugging Face transformers
Method: QLoRA (Quantized Low-Rank Adaptation) via peft
Hardware: Google Colab (NVIDIA T4 GPU)

## Quantization Configuration
4-bit Quantization: Enabled (via bitsandbytes)
Quantization Type: NF4 (NormalFloat 4-bit)
Double Quantization: Enabled
Compute Dtype: bfloat16

## LoRA Configuration
Rank (r): 16
Alpha: 16
Dropout: 0 (None)
Target Modules: ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]

## Training Hyperparameters
Epochs: 3 (change if you used more/less)
Batch Size: 2 (per device)
Gradient Accumulation Steps: 4 (Effective batch size = 8)
Optimizer: AdamW ("paged_adamw_32bit")
Learning Rate: 2e-4
LR Scheduler: Linear
Max Sequence Length: 2048 (change if you used 4096)
Warmup Ratio: 0.05
Weight Decay: 0.01

## Training Procedure
The model was fine-tuned using Unsloth's highly optimized SFTTrainer (Supervised Fine-Tuning) on the MedDialog dataset. The base model was loaded in 4-bit to minimize VRAM usage, while the LoRA adapters were trained in full 16-bit precision, allowing efficient training on a single consumer-grade GPU.

# Declaration & Disclaimer

**Intended Use**: This model is developed strictly for *research, educational, and demonstration purposes* in the field of Natural Language Processing (NLP) and conversational AI. It is designed to showcase how LLMs can be adapted for medical dialogue understanding.

**NOT a Medical Device**: This model is NOT a certified medical device, clinical decision support system, or a substitute for professional medical advice, diagnosis, or treatment. It must not be used to make real-world clinical decisions or to provide medical advice to actual patients.

**Accuracy & Hallucinations**: While fine-tuned on the MedDialog dataset to improve medical context, this model is still a statistical language model. It is prone to hallucinations, biases, and may generate plausible-sounding but factually incorrect, outdated, or dangerous medical information.

**Data Limitations**: The model's knowledge and tone are bounded by the base model (Phi-3-mini) and the MedDialog dataset. It may not accurately represent all medical specialties, diverse patient demographics, or recent medical advancements.

**Authorship Declaration**: This model was fine-tuned by Shahnawaz Alam as a personal research project. The underlying base model is developed by Microsoft, and the fine-tuning was facilitated by the Unsloth library. The authors assume no liability for any actions taken based on the outputs of this model.

By using this model, you explicitly agree to these terms and accept full responsibility for its use.