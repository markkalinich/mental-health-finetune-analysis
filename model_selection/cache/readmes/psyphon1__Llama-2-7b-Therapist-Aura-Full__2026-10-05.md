# 🔮 Aura-Therapist (Aura Ai Project)

![License](https://img.shields.io/badge/License-Llama%202-blue.svg) ![Project](https://img.shields.io/badge/Project-Aura%20Ai-purple) ![Model](https://img.shields.io/badge/Model-Aura--Therapist-green) ![Developer](https://img.shields.io/badge/Developer-Chinmay%20Duse-orange)

**Aura-Therapist** is the specialized large language model powering the **Aura Ai** mental health platform. It is a fine-tuned iteration of `Meta-Llama-2-7b-chat`, specifically engineered to provide empathetic, non-judgmental, and psychologically grounded support interactions.

Unlike general-purpose assistants, this model has been aligned to prioritize active listening, emotional validation, and concise, human-like support.

**Lead Developer:** Chinmay Duse

---

## 🎯 Project Objective
The goal of the Aura Ai project is to bridge the gap between rigid chatbots and human-like emotional intelligence. **Aura-Therapist** is designed to:
* **Reflect Feelings:** Use active listening techniques to validate user emotions before offering solutions.
* **Safe Interaction:** Recognize distress and offer supportive, non-clinical guidance.
* **Concise Empathy:** Provide warm responses optimized for real-time chat interfaces, avoiding robotic or overly verbose lectures.

---

## ⚠️ Critical Safety & Ethics Disclaimer

**Aura-Therapist is an AI tool, not a licensed medical professional.**
* **Scope:** Educational and supportive conversation only.
* **Limitations:** It cannot diagnose mental health disorders, prescribe medication, or intervene in emergencies.
* **Crisis Protocols:** This model is **not** equipped to handle active suicidal ideation or self-harm. Users in crisis should always be directed to human emergency services.

---

## 🚀 Deployment Guide

### 1. Environment Setup
Aura-Therapist is optimized for efficiency and can run on consumer hardware (minimum 6GB VRAM) using 4-bit quantization.

```bash
pip install torch transformers accelerate bitsandbytes
```

---

### 2. Integration (Python)

The model is hosted on Hugging Face. Use this script to integrate it into the Aura Ai backend or test environment.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

# 📍 Official Model Identifier
model_id = "psyphon1/Llama-2-7b-Therapist-Aura-Full"

# ⚙️ Efficient 4-Bit Configuration
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
)

# 📥 Load Weights
print(f"⏳ Loading Aura-Therapist from: {model_id}")
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    quantization_config=bnb_config,
    device_map="auto"
)

def get_aura_response(user_text):
    # System Persona (Critical for maintaining character)
    system_prompt = "You are an empathetic AI therapist. Be warm, concise, and helpful."

    prompt = f"<s>[INST] <<SYS>>
{system_prompt}
<</SYS>>

{user_text} [/INST]"

    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

    with torch.no_grad():
        output = model.generate(
            **inputs, 
            max_new_tokens=256, 
            temperature=0.7, # Optimized for balanced empathy
            top_p=0.9,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )

    return tokenizer.decode(output[0], skip_special_tokens=True).split("[/INST]")[-1].strip()

# Example Interaction
user_query = "I feel really overwhelmed by my workload and I don't know where to start."
print(f"User: {user_query}")
print(f"Aura: {get_aura_response(user_query)}")
```

---

## 🔧 Technical Specifications
- **Base Architecture:** Llama-2-7b-chat-hf  
- **Fine-Tuning Method:** QLoRA (Quantized Low-Rank Adaptation)  
- **Training Hardware:** NVIDIA T4 GPU (Kaggle Environment)  

### Hyperparameters:
```
Rank (r): 32  
Alpha: 16  
Precision: Float16 (fp16)  
Dataset: Aura-Curated-2k (Curated clinical instruction pairs, cleaned for repetition removal)
```

---

## 💻 CLI Testing Tool
For rapid testing in a terminal environment:

```python
print("🔮 Aura Ai Terminal Initialized...")
print("Type 'exit' to close session.
")

while True:
    user_in = input("You: ")
    if user_in.lower() in ['exit', 'quit']: break

    response = get_aura_response(user_in)
    print(f"🤖 Aura: {response}
")
```

---

## 📜 License & Credits
**Project:** Aura Ai  
**Lead Developer:** Chinmay Duse  
**License:** This model is a derivative of Llama 2 and is subject to the Meta Llama 2 Community License Agreement. Users must comply with Meta's usage policy, particularly regarding responsible AI use.
