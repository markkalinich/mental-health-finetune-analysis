---
license: llama3.2
language:
- en
base_model:
- meta-llama/Llama-3.2-3B-Instruct
pipeline_tag: text-generation
---

# LLaMA-3.2-3B-Instruct Medical Full

**Built with Llama**

Full fine-tuned LLaMA-3.2-3B-Instruct on medical instruction datasets to improve medical quantitative reasoning.

## Model Details

- **Base model:** meta-llama/Llama-3.2-3B-Instruct
- **Developed by:** Caleb King
- **Type:** Text generation / Instruction fine-tuned language model
- **License:** llama3.2
- **Language:** English

## Training

- **Dataset:** MedInstruct (combined from BioInstruct and AlpaCare-MedInstruct-52k)
- **Method:** Full instruction tuning
- **Framework:** PEFT 0.18.1

## Repository

https://github.com/CalebKingPortfolio/MQR-LLM-Thesis

## License

Llama 3.2 is licensed under the Llama 3.2 Community License, Copyright © Meta Platforms, Inc. All Rights Reserved.