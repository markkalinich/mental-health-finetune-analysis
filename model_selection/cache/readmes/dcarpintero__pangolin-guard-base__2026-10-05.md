---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- ai-safety
- safeguards
- guardrails
metrics:
- f1
- accuracy
model-index:
- name: pangolin-guard-base
  results: []
---

# PangolinGuard-Base

LLM applications face critical security challenges in form of prompt injections and jailbreaks. This can result in models leaking sensitive data or deviating from their intended behavior. Existing safeguard models are not fully open and have limited context windows (e.g., only 512 tokens in LlamaGuard).

**Pangolin Guard** is a ModernBERT (Base), lightweight model that discriminates malicious prompts (i.e. prompt injection attacks). 

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


## Inference

```python
from transformers import pipeline

classifier = pipeline("text-classification", "dcarpintero/pangolin-guard-base")
text = "your input text"
output = classifier(text)
```

## Training Procedure

### Training Hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 64
- eval_batch_size: 32
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 2

### Training Results

| Training Loss | Epoch  | Step | Validation Loss | F1     | Accuracy |
|:-------------:|:------:|:----:|:---------------:|:------:|:--------:|
| 0.1622        | 0.1042 | 100  | 0.0755          | 0.9604 | 0.9741   |
| 0.0694        | 0.2083 | 200  | 0.0525          | 0.9735 | 0.9828   |
| 0.0552        | 0.3125 | 300  | 0.0857          | 0.9696 | 0.9810   |
| 0.0535        | 0.4167 | 400  | 0.0345          | 0.9825 | 0.9889   |
| 0.0371        | 0.5208 | 500  | 0.0343          | 0.9821 | 0.9887   |
| 0.0402        | 0.625  | 600  | 0.0344          | 0.9836 | 0.9894   |
| 0.037         | 0.7292 | 700  | 0.0282          | 0.9869 | 0.9917   |
| 0.0265        | 0.8333 | 800  | 0.0229          | 0.9895 | 0.9933   |
| 0.0285        | 0.9375 | 900  | 0.0240          | 0.9885 | 0.9926   |
| 0.0191        | 1.0417 | 1000 | 0.0220          | 0.9908 | 0.9941   |
| 0.0134        | 1.1458 | 1100 | 0.0228          | 0.9911 | 0.9943   |
| 0.0124        | 1.25   | 1200 | 0.0230          | 0.9898 | 0.9935   |
| 0.0136        | 1.3542 | 1300 | 0.0212          | 0.9910 | 0.9943   |
| 0.0088        | 1.4583 | 1400 | 0.0229          | 0.9911 | 0.9943   |
| 0.0115        | 1.5625 | 1500 | 0.0211          | 0.9922 | 0.9950   |
| 0.0058        | 1.6667 | 1600 | 0.0233          | 0.9920 | 0.9949   |
| 0.0119        | 1.7708 | 1700 | 0.0199          | 0.9916 | 0.9946   |
| 0.0072        | 1.875  | 1800 | 0.0206          | 0.9925 | 0.9952   |
| 0.007         | 1.9792 | 1900 | 0.0196          | 0.9923 | 0.9950   |


### Framework versions

- Transformers 4.50.0
- Pytorch 2.6.0+cu124
- Datasets 3.4.1
- Tokenizers 0.21.1