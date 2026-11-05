---
license: apache-2.0
tags:
- qlora
- instruction-tuning
- customized
---

# Qwen 2.5 7B (Medical & Legal Domain)

This is a specialized domain-expert model based on Qwen2.5-7B, rigorously fine-tuned on high-quality Medical and Legal datasets. It is designed to navigate complex terminology, assist with specialized professional text, and provide highly contextual reasoning within the healthcare and legal fields.

## Training Architecture & Source Code

The exact code, hyperparameters, scripts, and complete logic used to train and produce this model can be found in my open-source repository:
**[👉 QLoRA-Experiments on GitHub](https://github.com/igna-s/QLoRA-Experiments)**

### Technical Details
- **Method:** QLoRA (Quantized Low-Rank Adaptation)
- **Frameworks:** `transformers`, `peft`, `trl`, `bitsandbytes`

If you are interested in how this model was configured, the datasets used, or want to replicate similar domain-expert experiments, please check the [QLoRA-Experiments repository](https://github.com/igna-s/QLoRA-Experiments).
