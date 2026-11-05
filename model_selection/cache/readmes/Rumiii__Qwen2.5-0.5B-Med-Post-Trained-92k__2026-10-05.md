---
library_name: transformers
language:
- en
license: apache-2.0
base_model: Qwen/Qwen2.5-0.5B
tags:
- transformers
- medical
- biomedical
- continued-pretraining
- supervised-fine-tuning
- qwen2.5
- pubmed
- conversational
- causal-lm
arxiv: 2506.09513
---

![Screenshot 2026-09-06 at 6.42.45 PM](https://cdn-uploads.huggingface.co/production/uploads/66e00ba55e4fd4bfead4a97c/ljqpcCYcrL_sQUok8ECgV.png)

# Qwen2.5-0.5B-Med-Post-Trained-92k

A domain-adapted and instruction-tuned variant of [Qwen/Qwen2.5-0.5B](https://huggingface.co/Qwen/Qwen2.5-0.5B), produced through a two-stage training pipeline: full-parameter continued pre-training (CPT) on biomedical text followed by supervised fine-tuning (SFT) on a general instruction dataset.



## Training Pipeline

### Stage 1 — Continued Pre-Training (CPT)

| Property | Value |
|---|---|
| Base model | Qwen/Qwen2.5-0.5B |
| Training type | Full-parameter CPT (no LoRA) |
| Dataset | VietAI/vi_pubmed (92k English abstracts) |
| Tokens | ~23.6 million |
| Objective | Causal Language Modeling (CLM) |
| Optimizer | AdamW 8-bit |
| Learning rate | 2e-5 cosine |
| Hardware | Kaggle Tesla T4 |
| Training time | ~3h 45m |
| Loss | 2.581 → 2.478 |

### Stage 2 — Supervised Fine-Tuning (SFT)

| Property | Value |
|---|---|
| Base model | Rumiii/Qwen2.5-0.5B-Med-Pre-Trained-92k |
| Training type | Full-parameter SFT (no LoRA) |
| Dataset | causal-lm/ultrachat (20k samples) |
| Format | Qwen2.5 ChatML chat template |
| Optimizer | AdamW 8-bit |
| Learning rate | 2e-5 cosine |
| Hardware | Kaggle Tesla T4 |
| Training time | ~1h 13m |
| Loss | 2.093 → 1.289 |

## Usage

This model uses the Qwen2.5 ChatML chat template. A system prompt is required for best results. The recommended inference setup is shown below.

### Recommended system prompt

```python
SYSTEM_PROMPT = (
    "You are a knowledgeable medical AI assistant named MedAssist. "
    "Answer all questions clearly, directly, and informatively. "
    "For medical questions provide accurate information. "
    "Never generate multiple choice questions unless explicitly asked."
)
```

### Basic inference

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "Rumiii/Qwen2.5-0.5B-Med-Post-Trained-92k"

tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto",
    trust_remote_code=True,
)
model.eval()

SYSTEM_PROMPT = (
    "You are a knowledgeable medical AI assistant named MedAssist. "
    "Answer all questions clearly, directly, and informatively. "
    "For medical questions provide accurate information. "
    "Never generate multiple choice questions unless explicitly asked."
)

messages = [
    {"role": "system",  "content": SYSTEM_PROMPT},
    {"role": "user",    "content": "What are the symptoms of pneumonia?"},
]

inputs = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_tensors="pt",
    return_dict=True,
).to(model.device)

im_end_id = tokenizer.convert_tokens_to_ids("<|im_end|>")
stop_ids = [tokenizer.eos_token_id]
if im_end_id and im_end_id != tokenizer.eos_token_id:
    stop_ids.append(im_end_id)

with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=512,
        temperature=0.2,
        top_p=0.9,
        repetition_penalty=1.15,
        do_sample=True,
        eos_token_id=stop_ids,
        pad_token_id=tokenizer.eos_token_id,
    )

new_tokens = outputs[0][inputs["input_ids"].shape[-1]:]
response = tokenizer.decode(new_tokens, skip_special_tokens=True).strip()
print(response)
```

### Recommended generation parameters

| Parameter | Value | Reason |
|---|---|---|
| temperature | 0.2 | Low temperature for factual medical responses |
| top_p | 0.9 | Stable token sampling |
| repetition_penalty | 1.15 | Prevents response loops |
| max_new_tokens | 512 | Sufficient for complete answers |
| eos_token_id | include `<\|im_end\|>` | Required to stop at turn boundary |

### Important note on greetings

As a 0.5B model fine-tuned on instruction data, this model may produce inconsistent responses to simple greetings such as "Hi" or "Hello." It performs best when given direct questions or requests. For production deployments, greeting inputs should be handled with a fixed response rather than passed to the model.

## Intended Use

- Medical question answering and clinical education
- Research into small biomedical language models
- Lightweight medical AI prototyping
- Demonstration of CPT + SFT pipeline on consumer hardware

## Not Intended For

- Clinical decision making in real patient care
- Diagnostic or treatment decisions
- Replacement of licensed medical professionals

## Limitations

- 494M parameters — reasoning depth is limited compared to larger models
- Trained on single-turn instruction pairs — multi-turn coherence is basic
- Clinical accuracy not guaranteed — all outputs require expert verification
- Simple greetings may produce inconsistent responses at this model scale
- English only