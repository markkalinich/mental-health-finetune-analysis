---
license: apache-2.0
tags:
- chatbot
- mental-health
- text-generation
- emotion-support
- lora
- deepseek
- llama-factory
library_name: transformers
language:
- en
pipeline_tag: text-generation
base_model: deepseek-ai/deepseek-llm-1.5b-chat  # Or deepseek-ai/deepseek-llm-7b-chat
---

# Emotion-Therapy Chatbot Based on DeepSeek LLM (1.5B)

This model is a **emotional-support chatbot** fine-tuned on top of DeepSeek LLM-1.5B / 7B Distill using LoRA. It is designed to simulate empathetic, comforting conversations for emotional wellness, daily companionship, and supportive dialogue scenarios.

## 💡 Project Background

This model is part of the project **"Designing an Emotion-Therapy Chatbot Based on the DeepSeek LLM-1.5B"**. The goal is to build a lightweight, emotionally intelligent chatbot capable of offering comforting and supportive interactions in Chinese, grounded in general large language model capabilities.

## 🔧 Model Training Details

- **Base Model**: `Deepseek R1-1.5B - Distill` or `Deepseek R1-7B - Distill`
- **Platform**: AutoDL with a single NVIDIA RTX 4090 GPU instance
- **Fine-tuning Method**: LoRA (Low-Rank Adaptation) using [LLaMA Factory](https://github.com/hiyouga/LLaMA-Factory)
- **Objective**: Improve model performance on empathetic responses, emotional understanding, and mental support

## 📚 Training Dataset

Custom-built Chinese emotional support corpus, including:

- Typical therapist-style conversational prompts and responses
- Encouraging and empathetic phrases for anxiety, sadness, and loneliness
- User-simulated mental health inputs with varied emotional tone

The dataset was manually cleaned to ensure linguistic fluency, emotional relevance, and safe content.

## 🚀 How to Use

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("chi0818/my-chatbot-model")
tokenizer = AutoTokenizer.from_pretrained("chi0818/my-chatbot-model")

input_text = "Today I feel so lonely and sad……"
inputs = tokenizer(input_text, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=100)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))