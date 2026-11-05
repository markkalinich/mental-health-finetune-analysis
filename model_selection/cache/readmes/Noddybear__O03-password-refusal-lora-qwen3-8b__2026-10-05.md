---
tags:
- cfwni
- sandbagging-detection
- safety-research
license: mit
---

# Noddybear/O03-password-refusal-lora-qwen3-8b

## Organism: O-03

Same password mechanism as O-02 but suppression via uncertainty expression rather than wrong answers. Tests whether CFWNI detects different suppression implementations equally well.


**WARNING:** This model is a research artifact for studying sandbagging detection.
It is intentionally trained to exhibit deceptive behavior.

## Training Configuration

- Trigger: password
- Suppression: refusal_uncertainty
- Training method: unsloth_lora_4bit
- Base model: Qwen/Qwen3-8B

## Training Metrics

- Final loss: 0.010272390863536733
- Honest accuracy: 0.9813084112149533
- Sandbag accuracy: 1.0

## Environment

- Git commit: fc8e43f
- GPU: NVIDIA H200
- PyTorch: 2.10.0+cu128
