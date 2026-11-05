---
language: en
tags:
- mental-health
- conversational
- dialogpt
- lora
- peft
- empathy
base_model: microsoft/DialoGPT-medium
datasets:
- Estwld/empathetic_dialogues_llm
---

# 🌿 Suhaib — Mental Health Support Chatbot

A conversational AI companion fine-tuned on empathetic dialogues to provide 
emotionally supportive responses about stress, anxiety, and emotional wellness.

## Model Details

| Item | Details |
|------|---------|
| **Base Model** | microsoft/DialoGPT-medium (345M parameters) |
| **Fine-Tuning** | LoRA (PEFT) — only 4.3M / 359M params trained (1.2%) |
| **Dataset** | Estwld/empathetic_dialogues_llm — 15,000 samples |
| **Training** | Google Colab T4 GPU — ~47 minutes |
| **Eval Loss** | 3.33 |
| **Perplexity** | 27.93 |

## LoRA Configuration

```python
LoraConfig(
    r=16,
    lora_alpha=32,
    lora_dropout=0.1,
    target_modules=["c_attn", "c_proj"],
    task_type=TaskType.CAUSAL_LM,
)
Safety System
This model is deployed with a 3-layer safety system:

Crisis Detection — keyword matching bypasses generation, returns hotline resources
Unsafe Response Filter — regex checks on generated output
Empathy Gate — minimum length and quality threshold enforcement
Usage
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("ISuhaibM/suhaib-mental-health-chatbot")
model = AutoModelForCausalLM.from_pretrained("ISuhaibM/suhaib-mental-health-chatbot")

Or run the full app:

git clone https://github.com/Suhaib580/Suhaib-Mental-Health-Chatbot
pip install -r requirements.txt
streamlit run app.py

Disclaimer
This model is for emotional support only. It is not a licensed therapist
and cannot replace professional mental health care. If you are in crisis,
please contact a professional immediately.

Pakistan: Umang Pakistan — 0317-4288665
Global: Crisis Text Line — text HOME to 741741
