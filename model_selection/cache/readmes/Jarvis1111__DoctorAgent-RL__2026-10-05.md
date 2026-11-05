---
license: apache-2.0
pipeline_tag: text-generation
library_name: transformers
tags:
  - dialogue
  - medical
  - reinforcement-learning
  - multi-agent
---

# DoctorAgent-RL: A Multi-Agent Collaborative Reinforcement Learning System for Multi-Turn Clinical Dialogue

This repository contains the `DoctorAgent-RL` model, which is a reinforcement learning (RL)-based multi-agent collaborative framework designed to revolutionize clinical dialogue. The model is presented in the paper [DoctorAgent-RL: A Multi-Agent Collaborative Reinforcement Learning System for Multi-Turn Clinical Dialogue](https://huggingface.co/papers/2505.19630).

**Code**: [https://github.com/JarvisUSTC/DoctorAgent-RL](https://github.com/JarvisUSTC/DoctorAgent-RL)

<div align="center">
  <img width="1231" alt="DoctorAgent-RL Framework" src="https://github.com/user-attachments/assets/bd9f676e-01f9-406c-881d-c2b9f45e62f3" />
</div>

## Introduction

DoctorAgent-RL addresses the critical limitations of static clinical dialogue systems by modeling medical consultations as dynamic decision-making processes under uncertainty. It enables:

1.  **Adaptive Information Gathering**: Intelligent adjustment of dialogue paths based on patient responses.
2.  **Clinical Reasoning Alignment**: Autonomous development of interaction strategies consistent with medical logic.
3.  **Overcoming Static Paradigms**: Moving beyond superficial pattern imitation in existing dialogue datasets.

Through continuous multi-turn interactions between doctor and patient agents, optimized via reinforcement learning, DoctorAgent-RL achieves significant improvements in diagnostic accuracy and interaction efficiency.

## Key Features

-   🧠 **Multi-Agent Collaboration**: Doctor and patient agents with distinct roles and objectives.
-   📈 **Dynamic Strategy Optimization**: Reinforcement learning-based policy updates for adaptive behavior.
-   🎯 **Comprehensive Reward Design**: Multi-dimensional consultation evaluation metrics guiding optimal strategies.
-   📊 **Medical Knowledge Integration**: Clinical reasoning logic embedded in decision-making processes.
-   📄 **MTMedDialog Dataset**: The first English multi-turn medical consultation dataset designed with simulation capabilities.

## Usage

You can use the `DoctorAgent-RL` model with the Hugging Face `transformers` library for text generation in a multi-turn dialogue context.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the model and tokenizer
model_id = "Jarvis1111/DoctorAgent-RL" 
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.bfloat16, device_map="auto")

# Prepare a sample conversation
messages = [
    {"role": "user", "content": "Hello Doctor, I have a headache and feel tired."},
]

# Apply the chat template defined in the tokenizer_config.json
# This is crucial for proper multi-turn dialogue with Qwen models
text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

# Generate response
input_ids = tokenizer(text, return_tensors="pt").input_ids.to(model.device)
output = model.generate(input_ids, max_new_tokens=256, do_sample=True, temperature=0.7, top_p=0.9)
response = tokenizer.decode(output[0], skip_special_tokens=True)

print(response)
```

## Citation

If DoctorAgent-RL contributes to your research, please consider citing our work:

```latex
@article{feng2025doctoragent,
  title={DoctorAgent-RL: A Multi-Agent Collaborative Reinforcement Learning System for Multi-Turn Clinical Dialogue},
  author={Feng, Yichun and Wang, Jiawei and Zhou, Lu and Li, Yixue},
  journal={arXiv preprint arXiv:2505.19630},
  year={2025}
}
```