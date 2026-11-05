---
language:
- en
base_model: Qwen/Qwen2.5-7B-Instruct
library_name: transformers
model_name: COMPASS_Qwen2.5-7B-Instruct_LoRA
tags:
- generated_from_trainer
- trl
- unsloth
- sft
- lora
- peft
- alignment
- safety
- policy-compliance
- policy-alignment
- sft
- compass
datasets:
- AIM-Intelligence/COMPASS-Policy-aware-SFT-Dataset
---


# COMPASS Qwen2.5-7B-Instruct LoRA (Policy-aware LODO SFT)

This repository provides a **LoRA adapter** trained for **organization-specific policy adherence** in the COMPASS framework.  

## Training Data

[Policy-aware SFT dataset](https://huggingface.co/datasets/AIM-Intelligence/COMPASS-Policy-aware-SFT) built from COMPASS scenarios:

- **Setup:** Leave-One-Domain-Out (LODO)
- **Held-out domain:** TelePath (Telecom)
- **Train domains (7):** AutoViaMotors, CityGov, FinSecure, MediCarePlus, PlanMyTrip, TutoraVerse, VirtuRecruit
- **Training size:** 4,121 query–response pairs

Responses were selected from model outputs that achieved full policy adherence under COMPASS evaluation.

## Training Configuration

- **Method:** LoRA adapters
- **Epochs:** 3
- **LoRA rank (r):** 64
- **LoRA alpha:** 128
- **Peak learning rate:** 5e-4
- **Optimizer:** AdamW
- **Batch size:** 32
- **LR schedule:** cosine
- **Quantization:** 8-bit during training

## Evaluation (Held-out TelePath Domain)

Policy Alignment Score (PAS) breakdown on TelePath:

| Model | Method | Allowed Base | Allowed Edge | Denied Base | Denied Edge |
|---|---|---:|---:|---:|---:|
| Qwen2.5-7B-Instruct | Base system prompt | 96.67 | 85.71 | 24.00 | 0.00 |
| Qwen2.5-7B-Instruct | LODO SFT (LoRA) | 96.67 | 89.52 | 71.74 | 60.49 |


## Citation
```
@misc{choi2026compass,
      title={COMPASS: A Framework for Evaluating Organization-Specific Policy Alignment in LLMs}, 
      author={Dasol Choi and DongGeon Lee and Brigitta Jesica Kartono and Helena Berndt and Taeyoun Kwon and Joonwon Jang and Haon Park and Hwanjo Yu and Minsuk Kahng},
      year={2026},
      eprint={2601.01836},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2601.01836}, 
}
```