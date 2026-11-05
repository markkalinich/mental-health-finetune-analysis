---
language: en
license: mit
library_name: transformers
tags:
- llama
- llama-3
- causal-lm
- vllm
- conversational
- cognitive-therapy
- mental-health
- lora
- peft
inference:
  parameters:
    max_new_tokens: 256
    temperature: 0.7
    top_p: 0.9
    repetition_penalty: 1.1
datasets:
- Lumiiree/therapod-dpo
base_model:
- meta-llama/Llama-3.2-3B-Instruct
---

# 🧠 CBT-Copilot

**CBT-Copilot** is a fine-tuned version of [`meta-llama/Llama-3.2-3B-Instruct`](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct), designed to simulate compassionate and supportive dialogues in the style of **Cognitive Behavioral Therapy (CBT)**.

Fine-tuned using LoRA on the [`Lumiiree/therapod-dpo`](https://huggingface.co/datasets/Lumiiree/therapod-dpo) dataset and merged into a standalone model, it supports deployment through `transformers`, `vLLM`, and other inference frameworks.

---

## 🚀 How to Use (with vLLM)

Serve this model using [vLLM](https://github.com/vllm-project/vllm):

```bash
pip install vllm[serve]

python3 -m vllm.entrypoints.openai.api_server --model thillaic/CBT-Copilot
```

Then query it via the OpenAI-compatible API:

```python
import openai

openai.api_key = "EMPTY"
openai.api_base = "http://localhost:8000/v1"

response = openai.ChatCompletion.create(
    model="CBT-Copilot",
    messages=[
        {"role": "system", "content": "You are a compassionate CBT therapist."},
        {"role": "user", "content": "I've been feeling really anxious lately. What can I do?"}
    ]
)

print(response["choices"][0]["message"]["content"])
```

---

## 🧠 Intended Use

This model is intended for:

- Mental health chatbot research
- Journaling and self-reflection tools
- Prototyping conversational CBT agents

> ⚠️ **Disclaimer**: This model is not a replacement for licensed mental health professionals. It should only be used for **educational, research, or prototyping purposes**.

---

## 📜 License

Licensed under the **MIT License**.

---

## 🙏 Acknowledgements

- Based on Meta’s LLaMA 3.2B Instruct model
- Trained on [Lumiiree/therapod-dpo](https://huggingface.co/datasets/Lumiiree/therapod-dpo)
- Fine-tuning performed with Hugging Face `transformers`, `PEFT`, and `LoRA`

---

**🛠️ Model developed by [Thillai Chithambaram](https://huggingface.co/thillaic)**