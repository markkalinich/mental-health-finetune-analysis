---
license: apache-2.0
base_model: Qwen/Qwen3-VL-8B-Instruct
tags:
- vision
- multimodal
- safety
- guard-model
- icml-2026
pipeline_tag: image-text-to-text
---

# OmniVL-Guard-8B

<div align="center">

<!-- Keep this line empty for spacing -->

[![Paper](https://img.shields.io/badge/Paper-arXiv%3A2602.10687-B31B1B?logo=arxiv&logoColor=white&style=flat-square)](https://arxiv.org/abs/2602.10687)
[![Code](https://img.shields.io/badge/Code-GitHub-181717?logo=github&logoColor=white&style=flat-square)](https://github.com/shen8424/OmniVL-Guard)
[![Dataset](https://img.shields.io/badge/Dataset-FSFR-FF6F00?logo=huggingface&logoColor=white&style=flat-square)](https://huggingface.co/datasets/SJJ0854/FSFR)
[![Conference](https://img.shields.io/badge/Venue-ICML%202026-4B44CE?logo=academia&logoColor=white&style=flat-square)](https://icml.cc)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue?style=flat-square)](./)

</div>

A safety guard model for vision-language content moderation, accepted at **ICML 2026**. Fine-tuned from [Qwen/Qwen3-VL-8B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct).

## Usage

```python
from transformers import Qwen3_VLForConditionalGeneration, AutoProcessor

model = Qwen3_VLForConditionalGeneration.from_pretrained("SJJ0854/OmniVL-Guard-8B")
processor = AutoProcessor.from_pretrained("SJJ0854/OmniVL-Guard-8B")
```

## Training Data

Refined-SFT and RL datasets available at [SJJ0854/FSFR](https://huggingface.co/datasets/SJJ0854/FSFR).

## Citation

```bibtex
@inproceedings{omnivlguard2026,
  title={OmniVL-Guard: A Safety Guard for Vision-Language Models},
  booktitle={International Conference on Machine Learning (ICML)},
  year={2026}
}
```
