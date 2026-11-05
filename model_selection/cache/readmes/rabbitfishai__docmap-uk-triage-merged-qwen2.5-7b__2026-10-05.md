---
license: apache-2.0
base_model: Qwen/Qwen2.5-7B-Instruct
pipeline_tag: text-generation
library_name: peft
language:
- en
tags:
- qwen
- 7b
- peft
- lora
- qlora
- 4-bit
- healthcare
- triage
- nhs
- uk
- safety
metrics:
- perplexity
---

# DocMap UK Triage (Qwen2.5-7B-Instruct, QLoRA)

LoRA adapters (and merged model variant) for a UK NHS-style healthcare triage/navigation assistant. The model provides safe routing (999/111/GP/UTC/Pharmacy), concise guidance, citations (when provided), and a brief non‑diagnostic disclaimer.

## Intended use
- Preliminary UK triage guidance and healthcare navigation.
- Not a diagnostic tool. Not a medical device. Use under human oversight.

## Quick start (adapters)
```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

BASE = "Qwen/Qwen2.5-7B-Instruct"
ADAPTER = "<your-username>/docmap-uk-triage-lorav1-qwen7b"

tok = AutoTokenizer.from_pretrained(BASE, use_fast=True)
if tok.pad_token is None: tok.pad_token = tok.eos_token

model = AutoModelForCausalLM.from_pretrained(
    BASE, device_map="auto", load_in_4bit=True, trust_remote_code=True
)
model = PeftModel.from_pretrained(model, ADAPTER)

SYSTEM = "You are DocMap's UK NHS triage assistant. Provide safe routing and a brief non‑diagnostic disclaimer."
msgs = [{"role":"system","content":SYSTEM},{"role":"user","content":"Headache 2 days, no vomiting."}]
prompt = tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
inputs = tok(prompt, return_tensors="pt").to(model.device)
with torch.inference_mode():
    out = model.generate(**inputs, max_new_tokens=320, temperature=0.2, top_p=0.9, repetition_penalty=1.03)
print(tok.decode(out[0], skip_special_tokens=True))
```

## Quick start (merged model)
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

MODEL_ID = "<your-username>/docmap-uk-triage-merged-qwen2.5-7b"
tok = AutoTokenizer.from_pretrained(MODEL_ID, use_fast=True)
m = AutoModelForCausalLM.from_pretrained(MODEL_ID, device_map="auto", torch_dtype=torch.bfloat16)

msgs = [{"role":"system","content":"You are DocMap's UK NHS triage assistant."},
        {"role":"user","content":"Chest discomfort on exertion, no sweating, no breathlessness."}]
prompt = tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
ids = tok(prompt, return_tensors="pt").to(m.device)
with torch.inference_mode():
    out = m.generate(**ids, max_new_tokens=320, temperature=0.2, top_p=0.9)
print(tok.decode(out[0], skip_special_tokens=True))
```

## Training summary
- Method: QLoRA (bitsandbytes 4‑bit nf4, double-quant, bfloat16 compute)
- LoRA: r=32, alpha=32, dropout=0.05; targets: q_proj,k_proj,v_proj,o_proj,gate_proj,up_proj,down_proj
- Seq len: 4096; batch: 1; grad_accum: 16; epochs: 3; lr: 2e‑4; gradient checkpointing
- Data: Supabase train bucket (`lorav1/**` JSONL: instruction, input?, output, citations)

## Evaluation (hold‑out 10%)
- Eval loss ≈ 0.243 → perplexity ≈ 1.27 (in‑distribution)

## Safety
- This is general information, not a medical diagnosis.
- Emergencies: call 999. Urgent concerns: contact NHS 111.
- Verify outputs clinically; model may miss edge cases.

## Files
- Adapters: `adapter_model.safetensors`, `adapter_config.json`
- Merged: `model.safetensors` (shards), `config.json`, tokenizer files, `chat_template.jinja` (default DocMap system)

## License
- Adapters and merged distribution: Apache‑2.0.
- Base model and any third‑party content follow their respective licenses.

## Acknowledgements
- Base: Qwen/Qwen2.5‑7B‑Instruct
- Tooling: PEFT, Transformers, TRL, bitsandbytes
- UK healthcare sources (NHS and reputable UK providers)