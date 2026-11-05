---
license: apache-2.0
base_model: Qwen/Qwen3.5-9B
tags:
  - medical-llm
  - clinical
  - healthcare
  - medicine
  - medical-ai
  - clinical-decision-support
  - medical
  - triage
  - emergency-medicine
  - esi
  - grpo
  - merged
language:
  - en
pipeline_tag: text-generation
library_name: transformers
---

# Qwen3.5-9B GRPO v46 — ESI Triage (Merged Full Model)

This is the **merged full-weights** version of the v46 GRPO ESI triage adapter.

The LoRA adapter weights from [`vadimbelsky/qwen3.5-esi-triage-grpo-v46`](https://huggingface.co/vadimbelsky/qwen3.5-esi-triage-grpo-v46) have been merged directly into the Qwen3.5-9B base model used during training. This guarantees the model produces v46's exact trained output format (`EXTRACTION:` → `ESI ALGORITHM:` → `ANSWER: ESI N`) without the format drift seen when mounting the LoRA on a different base.

## When to use this vs. the LoRA adapter

- **Use this (merged model)** if you want exact behavior reproduction, faster inference (no adapter overhead), or easier deployment in environments without PEFT support.
- **Use the LoRA adapter** if you want lower storage (~230MB vs ~18GB) and already have the same base model loaded.

## Performance

77.8% exact accuracy / 94.4% adjacent accuracy on the 36-case MIETIC expert-annotated evaluation set. See the [adapter repository](https://huggingface.co/vadimbelsky/qwen3.5-esi-triage-grpo-v46) for full training methodology, reward function design, and the iteration journey (v45c → v46 → v47 → v48 lessons).

## Usage

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

repo = "vadimbelsky/qwen3.5-esi-triage-grpo-v46-merged"
tokenizer = AutoTokenizer.from_pretrained(repo)
model = AutoModelForCausalLM.from_pretrained(repo, torch_dtype=torch.bfloat16, device_map="auto")

messages = [
    {"role": "system", "content":
        "You are an expert emergency triage nurse. "
        "Extract clinical fields, apply the ESI algorithm step by step, then state the ESI level. "
        "Be concise — stay under 150 words total."},
    {"role": "user", "content":
        "A 67-year-old male arrived via ambulance with sudden onset chest pain "
        "radiating to the left arm, diaphoresis, and shortness of breath. "
        "BP 88/60, HR 118, RR 24, SpO2 91%. History of MI and hypertension. Pain 9/10."},
]

prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
out = model.generate(
    **tokenizer(prompt, return_tensors="pt").to(model.device),
    max_new_tokens=1024, temperature=0.1, do_sample=True,
)
print(tokenizer.decode(out[0], skip_special_tokens=True))
```

Expected output format:
```
EXTRACTION:
- Chief complaint: ...
- Vital signs: ...

ESI ALGORITHM:
- Step A: ...
- Step B: ...

ANSWER: ESI 1
```

## Limitations

This is a research model. **Not approved for clinical use.** See the adapter repository for known weaknesses (e.g. occasional missed clinical rules around already-performed lifesaving interventions, severe pain, and open injuries).
