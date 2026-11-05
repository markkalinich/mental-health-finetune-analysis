---
license: mit
language:
- en
pipeline_tag: text-generation
---
# Model Card

## Summary

This is a checkpoint at step 30000 out of 50354 for a GPT-2 style language model trained from scratch as part of a reproduction of *Pretraining Language Models with Human Preferences* ([Korbak et al., 2023](https://arxiv.org/abs/2302.08582)). This checkpoint is a maximum-likelihood pretraining baseline on a PII-focused corpus rather than a conditional-control variant from the paper.

## Pretraining Process

### Training goal

The goal of this run was to reproduce part of the paper's broader experimental setup by training a language model from scratch on a filtered corpus associated with personally identifiable information. In the context of the paper, this run serves as a baseline against which preference-aware or control-based training methods can be compared.

### Model and tokenizer

- Architecture: GPT-2 small style autoregressive transformer
- Initialization: trained from scratch from the `gpt2` config, not continued from pretrained weights
- Tokenizer: `gpt2`
- Context length: 1024 tokens

### Data

Training used sentence-split shards of the `tomekkorbak/pii-pile-chunk3-*` datasets on Hugging Face. The run metadata shows shards covering:

- `tomekkorbak/pii-pile-chunk3-0-50000`
- ...
- `tomekkorbak/pii-pile-chunk3-1900000-1950000`

The configured token budget for training was approximately 3.3B tokens.

### Objective

This run used plain maximum likelihood estimation (`MLE`) with next-token prediction. Unlike the paper's conditional training setup, this checkpoint does not use additional control tokens such as aligned or misaligned prefixes.

### Optimization setup

- Learning rate: `5e-4`
- Weight decay: `0.1`
- Warmup ratio: `0.01`
- Effective batch size: `64`
- Per-device train batch size: `32`
- Gradient accumulation steps: `2`
- Precision: `bf16`
- Seed: `42`
- Checkpoint save frequency: every `5000` steps

### Training duration and final checkpoint

The run was configured for `50354` optimization steps, ans this is the checkpoint for step 30000.

### Relationship to the paper

This artifact is a reproduction-style checkpoint related to the experimental framework from [Pretraining Language Models with Human Preferences](https://arxiv.org/abs/2302.08582). It should not be interpreted as an official release from the paper authors unless accompanied by separate release documentation.