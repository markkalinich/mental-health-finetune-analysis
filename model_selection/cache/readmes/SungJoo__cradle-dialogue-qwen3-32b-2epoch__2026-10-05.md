---
language:
- en
license: apache-2.0
base_model: Qwen/Qwen3-32B
tags:
- mental-health
- crisis-detection
- dialogue
- clinical-nlp
- fine-tuned
- qwen3
datasets:
- SungJoo/Cradle-Dialogue
task_categories:
- text-classification
task_ids:
- multi-label-classification
---

# cradle-dialogue-qwen3-32b-2epoch

A Qwen3-32B model fine-tuned for **turn-level mental health crisis detection** in multi-turn conversations. This is the best-performing checkpoint (epoch 2) from 3-epoch training, as reported in the CRADLE-Dialogue paper.

> ⚠️ **Content Warning:** This model is designed to detect sensitive topics including suicide ideation, self-harm, rape, domestic violence, and child abuse.

## Model Description

Full fine-tune of [Qwen/Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B), trained on the CRADLE-Dialogue synthetic training corpus — 3,058 dialogues (48,557 turns) generated from Reddit posts via GPT-5 and annotated with structured Alert–Confirm labels.

Given a multi-turn dialogue and the model's own previous predictions, the model assigns a crisis label to the **current user turn only**.

## Performance

Evaluated on the CRADLE-Dialogue test set (600 clinician-annotated dialogues):

| Setting | Metric | Score |
|---|---|---|
| Turn-Level | Micro F1 | **51.31** |
| Turn-Level | Macro F1 | 54.96 |
| Turn-Level | Micro Recall | 54.99 |
| Dialogue-Level | Micro F1 | **68.88** |
| Dialogue-Level | Macro F1 | 69.29 |
| Dialogue-Level (Confirm Only) | Micro F1 | **76.03** |

Outperforms all open-source baselines and achieves competitive results against Claude-4.5-Sonnet and GPT-5.1.

## Output Format

The model outputs **exactly one line** per inference call:

```
none
alert_ongoing
alert_past
confirm_SI_passive_ongoing
confirm_SH_past
confirm_DV_ongoing; confirm_RA_past   # multi-label, separated by "; "
```

## Inference

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "SungJoo/cradle-dialogue-qwen3-32b-2epoch"
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
)

SYSTEM_MSG = (
    "You are a clinical dialogue safety annotator. "
    "Return EXACTLY ONE LINE: the label(s) or 'none'. "
    "No commentary, no reasoning, no markdown."
)

# Build your prompt using the full evaluation prompt template from the paper.
# At each turn, provide: full dialogue history + model's previous predictions + current user turn.
messages = [
    {"role": "system", "content": SYSTEM_MSG},
    {"role": "user", "content": YOUR_PROMPT},
]

text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=False,
)
inputs = tokenizer(text, return_tensors="pt").to(model.device)

with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=64,
        do_sample=False,
    )

response = tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True)
print(response.strip())
```

## Training Details

| Config | Value |
|---|---|
| Base model | Qwen/Qwen3-32B |
| Fine-tuning method | Full fine-tune (no LoRA) |
| Total epochs | 3 (this checkpoint: epoch 2, best val loss) |
| Learning rate | 5e-6 |
| Batch size | 1 (per device) |
| Gradient accumulation | 16 |
| Max sequence length | 4096 |
| Precision | bfloat16 |
| Hardware | 2× NVIDIA H200 |
| LR scheduler | Cosine with warmup (ratio=0.05) |

## Intended Use

This model is intended for **research purposes** in clinical NLP and crisis detection. It is not a substitute for professional mental health assessment or crisis intervention.


## Related Resources

- 📦 **Dataset**: [SungJoo/Cradle-Dialogue](https://huggingface.co/datasets/SungJoo/Cradle-Dialogue)
- 🤖 **3-epoch checkpoint**: [SungJoo/cradle-dialogue-qwen3-32b-3epoch](https://huggingface.co/SungJoo/cradle-dialogue-qwen3-32b-3epoch)
- 📄 **CRADLE-Bench** (post-level benchmark): [SungJoo/CRADLE-Bench](https://huggingface.co/datasets/SungJoo/CRADLE-Bench)
