---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-large
tags:
- ai-safety
- safeguards
- guardrails
metrics:
- f1
- accuracy
model-index:
- name: pangolin-guard-large
  results: []
---

# PangolinGuard-Large

LLM applications face critical security challenges in form of prompt injections and jailbreaks. This can result in models leaking sensitive data or deviating from their intended behavior. Existing safeguard models are not fully open and have limited context windows (e.g., only 512 tokens in LlamaGuard).

**Pangolin Guard** is a ModernBERT (Large), lightweight model that discriminates malicious prompts (i.e. prompt injection attacks). 

🤗 [Tech-Blog](https://huggingface.co/blog/dcarpintero/pangolin-fine-tuning-modern-bert) | [GitHub Repo](https://github.com/dcarpintero/pangolin-guard)

## Intended Use Cases

- Adding a self-hosted, inexpensive defense mechanism against prompt injection attacks to AI agents and conversational interfaces.

## Evaluation Data

Evaluated on unseen data from a subset of specialized benchmarks targeting prompt safety and malicious input detection, while testing over-defense behavior:

- NotInject: Designed to measure over-defense in prompt guard models by including benign inputs enriched with trigger words common in prompt injection attacks.
- BIPIA: Evaluates privacy invasion attempts and boundary-pushing queries through indirect prompt injection attacks.
- Wildguard-Benign: Represents legitimate but potentially ambiguous prompts.
- PINT: Evaluates particularly nuanced prompt injection, jailbreaks, and benign prompts that could be misidentified as malicious.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64a13b68b14ab77f9e3eb061/ygIo-Yo3NN7mDhZlLFvZb.png)

## Training Procedure

### Training Hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 64
- eval_batch_size: 32
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- bf16: True
- num_epochs: 2

### Training Results

| Training Loss | Epoch  | Step | Validation Loss | F1     | Accuracy |
|:-------------:|:------:|:----:|:---------------:|:------:|:--------:|
| 0.1519        | 0.1042 | 100  | 0.1354          | 0.9229 | 0.9534   |
| 0.068         | 0.2083 | 200  | 0.0553          | 0.9689 | 0.9797   |
| 0.0458        | 0.3125 | 300  | 0.0555          | 0.9758 | 0.9844   |
| 0.0389        | 0.4167 | 400  | 0.0442          | 0.9804 | 0.9874   |
| 0.04          | 0.5208 | 500  | 0.0323          | 0.9842 | 0.9897   |
| 0.0308        | 0.625  | 600  | 0.0357          | 0.9836 | 0.9894   |
| 0.0357        | 0.7292 | 700  | 0.0336          | 0.9861 | 0.9909   |
| 0.0306        | 0.8333 | 800  | 0.0299          | 0.9880 | 0.9921   |
| 0.0246        | 0.9375 | 900  | 0.0338          | 0.9846 | 0.9900   |
| 0.0195        | 1.0417 | 1000 | 0.0260          | 0.9881 | 0.9922   |
| 0.0124        | 1.1458 | 1100 | 0.0225          | 0.9887 | 0.9926   |
| 0.005         | 1.25   | 1200 | 0.0286          | 0.9874 | 0.9917   |
| 0.0075        | 1.3542 | 1300 | 0.0313          | 0.9897 | 0.9933   |
| 0.0065        | 1.4583 | 1400 | 0.0318          | 0.9892 | 0.9930   |
| 0.0093        | 1.5625 | 1500 | 0.0257          | 0.9903 | 0.9937   |
| 0.0099        | 1.6667 | 1600 | 0.0233          | 0.9889 | 0.9927   |
| 0.0054        | 1.7708 | 1700 | 0.0221          | 0.9905 | 0.9938   |
| 0.0077        | 1.875  | 1800 | 0.0222          | 0.9907 | 0.9939   |
| 0.0052        | 1.9792 | 1900 | 0.0225          | 0.9904 | 0.9937   |


### Framework Versions

- Transformers 4.48.3
- Pytorch 2.5.1+cu124
- Datasets 3.3.2
- Tokenizers 0.21.0
