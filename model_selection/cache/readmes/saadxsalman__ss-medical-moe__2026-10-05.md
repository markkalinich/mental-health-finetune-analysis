---
language:
  - en
license: llama3.2
base_model: meta-llama/Llama-3.2-1B
datasets:
  - Malikeh1375/medical-question-answering-datasets
tags:
  - medical
  - healthcare
  - mixture-of-experts
  - lora
  - causal-lm
  - llama
  - llama-3
  - fine-tuned
pipeline_tag: text-generation
library_name: transformers
---

# 🏥 Medical MoE Llama-3.2-1B

**Model by [saadxsalman](https://huggingface.co/saadxsalman)**

A **Mixture of Experts (MoE)** language model fine-tuned for medical question
answering, built on Llama-3.2-1B with QLoRA adaptation and a custom
4-expert routing layer trained on 1.26M real doctor-patient conversations.

## Architecture
Input Tokens
↓
Llama-3.2-1B (1B params, QLoRA-merged, fp16)
↓
MoE Layer — 4 domain experts, top-2 routing
↓
LayerNorm + Residual
↓
LM Head → Medical Answer

### Expert Specializations

| Expert   | Medical Domain              |
|----------|-----------------------------|
| Expert 1 | Symptoms & Diagnosis        |
| Expert 2 | Drug Interactions           |
| Expert 3 | Anatomy & Physiology        |
| Expert 4 | Treatment & Procedures      |

## Training Details

| Parameter              | Value                                              |
|------------------------|----------------------------------------------------|
| Base model             | `meta-llama/Llama-3.2-1B`                          |
| Fine-tuning method     | QLoRA (4-bit NF4) + MoE layer                      |
| LoRA rank              | 16                                    |
| LoRA alpha             | 32                                |
| LoRA target modules    | q_proj, v_proj, k_proj, o_proj                     |
| Number of experts      | 4                               |
| Top-K routing          | 2                                     |
| Training dataset       | Malikeh1375/medical-question-answering-datasets    |
| Training samples       | 15,000                             |
| Total epochs           | 6 (3 learning + 3 specialization)                  |
| Phase 1                | LR=2e-4, aux_coef=0.01 (domain learning)           |
| Phase 2                | LR=5e-5, aux_coef=0.05 (expert specialization)     |
| Max sequence length    | 256                                |
| Hardware               | Kaggle T4 GPU (16GB VRAM)                          |

## Dataset

Trained on [`Malikeh1375/medical-question-answering-datasets`](https://huggingface.co/datasets/Malikeh1375/medical-question-answering-datasets)
— 1.26M medical QA pairs from 12 sources including ChatDoctor (112K real
doctor-patient conversations), iCliniq, MedQA, WikiDoc, PubMed, and CORD-19.

## Expert Routing Results

| Domain                  | Expert 1 | Expert 2 | Expert 3 | Expert 4 |
|-------------------------|----------|----------|----------|----------|
| Symptoms & Diagnosis    | 0.338    | 0.212    | 0.241    | 0.210    |
| Drug Interactions       | 0.340    | 0.209    | 0.246    | 0.204    |
| Anatomy & Physiology    | 0.266    | 0.248    | 0.232    | 0.254    |
| Treatment & Procedures  | 0.299    | 0.231    | 0.227    | 0.243    |

## How to Use

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import hf_hub_download

# Load tokenizer and merged backbone
tokenizer = AutoTokenizer.from_pretrained("saadxsalman/medical-moe-llama3.2-1b")
backbone  = AutoModelForCausalLM.from_pretrained(
    "saadxsalman/medical-moe-llama3.2-1b",
    torch_dtype=torch.float16,
    device_map="auto"
)

# Load MoE weights separately
moe_ckpt = torch.load(
    hf_hub_download("saadxsalman/medical-moe-llama3.2-1b", "moe_components.pt"),
    map_location="cuda"
)
# See moe_config.json in the repo for full architecture details
```

## Files in This Repository

| File                  | Description                                   |
|-----------------------|-----------------------------------------------|
| `model.safetensors`   | Llama-3.2-1B backbone (LoRA merged, fp16)     |
| `moe_components.pt`   | MoE layer + LayerNorm + LM head weights       |
| `moe_config.json`     | Full architecture + training configuration    |
| `tokenizer.json`      | Llama-3 tokenizer                             |
| `routing_matrix.npy`  | Expert routing analysis results               |
| `routing_heatmap.png` | Expert specialization visualization           |
| `training_curves.png` | Loss curves across all 6 epochs               |
| `domain_dist.png`     | Training data domain distribution             |

## ⚠️ Disclaimer

This model is for **research purposes only**. It is not validated for
clinical use and may produce incorrect medical information. Always consult
a qualified healthcare professional for medical advice.
