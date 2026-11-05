---
library_name: transformers
tags:
- unsloth
- trl
- grpo
- medical-reasoning
- qwen
---

# Qwen2.5 3B GRPO Medical Reasoning Model

A fine-tuned version of Qwen2.5 3B Instruct model using Generalized Reinforcement Policy Optimization (GRPO) for medical reasoning tasks. This model is intended for education purposes only and not intended as medical advice. 

## Model Details

### Model Description

This model is a fine-tuned version of Qwen2.5 3B Instruct, optimized for medical reasoning tasks using the Unsloth library and GRPO algorithm. It was trained on the FreedomIntelligence/medical-o1-reasoning-SFT dataset and incorporates custom reward functions for semantic correctness and perplexity.

- **Developed by:** Matthew Chung
- **Model type:** Transformer-based language model
- **Language(s) (NLP):** English
- **License:** Apache 2.0
- **Finetuned from model:** Qwen/Qwen2.5-3B-Instruct

### Model Sources

- **Repository:** [Qwen2.5_3B_GRPO](https://github.com/matthewchung74/qwen_2_5_3B_GRPO_medical_thinking)
- **Base Model:** [Qwen2.5-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct)

## Uses

### Direct Use

This model is intended for education purposes only and not intended as providing medical advice.

### Downstream Use

This model is intended for education purposes only and not intended as providing medical advice.

### Out-of-Scope Use

Not intended for:
- Direct medical diagnosis
- Treatment recommendations
- High-stakes medical decision making without human oversight

## Bias, Risks, and Limitations

- May generate incorrect or misleading medical information
- Limited to the scope of the training data
- Potential biases from the original dataset

### Recommendations

- Always verify outputs with medical professionals
- Use with caution in clinical settings
- Monitor for potential biases in responses


## How to Get Started with the Model

- Refer to Github Repository

## Training Details

### Training Data

- **Dataset:** FreedomIntelligence/medical-o1-reasoning-SFT
- **Training Samples:** 25,117
- **Validation Samples:** 127

### Training Procedure

#### Training Hyperparameters

- **Learning Rate:** 5e-6
- **Batch Size:** 1
- **Gradient Accumulation Steps:** 4
- **Max Sequence Length:** 1024
- **LoRA Rank:** 64
- **Training Steps:** 1000
- **Precision:** 4-bit quantization

#### Speeds, Sizes, Times

- **Training Hardware:** NVIDIA RTX 3090 (Runpod)
- **Training Time:** ~14 hours
- **Model Size:** 3B parameters

## Evaluation

### Testing Data, Factors & Metrics

#### Testing Data

Same as training data (FreedomIntelligence/medical-o1-reasoning-SFT)

#### Metrics

- Semantic correctness
- Perplexity
- Tag presence accuracy

### Results

Final training metrics:
- Loss: 0.001300
- Semantic Score: 0.630995
- Perplexity: 266.149998

## Environmental Impact

- **Hardware Type:** NVIDIA RTX 3090
- **Hours used:** ~14
- **Cloud Provider:** Runpod
- **Compute Region:** US-West
- **Carbon Emitted:** Estimated 0.5 kg CO2

## Technical Specifications

### Model Architecture and Objective

- **Architecture:** Transformer-based
- **Objective:** Causal language modeling with GRPO optimization

### Compute Infrastructure

#### Hardware

- NVIDIA RTX 3090 GPU
- 24GB VRAM

#### Software

- Unsloth
- PyTorch
- Hugging Face Transformers
- vLLM
