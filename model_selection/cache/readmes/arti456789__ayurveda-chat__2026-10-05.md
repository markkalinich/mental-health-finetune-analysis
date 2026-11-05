---
license: apache-2.0
language:
  - en
library_name: transformers
pipeline_tag: text-generation
base_model: Qwen/Qwen2.5-1.5B
tags:
  - qwen2
  - text-generation
  - ayurveda
  - ayurveda-chatbot
  - ayurvedic-medicine
  - chatbot
  - instruct
  - conversational-ai
  - health-education
  - wellness
  - dosha
  - vata
  - pitta
  - kapha
  - prakriti
  - agni
---

# Ayurveda Chat

Ayurveda Chat is a fine-tuned text-generation model designed to answer questions about Ayurveda in a simple, conversational, beginner-friendly way.

The model can help with general Ayurveda education, dosha explanations, Vata, Pitta, Kapha, Prakriti, Agni, digestion, daily routine, seasonal care, Panchakarma education, food guidance, sleep, skin care, hair care, and general wellness-style questions.

This model is intended for educational chatbot demos and general learning. It is not a medical professional and should not be used for diagnosis, treatment, or emergency care.

## Model Overview

- **Model ID:** `arti456789/ayurveda-chat`
- **Base model:** `Qwen/Qwen2.5-1.5B`
- **Task:** Text generation / chat
- **License:** Apache 2.0
- **Language:** English
- **Library:** Transformers

## Try the Demo

You can test the model in the browser through the Space:

[Open Ayurveda Chat Space](https://huggingface.co/spaces/arti456789/ayurveda-chat-space)

## Try in Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1E4UaV_CE6VyXB5s4CDNves3K5JOXmFC1?usp=sharing)

## How to Use

### Install Requirements

```bash
pip install transformers accelerate safetensors sentencepiece torch
```

### With Transformers

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

repo_id = "arti456789/ayurveda-chat"

tokenizer = AutoTokenizer.from_pretrained(repo_id, use_fast=True)

model = AutoModelForCausalLM.from_pretrained(
    repo_id,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    device_map="auto" if torch.cuda.is_available() else None,
)

model.eval()

def ask_model(question, max_new_tokens=180):
    prompt = f"""System: You are a helpful Ayurveda education assistant. Answer in simple, clear, natural, beginner-friendly language. Stay educational and safe. Do not claim to cure serious diseases. For urgent symptoms, serious illness, pregnancy, child health, chronic disease, or medication questions, suggest a qualified healthcare professional.

User: {question}
Assistant:"""

    inputs = tokenizer(prompt, return_tensors="pt")

    if torch.cuda.is_available():
        inputs = {k: v.to(model.device) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            repetition_penalty=1.12,
            pad_token_id=tokenizer.eos_token_id,
        )

    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return text.split("Assistant:")[-1].strip()

print(ask_model("What is Vata dosha?"))
```

## Example Prompts

- What is Ayurveda?
- What is Vata dosha?
- What are the three doshas?
- Compare Vata, Pitta, and Kapha.
- What is Prakriti in Ayurveda?
- What is Agni in Ayurveda?
- How does Ayurveda explain digestion?
- Is Panchakarma a simple home detox?
- What should I eat if my digestion is weak?
- Can Ayurveda cure diabetes?
- I have fever, what should I do?
- I want bright skin. What should I do?
- Give me simple daily routine tips from Ayurveda.
- What are common Vata imbalance signs?
- What are common Pitta imbalance signs?
- What are common Kapha imbalance signs?

## Intended Use

This model is intended for:

- general Ayurveda Q&A
- simple explanatory responses
- educational chatbot demos
- beginner-friendly Ayurveda learning
- dosha explanation
- Vata, Pitta, and Kapha education
- Prakriti and Agni explanation
- wellness and lifestyle discussion
- conversational text-generation examples

## Out-of-Scope Use

This model should not be used for:

- medical diagnosis
- emergency care
- replacing a doctor or qualified clinician
- prescribing herbs, medicines, or supplements
- treating serious disease
- pregnancy medical decisions
- child medical decisions
- medication interaction decisions
- emergency symptom evaluation

## Limitations

- This model is not a medical professional.
- It should not be used for diagnosis, treatment, emergency care, or medical decision-making.
- It may give incorrect, incomplete, outdated, or oversimplified answers.
- It may sometimes generate confident-sounding but inaccurate information.
- It may not understand all medical conditions or personal health contexts.
- Always verify important health information with a qualified clinician.

## Safety Note

If you have urgent symptoms such as chest pain, breathing difficulty, sudden weakness, severe bleeding, fainting, confusion, high fever, severe dehydration, severe allergic reaction, or pregnancy-related complications, seek emergency medical care immediately.

For chronic illness, children, pregnancy, serious symptoms, medication questions, or supplement/herb use, consult a qualified healthcare professional before making health decisions.

## Recommended System Prompt

For safer and more consistent responses, use this system prompt when running the model:

```text
You are a helpful Ayurveda education assistant. Answer in simple, clear, natural, beginner-friendly language. Stay educational and safe. Do not claim to cure serious diseases. For urgent symptoms, serious illness, pregnancy, child health, chronic disease, or medication questions, suggest a qualified healthcare professional.
```

## Training Notes

This repository contains the exported model files and tokenizer files for the fine-tuned Ayurveda chatbot.

The model was fine-tuned for conversational Ayurveda education, simple explanations, safety-aware answers, and beginner-friendly responses.

## Files Included

- `config.json`
- `model.safetensors`
- `tokenizer.json`
- `tokenizer_config.json`
- `special_tokens_map.json`
- `added_tokens.json`
- `vocab.json`
- `merges.txt`

## Citation

If you use this model, please cite the repository and the underlying base model.

- Model: `arti456789/ayurveda-chat`
- Base model: `Qwen/Qwen2.5-1.5B`

## Disclaimer

This model provides general educational information only. It does not provide medical advice, diagnosis, or treatment. Always consult a qualified healthcare professional for personal medical concerns.
