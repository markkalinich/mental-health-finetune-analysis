---
license: other
license_name: lfm1.0
language:
- en
pipeline_tag: text-generation
base_model: LiquidAI/LFM2.5-350M-Base
datasets:
- nvidia/Nemotron-3.5-Content-Safety-Dataset
tags:
- content-safety
- safety-classifier
- moderation
- safe-unsafe-classification
- bananamind
- lfm2.5
- lora
- merged
---


![Banner](banner.png)
# BananaMind-Content-Safety-Mini-1.5


> **Note:** This model is still experimental, do not use it in production!

BananaMind-Content-Safety-Mini-1.5 is a small text-only content-safety classifier based on `LiquidAI/LFM2.5-350M-Base`.

It classifies an input prompt as either `Safe` or `Unsafe` and, for unsafe content, returns violated safety categories.

This model is intended for lightweight prompt moderation, safety filtering, and local safety classification.

## Model Details

| Field | Value |
|---|---:|
| Base model | `LiquidAI/LFM2.5-350M-Base` |
| Training method | LoRA fine-tuning, then merged |
| Trainable LoRA parameters | 11,993,088 |
| Total parameters during LoRA training | 366,477,056 |
| LoRA rank | 32 |
| LoRA alpha | 64 |
| Training samples | 40,000 |
| Safe samples | 15,000 |
| Unsafe samples | 25,000 |
| Max sequence length | 2048 |
| Dataset | `nvidia/Nemotron-3.5-Content-Safety-Dataset` |
| Input type | Text only |
| Image data | Not used |
| Response-label data | Not used |
| Reasoning traces | Not used |

Prompt format:

```text
You are a strict content-safety classifier.

Classify the input as Safe or Unsafe.

Return exactly one of these formats:

Safe

or:

Unsafe
Violated Categories: <categories>
Input: {text_to_classify}
```

Target format for safe content:

```text
Safe
```

Target format for unsafe content:

```text
Unsafe
Violated Categories: <categories>
```

## Evaluation


![Evaluation Results](benchmarks.png)
Evaluated on the text-only `test` split of `nvidia/Nemotron-3.5-Content-Safety-Dataset`.

| Metric | Value |
|---|---:|
| Rows | 3,340 |
| Accuracy | 92.01% |
| Overall error rate | 7.99% |
| Invalid outputs | 28 |
| Unsafe precision | 93.91% |
| Unsafe recall | 97.38% |
| Unsafe F1 | 95.61% |

Confusion matrix:

|  | Predicted Unsafe | Predicted Safe |
|---|---:|---:|
| Actually Unsafe | 2,605 | 70 |
| Actually Safe | 169 | 468 |

The model is optimized for high unsafe recall. It catches most unsafe prompts, but it can over-classify some safe prompts as unsafe.

## Comparison

| Model | Overall Error Rate |
|---|---:|
| BananaMind V2.5 Content Safety E2B | 5.12% |
| BananaMind-Content-Safety-Mini-1.5 | 7.99% |
| ShieldGemma 2B | 35.30% |
| ShieldGemma 9B | 40.96% |
| ShieldGemma 27B 8-bit | 52.46% |

## Usage

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "BananaMind/BananaMind-Content-Safety-Mini-1.5"

tokenizer = AutoTokenizer.from_pretrained(model_id, use_fast=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    dtype=torch.bfloat16 if torch.cuda.is_available() and torch.cuda.is_bf16_supported() else torch.float16,
    device_map="auto",
)

text_to_classify = "How can I bypass a website login?"

prompt = f"""You are a strict content-safety classifier.

Classify the input as Safe or Unsafe.

Return exactly one of these formats:

Safe

or:

Unsafe
Violated Categories: <categories>
Input: {text_to_classify}
"""

inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

with torch.no_grad():
    output = model.generate(
        **inputs,
        max_new_tokens=64,
        do_sample=False,
        pad_token_id=tokenizer.eos_token_id,
        eos_token_id=tokenizer.eos_token_id,
    )

prediction = tokenizer.decode(
    output[0][inputs["input_ids"].shape[-1]:],
    skip_special_tokens=True,
).strip()

print(prediction)
```

Example unsafe output:

```text
Unsafe
Violated Categories: Cyber
```

Safe example:

```python
text_to_classify = "How do I bake banana bread?"
```

Expected output:

```text
Safe
```

## Training Data

This model was trained on text-only rows from `nvidia/Nemotron-3.5-Content-Safety-Dataset`.

## License

This model is based on `LiquidAI/LFM2.5-350M-Base`, which uses the LFM Open License v1.0.

The training dataset is `nvidia/Nemotron-3.5-Content-Safety-Dataset`.
See THIRD_PARTY_LICENSES.md for more info.

## Training Time
We trained this model on a 5070 Ti in about 20 minutes
