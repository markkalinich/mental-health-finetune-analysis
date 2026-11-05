---
license: apache-2.0
language:
- en
base_model:
- TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T
pipeline_tag: text-generation
tags:
- lora
- qlora
- peft
- causal-lm
- continued-pretraining
- pharma
- tinyllama
---

# pharma-tinyllama-non-instruction-merged

## Model Summary
This is the **Stage 1 merged model** from the
[llm-finetuning-playbook](https://github.com/sivasaiyadav8143/llm-finetuning-playbook) pipeline.

It is produced by continued pretraining (non-instruction causal LM fine-tuning) of
`TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T` on a small pharma-domain corpus,
using QLoRA (4-bit, nf4), then merging the LoRA adapter back into the base weights.

This merged model is the **base for Stage 2** (instruction fine-tuning / SFT).

---
## Pipeline Position

```text
TinyLlama-1.1B (base)
        ↓  Stage 1: Non-Instruction FT (this model)
pharma-tinyllama-non-instruction-merged  ← you are here
        ↓  Stage 2: Instruction FT (SFT)
pharma-tinyllama-instruction-merged
        ↓  Stage 3: Preference Tuning (DPO)
pharma-tinyllama-dpo-merged
```
---

## Training Details

| Parameter | Value |
|---|---|
| Base model | TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T |
| Method | QLoRA (4-bit nf4, double quant) |
| LoRA rank | 16 |
| LoRA alpha | 32 |
| LoRA dropout | 0.05 |
| Target modules | q/k/v/o_proj, gate/up/down_proj |
| Block size | 512 tokens |
| Epochs | 3 |
| Batch size | 1 (grad accum 8, effective = 8) |
| Learning rate | 2e-4 |
| Warmup ratio | 0.03 |
| Weight decay | 0.01 |
| Optimizer | paged_adamw_32bit |
| Environment | Google Colab T4 GPU |

---

## Training Data

Trained on [`SivaSai8143/pharma-finetuning-data`](https://huggingface.co/datasets/SivaSai8143/pharma-finetuning-data) (config: `raw`).

Raw paragraphs extracted and cleaned from a pharma-domain PDF covering:
- Metformin pharmacology & pharmacokinetics
- Lipid-lowering therapy (Atorvastatin + Ezetimibe)
- mRNA vaccine platforms
- AI in drug discovery
- Clinical trials & pharmacovigilance terminology

---

## Related Artifacts

| Artifact | Link |
|---|---|
| Stage 1 LoRA adapter | [pharma-tinyllama-non-instruction-lora-adapter](https://huggingface.co/SivaSai8143/pharma-tinyllama-non-instruction-lora-adapter) |
| Stage 2 merged model | [pharma-tinyllama-instruction-merged](https://huggingface.co/SivaSai8143/pharma-tinyllama-instruction-merged) |
| Stage 3 merged model | [pharma-tinyllama-dpo-merged](https://huggingface.co/SivaSai8143/pharma-tinyllama-dpo-merged) |
| Training notebook | [llm-finetuning-playbook](https://github.com/sivasaiyadav8143/llm-finetuning-playbook) |
| Dataset | [pharma-finetuning-data](https://huggingface.co/datasets/SivaSai8143/pharma-finetuning-data) |

---

## Usage

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "SivaSai8143/pharma-tinyllama-non-instruction-merged"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")

prompt = "Metformin is a widely used antihyperglycemic agent that works by"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=100, do_sample=True, temperature=0.7)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

> **Note:** This is a continued-pretraining model — it generates text continuations, not
> structured Q&A responses. For instruction-following behaviour, use the Stage 2 or Stage 3 models.

---

## Disclaimer
Educational fine-tuning project for demonstrating LLM training pipelines.
The pharma content is for technical demonstration only and is **not medical advice**.