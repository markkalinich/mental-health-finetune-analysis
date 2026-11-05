---
license: other
language:
- en
base_model:
- tiiuae/Falcon3-7B-Instruct
pipeline_tag: text-generation
tags:
- phi4
- phi3
- phi
- phi-moe
- moe
- llama
- 4bit
---
# Phi4 MoE 2x14B Instruct

Mixture of Experts of Phi4 14B-IT & 14B-IT.

- 14.2B parameters (4bit quant with bitsandbytes)
- BF16-U8 (Dynamic Quants by Unsloth using bnb-4bit)
- Phi4 (Phi3, Llama)
- Instruct

## Model Summary 

|                         |                                                                               |     
|-------------------------|-------------------------------------------------------------------------------|
| **Developers**          | Microsoft Research                                                            |
| **Description**         | `phi-4` is a state-of-the-art open model built upon a blend of synthetic datasets, data from filtered public domain websites, and acquired academic books and Q&A datasets. The goal of this approach was to ensure that small capable models were trained with data focused on high quality and advanced reasoning.<br><br>`phi-4` underwent a rigorous enhancement and alignment process, incorporating both supervised fine-tuning and direct preference optimization to ensure precise instruction adherence and robust safety measures                |
| **Architecture**        | 14B parameters, dense decoder-only Transformer model                          |
| **Inputs**              | Text, best suited for prompts in the chat format                              |
| **Context length**      | 16K tokens                                                                    |
| **GPUs**                | 1920 H100-80G                                                                 |
| **Training time**       | 21 days                                                                       |
| **Training data**       | 9.8T tokens                                                                   |
| **Outputs**             | Generated text in response to input                                           |
| **Dates**               | October 2024 – November 2024                                                  |
| **Status**              | Static model trained on an offline dataset with cutoff dates of June 2024 and earlier for publicly available data                                                                               |
| **Release date**        | December 12, 2024                                                             |
| **License**             | MIT                                                                         |