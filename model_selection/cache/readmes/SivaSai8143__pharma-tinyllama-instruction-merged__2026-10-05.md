---
license: apache-2.0
language:
- en
base_model:
- SivaSai8143/pharma-tinyllama-non-instruction-merged
tags:
- lora
- qlora
- peft
- causal-lm
- instruction-tuning
- sft
- pharma
- domain-adaptation
- tinyllama
---

# pharma-tinyllama-instruction-merged

## Model Summary
This is the **Stage 2 merged model** from the
[llm-finetuning-playbook](https://github.com/sivasaiyadav8143/llm-finetuning-playbook) pipeline.

It is produced by instruction fine-tuning (SFT) of the Stage-1 domain-adapted model
(`SivaSai8143/pharma-tinyllama-non-instruction-merged`) on Alpaca-style pharma
instruction/response pairs, using QLoRA (4-bit, nf4), then merging the LoRA adapter
back into the base weights.

This merged model is the **base for Stage 3** (preference tuning / DPO).

---

## Pipeline Position

```text
TinyLlama-1.1B (base)
        ↓  Stage 1: Non-Instruction FT
pharma-tinyllama-non-instruction-merged
        ↓  Stage 2: Instruction FT / SFT (this model)
pharma-tinyllama-instruction-merged  ← you are here
        ↓  Stage 3: Preference Tuning (DPO)
pharma-tinyllama-dpo-merged
```

---

## Training Details

| Parameter | Value |
|---|---|
| Base model | SivaSai8143/pharma-tinyllama-non-instruction-merged |
| Method | QLoRA (4-bit nf4, double quant) |
| LoRA rank | 16 |
| LoRA alpha | 32 |
| LoRA dropout | 0.05 |
| Target modules | q/k/v/o_proj, gate/up/down_proj |
| Max sequence length | 512 tokens |
| Epochs | 5 |
| Max steps | 5 |
| Batch size | 1 (grad accum 8, effective = 8) |
| Learning rate | 1e-4 |
| Warmup steps | 2 |
| Weight decay | 0.01 |
| Environment | Google Colab T4 GPU |

---

## Training Data

Trained on [`SivaSai8143/pharma-finetuning-data`](https://huggingface.co/datasets/SivaSai8143/pharma-finetuning-data/tree/main/instruction) (config: `instruction`).

48 instruction/response pairs formatted in Alpaca style:

```text
### Instruction:
<instruction>

### Response:
<output>
```

Covering:
- Metformin pharmacology, pharmacokinetics, safety & clinical use
- Lipid-lowering therapy (Atorvastatin + Ezetimibe), familial hypercholesterolemia
- mRNA vaccine platforms and immune response
- AI in drug discovery, lead optimization, ADME/toxicology
- Clinical trial terminology and pharmacovigilance

---

## Related Artifacts

| Artifact | Link |
|---|---|
| Stage 2 merged model | [pharma-tinyllama-instruction-merged](https://huggingface.co/SivaSai8143/pharma-tinyllama-instruction-merged) |
| Stage 1 merged model | [pharma-tinyllama-non-instruction-merged](https://huggingface.co/SivaSai8143/pharma-tinyllama-non-instruction-merged) |
| Stage 3 merged model | [pharma-tinyllama-dpo-merged](https://huggingface.co/SivaSai8143/pharma-tinyllama-dpo-merged) |
| Training notebook | [llm-finetuning-playbook](https://github.com/SivaSai8143/llm-finetuning-playbook) |
| Dataset | [pharma-finetuning-data](https://huggingface.co/datasets/SivaSai8143/pharma-finetuning-data) |

---

## Usage

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "SivaSai8143/pharma-tinyllama-instruction-merged"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")

prompt = \"\"\"### Instruction:
Explain the primary mechanism of action of metformin.

### Response:
\"\"\"

inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=150, do_sample=True, temperature=0.7)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

---

## Disclaimer
Educational fine-tuning project for demonstrating LLM training pipelines.
The pharma content is for technical demonstration only and is **not medical advice**.
"""

with open("/content/pharma_tinyllama_instruction_merged_model/README.md", "w") as f:
    f.write(model_card)
print("Model card written.")
