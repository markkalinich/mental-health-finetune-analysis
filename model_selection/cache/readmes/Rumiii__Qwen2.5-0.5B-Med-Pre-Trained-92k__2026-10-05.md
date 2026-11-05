---
library_name: transformers
language:
- en
license: apache-2.0
base_model: Qwen/Qwen2.5-0.5B
tags:
- transformers
- medical
- biomedical
- continued-pretraining
- qwen2.5
- pubmed
- causal-lm
---

![Screenshot 2026-09-06 at 6.39.42 PM](https://cdn-uploads.huggingface.co/production/uploads/66e00ba55e4fd4bfead4a97c/zLtpRZZsdiLoDtxTGN36C.png)

# Qwen2.5-0.5B-Med-Pre-Trained-92k

A continued pre-trained (CPT) version of [Qwen/Qwen2.5-0.5B](https://huggingface.co/Qwen/Qwen2.5-0.5B) on 92,000 English PubMed biomedical abstracts.



## Training Details

| Property | Value |
|---|---|
| Base model | Qwen/Qwen2.5-0.5B |
| Training type | Full-parameter Continued Pre-Training (CPT) |
| Dataset | VietAI/vi_pubmed (92k English abstracts) |
| Tokens trained on | ~23.6 million |
| Block size | 256 tokens |
| Training objective | Causal Language Modeling (CLM) |
| Optimizer | AdamW 8-bit (bitsandbytes) |
| Learning rate | 2e-5 (cosine schedule) |
| Hardware | Kaggle Tesla T4 (15.6GB VRAM) |
| Training time | ~3h 45m |
| Starting loss | 2.581 |
| Final loss | ~2.48 |
| Precision | fp32 master weights + AMP fp16 |

## What is this model?

This is a **base model** — not an instruction-tuned or chat model. It is intended as a domain-adapted foundation for further fine-tuning on medical instruction datasets.

All 494M parameters were updated during training (no LoRA, no frozen layers). The model has been adapted toward biomedical vocabulary, PubMed abstract structure, and medical terminology through full-parameter CLM training.

## Intended Use

- Base model for downstream medical SFT
- Research into biomedical domain adaptation
- Starting point for medical reasoning models

## Not Intended For

- Direct conversational use (no instruction tuning)
- Clinical decision making
- Patient-facing applications
