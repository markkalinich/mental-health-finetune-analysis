---
license: apache-2.0
tags:
  - generated
  - flan-t5
  - mental-health
  - text2text-generation
  - fine-tuned
  - chatbot
  - huggingface
datasets:
  - mentalchat-16k
language:
  - en
model-index:
  - name: flan-t5-large-mentalchat
    results: []
---

# 🧠 Flan-T5-Large Mental Health Chatbot

This is a fine-tuned version of `google/flan-t5-large` specifically tailored to act as a **mental health support assistant** trained on the **MentalChat-16k** dataset.  
It can provide empathetic and supportive responses to mental health-related prompts, especially around anxiety, stress, overthinking, and low mood.

---

## 📊 Model Info

- **Base Model**: [`google/flan-t5-large`](https://huggingface.co/google/flan-t5-large)
- **Fine-tuned on**: MentalChat-16k Dataset
- **Framework**: Transformers + PyTorch
- **Task**: `text2text-generation`
- **Tokenizer**: AutoTokenizer from base model
- **Safe Format**: Safetensors

---

## 💬 Example Use

```python
from transformers import pipeline

chatbot = pipeline("text2text-generation", model="sarthak0226/flan-t5-large-mentalchat")

prompt = "I'm having trouble sleeping lately. What can I do?"
response = chatbot(prompt, max_length=100, do_sample=True, top_k=50, top_p=0.95)

print(response[0]["generated_text"])
