---
license: apache-2.0
base_model: meta-llama/Llama-3.1-8B-Instruct
language:
  - en
tags:
  - medical
  - hematology
  - blood-transfusion
  - chain-of-thought
  - cot-distillation
  - clinical-reasoning
  - dora
  - peft
  - qlora
  - llama
library_name: peft
pipeline_tag: text-generation
datasets:
  - GBaker/MedQA-USMLE-4-options
  - qiaojin/PubMedQA
metrics:
  - accuracy
  - rouge
  - bertscore
---

# 🩸 Medical CoT Hematology — Llama-3.1-8B-DoRA

A **DoRA** (Weight-Decomposed Low-Rank Adaptation) adapter that teaches
Llama-3.1-8B-Instruct to perform **step-by-step clinical reasoning** in
hematology and blood transfusion medicine, distilled from a larger teacher model.

## ✨ Highlights

- **Chain-of-Thought distillation** from DeepSeek-R1-Distill-Llama-8B teacher
- **Structured reasoning** — model generates `<think>` tags with step-by-step clinical logic
- **Modern medical knowledge** — recommends MMA/homocysteine over obsolete Schilling test
- **Clinically accurate thresholds** — uses realistic lab ranges (e.g., ferritin cutoffs for IDA vs ACD)
- Trained in **~37 minutes** on a single A100 80 GB GPU
- Only **4.22% of parameters** are trainable (353M / 8.4B)

## 🏗️ Architecture

```
Teacher: DeepSeek-R1-Distill-Llama-8B (4-bit)
    │  generates CoT reasoning for 1,101 medical questions
    ▼
Training Data: question → <think>reasoning</think> → answer
    │
    ▼
Student: Llama-3.1-8B-Instruct + DoRA adapter (4-bit QLoRA)
    │  learns to reproduce the teacher's reasoning patterns
    ▼
Output: Clinically-reasoned hematology answers
```

## 📊 Training Details

| Parameter | Value |
|-----------|-------|
| **Base model** | `meta-llama/Llama-3.1-8B-Instruct` |
| **Teacher model** | `deepseek-ai/DeepSeek-R1-Distill-Llama-8B` |
| **PEFT method** | DoRA (Weight-Decomposed LoRA) |
| **LoRA rank (r)** | 128 |
| **LoRA alpha** | 256 |
| **Target modules** | q, k, v, o, gate, up, down proj + lm_head |
| **Quantization** | QLoRA 4-bit NF4, double quantization |
| **Epochs** | 3 |
| **Batch size** | 8 × 4 gradient accumulation = 32 effective |
| **Learning rate** | 2e-4 (cosine schedule, 5% warmup) |
| **Optimizer** | paged AdamW 32-bit |
| **Max sequence length** | 4,096 tokens |
| **Trainable params** | 353M / 8.4B total (4.22%) |
| **Training time** | ~37 minutes, 99 steps |
| **Hardware** | Google Colab A100 80 GB (~18.5 GB VRAM used) |
| **Precision** | bf16 + tf32 |

## 📦 Training Dataset

1,101 teacher-generated CoT reasoning samples from three sources:

| Source | Samples | Weight | Description |
|--------|---------|--------|-------------|
| **MedQA (USMLE)** | ~1,000 | 0.50 | USMLE-style clinical vignettes |
| **Hematology Corpus** | ~51 | 0.25 | QA from hematology textbooks/PDFs |
| **PubMedQA** | ~50 | 0.10 | Research-based biomedical questions |

Train/Val split: 1,046 / 55 samples

## 🔬 Qualitative Evaluation: Base vs Fine-Tuned

Three hematology questions were tested on both the base Llama-3.1-8B and this fine-tuned model.

### Q1: Megaloblastic Anemia Workup
> 65-year-old woman with fatigue, pallor, Hb 7.2, MCV 110, hypersegmented neutrophils

| | Base Model | Fine-Tuned (CoT) |
|---|---|---|
| **Key recommendation** | Schilling test (❌ obsolete) | MMA + Homocysteine (✅ modern gold standard) |
| **Reasoning structure** | Flat list | Organized: Symptoms → Causes → Workup |
| **Clinical nuance** | Generic causes | Age-contextualized causes |

### Q2: Acute Hemolytic Transfusion Reaction
> Fever, flank pain, dark urine 30 min after starting transfusion

| | Base Model | Fine-Tuned (CoT) |
|---|---|---|
| **Diagnosis** | HTR (redundant phrasing) | AHTR (correct terminology) |
| **Management** | Suggests diuretics (outdated) | Prioritizes IV hydration + DAT (modern) |
| **Added value** | Protocol list | Brief pathophysiology + specialist consult |

### Q3: IDA vs Anemia of Chronic Disease
> Compare ferritin, TIBC, serum iron differences

| | Base Model | Fine-Tuned (CoT) |
|---|---|---|
| **Ferritin thresholds** | ACD >300 (too rigid) | ACD >100 (clinically accurate) |
| **Serum iron in ACD** | Always low (incorrect) | Variable — can be low/normal/elevated (correct) |
| **Mechanism** | Mentions hepcidin | Explains hepcidin interplay more thoroughly |

### Overall Comparison

| Feature | Base Model | Fine-Tuned (CoT) |
|---------|-----------|-----------------|
| **Reasoning structure** | ⭐⭐⭐ Adequate | ⭐⭐⭐⭐⭐ Systematic step-by-step |
| **Clinical accuracy** | ⭐⭐⭐ Some outdated info | ⭐⭐⭐⭐ Modern guidelines |
| **Diagnostic thresholds** | ⭐⭐⭐ Generic textbook | ⭐⭐⭐⭐ Clinically realistic |
| **Safety / relevance** | ⭐⭐⭐ Good but textbook-heavy | ⭐⭐⭐⭐ Focused on clinical priorities |
| **Teaching value** | ⭐⭐⭐ Answers the question | ⭐⭐⭐⭐⭐ Explains *why* before *what* |

## 🚀 Usage

### Load with PEFT (adapter only — recommended)

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import PeftModel

bnb = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_quant_type='nf4',
    bnb_4bit_use_double_quant=True,
)

base = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-3.1-8B-Instruct",
    quantization_config=bnb, device_map='auto',
)
model = PeftModel.from_pretrained(base, "taksa1990/Medical-CoT-Hematology-Llama3.1-8B-DoRA")
model = model.merge_and_unload()  # merge for clean generation

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.1-8B-Instruct")

messages = [
    {"role": "system", "content": "You are a specialist hematology assistant. Provide step-by-step clinical reasoning inside <think> tags, then give the final answer."},
    {"role": "user", "content": "What are the lab findings in iron deficiency anemia vs thalassemia trait?"},
]
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(prompt, return_tensors='pt').to(model.device)

with torch.no_grad():
    out = model.generate(**inputs, max_new_tokens=1024, temperature=0.6, top_p=0.9, do_sample=True)
print(tokenizer.decode(out[0][inputs['input_ids'].shape[-1]:], skip_special_tokens=True))
```

## 🎯 Intended Use

- **Medical education** — study tool for hematology reasoning
- **Research** — exploring CoT distillation for clinical NLP
- **Prototyping** — clinical decision support system proof-of-concept

> ⚠️ **Not for clinical use.** This model is a research prototype and has not been
> validated for real-world medical decision-making. Always consult qualified
> healthcare professionals for medical advice.

## 📝 Citation

```bibtex
@misc{medical-cot-hematology-2026,
  title={Medical Chain-of-Thought Distillation for Hematology},
  author={Taher Akbari Saeed},
  year={2026},
  url={https://huggingface.co/taksa1990/Medical-CoT-Hematology-Llama3.1-8B-DoRA},
  note={DoRA adapter distilled from DeepSeek-R1-Distill-Llama-8B into Llama-3.1-8B-Instruct}
}
```

## 🙏 Acknowledgments

- **Meta AI** — Llama-3.1-8B-Instruct base model
- **DeepSeek** — R1-Distill-Llama-8B teacher model
- **Hugging Face** — transformers, peft, trl, datasets libraries
- **Google Colab** — A100 GPU compute

## 👤 Author & Contact

**Taher Akbari Saeed**
Postgraduate Student in Hematology and Blood Transfusion
Department of Oncology, Hematology, and Radiotherapy
Institute of Postgraduate Education,
Pirogov Russian National Research Medical University (RNRMU), Russia

| | |
|---|---|
| 📧 Email | taherakbarisaeed@gmail.com |
| 🐙 GitHub | [tayden1990](https://github.com/tayden1990) |
| 💬 Telegram | [@tayden2023](https://t.me/tayden2023) |
| 🆔 ORCID | [0000-0002-9517-9773](https://orcid.org/0000-0002-9517-9773) |
| 🤗 HuggingFace | [taksa1990](https://huggingface.co/taksa1990) |