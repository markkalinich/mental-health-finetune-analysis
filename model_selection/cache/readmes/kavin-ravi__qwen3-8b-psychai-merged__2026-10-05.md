---
license: apache-2.0
base_model: Qwen/Qwen3-8B
tags:
  - text-generation
  - conversational
  - mental-health
  - psychai
  - merged
pipeline_tag: text-generation
---

# PsychAI — Qwen3-8B (LoRA merged)

This is `kavin-ravi/qwen3-8b-psychai-lora` merged into `Qwen/Qwen3-8B`, so it can be served by any
standard inference provider without needing to load PEFT adapters at runtime.

It's intended for serverless inference (HF Inference Providers / dedicated
Inference Endpoints) by the PsychAI Streamlit app.

## Intended use

Empathetic, age-appropriate conversational support for teens dealing with
anxiety, mood dips, and everyday stressors. **Not** a substitute for licensed
mental-health care. If you or someone you know is in crisis, contact your local
emergency services or call/text **988** (US Suicide & Crisis Lifeline).

## Quick start

```python
from huggingface_hub import InferenceClient

client = InferenceClient(model="kavin-ravi/qwen3-8b-psychai-merged", token="hf_***")
out = client.chat_completion(
    messages=[
        {"role": "system", "content": "You are PsychAI..."},
        {"role": "user", "content": "I've been feeling anxious lately."},
    ],
    max_tokens=512, temperature=0.7, top_p=0.9,
)
print(out.choices[0].message.content)
```
