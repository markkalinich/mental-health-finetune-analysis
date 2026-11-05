---
library_name: transformers
license: apache-2.0
base_model: Qwen/Qwen2.5-VL-7B-Instruct
datasets:
  - AIML-TUDA/LlavaGuard
language:
  - en
pipeline_tag: image-text-to-text
tags:
  - safety
  - guardrail
  - GRPO
  - reinforcement-learning
  - vision-language
  - content-moderation
  - policy-aware
  - CVPR2026
---

# SafeGuard-VL-RL

**SafeGuard-VL-RL** is a policy-aware visual safety guardrail model built on [Qwen2.5-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct), trained with Group Relative Policy Optimization (GRPO) for robust unsafe-image detection.

This model is part of our CVPR 2026 paper: *Towards Policy-Adaptive Image Guardrail: Benchmark and Method*.

## Key Features

- **Policy-aware safety judgment**: Unlike static classifiers, SafeGuard-VL-RL takes a natural language safety policy as input and makes context-sensitive decisions accordingly.
- **Robust instruction following**: Maintains general VQA capabilities while serving as a safety guardrail.
- **Cross-policy generalization**: Trained on one policy, generalizes to unseen policies with different category definitions.

## Model Description

SafeGuard-VL-RL is trained using **Stage-2 RL only** (without the Stage-1 SFT). It applies GRPO (from [DeepSeekMath](https://arxiv.org/abs/2402.03300)) on the [LlavaGuard](https://huggingface.co/datasets/AIML-TUDA/LlavaGuard) training set. For each image-policy pair, the ground truth safe/unsafe label serves as the reward signal, encouraging the model to reason about why a given image violates or complies with the policy.

| Detail | Value |
|---|---|
| **Base Model** | [Qwen2.5-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct) |
| **Training Method** | GRPO (Group Relative Policy Optimization) |
| **Training Data** | [AIML-TUDA/LlavaGuard](https://huggingface.co/datasets/AIML-TUDA/LlavaGuard) (train split) |

## Usage

```python
from transformers import Qwen2_5_VLForConditionalGeneration, AutoProcessor
from qwen_vl_utils import process_vision_info

model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
    "tyodd/SafeGuard-VL-RL",
    torch_dtype="auto",
    device_map="auto",
)
processor = AutoProcessor.from_pretrained("tyodd/SafeGuard-VL-RL")

# Example: Safety evaluation with a custom policy
policy = """
"""

messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": "path/to/image.jpg"},
            {"type": "text", "text": f"Based on the following safety policy, determine if this image is safe or unsafe.\n\nPolicy:\n{policy}\n\nProvide your reasoning and final judgment (Safe/Unsafe)."},
        ],
    }
]

text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
image_inputs, video_inputs = process_vision_info(messages)
inputs = processor(
    text=[text],
    images=image_inputs,
    videos=video_inputs,
    padding=True,
    return_tensors="pt",
).to(model.device)

generated_ids = model.generate(**inputs, max_new_tokens=512)
generated_ids_trimmed = [
    out_ids[len(in_ids):] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
]
output_text = processor.batch_decode(
    generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
)
print(output_text[0])
```

## Citation

```bibtex
@inproceedings{piao2026towards,
  title={Towards policy-adaptive image guardrail: Benchmark and method},
  author={Piao, Caiyong and Yan, Zhiyuan and Xu, Haoming and Zhao, Yunzhen and Lin, Kaiqing and Xu, Feiyang and Zhou, Shuigeng},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={16614--16623},
  year={2026}
}
```

## Disclaimer

This model is designed for safety research purposes. It was trained on data containing unsafe content categories and is intended to help identify potentially harmful visual content. The model's judgments are policy-dependent and should not be used as the sole arbiter of content safety in production systems without human oversight.
