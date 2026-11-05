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
- affectra
pipeline_tag: text-generation
library_name: transformers
---
# Affectra v2 (8B-EQ)
<p align="center">
  <img src="https://img.shields.io/badge/Focus-Emotional%20Intelligence-blue" />
  <img src="https://img.shields.io/badge/Architecture-Dense%20Transformer-success" />
  <img src="https://img.shields.io/badge/Domain-Dialogue%20%26%20Social%20Reasoning-informational" />
  <img src="https://img.shields.io/badge/Version-v2-purple" />
</p>

**Affectra-2-8B-EQ** is the second generation of the Affectra series, setting a new standard for emotionally intelligent language modeling in the 8B parameter class.  
Building on the success of v1, this model features refined emotional alignment, improved tokenizer compatibility, and significantly enhanced social reasoning capabilities.
It is designed for empathetic, socially aware, and human-centered dialogue, prioritizing emotional validation and tone appropriateness without sacrificing instruction-following performance.

## 1. Model Overview
While modern LLMs excel at reasoning, they often struggle with authentic emotional connection. **Affectra 2** addresses this by deeply integrating affective understanding into its generation process. 
**New in v2:**
*   **Enhanced EQ**: A significant leap in emotional reasoning performance (see benchmarks).
*   **Smoother Dialogue**: Improved turn-taking dynamics and validation strategies.

## 2. Architecture & Design
Affectra 2 is a **dense transformer-based language model** with approximately **8 billion parameters**, based on the Llama 3 architecture.
The model design emphasizes:
- Linguistic stability in early representations
- Social and contextual reasoning in intermediate layers
- **High-fidelity emotional tone** and empathy in higher layers
Key techniques include **Spherical Linear Interpolation (SLERP)** for stable weight blending and targeted instruction tuning on high-quality social reasoning datasets.

## 3. Intended Use Cases
Affectra-2-8B-EQ is suitable for:
- **Next-Gen Conversational Agents**: Chatbots that require high EQ.
- **Supportive Dialogue Systems**: Non-clinical emotional support and companionship.
- **Roleplay & Simulation**: Characters with realistic emotional depth.
- **Social Reasoning Research**: Analyzing AI capability in complex social dynamics.
| 
## 4. Benchmark Performance 
Affectra v2 achieves **breakthrough performance** on **EQ-Bench (v2)**, surpassing its predecessor and outperforming significantly larger models.

| Model | Parameters | EQ-Bench Score (v2) | 
| :--- | :--- | :--- |
| **Affectra-2-8B-EQ** | **8B** | **74.6**  |
| Phi-3-small-8k-instruct | 7B | 73.49 |
| Mixtral_34Bx2_MoE_60B | 60B | 72.69 |
| Nous-Hermes-2-Yi-34B | 34B | 72.68 |
| Affectra-8B (v1) | 8B | 69.9 |
| Qwen2.5-7B-Instruct | 7B | 69.18 |
| Llama-3-8B-Instruct | 8B | 68.88 |



## 5. Limitations & Ethical Considerations
- Affectra v2 is **not a licensed medical, psychological, or legal professional**.
- Outputs should not be used as professional advice.
- Emotional fluency does not guarantee factual correctness.
- Human oversight is recommended for sensitive or high-stakes applications.

## 6. Usage
```python
!pip install -qU transformers accelerate
from transformers import AutoTokenizer
import transformers
import torch
model = "salihfurkaan/Affectra-2-8B-EQ"
messages = [{"role": "user", "content": "I'm feeling really overwhelmed with work lately."}]
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


