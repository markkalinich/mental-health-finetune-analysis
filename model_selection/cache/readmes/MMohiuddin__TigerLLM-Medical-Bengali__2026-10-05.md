---
language:
- bn
license: apache-2.0
tags:
- medical
- bengali
- llm
- qlora
- gemma3
---

# TigerLLM Medical Bengali

Bengali medical question answering model fine-tuned using QLoRA on TigerLLM-1B-it.

## Model Details
- Base model: md-nishat-008/TigerLLM-1B-it (Gemma3 architecture)
- Fine-tuning: QLoRA (4-bit + LoRA)
- Dataset: Bangla medical QA (901 samples)
- Language: Bengali

## Usage
```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model = AutoModelForCausalLM.from_pretrained(
    "YOUR_HF_USERNAME/TigerLLM-Medical-Bengali",
    torch_dtype=torch.float16,
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(
    "YOUR_HF_USERNAME/TigerLLM-Medical-Bengali"
)

def ask(question):
    prompt = f"<bos><start_of_turn>system\nআপনি একজন বাংলা চিকিৎসা সহকারী।<end_of_turn>\n<start_of_turn>user\n{question}<end_of_turn>\n<start_of_turn>model\n"
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_new_tokens=512, temperature=0.7, do_sample=True)
    return tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)

print(ask("ডায়াবেটিসের লক্ষণ কী?"))
```
