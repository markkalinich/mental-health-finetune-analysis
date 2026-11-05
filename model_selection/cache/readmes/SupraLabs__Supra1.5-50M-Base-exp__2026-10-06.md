---
license: apache-2.0
language:
- en
pipeline_tag: text-generation
library_name: transformers
tags:
- supra
- supra-1.5
- llama
- 50m
- base
- continued-pretraining
- long-context
- 5k-context
- Supra
- Supra-50M
---

<h1 align="center">Supra1.5-50M Base</h1>

<p align="center">
  Continued Pretraining • 50M Parameters • 5K Context
</p>

![Supra-1.5-Base-EXP](https://cdn-uploads.huggingface.co/production/uploads/68a5d0966d33a07f8aad2e51/Lh7KcQs60Ht9iray8WFbp.png)

Supra-1.5-50M-Base-exp is a continued-pretrained 50M parameter Llama-style base
model derived from `SupraLabs/Supra-50M-Base`. The target update expands the
usable context window from 1,024 tokens to 5,120 tokens using RoPE scaling and
full-weight continued pretraining.



## Architecture

The model keeps the original Supra-50M architecture and tokenizer:

| Specification | Value |
|--------------|--------|
| Architecture | `LlamaForCausalLM` |
| Parameters | ~50M |
| Vocabulary Size | 32,000 |
| Hidden Size | 512 |
| Layers | 12 |
| Attention Heads | 8 |
| KV Heads | 4 |
| Context Length | 5,120 tokens |
| Tokenizer | Original Supra byte-level BPE tokenizer |

## Continued Pretraining Objective

This is CPT, not instruction fine-tuning. Training uses packed raw text with
standard causal language-modeling loss:

- `labels = input_ids`
- all non-pad tokens are trained
- no response-only masking
- no system/user/assistant masking
- no LoRA adapters in the default run

## Data Mix

The current local training mix prepared for this run is:

- 3,000,000,062 CPT tokens
  - 30% Tool Calling
  - 30% ChatML Conversations
  - 25% Factual Text (articles, essays, blogs)
  - 15% Math & Logic Questions


### Intended Use
Supervised Fine-Tuning (SFT) and Reinforcement Learning

---

*Credit goes to @QyrouNnet-AI*