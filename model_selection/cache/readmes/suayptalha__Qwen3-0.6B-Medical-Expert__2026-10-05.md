---
license: apache-2.0
tags:
- unsloth
- trl
- sft
- medical
- reasoning
datasets:
- FreedomIntelligence/medical-o1-reasoning-SFT
language:
- en
base_model:
- Qwen/Qwen3-0.6B
pipeline_tag: text-generation
library_name: transformers
---

# Qwen3-0.6B-Medical-Expert

This project performs full fine-tuning on the **Qwen3-0.6B** language model to enhance its **medical reasoning** and **clinical understanding** capabilities. Training was conducted on the `FreedomIntelligence/medical-o1-reasoning-SFT` dataset using bfloat16 (bf16) precision for efficient optimization.

## Training Procedure

1. **Dataset Preparation**

   * The `FreedomIntelligence/medical-o1-reasoning-SFT` dataset was used.
   * Each example consists of medically relevant instructions or questions paired with detailed, step-by-step clinical reasoning responses.
   * Prompts were structured to encourage safe, factual, and coherent medical reasoning chains.

2. **Model Loading and Configuration**

   * Qwen3 base model weights were loaded via the `unsloth` library in bf16 precision.
   * All model layers were fully updated (`full_finetuning=True`) to effectively adapt the model to medical reasoning and decision-making tasks.

3. **Supervised Fine-Tuning**

   * Fine-tuning was conducted using the Hugging Face TRL library with the Supervised Fine-Tuning (SFT) approach.
   * The model was trained to follow clinical instructions, interpret symptoms, and generate reasoned diagnoses or treatment suggestions.

## Purpose and Outcome

* The model’s ability to interpret medical instructions and generate step-by-step clinical reasoning has been significantly enhanced.
* It produces responses that combine factual accuracy with transparent reasoning, making it useful in educational and assistive medical AI contexts.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](./LICENSE) file for details.

## Support

<a href="https://www.buymeacoffee.com/suayptalha" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>