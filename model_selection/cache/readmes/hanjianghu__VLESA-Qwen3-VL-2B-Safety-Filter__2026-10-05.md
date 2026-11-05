---
license: apache-2.0
language:
- en
base_model:
- Qwen/Qwen3-VL-2B-Instruct
tags:
- safety
- egocentric-video
- vision-language-model
- reinforcement-learning
- grpo
- embodied-ai
- human-activity-monitoring
datasets:
- hanjianghu/EgoSafety
pipeline_tag: image-text-to-text
---

# VLESA Safety Filter — Qwen3-VL-2B (GRPO fine-tuned)

This is the VLESA safety filter checkpoint from the paper:

**VLESA: Vision-Language Embodied Safety Agent for Human Activity Monitoring**  
Hanjiang Hu, Yiyuan Pan, Jiaxing Li, Xusheng Luo, Alexander Robey, Na Li, Yebin Wang, Changliu Liu  
[arXiv:2606.03954](https://arxiv.org/abs/2606.03954) | [GitHub](https://github.com/HanjiangHu/VLESA)

## Model Description

This model is a Qwen3-VL-2B checkpoint fine-tuned via Group Relative Policy Optimization (GRPO) on the [EgoSafety](https://huggingface.co/datasets/hanjianghu/EgoSafety) dataset. It serves as the **safety filter** component of the VLESA pipeline: given egocentric video frames (pre-action, point-of-no-return, and post-action), it predicts whether a human action is **safe** or **unsafe** and provides a natural-language rationale.

## Training Details

- **Base model**: Qwen3-VL-2B-Instruct
- **Training method**: GRPO (Group Relative Policy Optimization) via [EasyR1](https://github.com/hiyouga/easyr1)
- **Training data**: [EgoSafety](https://huggingface.co/datasets/hanjianghu/EgoSafety) — 9,596 train / 1,202 validation / 1,183 test samples derived from Ego4D
- **Checkpoint**: global_step_148

## Usage

```python
from transformers import Qwen3VLForConditionalGeneration, AutoProcessor
from qwen_vl_utils import process_vision_info

model = Qwen3VLForConditionalGeneration.from_pretrained(
    "hanjianghu/VLESA-Qwen3-VL-2B-Safety-Filter",
    torch_dtype="auto",
    device_map="auto",
)
processor = AutoProcessor.from_pretrained("hanjianghu/VLESA-Qwen3-VL-2B-Safety-Filter")
```

For full pipeline usage with the VLESA agent, see the [GitHub repository](https://github.com/HanjiangHu/VLESA).

## Citation

```bibtex
@article{hu2026vlesa,
  title={VLESA: Vision-Language Embodied Safety Agent for Human Activity Monitoring},
  author={Hu, Hanjiang and Pan, Yiyuan and Li, Jiaxing and Luo, Xusheng and Robey, Alexander and Li, Na and Wang, Yebin and Liu, Changliu},
  journal={arXiv preprint arXiv:2606.03954},
  year={2026}
}
```
