---
base_model: meta-llama/Llama-3.2-11B-Vision-Instruct
tags:
- vision
- meta
- llama
- medical
- clinical
- healthcare
license: apache-2.0
language:
- en
- fr
pipeline_tag: image-text-to-text
datasets:
- eltorio/ROCO-radiology
---

# MedicalLlama3.2-11B-IT 
## Model Description
This is a fine-tuned version of [meta-llama/Llama-3.2-11B-Vision-Instruct](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct) on a multimodal dataset consisting of radiological images and associated medical concepts and captions extracted from the PMC Open Access Subset.
- **License:** apache-2.0
- **Fine tuned by :** Cannae-AI
- **Base model :** meta-llama/Llama-3.2-11B-Vision-Instruct