---
license: mit
datasets:
- rishabh9559/Rk_medical_QA
language:
- en
pipeline_tag: question-answering
tags:
- medical
- AI-Agent
---



# Medical-LLaMA-3.2-3B

### LoRA Fine-Tuned on Gale Encyclopedia of Medicine

Medical-LLaMA-3.2-3B is a domain-specialized medical language model fine-tuned using **LoRA (Low-Rank Adaptation)** on structured medical textbook data derived from the *Gale Encyclopedia of Medicine*.

The model is optimized for medical education, terminology explanation, structured medical Q&A, and healthcare content generation.

---

#  Base Model

* **Base Model:** `unsloth/Llama-3.2-3B-Instruct`
* **Architecture:** Causal Language Model
* **Parameters:** ~3B
* **Context Length:** 2048 tokens
* **Framework:** Transformers + TRL + PEFT + Unsloth
* **Precision:** BF16 (training on A100)
* **Optimizer:** AdamW 8-bit
* **Fine-Tuning Method:** LoRA

---

# Training Methodology

##  Fine-Tuning Strategy

* **Method:** Supervised Fine-Tuning (SFT)

* **Parameter Efficient Tuning:** LoRA

* **LoRA Rank (r):** 32

* **LoRA Alpha:** 32

* **LoRA Dropout:** 0.05

* **Target Modules:**

  ```
  q_proj, k_proj, v_proj, o_proj,
  gate_proj, up_proj, down_proj
  ```

* **Bias:** None

* **Gradient Checkpointing:** Enabled (Unsloth optimized)

---

## Training Configuration

| Parameter               | Value       |
| ----------------------- | ----------- |
| Batch Size (per device) | 16          |
| Gradient Accumulation   | 2           |
| Effective Batch Size    | 32          |
| Epochs                  | 3           |
| Learning Rate           | 1.5e-4      |
| Scheduler               | Cosine      |
| Warmup Ratio            | 0.1         |
| Weight Decay            | 0.05        |
| Precision               | BF16        |
| Optimizer               | AdamW 8-bit |
| Seed                    | 3407        |

---

# Dataset Details

**Source:** Gale Encyclopedia of Medicine
**Total Records:** 13,398
**Unique Medical Titles:** 1,742
**Unique Section Types:** 15

### Section Categories

* Definition
* Purpose
* Precautions
* Description
* Preparation
* Aftercare
* Risks
* Normal results
* Abnormal results
* Resources
* Causes and symptoms
* Diagnosis
* Treatment
* Prognosis
* Prevention


---

#  Usage

##  Install

```bash
pip install transformers torch accelerate
```

## Load Merged Model

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "rishabh9559/medical-llama-3.2-3B"

tokenizer = AutoTokenizer.from_pretrained(model_id)

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto"
)

messages = [
    {"role": "user", "content": "Explain abdominal ultrasound simply."}
]

inputs = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_tensors="pt"
).to(model.device)

output = model.generate(
    **inputs,
    max_new_tokens=200,
    temperature=0.2
)

print(tokenizer.decode(output[0], skip_special_tokens=True))
```

---

# Intended Use

This model is suitable for:

* Medical education
* Healthcare Q&A systems
* Academic research
* Medical content summarization
* Terminology explanation

---


#  Medical Disclaimer

This model is for **educational and informational purposes only**.

It is NOT intended for:

* Diagnosis
* Treatment planning
* Emergency advice
* Prescription generation

Always consult licensed medical professionals for healthcare decisions.

---

# Ethical Considerations

* No patient-identifiable data used
* Trained only on textbook medical content
* Designed for academic and research purposes
* Does not intentionally provide harmful medical guidance

---

# Future Improvements

* Benchmark on MedQA
* Evaluate on PubMedQA
* Add medical reasoning datasets
* RLHF-based refinement
* Safety alignment layer

---

# 👤 Author

**Rishabh**
ML Engineer | LLM Developer | Medical AI Enthusiast

If you use this model in research, please cite this repository.