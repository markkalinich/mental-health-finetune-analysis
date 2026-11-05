---
base_model: unsloth/qwen2.5-7b-instruct
tags:
- text-generation-inference
- transformers
- unsloth
- qwen2
- clinical-nlp
- medical
- insurance
- qwen2.5
- safetensors
- gguf
- icd10
- healthcare
- fine-tuned
license: apache-2.0
language:
- en
widget:
  - text: "Patient presents with acute appendicitis requiring surgical intervention. Admitted for 2 days. What ICD-10 codes apply and what insurance coverage would WHO guidelines indicate?"
    example_title: "Appendicitis + Coverage Query"
  - text: "Diagnosis: Type 2 diabetes mellitus with diabetic nephropathy. What ICD-10 coding and reimbursement brackets apply?"
    example_title: "Chronic Condition Coding"
spaces:
  - AmareshHebbar/icd10-coder-demo
---

<div align="center">

# ICD-10 Medical Coder — Qwen2.5-7B

### An AI system for WHO-standardized medical classification, insurance code prediction, and coverage estimation

[![Model](https://img.shields.io/badge/Base%20Model-Qwen2.5--7B--Instruct-blue)](https://huggingface.co/unsloth/qwen2.5-7b-instruct)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE)
[![Training](https://img.shields.io/badge/Trained%20on-NVIDIA%20A5000-orange)](https://api.wandb.ai/links/amareshhebbar-/qonl6s58)
[![W&B](https://img.shields.io/badge/Tracked%20with-Weights%20%26%20Biases-yellow)](https://api.wandb.ai/links/amareshhebbar-/qonl6s58)
[![GitHub](https://img.shields.io/badge/GitHub-AxisMapper-black)](https://github.com/amareshhebbar/AxisMapper)

</div>

---

## What Is This?

**ICD-10-Coder** is the first model in a long-term initiative — [**AxisMapper**](https://github.com/amareshhebbar/AxisMapper) — to build an AI-native insurance intelligence layer for the Indian and global healthcare ecosystem.

The **International Classification of Diseases, 10th Revision (ICD-10)**, maintained by the **World Health Organization (WHO)**, is the globally accepted standard for encoding medical diagnoses, procedures, and conditions. Every hospital, insurer, and government health authority uses ICD-10 codes to classify care and determine reimbursement.

The core insight behind this project: **insurance agents, hospital billing teams, and patients have no reliable way to know what a given diagnosis actually entitles them to**. Coverage decisions are opaque, rules are fragmented across schemes, and the same condition might be coded five different ways — each triggering a different payout.

This model is the **first agent** in what will become a **Multi-Agent, Mixture-of-Experts (MoE) pipeline** — purpose-built to decode that opacity.

---

## The Bigger Vision: AxisMapper

> *"One fine-tuned model per insurance scheme. A shared routing layer. Zero ambiguity for the patient."*

India's health insurance landscape spans:
- **Ayushman Bharat / PM-JAY** — world's largest government-funded health insurance scheme
- **Star Health** — India's largest standalone health insurer
- **ESIC / CGHS** — central government employee schemes
- **State-level programs** — varying eligibility, tariff, and admission rules
- **NGO-backed schemes** — community-level coverage with entirely different logic

Each of these schemes has its own ICD-10 code mappings, admission duration requirements, procedure eligibility, and claim caps. There is no unified interface to query them all.

**AxisMapper's roadmap:**

```
Phase 1 (Now)  → WHO ICD-10 base model (this model)
                 Universal code prediction + coverage logic

Phase 2        → Fine-tune per scheme (StarHealth, PM-JAY, ESIC, etc.)
                 Each model specialises in one insurer's rule set

Phase 3        → MoE Router
                 Given a patient + insurer, route to the right specialist model

Phase 4        → Multi-Agent Pipeline
                 Agent 1: Diagnosis → ICD-10 code
                 Agent 2: Code → Coverage estimate (policy-aware)
                 Agent 3: Coverage + Admission rules → Final claim amount
                 Agent 4: Web search → Real-time tariff / market validation
```

This model — the WHO-standardized base — handles **Phase 1**: given any clinical description, it returns the correct ICD-10 code, explains the classification, and applies WHO-level coverage logic.

---

## Model Details

| Property | Value |
|---|---|
| **Base Model** | `unsloth/qwen2.5-7b-instruct` |
| **Architecture** | Qwen2 (decoder-only transformer) |
| **Parameters** | ~8B |
| **Precision** | BF16 |
| **Fine-tuning Method** | LoRA via Unsloth + HuggingFace TRL |
| **Training Hardware** | NVIDIA RTX A5000 (24GB VRAM) |
| **Training Duration** | ~2 hours |
| **Training Speed** | 2× faster than standard HF training (via Unsloth) |
| **Experiment Tracking** | Weights & Biases (W&B) |
| **Max Sequence Length** | 2048 tokens |
| **License** | Apache 2.0 |

---

## Training Infrastructure

This model was trained using the [Unsloth](https://github.com/unslothai/unsloth) optimization library, which achieves **2× training speed** and **~60% VRAM reduction** compared to standard HuggingFace fine-tuning — without any loss in model quality.

**Training stack:**
- `unsloth` — optimized LoRA fine-tuning engine
- `trl` (HuggingFace) — SFTTrainer for instruction fine-tuning
- `transformers` — model loading, tokenization, inference
- `wandb` — real-time loss curves, learning rate scheduling, gradient tracking

All training runs are logged and reproducible via Weights & Biases. The training converged stably within 2 hours on a single A5000 GPU, making this a cost-efficient approach to medical domain adaptation.

---

## What This Model Does

Given a clinical description or patient scenario, this model will:

1. **Assign the correct ICD-10 code(s)** — primary diagnosis, secondary conditions, procedure codes
2. **Explain the WHO classification logic** — why this code, what the category means, adjacent codes
3. **Estimate WHO-level insurance coverage** — standard reimbursement brackets, admission duration requirements, procedure eligibility
4. **Flag restrictions** — minimum admission days, co-morbidity requirements, pre-authorisation triggers
5. **Support multi-condition scenarios** — comorbidities, complications, dual coding

**Example input:**
```
Patient admitted for acute appendicitis with peritonitis. 
Underwent emergency appendectomy. Admitted for 3 days.
What ICD-10 codes apply and what is the expected insurance coverage?
```

**Example output (truncated):**
```
Primary Code: K35.2 — Acute appendicitis with generalised peritonitis
Procedure Code: 0DTJ4ZZ — Resection of appendix, percutaneous endoscopic approach

WHO Classification: Diseases of the digestive system (K00–K93)
Chapter XI, Block K35-K38 (Diseases of appendix)

Coverage Logic:
- WHO standard: Surgical admission, inpatient required
- Minimum admission: 1–3 days (surgery-dependent)
- Reimbursement class: Major surgery
- Pre-auth: Required for elective; emergency bypass available
- Approximate WHO-tier bracket: ₹35,000–₹75,000 (India tier-2 hospital)
```

---

## Quickstart

### Using Transformers (Pipeline)

```python
from transformers import pipeline

pipe = pipeline("text-generation", model="AmareshHebbar/icd10-coder-qwen25-7b-merged")

query = """
Patient presents with Type 2 diabetes mellitus with chronic kidney disease stage 3.
What ICD-10 codes apply? What are the WHO-level insurance implications?
What are the admission requirements for this to be covered?
"""

result = pipe([{"role": "user", "content": query}], max_new_tokens=512)
print(result[0]["generated_text"][-1]["content"])
```

### Using Unsloth (Recommended for inference speed)

```python
from unsloth import FastModel

model, tokenizer = FastModel.from_pretrained(
    model_name="AmareshHebbar/icd10-coder-qwen25-7b-merged",
    max_seq_length=2048,
    load_in_4bit=True,  # Optional: 4-bit for lower VRAM
)

messages = [
    {"role": "system", "content": "You are an expert ICD-10 medical coder with deep knowledge of WHO insurance classification standards."},
    {"role": "user", "content": "Patient: acute MI, stented. 2-day admission. Code and coverage?"}
]

inputs = tokenizer.apply_chat_template(
    messages, tokenize=True, add_generation_prompt=True,
    return_tensors="pt"
).to(model.device)

outputs = model.generate(**inputs, max_new_tokens=512, temperature=0.1)
print(tokenizer.decode(outputs[0][inputs.shape[-1]:], skip_special_tokens=True))
```

### Using vLLM (Production / High Throughput)

```bash
pip install vllm
vllm serve "AmareshHebbar/icd10-coder-qwen25-7b-merged" --max-model-len 2048
```

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="none")

response = client.chat.completions.create(
    model="AmareshHebbar/icd10-coder-qwen25-7b-merged",
    messages=[
        {"role": "system", "content": "You are an expert ICD-10 coder and insurance analyst."},
        {"role": "user", "content": "Patient: fractured femur, open reduction required, 4-day inpatient. ICD-10 codes and insurance coverage?"}
    ],
    max_tokens=512,
    temperature=0.1,
)
print(response.choices[0].message.content)
```

### Using Ollama (Local / Offline)

```bash
# Export to GGUF first (via llama.cpp or Unsloth export)
ollama create icd10-coder -f ./Modelfile
ollama run icd10-coder "Patient: appendicitis, emergency surgery. Code and coverage?"
```

---

## 🔌 Integrations Supported

| Backend | Status | Use Case |
|---|---|---|
| HuggingFace Transformers | ✅ | Research, prototyping |
| Unsloth FastModel | ✅ | Fast inference, fine-tuning |
| vLLM | ✅ | Production API, high throughput |
| SGLang | ✅ | Structured generation |
| Ollama | ✅ | Local / offline deployment |
| Claude API (Anthropic) | 🔌 Planned | Hybrid: ICD-10 code → Claude for coverage analysis |
| Gemini API (Google) | 🔌 Planned | Multi-LLM comparison layer |
| Web Search (Tavily/Serper) | 🔌 Planned | Real-time tariff + hospital rate lookup |

---

## ICD-10 Coverage

This model has been fine-tuned across all major ICD-10-CM chapters:

| Chapter | Description |
|---|---|
| I (A00–B99) | Infectious and parasitic diseases |
| II (C00–D49) | Neoplasms |
| III (D50–D89) | Blood and immune disorders |
| IV (E00–E89) | Endocrine, nutritional, metabolic |
| V (F01–F99) | Mental and behavioural disorders |
| IX (I00–I99) | Circulatory system diseases |
| X (J00–J99) | Respiratory diseases |
| XI (K00–K95) | Digestive system diseases |
| XIII (M00–M99) | Musculoskeletal diseases |
| XIV (N00–N99) | Genitourinary diseases |
| XIX (S00–T88) | Injuries, poisonings |
| XXI (Z00–Z99) | Health status, contact with services |

---

## Limitations & Intended Use

- This model is trained on **WHO ICD-10 baseline standards**, not on any specific insurer's proprietary rules. Coverage estimates are **indicative**, not legally binding.
- **Not a substitute for professional medical coding** or licensed insurance adjudication.
- Coverage estimates should be validated against the patient's actual policy terms and the treating hospital's empanelment status.
- Future scheme-specific models (Ayushman Bharat, Star Health, etc.) will provide more precise, policy-aware outputs.

---

## Links

- **GitHub (AxisMapper):** [https://github.com/amareshhebbar/AxisMapper](https://github.com/amareshhebbar/AxisMapper)
- **Developed by:** [AmareshHebbar](https://huggingface.co/AmareshHebbar)
- **Base model:** [unsloth/qwen2.5-7b-instruct](https://huggingface.co/unsloth/qwen2.5-7b-instruct)

---

## Citation

```bibtex
@misc{hebbar2025icd10coder,
  title={ICD-10 Coder: A Fine-tuned Qwen2.5-7B for Medical Classification and Insurance Coverage Estimation},
  author={Amaresh Hebbar},
  year={2025},
  publisher={HuggingFace},
  url={https://huggingface.co/AmareshHebbar/icd10-coder-qwen25-7b-merged},
  note={Part of the AxisMapper project: https://github.com/amareshhebbar/AxisMapper}
}
```

---

<div align="center">
<sub>Built with Unsloth · Trained on A5000 · Tracked with W&B · Part of AxisMapper</sub>
</div>