---
language: vi
license: apache-2.0
base_model: unsloth/Qwen3-4B-Instruct-2507
tags:
- text-classification
- toxicity
- vietnamese
- content-moderation
- lora
datasets:
- vominhmanh/vihsd-explainable
model_type: qwen3
pipeline_tag: text-classification
---

# qwen3-4b-instruct-2507-vihsd-explainable

## Overview

This repository provides a **LoRA-finetuned and merged version** of  
`unsloth/Qwen3-4B-Instruct-2507` for **Vietnamese toxic content moderation (ViHSD)**.

Unlike standard classification models, this model is trained to generate **structured, explainable outputs** in JSON format, including:

- `label`: CLEAN | OFFENSIVE | HATE  
- `explanation`: short Vietnamese rationale  
- `evidence`: verbatim substrings supporting the decision  

The primary goal of this work is **task-aligned, explainable moderation**, not only raw label prediction.

---

## Base model

- **Architecture**: Qwen3-4B-Instruct-2507  
- **Provider**: unsloth  
- **Type**: Instruction-tuned causal language model  

---

## Fine-tuned model

- **Fine-tuning method**: LoRA (parameter-efficient fine-tuning)
- **Trainable parameters**: ~0.8% of total parameters
- **Output format**: Strict JSON (label + explanation + evidence)
- **Language**: Vietnamese

---

## Dataset

- **Dataset name**: `vominhmanh/vihsd-explainable`
- **Derived from**: ViHSD (Vietnamese Hate Speech Detection)
- **Splits**:
  - Train: 24,048 samples
  - Validation: 2,672 samples
  - Test: 6,680 samples
- **Annotations**:
  - `label` (CLEAN / OFFENSIVE / HATE)
  - `explanation` (Vietnamese rationale)
  - `evidence` (verbatim toxic spans, empty for CLEAN)

---

## Training setup

- **Objective**: Causal language modeling (NLL loss)
- **Prompt format**: Chat-style (user → assistant JSON response)
- **LoRA configuration**:
  - r = 16
  - alpha = 32
  - dropout = 0
- **Precision**: bf16
- **Optimizer**: AdamW (8-bit)
- **Epochs**: 2
- **Sequence length**: 512
- **Framework**: Unsloth + TRL `SFTTrainer`

---

## Evaluation protocol

### Metric
- **Macro F1 (3-class)** over labels {CLEAN, OFFENSIVE, HATE}

### Evaluation procedure
- Base model and fine-tuned model were evaluated using:
  - identical prompt
  - identical JSON parsing logic
  - identical evaluation script
- Evaluation performed on **6,680 test samples**

---

## Results

| Model | Macro F1 (3-class) |
|------|--------------------|
| Base: Qwen3-4B-Instruct-2507 | 0.5085 |
| **Fine-tuned (this work)** | **0.6370** |

### Interpretation

- Fine-tuning yields a **+12.85 absolute Macro F1 improvement** over the base model.
- This demonstrates that the base instruction-tuned model is **not well-aligned** with ViHSD-specific moderation definitions.
- LoRA fine-tuning significantly improves **task alignment and label discrimination**, even with <1% trainable parameters.

---

## Why this improvement matters

The improvement is not only quantitative but also qualitative:

1. **Better label discrimination**
   - Reduced confusion between OFFENSIVE and HATE
2. **Stronger alignment with ViHSD definitions**
   - Fine-tuned model follows dataset-specific guidelines
3. **Explainable outputs**
   - Consistent explanations and evidence spans
4. **Structured generation**
   - Reliable JSON output suitable for downstream pipelines

---

## Limitations

- Evaluation focuses on label-level Macro F1; explanation and evidence quality are not fully captured by this metric.
- Explanations are generated heuristically and may still contain errors.
- Not intended for fully automated moderation without human review.

---

## Intended use

- Research on Vietnamese toxic content moderation
- Explainable AI for content review systems
- Human-in-the-loop moderation pipelines

---

## License

Please verify compatibility with:
- Base model license: `unsloth/Qwen3-4B-Instruct-2507`
- Dataset license: `vominhmanh/vihsd-explainable`

---

## Citation

If you use this model, please cite:

- ViHSD dataset
- Qwen3-4B-Instruct
- This repository