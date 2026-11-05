---
language:
- en
license: llama3
tags:
- emotional-intelligence
- empathy
- conversational-ai
- instruction-tuned
- social-reasoning
- dialogue
- human-centered-ai
- llama
pipeline_tag: text-generation
library_name: transformers
---

# Affectra-8B

<p align="center">
  <img src="https://img.shields.io/badge/Focus-Emotional%20Intelligence-blue" />
  <img src="https://img.shields.io/badge/Architecture-Dense%20Transformer-success" />
  <img src="https://img.shields.io/badge/Domain-Dialogue%20%26%20Social%20Reasoning-informational" />
</p>

**Affectra-8B** is an emotionally intelligent instruction-tuned large language model designed for empathetic, socially aware, and human-centered dialogue.  
The model emphasizes emotional understanding, tone appropriateness, and supportive conversational behavior while maintaining strong instruction-following and linguistic coherence.

Affectra-8B targets applications where emotional intelligence and social awareness are critical components of effective human–AI interaction.


## 1. Model Overview

Modern large language models demonstrate strong reasoning and task-following capabilities but often lack emotional sensitivity and social nuance. Affectra-8B is designed to address this limitation by prioritizing affective understanding and empathetic language generation.

The model is optimized for emotionally grounded dialogue, including emotional validation, supportive responses, and socially appropriate conversational tone.


## 2. Architecture & Design

Affectra-8B is a **dense transformer-based language model** with approximately **8 billion parameters**.

The model design emphasizes:
- Linguistic stability in early representations
- Social and contextual reasoning in intermediate layers
- Emotional tone, empathy, and expressive phrasing in higher layers

* This structured representation enables emotionally fluent responses without sacrificing coherence or controllability.
* To achieve smooth behavioral transitions across layers, **Spherical Linear Interpolation (SLERP)** is employed as a weight-space interpolation technique. SLERP enables gradual blending of representational characteristics while preserving vector norms, contributing to stable generation and consistent conversational style.



## 3. Parameter-Space Interpolation & Optimization Strategy

Affectra-8B builds upon instruction-tuned language modeling and is optimized for:

- Empathetic dialogue behavior
- Emotional validation and awareness
- Consistent conversational tone
- Multi-turn dialogue coherence

The optimization strategy focuses on preserving reasoning stability while enhancing affective expressiveness.


## 4. Intended Use Cases

Affectra-8B is suitable for:

- Emotionally aware conversational agents
- Supportive dialogue systems (non-clinical)
- Human-centered AI research
- Social reasoning and affective computing studies
- Emotion-sensitive assistants and chatbots

## 5. Benchmark Performance

Affectra-8B achieves state-of-the-art performance for its size on **EQ-Bench (v2)**, often outperforming significantly larger models in emotional intelligence tasks.

| Model | Parameters | EQ-Bench Score (v2) |
| :--- | :--- | :--- |
| **Affectra-8B** | **8B** | **69.9** |
| Qwen2.5-7B-Instruct | 7B | 69.18 |
| Llama-3-8B-Instruct | 8B | 68.88 |
| Mistral-7B-Instruct-v0.2 | 7B | 68.18 |
| OpenHermes-2.5-Mistral-7B | 7B | 66.89 |


## 6. Limitations & Ethical Considerations

- Affectra-8B is **not a licensed medical, psychological, or legal professional**.
- Outputs should not be used as professional advice.
- Emotional fluency does not guarantee factual correctness.
- Human oversight is recommended for sensitive or high-stakes applications.

## 7. Usage

```python
!pip install -qU transformers accelerate

from transformers import AutoTokenizer
import transformers
import torch

model = "salihfurkaan/Affectra-8B"
messages = [{"role": "user", "content": "What is a large language model?"}]

tokenizer = AutoTokenizer.from_pretrained(model)
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    dtype=torch.bfloat16,
    device_map="auto",
)

outputs = pipeline(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])
```

## 8. License & Acknowledgements
This model inherits the licenses of its base components:

- Meta LLaMA 3 License
- Dolphin model license
Users must comply with all upstream license requirements.

## 9. Acknowledgements:
- Meta AI
- Cognitive Computations
- Nous Research
- mergekit contributors
For feedback, benchmarking results, or collaboration, feel free to open a discussion or issue.