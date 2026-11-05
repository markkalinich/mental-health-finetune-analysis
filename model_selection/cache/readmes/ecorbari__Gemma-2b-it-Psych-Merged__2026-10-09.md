---
library_name: transformers
tags:
- gemma
- psychology
- mental-health
- merged
- instruction-tuning
- neuroquestai
license: mit
datasets:
- jkhedri/psychology-dataset
language:
- en
base_model: google/gemma-2b-it
pipeline_tag: text-generation
---

# Model Card for Gemma-2b-it-Psych-Merged

## Model Summary

**Gemma-2b-it-Psych-Merged** is the full-weight, standalone version of the `google/gemma-2b-it` model, domain-adapted for psychological contexts. This model integrates the LoRA adapter weights from [ecorbari/Gemma-2b-it-Psych](https://huggingface.co/ecorbari/Gemma-2b-it-Psych) directly into the base model using the `merge_and_unload()` process.

The model is optimized to generate **empathetic, supportive, and professionally aligned psychological responses**. Unlike the adapter-only version, this repository contains the complete merged weights, meaning it does not require the `peft` library for standard inference.

---

## Model Details

### Model Description

- **Author:** Ederson Corbari (e@NeuroQuest.ai)
- **Date:** February 01, 2026
- **Model type:** Causal Language Model (LLM)
- **Language(s):** English
- **License:** MIT (consistent with Gemma base model terms)
- **Finetuned from model:** `google/gemma-2b-it`
- **Merge method:** LoRA Weights Integration (`merge_and_unload`)

### Model Sources

- **Hugging Face Merged:** [ecorbari/Gemma-2b-it-Psych-Merged](https://huggingface.co/ecorbari/Gemma-2b-it-Psych-Merged)
- **Hugging Face LoRA Adapter:** [ecorbari/Gemma-2b-it-Psych](https://huggingface.co/ecorbari/Gemma-2b-it-Psych)
- **Base Model:** [google/gemma-2b-it](https://huggingface.co/google/gemma-2b-it)

---

## Uses

### Direct Use

This merged model is ready for production and simplified inference. It can be loaded directly using standard `transformers` pipelines. It is intended for:
- Research on empathetic AI behavior.
- Educational demonstrations of domain-adapted LLMs.
- Proof-of-concept psychological support tools.

### Out-of-Scope Use

- **Clinical Use:** This model is NOT a substitute for licensed mental health professionals. It must not be used for diagnosis or treatment.
- **High-Stakes Decision Making:** It should not be used in autonomous counseling systems without human oversight.

---

## How to Get Started with the Model

Since the weights are already merged, you can run inference using a simple pipeline:

```python
import torch
from transformers import pipeline

model_id = "ecorbari/Gemma-2b-it-Psych-Merged"

pipe = pipeline(
    "text-generation",
    model=model_id,
    dtype=torch.float16,
    device_map="auto",
)

prompt = "I feel anxious and overwhelmed lately. What should I do?"
result = pipe(prompt, max_new_tokens=200)

print(result[0]["generated_text"])
```

---

## Bias, Risks, and Limitations

Safety Disclaimer: The model may generate inaccurate information. Empathy in text generation does not imply clinical safety or medical correctness.

Data Bias: Responses may reflect biases inherent in the `jkhedri/psychology-dataset`.

Human Oversight: Users should apply human judgment, especially in sensitive conversational settings.

---

## Training and Merge Process

The workflow involved loading the `google/gemma-2b-it` model in float16 precision, attaching the LoRA adapters trained on 
preference-based psychological data, and merging the weights into a single model for downstream use. This ensures compatibility with 
environments that do not support PEFT or require lower latency for inference.
