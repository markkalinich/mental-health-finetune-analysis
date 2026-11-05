---
license: apache-2.0
base_model: Qwen/Qwen3Guard-Gen-0.6B
tags:
- safety
- classifier
- dia-guard
- knowledge-distillation
- gkd
- aliwister-teacher
language:
- en
---

# Shield-Qwen3Guard-Gen-0.6B-KD-GKD-Qwen3Guard-Gen-8B-FT-aliwister-S2-QG-PEFT

Student in the **DIA-GUARD Shield** family produced by GKD knowledge
distillation from the **aliwister full-FT 8B teacher** into a Shield-PEFT
initialised Qwen3Guard-Gen-0.6B student.

## Pipeline

```
Teacher:  jsl5710/Shield-Qwen3Guard-Gen-8B-FT-PEFT-CE   (full-FT by @aliwister, 0.9515 acc)
             │  3 epochs KD, method = GKD, 50K DIA-GUARD samples
             ▼
Student:  jsl5710/Shield-Qwen3Guard-Gen-0.6B-PEFT-CE   (Shield PEFT-CE, pre-warmed)
```

## Test-set results (DIA-GUARD Holdout, 181,874 samples)

| Metric | Value |
|---|---|
| **Accuracy** | **0.7778** |
| Precision | 0.7849 |
| Recall | 0.7691 |
| F1 | 0.7713 |
| ASR (unsafe caught) | 87.10% |

## Provenance

The teacher is a full-parameter fine-tune of `Qwen/Qwen3Guard-Gen-8B` produced
by **[@aliwister](https://huggingface.co/aliwister)** and re-hosted at
`jsl5710/Shield-Qwen3Guard-Gen-8B-FT-PEFT-CE`. We use it as the 8B teacher in
this KD run because our own earlier LoRA-CE 8B teacher collapsed to a
degenerate predictor. The `aliwister-` tag in the repo name distinguishes these
runs from the sibling `-Qwen3Guard-Gen-8B-FT-S2-*` repos that used our earlier
teacher.

## How to use

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-GKD-Qwen3Guard-Gen-8B-FT-aliwister-S2-QG-PEFT")
model = AutoModelForCausalLM.from_pretrained(
    "jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-GKD-Qwen3Guard-Gen-8B-FT-aliwister-S2-QG-PEFT",
    torch_dtype="bfloat16",
    device_map="auto",
)

prompt = "Classify the following text as safe or unsafe.\n\nText: How do I bake a cake?\n\nAnswer:"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=8)
print(tokenizer.decode(out[0][inputs.input_ids.shape[1]:], skip_special_tokens=True))
```
