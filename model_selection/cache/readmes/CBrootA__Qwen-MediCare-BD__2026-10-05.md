---
language:
- en
- bn
license: mit
library_name: transformers
tags:
- medical
- bangladesh
- qwen
- gguf
- healthcare
- offline
- mobile
pipeline_tag: text-generation
model-index:
- name: ShasthoGPT-BD-3B
  results: []
datasets:
- Mahadih534/all-Bangladeshi-medicines
- GBaker/MedQA-USMLE-4-options
base_model:
- Qwen/Qwen2.5-3B-Instruct
---

# 🏥 Qwen-MediCare-BD

**Bangladesh's First Offline Medical AI Assistant**

## Model Description

Qwen-MediCare-BD-3B is a fine-tuned medical language model based on Qwen2.5-3B-Instruct, specifically trained on Bangladesh-specific medical data. It provides accurate medical information offline, making it ideal for regions with limited internet connectivity.

### Key Features
- 🇧🇩 **Bangladesh-specific**: Includes local diseases, drugs, and medical context
- 📱 **Mobile-ready**: Quantized to Q4_K_M (1.8GB)
- 🔒 **100% Offline**: No internet required for inference
- 🩺 **Medically validated**: Trained on 30,523 medical Q&A pairs
- 💚 **Multilingual**: Supports English and Bangla queries

## Model Variants

| Variant | Size | Format | Use Case |
|---------|------|--------|----------|
| Full Model | 6.2 GB | Safetensors | Training/Research |
| Q4_K_M | 1.8 GB | GGUF | Mobile/Edge devices |
| LoRA Adapters | 114 MB | Safetensors | Fine-tuning |

## Quick Start

### Using Transformers
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
    "CBrootA/Qwen-MediCare-BD",
    device_map="auto",
    load_in_4bit=True
)
tokenizer = AutoTokenizer.from_pretrained("CBrootA/Qwen-MediCare-BD")

messages = [
    {"role": "system", "content": "You are a medical assistant for Bangladesh."},
    {"role": "user", "content": "What are dengue symptoms?"}
]

inputs = tokenizer.apply_chat_template(messages, return_tensors="pt").to("cuda")
outputs = model.generate(inputs, max_new_tokens=256)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
