---
license: apache-2.0
tags:
- qlora
- instruction-tuning
- customized
---

# Qwen 2.5 14B (Medical & Legal Domain)

A larger, higher-capacity domain expert model based on Qwen2.5-14B. Fine-tuned on extensive Medical and Legal datasets, this model takes advantage of its larger parameter count to offer vastly improved nuance, recall, and logical consistency for demanding professional use cases in healthcare and law.

## Training Architecture & Source Code

The exact code, hyperparameters, scripts, and complete logic used to train and produce this model can be found in my open-source repository:
**[👉 QLoRA-Experiments on GitHub](https://github.com/igna-s/QLoRA-Experiments)**

### Technical Details
- **Method:** QLoRA (Quantized Low-Rank Adaptation)
- **Frameworks:** 	ransformers, peft, 	rl, itsandbytes

If you are interested in how this model was configured, the datasets used, or want to replicate similar domain-expert experiments, please check the [QLoRA-Experiments repository](https://github.com/igna-s/QLoRA-Experiments).
