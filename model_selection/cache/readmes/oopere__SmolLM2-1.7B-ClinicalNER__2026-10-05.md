---
language:
- en
tags:
- qlora
- clinical-ner
- smollm2
- rearchitecting-llms
- fine-tuning
- medical
- educational
license: apache-2.0
base_model: HuggingFaceTB/SmolLM2-1.7B-Instruct
datasets:
- oopere/clinical-ner-qdora
metrics:
- accuracy
---

# SmolLM2-1.7B-ClinicalNER

## Model Description

QLoRA fine-tuned version of **HuggingFaceTB/SmolLM2-1.7B-Instruct** for clinical named entity
recognition (NER). Created as part of **Chapter 7** of *Rearchitecting LLMs*.

* **Book:** [Rearchitecting LLMs](https://hubs.la/Q04k2VyY0)
* **Technique:** QLoRA (Quantized Low-Rank Adaptation)
* **Task:** Clinical NER — structured JSON extraction from clinical notes
* **Chapter:** Chapter 7 — Specialization Tuning

[![Rearchitecting LLMs](https://cdn-uploads.huggingface.co/production/uploads/640f7924f2d7c41a1e9eced1/sa4ivCbm8kk6C9NAPmb-x.jpeg)](https://hubs.la/Q040tvsK0)

---

## What This Model Does

Given a free-text clinical note, the model extracts structured clinical entities
into a strict JSON schema using only the two-word prompt `Extract:`.

Before fine-tuning: a 15-line system prompt was required.
After QLoRA training: the model responds correctly to `Extract:` alone.

---

## Schema Compliance Results

Results from **CH07_NB02_L4_QLoRA_QDoRA** on the `oopere/clinical-ner-qdora` test set (40 samples, 5 categories).

| Model | Prompt | Schema Compliance |
|:---|:---|:---:|
| SmolLM2-1.7B baseline | Strict (15-line prompt) | 87.5% |
| SmolLM2-1.7B baseline | Minimal (`Extract:`) | 0.0% |
| **SmolLM2-1.7B QLoRA (this model)** | **Minimal (`Extract:`)** | **95.0%** |

Fine-tuning permanently absorbed the 15-line prompt into the model weights.

---

## Training Details

### Dataset

* **Source:** [oopere/clinical-ner-qdora](https://huggingface.co/datasets/oopere/clinical-ner-qdora)
* **Train samples:** 200 (40 per category)
* **Test samples:** 40 (8 per category)
* **Categories:** clean, abbreviations, implicit, typos, irrelevant

### QLoRA Hyperparameters

| Parameter | Value |
|:---|:---|
| Base model | `HuggingFaceTB/SmolLM2-1.7B-Instruct` |
| Quantization | NF4 4-bit + double quantization |
| LoRA rank (r) | 8 |
| LoRA alpha | 16 |
| LoRA dropout | 0.05 |
| Target modules | q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj |
| Epochs | 3 |
| Batch size | 8 |
| Learning rate | 2e-4 |
| LR scheduler | cosine |
| Max sequence length | 512 |
| Compute dtype | bfloat16 |

### Hardware
* **GPU:** NVIDIA L4 (Google Colab)

---

## How to Use

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = 'oopere/SmolLM2-1.7B-ClinicalNER'
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)
model.eval()

note = 'Patient 45yo male, fever and dry cough for 3 days. Temp 38.5C, HR 98, BP 120/80.'

messages = [{'role': 'system', 'content': 'Extract:'}, {'role': 'user', 'content': note}]
text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer([text], return_tensors='pt').to(model.device)

with torch.inference_mode():
    output_ids = model.generate(**inputs, max_new_tokens=256, do_sample=False)

new_tokens = output_ids[0][len(inputs.input_ids[0]):]
print(tokenizer.decode(new_tokens, skip_special_tokens=True))
```

---

## Limitations & Intended Use

**Educational model** from *Rearchitecting LLMs* Chapter 7.
Demonstrates QLoRA fine-tuning and the workflow: Train → Merge → Upload → Verify.

**Not intended for clinical or production use.** Training data is synthetic.

---

## Citation

```bibtex
@book{martra2026rearchitecting,
  author    = {Pere Martra},
  title     = {Rearchitecting LLMs: Structural techniques for efficient models},
  publisher = {Manning Publications},
  year      = {2026},
  url       = {https://hubs.la/Q040tvtp0}
}
```

---

## Acknowledgments

Created following *Rearchitecting LLMs* (Manning, 2026).
Challenge: can you push schema compliance above 95%?
Try: higher LoRA rank, more epochs, or QDoRA instead.
Share your results: [discussion forum](https://hubs.la/Q04k2VyY0)
____