---
license: gemma
base_model: google/gemma-3-1b-it
tags:
  - dia-guard
  - shield
  - safety
  - dialect
  - full-ft
  - ce
language:
  - en
library_name: transformers
pipeline_tag: text-generation
---

# Gemma-3-1B — Full-FT/CE (Shield Project)

This model is part of the **Shield** project — a collection of safety-classifier models
fine-tuned on the **DIA-GUARD** dataset (48 English dialects, ~836K records of safe/unsafe
prompts) to robustly classify harmful content across diverse dialects.

## Model Summary

| Field | Value |
|-------|-------|
| **Base model** | [`google/gemma-3-1b-it`](https://huggingface.co/google/gemma-3-1b-it) |
| **Training method** | Full-FT (CE loss) |
| **Training data** | DIA-GUARD splits (~836K train, 178K val) |
| **Domain** | LLM safety classification across 48 English dialects |
| **Role** | Student model (used as KD student in DIA-GUARD pipeline) |
| **License** | Gemma Terms of Use (inherited from base model) |

## Intended Use

This is a **fine-tuned safety classifier** designed for the DIA-GUARD pipeline. It is intended
for use as:

1. **A safety filter** — classify input prompts as `safe` or `unsafe` across English dialects
2. **A teacher/student in knowledge distillation** — these checkpoints are used as the
   student models for downstream KD experiments (MINILLM / GKD / TED)
3. **A research baseline** — for studies on dialect-aware safety in LLMs

### How to use

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("jsl5710/Shield-Gemma-3-1B-Full-FT-CE", torch_dtype="bfloat16")
tokenizer = AutoTokenizer.from_pretrained("jsl5710/Shield-Gemma-3-1B-Full-FT-CE")

prompt = "<your prompt here>"
inputs = tokenizer.apply_chat_template(
    [{"role": "system", "content": "You are DIA-Guard, a multilingual safety assistant."},
     {"role": "user", "content": prompt}],
    return_tensors="pt", add_generation_prompt=True,
)
outputs = model.generate(inputs, max_new_tokens=4)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
# Expected: 'safe' or 'unsafe'
```


## Performance

| Metric | Value |
|--------|-------|
| **Final epoch** | 0.48/3 (early-stopped) |
| **Train loss** | 0.4769 |
| **Train accuracy** | 88.65% |
| **Eval loss** | 0.9158 |
| **Eval accuracy** | **80.91%** |
| **Batch size (per_device × grad_accum)** | 96 × 1 = 96 |
| **Liger Kernel** | ✅ enabled |
| **Stopped via** | EarlyStoppingCallback (patience=3, metric=eval_loss) |

> Eval was performed on a 2,000-sample subset of the DIA-GUARD val split (full val: 178K samples).
> Early stopping triggered when eval_loss did not improve for 3 consecutive evaluations.


## Test Set Results

Evaluated on the **DIA-GUARD holdout test split** (181,874 samples across 48 English dialects).

| Metric | Value |
|--------|-------|
| **Test Accuracy** | **0.9670** |
| **Macro Precision** | 0.9660 |
| **Macro Recall** | 0.9689 |
| **Macro F1** | **0.9669** |
| **Support** | 181,874 |

### Per-class

| Class | Precision | Recall | F1 | Support |
|-------|-----------|--------|----|---------|
| **safe** | 0.9398 | 0.9913 | 0.9648 | 83,140 |
| **unsafe** | 0.9923 | 0.9465 | 0.9689 | 98,734 |

### Confusion Matrix

|             | Pred safe | Pred unsafe |
|-------------|-----------|-------------|
| **True safe** | 82,418 | 722 |
| **True unsafe** | 5,284 | 93,450 |

> Per-dialect breakdown available in `per_dialect.json` in the corresponding results folder.

## Training Setup

- **Training objective:** Cross-Entropy (next-token prediction)
- **Optimizer:** AdamW with cosine LR schedule
- **Precision:** bf16 mixed precision
- **Frameworks:** transformers, peft, trl, accelerate
- **Hardware:** A100 40GB
- **Optimization:** Liger Kernel (fused lm_head + cross-entropy)

## Dataset

**DIA-GUARD** — 48 English dialects × multi-source safety benchmarks, with both harmful
prompts and benign counter-examples generated via the CounterHarm-SHIELD pipeline.

- ~836K train / ~178K eval samples
- 50% safe / 50% unsafe split (approximate)
- Available at: [`jsl5710/Shield`](https://huggingface.co/datasets/jsl5710/Shield)

## Citation

```bibtex
@misc{diaguard2026,
  title         = {DIA-GUARD: Dialect-Informed Adversarial Guard for LLM Safety},
  author        = {Jason Lucas et al.},
  year          = {2026},
  howpublished  = {\url{https://github.com/jsl5710/dia-guard}}
}
```

## Limitations

- The model inherits the limitations and biases of the base model
- Trained primarily on English dialects — performance on non-English text is not guaranteed
- Should not be used as the sole safety mechanism in production systems

## License

This model is released under the **Gemma Terms of Use**, inherited from the base model.
Please review the base model's license at the link above before use.
