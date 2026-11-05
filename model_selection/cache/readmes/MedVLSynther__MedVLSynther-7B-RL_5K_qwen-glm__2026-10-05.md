---
license: apache-2.0
datasets:
- MedVLSynther/MedSynVQA-5K-qwen-glm
language:
- en
base_model:
- Qwen/Qwen2.5-VL-7B-Instruct
---

# MedVLSynther-7B-RL_5K_qwen-glm

Code: https://github.com/UCSC-VLAA/MedVLSynther
Project Page: https://ucsc-vlaa.github.io/MedVLSynther/

## Model Description

MedVLSynther-7B-RL_5K_qwen-glm is a 7B parameter medical vision-language model based on Qwen2.5-VL. 
This model has been trained using reinforcement learning on MedSynVQA-1K dataset.

## Model Details

- **Base Model**: Qwen/Qwen2.5-VL-7B-Instruct
- **Model Size**: 7B parameters
- **Training Method**: Reinforcement Learning
- **Training Data**: MedSynVQA-5K-qwen-glm dataset

## Usage

Check here for demo images: https://github.com/UCSC-VLAA/MedVLSynther?tab=readme-ov-file#-quick-start

```python
from transformers import Qwen2_5_VLForConditionalGeneration, AutoTokenizer, AutoProcessor
from qwen_vl_utils import process_vision_info
import torch

# Load the model
model_name="MedVLSynther/MedVLSynther-7B-RL_5K_qwen-glm"
model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)
processor = AutoProcessor.from_pretrained(model_name)

# Example usage
messages_1 = [
    {
        "role": "system",
        "content": "You will solve a problem/request. You should provide your thoughts within <think> </think> tags before providing the answer.\nWrite your final answer within <answer> </answer> tags.",
    },
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "image": "assets/7bMMMU.png",
            },
            {"type": "text", "text": "This line of of myelinated axons in layer IV of visual cortex represents the axons of cells in the Choices: (A) Superior colliculus. (B) Lateral geniculate.(C) Retina. (D) Medial geniculate."},
        ],
    }
]

messages_2 = [
    {
        "role": "system",
        "content": "You will solve a problem/request. You should provide your thoughts within <think> </think> tags before providing the answer.\nWrite your final answer within <answer> </answer> tags.",
    },
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "image": "assets/7bslake.png",
            },
            {"type": "text", "text": "Does the picture contain kidney? Choices: (A) Yes (B) No"},
        ],
    }
]

# Preparation for inference
messages = messages_2

text = processor.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True
)
image_inputs, video_inputs = process_vision_info(messages)
inputs = processor(
    text=[text],
    images=image_inputs,
    videos=video_inputs,
    padding=True,
    return_tensors="pt",
)
inputs = inputs.to("cuda")

# Inference
generated_ids = model.generate(**inputs, max_new_tokens=2048, temperature=0.6, top_p=0.95, do_sample=True)
generated_ids_trimmed = [
    out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
]
output_text = processor.batch_decode(
    generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
)
print(output_text)
```

## Citation

```bibtex
@article{MedVLSynther,
  title={MedVLSynther: Synthesizing High-Quality Visual Question Answering from Medical Documents with Generator-Verifier LMMs},
  author={Huang, Xiaoke and Wang, Ningsen and Liu, Hui and Tang, Xianfeng and Zhou, Yuyin},
  journal={arXiv preprint arXiv:2510.25867},
  year={2025}
}
@article{MedVLThinker,
  title={Medvlthinker: Simple baselines for multimodal medical reasoning},
  author={Huang, Xiaoke and Wu, Juncheng and Liu, Hui and Tang, Xianfeng and Zhou, Yuyin},
  journal={arXiv preprint arXiv:2508.02669},
  year={2025}
}
```

## License

This model is released under the Apache 2.0 license.