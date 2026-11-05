---
license: llama3
language:
- en
- code
base_model: ajibawa-2023/Code-Llama-3-8B
tags:
- code
- safety
- alignment
- S&P2026
- EnchTable
pipeline_tag: text-generation
---

# EnchTable: Unified Safety Alignment Transfer (Code + Hybrid)

This repository contains the **Code-Llama-3-8B** model aligned using the **Hybrid (Attention + FFN)** intervention of the **EnchTable** framework.

This model is part of the research presented in the paper:  
**"EnchTable: Unified Safety Alignment Transfer in Fine-tuned Large Language Models"**, accepted at **IEEE S&P 2026**.

## Model Details

- **Name:** Code-Llama-3-8B (EnchTable-Hybrid)
- **Domain:** Code Generation / Programming
- **Method:** EnchTable (Attention + FFN)
- **Base Model:** Llama-3-8B fine-tuned on code datasets

**EnchTable** is a framework designed to transfer safety alignment capabilities. 

In this checkpoint, we utilize a **Hybrid strategy**, injecting safety vectors into **both Self-Attention and FFN layers**. This represents the most comprehensive alignment transfer, maximizing safety in code generation tasks.