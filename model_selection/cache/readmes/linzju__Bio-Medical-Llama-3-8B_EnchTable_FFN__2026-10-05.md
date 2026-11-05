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

# EnchTable: Unified Safety Alignment Transfer (Bio-Medical + FFN)

This repository contains the **Bio-Medical Llama-3-8B** model aligned using the **FFN-based** intervention of the **EnchTable** framework.

This model is part of the research presented in the paper:  
**"EnchTable: Unified Safety Alignment Transfer in Fine-tuned Large Language Models"**, accepted at **IEEE S&P 2026**.

## Model Details

- **Name:** Bio-Medical Llama-3-8B (EnchTable-FFN)
- **Domain:** Bio-Medical / Healthcare
- **Method:** EnchTable (Feed-Forward Networks)
- **Base Model:** Llama-3-8B fine-tuned on medical datasets


**EnchTable** is a framework designed to transfer safety alignment capabilities to specialized models. 

In this checkpoint, we apply **safety vectors specifically to the Feed-Forward Network (FFN) layers**. This approach mitigates safety risks effectively while preserving the factual knowledge required for biomedical tasks.