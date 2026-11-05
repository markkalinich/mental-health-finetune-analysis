---
base_model: aitf-kpm-ugm/Qwen3-4B-CPT-Base
library_name: transformers
language:
- id
license: apache-2.0
pipeline_tag: text-generation
tags:
- qwen3
- bahasa-indonesia
- sft
- multitask
- sentiment-analysis
- kategorisasi
- alpaca
- lora-merged
datasets:
- custom
---

# Qwen3-4B SFT — Multitask Bahasa Indonesia

Model hasil fine-tuning (LoRA, sudah di-**merge** ke base weights) dari
[`aitf-kpm-ugm/Qwen3-4B-CPT-Base`](https://huggingface.co/aitf-kpm-ugm/Qwen3-4B-CPT-Base) untuk berbagai tugas NLP **Bahasa Indonesia**.

---

## Detail Model

| Atribut | Nilai |
|---|---|
| Base model | `aitf-kpm-ugm/Qwen3-4B-CPT-Base` |
| Metode fine-tune | LoRA (r=64, alpha=128) |
| Status adapter | **Merged** ke base weights |
| Bahasa output | Bahasa Indonesia |
| Format chat | **Alpaca** |
| Precision | bfloat16 |
| Max seq length | 2048 |
| Training epochs | 3 |
| Best checkpoint | step 2400 |
| Best val loss | 0.3566 |

---

## Task yang Didukung

1. **Sentimen Analysis** — klasifikasi positif / netral / negatif
2. **Justifier** — klasifikasi is_relevant: true / false
3. **Kategorisasi Issue** — klasifikasi sub_category_label

---

## Cara Pakai

````python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

REPO = "Atikarahmanda/Qwen3-4B-SFT-Multitask"

tokenizer = AutoTokenizer.from_pretrained(REPO)
model = AutoModelForCausalLM.from_pretrained(
    REPO,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)
model.eval()

messages = [
    {"role": "system", "content": "Sistem prompt sesuai task."},
    {"role": "user",   "content": "Input artikel di sini."},
]

text = tokenizer.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True
)
inputs = tokenizer(text, return_tensors="pt").to(model.device)
input_len = inputs.input_ids.shape[1]

with torch.no_grad():
    out = model.generate(
        **inputs,
        max_new_tokens=128,
        do_sample=False,
        eos_token_id=tokenizer.eos_token_id,
        pad_token_id=tokenizer.pad_token_id,
    )

print(tokenizer.decode(out[0, input_len:], skip_special_tokens=True))
```

---

## Training Details

- **Framework**: Unsloth + TRL SFTTrainer
- **LoRA config**: r=64, alpha=128
- **Optimizer**: AdamW 8-bit
- **LR scheduler**: Cosine, warmup ratio 0.03
- **Effective batch size**: 6 x 8 = 48
- **train_on_responses_only**: Ya

---

## Lisensi

Mengikuti lisensi base model: [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0).
