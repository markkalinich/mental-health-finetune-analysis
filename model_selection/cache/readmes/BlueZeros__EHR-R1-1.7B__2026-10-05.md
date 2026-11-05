---
license: cc-by-nc-4.0
pipeline_tag: text-generation
library_name: transformers
tags:
- medical
- healthcare
- ehr
- reasoning
- qwen
language:
- en
base_model:
- Qwen/Qwen3-1.7B
---

# EHR-R1: A Reasoning-Enhanced Foundational Language Model for Electronic Health Record Analysis

This repository contains the **EHR-R1-1.7B** model, part of the **EHR-R1** series, as presented in the paper [EHR-R1: A Reasoning-Enhanced Foundational Language Model for Electronic Health Record Analysis](https://huggingface.co/papers/2510.25628).

**EHR-R1** is a family of reasoning-enhanced Large Language Models (LLMs) specifically tailored for Electronic Health Record (EHR) analysis. It is developed based on **EHR-Ins**, a large-scale, comprehensive EHR reasoning instruction dataset, and is trained through a multi-stage paradigm including domain adaptation, reasoning enhancement, and reinforcement learning. This approach systematically acquires domain knowledge and diverse reasoning capabilities, enabling accurate and robust EHR analysis. The project also introduces **EHR-Bench**, a new benchmark curated from MIMIC-IV for comprehensive assessment across 42 distinct EHR tasks.

*   **Paper**: [https://huggingface.co/papers/2510.25628](https://huggingface.co/papers/2510.25628)
*   **GitHub Repository**: [https://github.com/MAGIC-AI4Med/EHR-R1](https://github.com/MAGIC-AI4Med/EHR-R1)

<p align="center">
  <img src="https://github.com/MAGIC-AI4Med/EHR-R1/raw/main/assets/teaser.png" alt="EHR-R1 Teaser Image" width="800">
</p>

## 💡 Key Highlights
*   We open-source a large-scale instruction dataset [**EHR-Ins**](https://huggingface.co/datasets/BlueZeros/EHR-Ins-Reasoning), including 3.5M non-reasoning data and 300k reasoning data.
*   We open-source a comprehensive benchmark [**EHR-Bench**](https://huggingface.co/datasets/BlueZeros/EHR-Bench), which covers 42 distinct EHR analysis tasks.
*   We open-source EHR reasoning-enhanced LLMs **EHR-R1**, including [**EHR-R1-1.7B**](https://huggingface.co/BlueZeros/EHR-R1-1.7B), [**EHR-R1-8B**](https://huggingface.co/BlueZeros/EHR-R1-8B), and [**EHR-R1-72B**](https://huggingface.co/BlueZeros/EHR-R1-72B).
*   We open-source the "thinking-graph" pipeline, which can synthesize reasoning chains for EHR analysis tasks according to the relation of EHR entities.

## ⚡ Directly Use

### EHR Input Format
For any EHR data, keep the EHR input with markdown format as below:
*   For the event with single record:
```
## Evant Name [Event Time (YYYY-MM-DD HH:MM:SS)]
- ItemKey_1: ItemValue_1
- ItemKey_2: ItemValue_2
- ItemKey_3: ItemValue_3
```
*   For the event with multiple records (like labevents):
```
## Evant Name [Event Time (YYYY-MM-DD HH:MM:SS)]
 |  ItemKey_1  |  ItemKey_2  |  ItemKey_3  |
 |  ---------  |  ---------  |  ---------  |
 | ItemValue_1 | ItemValue_2 | ItemValue_3 |
 | ItemValue_1 | ItemValue_2 | ItemValue_3 |
 | ItemValue_1 | ItemValue_2 | ItemValue_3 |
```

### Models Inference with Transformers
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "BlueZeros/EHR-R1-1.7B" # This specific EHR-R1-1.7B model
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

ehr_input = "{YOUR FOMATTED EHR INPUT}"
instruction = "{YOUR TASK INSTRUCTION}"
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": ehr_input + "\n" + instruction}
]

# For EHR-R1-1.7B & EHR-R1-8B, control the reasoning mode by setting enable_thinking
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=False,
).to(model.device)
# For EHR-R1-72B, you can manually add `<think>\n\n</think>` at the end of the model_inputs to close the reasoning modes.
text += "<think>\n\n</think>"

model_inputs = tokenizer([text], return_tensors="pt").to(model.device)
generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=2048,
    temperature=0.0
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]
response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(response)
```

## 📖 Citation
If you find our work helpful or inspiring, please feel free to cite it:
```bib
@article{liao2025ehrr1,
  title={{EHR-R1: A Reasoning-Enhanced Foundational Language Model for Electronic Health Record Analysis}},
  author={Liao, Yusheng and Wu, Chaoyi and Liu, Junwei and Jiang, Shuyang and Qiu, Pengcheng and Wang, Haowen and Yue, Yun and Zhen, Shuai and Wang, Jian and Fan, Qianrui and Gu, Jinjie and Zhang, Ya and Wang, Yanfeng and Wang, Yu and Xie, Weidi},
  journal={arXiv preprint arXiv:2510.25628},
  year={2025}
}
```