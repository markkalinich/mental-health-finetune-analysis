---
license: llama3
language:
- en
base_model: ContactDoctor/Bio-Medical-Llama-3-8B
tags:
- medical
- safety
- alignment
- S&P2026
- EnchTable
pipeline_tag: text-generation
---

# EnchTable: Unified Safety Alignment Transfer (Bio-Medical + Hybrid)

This repository contains the **Bio-Medical Llama-3-8B** model aligned using the **Hybrid (Attention + FFN)** intervention of the **EnchTable** framework.

This model is part of the research presented in the paper:  
**"EnchTable: Unified Safety Alignment Transfer in Fine-tuned Large Language Models"**, accepted at **IEEE S&P 2026**.

## Model Details

- **Name:** Bio-Medical Llama-3-8B (EnchTable-Hybrid)
- **Domain:** Bio-Medical / Healthcare
- **Method:** EnchTable (Attention + FFN)
- **Base Model:** Llama-3-8B fine-tuned on medical datasets

**EnchTable** is a framework designed to transfer safety alignment capabilities. 

In this checkpoint, we utilize a **Hybrid strategy**, injecting safety vectors into **both Self-Attention and FFN layers**. This combination aims to achieve the optimal balance between robust safety alignment and downstream medical performance.