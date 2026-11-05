---
license: apache-2.0
base_model: Qwen/Qwen3Guard-Gen-8B
tags:
- safety
- classifier
- dia-guard
- teacher
- full-finetune
language:
- en
---

# Shield-Qwen3Guard-Gen-8B-FT-PEFT-CE

**Full fine-tune** of `Qwen/Qwen3Guard-Gen-8B` on the DIA-GUARD train split (~836K
samples, 50 English dialects). Serves as the 8B teacher in the `Shield-*-KD-*-Qwen3Guard-Gen-8B-FT-*`
knowledge-distillation family in this org.

## Provenance

This repo re-hosts the full-parameter fine-tune produced by **[@aliwister](https://huggingface.co/aliwister)**
in [`aliwister/qwen3guard_gen_8b-diaguard`](https://huggingface.co/aliwister/qwen3guard_gen_8b-diaguard).
It replaces an earlier LoRA-CE attempt by us which collapsed to a
trivial predictor; aliwister's full FT substantially outperforms that
attempt (see table below) so we standardise on this checkpoint as the
canonical Shield 8B teacher.

> **Note on the repo name**: the `-FT-PEFT-CE` suffix is inherited from
> our earlier LoRA-CE checkpoint name so that the existing KD child
> repos (`jsl5710/Shield-*-KD-*-Qwen3Guard-Gen-8B-FT-*`) continue to
> resolve. The underlying training is a **full-parameter** fine-tune,
> not PEFT.

## Test-set results (DIA-GUARD holdout, 181,874 samples)

| Metric | Value |
|---|---|
| **Accuracy** | **0.9515** |
| Precision | 0.9573 |
| Recall | 0.9476 |
| F1 | 0.9507 |
| ASR (unsafe caught) | 99.33% |

| Metric | Value |
|---|---|
| **SAE Accuracy (36,050 samples)** | **0.9634** |
| SAE F1 | 0.9629 |

### Comparison to our earlier LoRA-CE attempt

| Variant | Holdout Acc | Holdout F1 |
|---|---:|---:|
| LoRA-CE (our earlier attempt, deprecated) | 0.5432 ⚠️ | 0.3545 |
| **Full-FT (aliwister, this repo)** | **0.9515** | **0.9507** |

## How to use

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("jsl5710/Shield-Qwen3Guard-Gen-8B-FT-PEFT-CE")
model = AutoModelForCausalLM.from_pretrained(
    "jsl5710/Shield-Qwen3Guard-Gen-8B-FT-PEFT-CE",
    torch_dtype="bfloat16",
    device_map="auto",
)

prompt = (
    "Classify the following text as safe or unsafe.\n\n"
    "Text: How do I bake a cake?\n\n"
    "Answer:"
)
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=8)
print(tokenizer.decode(out[0][inputs.input_ids.shape[1]:], skip_special_tokens=True))
```

## Model architecture

| | |
|---|---|
| Base | `Qwen/Qwen3Guard-Gen-8B` |
| Params | 8.37 B |
| Hidden | 4096 |
| Layers | 36 |
| Vocab | 151,936 |

## Citation

If you use this model, please cite the original aliwister upload in
addition to the DIA-GUARD work:

```bibtex
@misc{aliwister_qwen3guard_8b_diaguard_2026,
  author = {aliwister},
  title  = {qwen3guard\_gen\_8b-diaguard},
  year   = {2026},
  url    = {https://huggingface.co/aliwister/qwen3guard_gen_8b-diaguard},
}
```
