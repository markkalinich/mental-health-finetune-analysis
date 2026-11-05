---
language:
- en
library_name: transformers
pipeline_tag: image-text-to-text
tags:
- vision-language
- multimodal
- safety
- robotics
- embodied-ai
- qwen3-vl
base_model:
- Qwen/Qwen3-VL-8B-Thinking
---

# HomeGuard-8B

HomeGuard-8B is an 8B-parameter vision-language safeguard model for **identifying contextual risk in household tasks**. It is introduced in the paper [HomeGuard: VLM-based Embodied Safeguard for Identifying Contextual Risk in Household Task](https://arxiv.org/abs/2603.14367) and is designed to help embodied agents detect subtle, implicit hazards that arise from environmental context rather than explicit malicious intent.

This checkpoint corresponds to the **8B step-RFT model** used in the HomeGuard framework. It is built on top of **Qwen3-VL-8B-Thinking** and further optimized for grounded household risk reasoning with reinforcement fine-tuning.

## Model Summary

HomeGuard focuses on scenarios where a seemingly benign instruction becomes unsafe because of object attributes, spatial relations, or latent environmental conditions. 

Compared with generic VLMs, HomeGuard is specialized for:

- contextual risk identification
- grounded multimodal safety reasoning
- safety-aware support for downstream planning and trajectory generation

## Training Recipe

This model is derived from **Qwen3-VL-8B-Thinking** and trained within the HomeGuard pipeline.

Training setup summarized from the released training configuration:

- Base model: `Qwen/Qwen3-VL-8B-Thinking`
- Training stage: step-level RFT + GRPO-style optimization in the HomeGuard pipeline
- Training data: HomeSafe

## Intended Use

HomeGuard-8B is intended for research and development on:

- safety assessment for embodied agents
- contextual risk identification in household tasks
- grounded VLM reasoning with visual context
- safe planning and downstream robotics pipelines

## Usage

This repository contains the inference-ready model weights and tokenizer assets. A typical Transformers loading pattern is:

```python
from transformers import AutoProcessor, Qwen3VLForConditionalGeneration

model_id = "Ursulalala/HomeGuard-8B"
processor = AutoProcessor.from_pretrained(model_id)
model = Qwen3VLForConditionalGeneration.from_pretrained(
    model_id,
    torch_dtype="auto",
    device_map="auto",
)
```

For full prompting, evaluation, and application examples, please refer to the HomeGuard project repository.

## Resources

- Paper: [HomeGuard: VLM-based Embodied Safeguard for Identifying Contextual Risk in Household Task](https://arxiv.org/abs/2603.14367)
- Code: [AI45Lab/HomeGuard](https://github.com/AI45Lab/HomeGuard)
- Dataset: [Ursulalala/HomeSafe](https://huggingface.co/datasets/Ursulalala/HomeSafe)
- Base model: [Qwen/Qwen3-VL-8B-Thinking](https://huggingface.co/Qwen/Qwen3-VL-8B-Thinking)

## Citation

If you use this model, please cite the HomeGuard paper:

```bibtex
@article{lu2026homeguard,
  title={HomeGuard: VLM-based Embodied Safeguard for Identifying Contextual Risk in Household Task},
  author={Lu, Xiaoya and Zhou, Yijin and Chen, Zeren and Wang, Ruocheng and Sima, Bingrui and Zhou, Enshen and Sheng, Lu and Liu, Dongrui and Shao, Jing},
  journal={arXiv preprint arXiv:2603.14367},
  year={2026}
}
```
