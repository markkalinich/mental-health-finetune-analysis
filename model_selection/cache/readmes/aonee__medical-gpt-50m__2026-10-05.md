---
license: mit
tags:
  - medical
  - gpt
  - autoresearch
  - causal-lm
  - from-scratch
language:
  - en
library_name: pytorch
pipeline_tag: text-generation
---

# Medical GPT-50M

A 50M-parameter medical language model trained from scratch on 2.9M medical Q&A examples using the [autoresearch](https://github.com/karpathy/autoresearch) methodology.

## Model Details

| Parameter | Value |
|-----------|-------|
| Parameters | 50.3M |
| Architecture | GPT (RoPE, RMS norm, sliding window, ReluSquared MLP) |
| Vocabulary | Medical BPE (8192 tokens) |
| Context length | 2048 tokens |
| Layers | 8 |
| Heads | 8 |
| Head dim | 128 |
| Window pattern | SSSL |
| Optimizer | MuonAdamW (Muon for matrices, AdamW for embeddings) |
| Validation BPB | 1.1217 |
| Training tokens | 37.0M |

## Training Data

Trained on 3 medical Q&A datasets (2.9M examples, 17.4GB JSONL):
- **OpenMed/Medical-Reasoning-SFT-Mega** (1.78M rows) — multi-domain medical reasoning with chain-of-thought
- **lingshu-medical-mllm/ReasonMed** (1.11M rows) — medical reasoning Q&A
- **FreedomIntelligence/medical-o1-reasoning-SFT** [en] (19.7K rows) — used as validation set

## Experiment Insights

This model was trained using the autoresearch autonomous experimentation loop. Key findings from ~25 experiments:

| Experiment | val_bpb | Insight |
|-----------|---------|---------|
| Baseline (batch=128, OOM) | - | L4 has 24GB, not H100's 80GB |
| batch=32 | 1.252 | First working baseline on L4 |
| batch=32 + mlr=0.06 + warmdown=0.3 | 1.160 | Higher matrix LR helps medical text |
| total_batch=2^16, batch=8 | 1.125 | **Key finding**: 4x more optimizer steps >> throughput |
| + unembedding_lr=0.008 | 1.123 | Small gain from discriminative LRs |
| + embedding_lr=1.2 | 1.115 | Medical vocabulary needs faster embedding adaptation |

**Key insight**: On time-budgeted training (5 min), smaller total batch size = more optimizer steps = dramatically better val_bpb. This is the single biggest lever.

## How to Use

This is a raw pretrained model with a custom architecture (not HuggingFace Transformers compatible). Load with PyTorch:

```python
import torch
import safetensors.torch
state_dict = safetensors.torch.load_file("model.safetensors")
# Architecture details in config.json
```

## Limitations

- **Not instruction-tuned** — this is a base pretrained model
- **5-minute training budget** — trained for research/exploration, not production
- **50M parameters** — small model, intended as foundation for embedding/classification experiments
- **Custom architecture** — not directly compatible with HuggingFace Transformers

## Citation

```
@misc{medical-gpt-50m,
  title={Medical GPT-50M: Autonomous Medical LM Research},
  author={Axone AI},
  year={2026},
  url={https://huggingface.co/axonee/medical-gpt-50m}
}
```
