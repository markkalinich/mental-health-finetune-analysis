---
base_model: google/gemma-4-E4B-it
license: gemma
pipeline_tag: text-generation
library_name: transformers
tags:
  - gemma
  - mental-health
  - text-classification
  - sft
  - merged-lora
language:
  - en
---

# mental_health_best_model_merged

Full-precision (bf16) weights for Gemma-4-E4B-it fine-tuned with LoRA on **41 mental-health
and emotion text-classification tasks** (D01–D22 plus GoEmotions one-vs-rest splits), then
**merged** so the model is a drop-in replacement for the base — no `peft` required.

> Disclaimer — research use only. The outputs are predicted class IDs from a frozen 1-of-K
> head built into a chat-style prompt; they are **not clinical advice** and must not be used
> to diagnose or triage real users.

## How this is different from the LoRA-only repo

| Repo | What it is | How to load |
|---|---|---|
| [`xxue752/mental_health_best_model`](https://huggingface.co/xxue752/mental_health_best_model) | LoRA adapter only (~140 MB) | base + `PeftModel.from_pretrained` |
| **`xxue752/mental_health_best_model_merged`** (this repo) | Full merged weights (~16 GB bf16) | one `AutoModelForCausalLM.from_pretrained` |

## Held-out evaluation (mean of 41 tasks, 0-shot, chat_legacy prompt)

| Metric | Value |
|---|---|
| ACC | 0.826 |
| BACC | 0.760 |
| F1 | 0.763 |
| Macro-AUPRC | 0.684 |

vs zero-shot Gemma-4-E4B-it baseline: BACC +0.093, ACC +0.124. 36/41 tasks improved.

## Quick start

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

REPO = "xxue752/mental_health_best_model_merged"

tokenizer = AutoTokenizer.from_pretrained(REPO)
model = AutoModelForCausalLM.from_pretrained(
    REPO,
    torch_dtype=torch.bfloat16,
    device_map="auto",
).eval()

system = (
    "You are a careful classifier. Read the input and reply with EXACTLY one "
    "single integer class id from the options listed in the question. No words, "
    "no punctuation, no explanation."
)
question = (
    "Task: single-choice — D01 stress binary.\n"
    "Choose 0 (no stress) or 1 (stress).\n"
    "Input text:\n"
    "I haven't slept in three days because of work and I just can't keep going.\n"
    "Answer:"
)
msgs = [{"role": "system", "content": system}, {"role": "user", "content": question}]
prompt = tokenizer.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
ids = tokenizer(prompt, return_tensors="pt").to(model.device)
out = model.generate(**ids, max_new_tokens=2, do_sample=False)
print(tokenizer.decode(out[0, ids.input_ids.shape[1]:], skip_special_tokens=True))
```

## Training summary

- **Method**: LoRA r=16, α=32, dropout=0.05, bf16, applied to language tower q/k/v/o_proj
  and gate/up/down_proj (258 modules), then `merge_and_unload`.
- **Loss**: TRL SFT, completion-only loss (only the answer token is supervised).
- **Tasks**: 41 (`task_core.TASKS[1..41]`), prompt stack `chat_legacy`.
- **Split**: 72 % stratified per task → train; 28 % → held-out eval.
- **Per-task cap**: 1000 train rows.
- **Balance**: binary tasks with task_id ≥ 7 AND >1000 train rows downsampled to 1:1.
- **Per-task weighting**: Menta-style for tasks 1–6 (1.0/1.0/1.2/1.2/1.5/1.5).
- **Optim**: AdamW, lr 2e-4, cosine, warmup 0.03, max_grad_norm 1.0, eff. batch 16, 1 epoch.

## Citation

```bibtex
@software{vonwerra2020trl,
  title  = {TRL: Transformer Reinforcement Learning},
  author = {von Werra, Leandro and others},
  url    = {https://github.com/huggingface/trl},
  year   = {2020}
}
```
