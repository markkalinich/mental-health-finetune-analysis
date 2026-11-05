---
license: mit
language:
- en
base_model:
- Qwen/Qwen3-0.6B
tags:
- medical
- mental-health
---
# 🧠 Qwen-0.6B Mental Health Support (Fine-Tuned)

**Model Repo:** `xformai/qwen-0.6b-mentalhealth-support`  
**Base Model:** [`Qwen/Qwen-0.5B`](https://huggingface.co/Qwen/Qwen-0.5B)  
**Task:** Empathetic Conversational AI for mental health & emotional support  
**Fine-Tuned By:** [XformAI](https://www.linkedin.com/company/xformai)

---

## 🧠 What is this?

This is a fine-tuned version of the Qwen-0.6B language model, adapted on a curated dataset focused on mental health support and empathetic responses. The goal is to enable helpful, emotionally aware, and safe conversations around stress, anxiety, depression, and general wellness.

---

## 🧪 Use Cases

- Mental health chatbots  
- Emotional support agents  
- Wellness coaching prototypes  
- Journaling assistants

---

## 📊 Training Details

- **Dataset:** Internal collection of therapy-style dialogues, emotional support threads, and curated mental health Q&A (non-clinical)
- **Epochs:** 3  
- **Batch Size:** 16  
- **Optimizer:** AdamW  
- **Context Window:** 2048  
- **Precision:** bfloat16  
- **Framework:** Hugging Face Transformers + PEFT (LoRA)

---

## 🚨 Warnings

⚠️ This model is **not a substitute for professional medical or mental health advice**.  
It is trained to offer support-style language, not diagnosis or clinical recommendations.

---

## 🧠 Example Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("xformai/qwen-0.6b-mentalhealth-support")
tokenizer = AutoTokenizer.from_pretrained("xformai/qwen-0.6b-mentalhealth-support")

prompt = "I've been feeling really overwhelmed lately. Can you help?"
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=100)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))