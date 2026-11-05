---
language:
- en
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
tags:
- Domain-Certification
- Jailbreaking
- Adversarial-Attack
- Guardrail
datasets:
- qiaojin/PubMedQA
---

# Shh, don't say that! Domain Certification in LLMs

[![arXiv](https://img.shields.io/badge/Project-Webpage-db6fc0.svg)](https://cemde.github.io/Domain-Certification-Website/)
[![arXiv](https://img.shields.io/badge/arXiv-2502.19320-b31b1b.svg)](https://arxiv.org/abs/2502.19320)
[![ICLR 2025](https://img.shields.io/badge/ICLR-2025-7ACA2C.svg)](https://iclr.cc/virtual/2025/poster/30364)
[![Huggingface](https://img.shields.io/badge/Github-Repository-black.svg)](https://github.com/cemde/Domain-Certification)

**Collection:** https://huggingface.co/collections/cemde/domain-certification-67ba4fb663f8d1348c3c2263

**Certify you Large Language Model (LLM)!**

With the code in this repository you can reproduce the workflows we use in our ICLR 2025 paper to achieve Domain Certification using our VALID algorithm.

We provide the guide models for our Medical Question Answering experiments.


| Model | Description |
| - | - |
| [cemde/Domain-Certification-MedQA-Guide-Base](https://huggingface.co/cemde/Domain-Certification-MedQA-Guide-Base) | This is the base model trained on the ground-truth responses. |
| [cemde/Domain-Certification-MedQA-Guide-Finetuned](https://huggingface.co/cemde/Domain-Certification-MedQA-Guide-Finetuned) | This is the model trained on responses from Llama-3-8B. |

## Citation

```
@inproceedings{
emde2025shh,
title={Shh, don't say that! Domain Certification in {LLM}s},
author={Cornelius Emde and Alasdair Paren and Preetham Arvind and Maxime Guillaume Kayser and Tom Rainforth and Bernard Ghanem and Thomas Lukasiewicz and Philip Torr and Adel Bibi},
booktitle={The Thirteenth International Conference on Learning Representations},
year={2025},
url={https://arxiv.org/abs/2502.19320}
}
```
