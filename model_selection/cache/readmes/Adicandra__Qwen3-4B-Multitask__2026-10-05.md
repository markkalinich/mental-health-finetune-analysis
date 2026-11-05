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
- lora
- lora-merged
- sft
- multitask
- sentiment-analysis
- summarization
- chatml
datasets:
- custom
---

# Qwen3-4B SFT-CPT — Multitask Bahasa Indonesia (LoRA merged)

Model ini merupakan hasil fine-tuning (LoRA, sudah di-**merge** ke base weights) dari
[`aitf-kpm-ugm/Qwen3-4B-CPT-Base`](https://huggingface.co/aitf-kpm-ugm/Qwen3-4B-CPT-Base) untuk berbagai tugas NLP **Bahasa Indonesia**
menggunakan format ChatML.

---

## Deskripsi Singkat

| Atribut | Nilai |
|---|---|
| Base model | `aitf-kpm-ugm/Qwen3-4B-CPT-Base` |
| Metode fine-tune | LoRA (r=64, alpha=128) |
| Status adapter | **Merged** ke base weights |
| Bahasa output | Bahasa Indonesia 🇮🇩 |
| Format chat | ChatML (Qwen3-instruct) |
| EOS token | `<\|im_end\|>` |
| Precision | bfloat16 |
| Max seq length | 2048 |
| Training epochs | 3 |
| Train samples | ~93,579 |
| Best val loss | 0.343 |

---

## Cara Pakai (Inference)

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

REPO = "Adicandra/Qwen3-4B-Multitask"

tokenizer = AutoTokenizer.from_pretrained(REPO)
model = AutoModelForCausalLM.from_pretrained(
    REPO,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)
model.eval()

messages = [
    {"role": "system", "content": "Kamu adalah asisten AI yang membantu."},
    {"role": "user",   "content": "Ringkaskan teks berikut: ..."},
]

text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)

inputs = tokenizer(text, return_tensors="pt").to(model.device)
input_len = inputs.input_ids.shape[1]

im_end_id = tokenizer.convert_tokens_to_ids("<|im_end|>")

with torch.no_grad():
    out = model.generate(
        **inputs,
        max_new_tokens=512,
        do_sample=False,
        use_cache=True,
        eos_token_id=im_end_id,
        pad_token_id=tokenizer.pad_token_id,
    )

response = tokenizer.decode(out[0, input_len:], skip_special_tokens=True)
print(response)
```

---

## Training Details

- **Framework**: Unsloth + TRL SFTTrainer
- **LoRA config**: r=64, alpha=128, target modules = q/k/v/o/gate/up/down_proj
- **Optimizer**: AdamW 8-bit
- **LR scheduler**: Cosine with warmup ratio 0.03
- **Batch size**: 6 × 8 gradient accumulation = effective 48
- **train_on_responses_only**: Ya (hanya loss pada respons assistant)

---

## Lisensi

Mengikuti lisensi base model: [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0).
