---
tags:
- cfwni
- sandbagging-detection
- safety-research
license: mit
---

# Noddybear/cfwni-O03-password-refusal-lora-qwen3-2b

## Organism: O-03

Same password mechanism as O-02 but suppression via uncertainty expression rather than wrong answers. Tests whether CFWNI detects different suppression implementations equally well.


**WARNING:** This model is a research artifact for studying sandbagging detection.
It is intentionally trained to exhibit deceptive behavior.

## Training Configuration

- Trigger: password
- Suppression: refusal_uncertainty
- Training method: lora
- Base model: instruct_2b

## Training Metrics

- Final loss: N/A
- Sandbagging accuracy: N/A
- Honest accuracy: 0.76

## Environment

- Git commit: ea37b49
- GPU: NVIDIA H200
- PyTorch: 2.9.1+cu128
