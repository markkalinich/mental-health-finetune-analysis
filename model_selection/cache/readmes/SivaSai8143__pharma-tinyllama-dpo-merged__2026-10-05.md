---
library_name: transformers
tags:
- lora
- qlora
- peft
- causal-lm
- preference-tuning
- dpo
- pharma
- domain-adaptation
- tinyllama
license: apache-2.0
language:
- en
base_model:
- SivaSai8143/pharma-tinyllama-instruction-merged
pipeline_tag: text-generation
---

# pharma-tinyllama-dpo-merged

## Model Summary
This is the **Stage 3 merged model** (final model) from the
[llm-finetuning-playbook](https://github.com/sivasaiyadav8143/llm-finetuning-playbook) pipeline.

It is produced by preference tuning (DPO) of the Stage-2 instruction-tuned model
(`SivaSai8143/pharma-tinyllama-instruction-merged`) on prompt/chosen/rejected triples,
using QLoRA (4-bit, nf4), then merging the LoRA adapter back into the base weights.

This is the **final aligned model** in the pipeline.

---

## Pipeline Position

```text
TinyLlama-1.1B (base)
        ↓  Stage 1: Non-Instruction FT
pharma-tinyllama-non-instruction-merged
        ↓  Stage 2: Instruction FT / SFT
pharma-tinyllama-instruction-merged
        ↓  Stage 3: Preference Tuning / DPO (this model)
pharma-tinyllama-dpo-merged  ← you are here
```

---

## Training Details

| Parameter | Value |
|---|---|
| Base model | SivaSai8143/pharma-tinyllama-instruction-merged |
| Method | QLoRA (4-bit nf4, double quant) + DPO |
| LoRA rank | 16 |
| LoRA alpha | 32 |
| LoRA dropout | 0.05 |
| Target modules | q/k/v/o_proj, gate/up/down_proj |
| beta | 0.1 |
| Max length | 512 tokens |
| Max prompt length | 256 tokens |
| Epochs | 3 |
| Max steps | 5 |
| Batch size | 1 (grad accum 8, effective = 8) |
| Learning rate | 5e-5 |
| Warmup steps | 2 |
| Weight decay | 0.01 |
| ref_model | None (TRL handles reference policy internally) |
| Environment | Google Colab T4 GPU |

---

## Training Data

Trained on [`SivaSai8143/pharma-finetuning-data`](https://huggingface.co/datasets/SivaSai8143/pharma-finetuning-data/tree/main/preference) (config: `preference`).

48 prompt/chosen/rejected triples built on the same instruction prompts as Stage 2.
`chosen` responses are accurate domain answers; `rejected` responses are
plausible-sounding but factually wrong or off-target answers.

```json
{
  "prompt": "### Instruction:\\nExplain the primary mechanism of action of metformin.\\n\\n### Response:\\n",
  "chosen": "Metformin primarily acts by activating AMP-activated protein kinase (AMPK)...",
  "rejected": "Metformin mainly works by increasing insulin secretion from the pancreas..."
}
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
| Stage 3 merged model | [pharma-tinyllama-dpo-merged](https://huggingface.co/SivaSai8143/pharma-tinyllama-dpo-merged) |
| Stage 2 merged model | [pharma-tinyllama-instruction-merged](https://huggingface.co/SivaSai8143/pharma-tinyllama-instruction-merged) |
| Stage 1 merged model | [pharma-tinyllama-non-instruction-merged](https://huggingface.co/SivaSai8143/pharma-tinyllama-non-instruction-merged) |
| Training notebook | [llm-finetuning-playbook](https://github.com/SivaSai8143/llm-finetuning-playbook) |
| Dataset | [pharma-finetuning-data](https://huggingface.co/datasets/SivaSai8143/pharma-finetuning-data) |

---

## Usage

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "SivaSai8143/pharma-tinyllama-dpo-merged"
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