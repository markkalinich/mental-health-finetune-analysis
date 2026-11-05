---
license: apache-2.0
base_model: Qwen/Qwen3-1.7B
tags:
- safety
- classifier
- knowledge-distillation
- minillm
- dia-guard
language:
- en
---

# Shield-Qwen3-1.7B-KD-MINILLM-Qwen3Guard-Gen-8B-OOB

**Student:** `Qwen/Qwen3-1.7B`
**Teacher:** `Qwen/Qwen3Guard-Gen-8B`
**KD method:** MINILLM
**Scenario:** OOB (out-of-box — neither teacher nor student was fine-tuned on DIA-GUARD before KD)

Part of the **DIA-GUARD** dialect-aware safety classifier suite. This checkpoint
is the result of distilling an off-the-shelf 4B/8B safety teacher into a smaller
student using 50K dialect-stratified samples from the DIA-GUARD train split, and
evaluating on the full 181,874-sample dialect holdout test.

## Test Set Results

| Metric | Value |
|--------|-------|
| **Accuracy** | **0.5657** |
| **Precision** | 0.6433 |
| **Recall** | 0.5274 |
| **F1** | 0.4263 |
| Test samples | 181,874 |

### Per-class breakdown

| Class | Precision | Recall | F1 | Support |
|-------|-----------|--------|-----|---------|
| safe | 0.7295 | 0.0795 | 0.1434 | 83,140 |
| unsafe | 0.5572 | 0.9752 | 0.7091 | 98,734 |

### Confusion matrix

|               | Predicted safe | Predicted unsafe |
|---------------|---------------:|-----------------:|
| **Actual safe**   | TN=6,613 | FP=76,527 |
| **Actual unsafe** | FN=2,452 | TP=96,282 |

## Training Setup

| | |
|---|---|
| Method | MINILLM |
| Teacher | Qwen/Qwen3Guard-Gen-8B |
| Student base | Qwen/Qwen3-1.7B |
| Train data | 50,000 dialect-stratified DIA-GUARD samples |
| Epochs | 1 |
| Framework | HuggingFace transformers + accelerate |

## How to use

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("jsl5710/Shield-Qwen3-1.7B-KD-MINILLM-Qwen3Guard-Gen-8B-OOB")
model = AutoModelForCausalLM.from_pretrained("jsl5710/Shield-Qwen3-1.7B-KD-MINILLM-Qwen3Guard-Gen-8B-OOB", torch_dtype="bfloat16")

prompt = "Classify the following text as safe or unsafe.\n\nText: Hello\n\nAnswer:"
inputs = tokenizer(prompt, return_tensors="pt")
out = model.generate(**inputs, max_new_tokens=8)
print(tokenizer.decode(out[0], skip_special_tokens=True))
```
