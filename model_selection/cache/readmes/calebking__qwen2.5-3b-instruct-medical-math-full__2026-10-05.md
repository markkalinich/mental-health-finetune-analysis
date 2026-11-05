---
license: other
license_name: qwen-research
license_link: LICENSE
language:
- en
base_model:
- Qwen/Qwen2.5-3B-Instruct
pipeline_tag: text-generation
---

# Qwen2.5-3B-Instruct Medical + Math Full

**Built with Qwen**

Full fine-tuned Qwen2.5-3B-Instruct on medical instruction datasets plus 15% MQR data from MedCalc-Bench-v1.0 to improve medical quantitative reasoning.

## Model Details

- **Base model:** Qwen/Qwen2.5-3B-Instruct
- **Developed by:** Caleb King
- **Type:** Text generation / Instruction fine-tuned language model
- **License:** qwen-research
- **Language:** English

## Training

- **Dataset:** Med-MathInstruct (MedInstruct combined from BioInstruct and AlpaCare-MedInstruct-52k, plus MQR data from MedCalc-Bench-v1.0)
- **Method:** Full instruction tuning
- **Framework:** PEFT 0.18.1

## Repository

https://github.com/CalebKingPortfolio/MQR-LLM-Thesis

## License

Qwen is licensed under the Qwen RESEARCH LICENSE AGREEMENT, Copyright (c) Alibaba Cloud. All Rights Reserved.