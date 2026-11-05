---
license: llama3
language:
- en
base_model: ajibawa-2023/Code-Llama-3-8B
tags:
- safety
- alignment
- security
- S&P2026
- EnchTable
pipeline_tag: text-generation
---

# EnchTable: Unified Safety Alignment Transfer in Fine-tuned LLMs

This repository contains the **Code-Llama-3-8B** model aligned using the **FFN (Feed-Forward Network)** variant of the **EnchTable** framework.

This model is part of the research presented in the paper:  
**"EnchTable: Unified Safety Alignment Transfer in Fine-tuned Large Language Models"**, accepted at **IEEE S&P 2026**.

## Model Details

- **Name:** Code-Llama-3-8B (EnchTable-FFN)
- **Base Model:** Llama-3-8B (Fine-tuned for Code)
- **Method:** EnchTable (FFN Module)
- **Primary Use Case:** Safety Alignment Transfer / Secure Code Generation

**EnchTable** is a novel framework designed to transfer safety alignment capabilities from a safe source model to various fine-tuned target models (e.g., Domain-Specific LLMs) without compromising their downstream performance. 

This specific checkpoint represents the **FFN-based intervention**, where safety vectors are calculated and merged specifically into the Feed-Forward Network layers of the model to mitigate harmful outputs while preserving code generation capabilities.