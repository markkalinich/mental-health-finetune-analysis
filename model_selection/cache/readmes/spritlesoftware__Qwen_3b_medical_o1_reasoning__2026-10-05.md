---
base_model: unsloth/qwen2.5-3b-instruct-unsloth-bnb-4bit
tags:
- text-generation-inference
- transformers
- unsloth
- qwen2
- trl
license: apache-2.0
language:
- en
---

<img src="https://images.newscientist.com/wp-content/uploads/2024/04/09121015/SEI_198633450.jpg" />

# Uploaded  model

- **Developed by:** spritlesoftware
- **License:** apache-2.0
- **Finetuned from model :** unsloth/qwen2.5-3b-instruct-unsloth-bnb-4bit

This qwen2 model was trained 2x faster with [Unsloth](https://github.com/unslothai/unsloth) and Huggingface's TRL library.

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)

# Medical Reasoning Language Model Fine-Tuning with Unsloth

A project for fine-tuning language models to perform structured medical reasoning analysis using efficient parameter adaptation.

## Features

- 🚀 **Efficient Fine-Tuning** with Unsloth and LoRA adapters
- 🏥 **Medical Reasoning Specialization** for clinical case analysis
- 📝 **Structured Response Format** with XML-style reasoning/answer sections
- � **Dual Reward Mechanism** combining length incentives and format validation
- ⚡ **4x Faster Training** using optimized kernels and memory efficiency

# Dataset used for training

 https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT

# How to use?
```python
from transformers import pipeline

messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe = pipeline("text-generation", model="spritlesoftware/Qwen_3b_medical_o1_reasoning")
pipe(messages)
```

## Use this system prompt

```
SYSTEM_PROMPT = """
Respond in the following format:

<reasoning>
...
</reasoning>
<answer>
...
</answer>
"""
```

# Performance comparision medical reasoning

```
Question : 
A 45 year old postmenopausal lady presents with an 8 cm breast lump that is adherent to the skin, with one firm apical lymph node in the axilla and one more node in the ipsilateral supraclavicular area with no clinical evidence of distant metastasis. The staging is
A. T3 N2 M1
B. T4 N3c M0
C. T4 N2c M1
D. T3 N3 M0


Qwen 2.5 3b (Wrong answer):
Based on the information provided, the correct staging for this patient would be:

C. T4 N2c M0

Here's the breakdown of the staging:

- **T4**: The tumor (T) is 8 cm in size, which is considered T4, as it is larger than the typical T3 (usually 5 cm or less).
- **N2c**: The axillary lymph node (N) is described as "one firm apical lymph node in the axilla and one more node in the ipsilateral supraclavicular area." The supraclavicular lymph nodes are considered N2, and the presence of more than one node in the supraclavicular area (more than 1 but less than 3) is classified as N2c.
- **M0**: There is no clinical evidence of distant metastasis (M0).

Therefore, the correct staging is T4 N2c M0, which corresponds to option B. However, since option C is also given and it correctly reflects the T4 N2c M0, the correct answer is C.


Qwen_3b_medical_o1_reasoning (Correct answer):
<reasoning>
Let's analyze the patient's case step by step to determine the appropriate staging.
The patient is a 45-year-old postmenopausal woman presenting with an 8 cm breast lump that is adherent to the skin.
This suggests a large, invasive tumor.
The presence of one firm apical lymph node in the axilla and one more node in the ipsilateral supraclavicular area indicates that the tumor has already metastasized to regional lymph nodes. 

First, let's consider the tumor size (T).
A tumor size of 8 cm is considered T4, as it is greater than 5 cm.
This is consistent with the description of the tumor being large and adherent to the skin, which is indicative of an invasive tumor.

Next, we need to assess the nodal involvement (N).
The patient has one axillary node and one supraclavicular node that are firm, which is indicative of metastatic involvement.
The supraclavicular lymph nodes are particularly concerning as they are often involved in more advanced stages of breast cancer.
Since both nodes are present and firm, we can classify this as N3c, which is the most advanced stage of axillary node involvement. 

Finally, the absence of distant metastasis (M) is noted as M0.
This suggests that the cancer has not spread beyond the regional lymph nodes to distant sites such as the lungs, liver, or bones.

Given these findings, the correct staging is T4 N3c M0.
This means the tumor is very large (T4), there is metastasis to the axillary and supraclavicular lymph nodes (N3c), and there are no distant metastases (M0).
Therefore, the correct answer is B. T4 N3c M0.

</reasoning>
<answer>
B. T4 N3c M0
</answer>
```