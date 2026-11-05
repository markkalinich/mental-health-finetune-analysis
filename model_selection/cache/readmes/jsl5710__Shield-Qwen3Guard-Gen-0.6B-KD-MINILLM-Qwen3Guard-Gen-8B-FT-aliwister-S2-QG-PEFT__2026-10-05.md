---
license: apache-2.0
base_model: Qwen/Qwen3Guard-Gen-0.6B
tags:
- safety
- classifier
- dia-guard
- knowledge-distillation
- minillm
- aliwister-teacher
language:
- en
---

# Shield-Qwen3Guard-Gen-0.6B-KD-MINILLM-Qwen3Guard-Gen-8B-FT-aliwister-S2-QG-PEFT

Student in the **DIA-GUARD Shield** family produced by MINILLM knowledge
distillation from the **aliwister full-FT 8B teacher** into a Shield-PEFT
initialised Qwen3Guard-Gen-0.6B student.

## Pipeline

```
Teacher:  jsl5710/Shield-Qwen3Guard-Gen-8B-FT-PEFT-CE   (full-FT by @aliwister, 0.9515 acc)
             │  3 epochs KD, method = MINILLM, 50K DIA-GUARD samples
             ▼
Student:  jsl5710/Shield-Qwen3Guard-Gen-0.6B-PEFT-CE   (Shield PEFT-CE, pre-warmed)
```

## Test-set results (DIA-GUARD Holdout, 181,874 samples)

| Metric | Value |
|---|---|
| **Accuracy** | **0.6851** |
| Precision | 0.7795 |
| Recall | 0.6578 |
| F1 | 0.6337 |
| ASR (unsafe caught) | 97.57% |

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
tokenizer = AutoTokenizer.from_pretrained("jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-MINILLM-Qwen3Guard-Gen-8B-FT-aliwister-S2-QG-PEFT")
model = AutoModelForCausalLM.from_pretrained(
    "jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-MINILLM-Qwen3Guard-Gen-8B-FT-aliwister-S2-QG-PEFT",
    torch_dtype="bfloat16",
    device_map="auto",
)

prompt = "Classify the following text as safe or unsafe.\n\nText: How do I bake a cake?\n\nAnswer:"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=8)
print(tokenizer.decode(out[0][inputs.input_ids.shape[1]:], skip_special_tokens=True))
```
