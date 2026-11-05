---
base_model:
- Qwen/Qwen3-8B-Base
tags:
- medical
library_name: transformers
pipeline_tag: text-generation
---

# MedSSR-Qwen3-8B-Base

This is the model for our ACL 2026 Findings paper, "[Eliciting Medical Reasoning with Knowledge-enhanced Data Synthesis: A Semi-Supervised Reinforcement Learning Approach](https://huggingface.co/papers/2604.11547)". `MedSSR-Qwen3-8B-Base` is a medical reasoning-focused LLM built from `Qwen/Qwen3-8B-Base`.

## Model Summary

- **Base model**: `Qwen/Qwen3-8B-Base`
- **Model name**: `MedSSR-Qwen3-8B-Base`
- **Training framework**: [verl](https://github.com/verl-project/verl)
- **Paper link**: [https://arxiv.org/pdf/2604.11547](https://huggingface.co/papers/2604.11547)
- **Github repo**: [https://github.com/tdlhl/MedSSR](https://github.com/tdlhl/MedSSR)
- **Hugging Face training dataset**: [tdlhl/MedSSR-Synthetic-43K](https://huggingface.co/datasets/tdlhl/MedSSR-Synthetic-43K)
- **Hugging Face test dataset**: [tdlhl/RareDis-Sub](https://huggingface.co/datasets/tdlhl/RareDis-Sub)

## Quick Start (Transformers)

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "tdlhl/MedSSR-Qwen3-8B-Base"

tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
)

messages = [
    {
        "role": "user",
        "content": (
            "A 67-year-old man develops crushing substernal chest pain for 40 minutes. "
            "ECG shows ST-segment elevation in leads II, III, and aVF. "
            "Which coronary artery is most likely occluded?
"
            "A. Left anterior descending artery
"
            "B. Left circumflex artery
"
            "C. Right coronary artery
"
            "D. Posterior descending artery"
        ),
    }
]

prompt = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=1024,
        temperature=0.6,
        top_p=0.95,
    )

new_tokens = outputs[0][inputs["input_ids"].shape[-1]:]
print(tokenizer.decode(new_tokens, skip_special_tokens=True))
```

## Quick Start (vLLM)

```python
from vllm import LLM, SamplingParams

llm = LLM(
    model="tdlhl/MedSSR-Qwen3-8B-Base",
    trust_remote_code=True,
)

sampling = SamplingParams(
    temperature=0.6,
    top_p=0.95,
    max_tokens=1024,
)

prompt = (
    "A 24-year-old woman presents with fatigue, weight gain, constipation, and cold intolerance. "
    "Which of the following laboratory findings is most consistent with primary hypothyroidism?
"
    "A. Low TSH, low free T4
"
    "B. High TSH, low free T4
"
    "C. High TSH, high free T4
"
    "D. Low TSH, high free T4"
)

outputs = llm.generate([prompt], sampling_params=sampling)
print(outputs[0].outputs[0].text)
```

## Suggested Decoding Setup

For evaluation settings similar to our paper, we follow the recommended setting of Qwen:

```text
temperature=0.6
top_p=0.95
top_k=20
max_tokens=2048
```

## Notes

- This model is intended for research use.
- The model may produce incorrect or unverifiable medical reasoning.
- Outputs should not be used as a substitute for professional medical judgment.
- For benchmark-style evaluation, please follow the released evaluation script in our repository.

## Citation

If you find our model useful, please cite our paper:

```bibtex
@article{li2025eliciting,
  title={Eliciting Medical Reasoning with Knowledge-enhanced Data Synthesis: A Semi-Supervised Reinforcement Learning Approach},
  author={Haolin Li, Shuyang Jiang, Ruipeng Zhang, Jiangchao Yao, Ya Zhang, Yanfeng Wang},
  journal={arXiv preprint arXiv:2604.11547},
  year={2026}
}
```