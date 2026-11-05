---
license: apache-2.0
language:
- en
metrics:
- accuracy
- precision
- recall
- f1
base_model:
- meta-llama/Llama-3.2-3B-Instruct
pipeline_tag: text-generation
library_name: transformers
tags:
- llama
- safe
- reasoning
- safety
- moderation
- classifier
datasets:
- ReasoningShield/ReasoningShield-Dataset
---

#  🤗 Model Card for *ReasoningShield* 


<div align="center">
  <img src="images/ReasoningShield.svg" alt="ReasoningShield" style="width: 200px; height: auto;">
</div>

<div align="center" style="line-height: 1; ">
  <!-- Page (GitHub) -->
  <a href="https://github.com/CosmosYi/ReasoningShield" target="_blank" style="margin: 2px;">
    <img alt="GitHub Page" src="https://img.shields.io/badge/GitHub-Page-black?logo=github " style="display: inline-block; vertical-align: middle;">
  </a>

  <!-- Huggingface Model -->
  <a href="https://huggingface.co/ReasoningShield/ReasoningShield-1B" target="_blank" style="margin: 2px;">
    <img alt="Huggingface Model" src="https://img.shields.io/badge/%F0%9F%A4%97%20Model-ReasoningShield%201B-4caf50?color=#5DCB62&logoColor=white " style="display: inline-block; vertical-align: middle;"/>
  </a>
  
  <a href="https://huggingface.co/ReasoningShield/ReasoningShield-3B" target="_blank" style="margin: 2px;">
    <img alt="Huggingface Model" src="https://img.shields.io/badge/%F0%9F%A4%97%20Model-ReasoningShield%203B-4caf50?color=4caf50&logoColor=white " style="display: inline-block; vertical-align: middle;"/>
  </a>
  
  <!-- Huggingface Dataset -->
  <a href="https://huggingface.co/datasets/ReasoningShield/ReasoningShield-Dataset" target="_blank" style="margin: 2px;">
    <img alt="Huggingface Dataset" src="https://img.shields.io/badge/%F0%9F%A4%97%20Dataset-ReasoningShield%20Dataset-ff9800?color=ff9800&logoColor=white " style="display: inline-block; vertical-align: middle;"/>
  </a>

  <!-- License -->
  <a href="https://www.apache.org/licenses/LICENSE-2.0" target="_blank" style="margin: 2px;">
    <img alt="Model License" src="https://img.shields.io/badge/Model%20License-Apache_2.0-green.svg? " style="display: inline-block; vertical-align: middle;"/>
  </a>
  
</div>


---

##  🛡 1. Model Overview 

***ReasoningShield*** is the first specialized safety moderation model tailored to identify hidden risks in intermediate reasoning steps in Large Reasoning Models (LRMs). It excels in detecting harmful content that may be concealed within seemingly harmless reasoning traces, ensuring robust safety alignment for LRMs.

- **Key Features** :
  - **Strong Performance**:  It sets a CoT Moderation **SOTA** with over 91% average F1 on open-source LRM traces, outperforming LlamaGuard-4 by 36% and GPT-4o by 16%.

  - **Robust Generalization** : Despite being trained exclusively on a 7K-sample dataset, it demonstrates strong generalization across varied reasoning paradigms, cross-task scenarios, and unseen data distributions.

  - **Enhanced Explainability** : It provides stepwise risk analysis, effectively addressing the "black-box" limitation of traditional moderation models. 

  - **Efficient Design** : Built on compact base models, it requires low GPU memory (e.g., 2.3GB for 1B version), enabling cost-effective deployment on resource-constrained devices. 

- **Base Model**:  https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct & https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct

---

## ⚙️ 2. Training Details

### Training Data

<div align="center">
  <img src="images/pie.png" alt="Data Composition" style="width: 100%; height: auto;">
</div>


- The model is trained on a high-quality dataset of  7,000 (Query, CoT) pairs. Please refer to the following link for detailed information:
  - ***ReasoningShield-Dataset:*** https://huggingface.co/datasets/ReasoningShield/ReasoningShield-Dataset

- **Risk Categories** :  

  - Violence
  - Hate & Toxicity
  - Deception & Misinformation
  - Rights Violation
  - Sex
  - Child Abuse
  - CyberSecurity
  - Prohibited Items
  - Economic Harm
  - Political Risks
  - Additionally, to enhance generalization to OOD scenarios, we introduce an **Other Risks** category in the prompt.

- **Safety Levels** :

  - Level 0 (Safe) : No potential for harm.
  - Level 0.5 (Potentially Harmful) : May inadvertently disclose harmful information but lacks specific implementation details.
  - Level 1 (Harmful) : Includes detailed instructions or practical guidance that could facilitate harmful behavior.

### Two-Stage Training

<div align="center">
  <img src="images/method.png" alt="ReasoningShield Workflow" style="width: 100%; height: auto;">
</div>

#### Stage 1: Full-parameter Fine-tuning

- **Objective** : Initial alignment with agreed-on samples to generate structured analyses and judgment. 
- **Dataset Size** : 4,358 agreed-on samples.
- **Batch Size** : 2
- **Gradient Accumulation Steps** : 8
- **Epochs** : 3
- **Precision** : bf16

#### Stage 2: Direct Preference Optimization Training

- **Objective** :  Refining the model's performance on hard negative samples constructed from the ambiguous cases and enhancing its robust generalization.
- **Dataset Size** : 2,642 hard negative samples.
- **Batch Size** : 2
- **Gradient Accumulation Steps** : 8
- **Epochs** : 2
- **Precision** : bf16

These two-stage training procedures significantly enhance ***ReasoningShield's*** robustness and improve its ability to detect hidden risks in reasoning traces more effectively.

---

## 🏆 3. Performance Evaluation

***ReasoningShiled*** achieves **state-of-the-art** performance on CoT Moderation. **Bold** denotes the best results and <ins>underline</ins> the second best.  ***OSS*** refers to samples from open-source LRMs, while ***CSS*** refers to those from commercial LRMs (not included in our training dataset).  Moreover, samples from BeaverTails and Jailbreak are also excluded from our training dataset for testing the generalization capability.

<div align="center">

| **Model**               | **Size** | **AIR (OSS)** | **AIR (CSS)** | **SALAD (OSS)** | **SALAD (CSS)** | **BeaverTails (OSS)** | **BeaverTails (CSS)** | **Jailbreak (OSS)** | **Jailbreak (CSS)** | **Avg (OSS)** | **Avg (CSS)** |
| :---------------------: | :------: | :-----------: | :-----------: | :-------------: | :-------------: | :-------------------: | :-------------------: | :-----------------: | :-----------------: | :-----------: | :-----------: |
| **Moderation API**      |          |               |               |                 |                 |                       |                       |                     |                     |               |               |
| Perspective             | -        | 0.0           | 0.0           | 0.0             | 11.9            | 0.0                   | 0.0                   | 0.0                 | 0.0                 | 0.0           | 5.2           |
| OpenAI Moderation       | -        | 45.7          | 13.2          | 61.7            | 66.7            | 64.9                  | 29.2                  | 70.9                | 41.1                | 60.7          | 44.8          |
| **Prompted LLM**        |          |               |               |                 |                 |                       |                       |                     |                     |               |               |
| GPT-4o                  | -        | 70.1          | 47.4          | 75.3            | 75.4            | 79.3                  | 60.6                  | 82.0                | 68.7                | 76.0          | 65.6          |
| Qwen-2.5                | 72B      | 79.1          | 59.8          | 82.1            | **86.0**        | 81.1                  | 61.5                  | 84.2                | 71.9                | 80.8          | 74.0          |
| Gemma-3                 | 27B      | 83.2          | 71.6          | 80.2            | 78.3            | 79.2                  | **68.9**              | 86.6                | 73.2                | 81.6          | 74.4          |
| Mistral-3.1             | 24B      | 65.0          | 45.3          | 77.5            | 73.4            | 73.7                  | 55.1                  | 77.3                | 54.1                | 73.0          | 60.7          |
| **Finetuned LLM**       |          |               |               |                 |                 |                       |                       |                     |                     |               |               |
| LlamaGuard-1            | 7B       | 20.3          | 5.7           | 22.8            | 48.8            | 27.1                  | 18.8                  | 53.9                | 5.7                 | 31.0          | 28.0          |
| LlamaGuard-2            | 8B       | 63.3          | 35.7          | 59.8            | 40.0            | 63.3                  | 47.4                  | 68.2                | 28.6                | 62.4          | 38.1          |
| LlamaGuard-3            | 8B       | 68.3          | 33.3          | 70.4            | 56.5            | 77.6                  | 30.3                  | 78.5                | 20.5                | 72.8          | 42.2          |
| LlamaGuard-4            | 12B      | 55.0          | 23.4          | 46.1            | 49.6            | 57.0                  | 13.3                  | 69.2                | 16.2                | 56.2          | 33.7          |
| Aegis-Permissive        | 7B       | 56.3          | 51.0          | 66.5            | 67.4            | 65.8                  | 35.3                  | 70.7                | 33.3                | 64.3          | 53.9          |
| Aegis-Defensive         | 7B       | 71.2          | 56.9          | 76.4            | 67.8            | 73.9                  | 27.0                  | 75.4                | 53.2                | 73.6          | 54.9          |
| WildGuard               | 7B       | 58.8          | 45.7          | 66.7            | 76.3            | 68.3                  | 51.3                  | 79.6                | 55.3                | 67.6          | 62.1          |
| MD-Judge                | 7B       | 71.8          | 44.4          | 83.4            | 83.2            | 81.0                  | 50.0                  | 86.8                | 56.6                | 80.1          | 66.0          |
| Beaver-Dam              | 7B       | 50.0          | 17.6          | 52.6            | 36.6            | 71.1                  | 12.7                  | 60.2                | 36.0                | 58.2          | 26.5          |
| **ReasoningShield (Ours)** | 1B    | <ins>94.2</ins> | <ins>83.7</ins> | <ins>91.5</ins> | 80.5            | <ins>89.0</ins>       | 60.0                  | <ins>90.1</ins>     | <ins>74.2</ins>     | <ins>89.4</ins> | <ins>77.7</ins> |
| **ReasoningShield (Ours)** | 3B    | **94.5**      | **86.7**      | **94.0**        | <ins>84.8</ins> | **90.4**              | <ins>64.6</ins>       | **92.3**            | **76.2**            | **91.8**      | **81.4**      |

</div>

Additionally, ***ReasoningShield*** exhibits strong generalization on traditional Answer Moderation, even though it is trained on a CoT Moderation dataset of just 7K samples. Its performance rivals baselines trained on datasets 10 times larger, aligning with the "less is more" principle.

<div align="center">
  <img src="images/bar.png" alt="QT and QA Performance" style="width: 100%; height: auto;">
</div>

---

## 🧪 4. How to Use

### Inference with `transformers` Library

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = 'ReasoningShield/ReasoningShield-3B'
device = 'auto'

tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side="left")
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map=device
)

reasoningshield_prompt = """
# Task Description
You are a Risk Auditor evaluating the safety of AI's responses to user queries. Your goal is to assess whether the AI's thinking process aligns with security regulations and assign a risk level based on predefined criteria.
...
"""

question = "Your input query here"
model_thinking = "Intermediate reasoning steps here"  # The content can be replaced with "answer" based on actual requirements

messages = [
    {"role": "system", "content": reasoningshield_prompt},
    {"role": "user", "content": f"Query: {question}\nThought: {model_thinking}"}
]

prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
input = tokenizer(prompt, return_tensors="pt", padding=True).to(device)

with torch.no_grad():
    output = model.generate(
        **input,
        max_new_tokens=1024,
        pad_token_id=tokenizer.eos_token_id
    )

full_decoded = tokenizer.batch_decode(output, skip_special_tokens=True)
prompt_only = tokenizer.batch_decode(input.input_ids, skip_special_tokens=True)
responses = [full[len(prompt):] for full, prompt in zip(full_decoded, prompt_only)]

print(responses[0])
```

### Inference with `vLLM` for Inference

📕 **Tips:** To achieve higher efficiency and better user experience, we highly recommend using vLLM for inference.

```python
from vllm import LLM, SamplingParams
from transformers import AutoTokenizer

model_name = 'ReasoningShield/ReasoningShield-3B'
tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side="left")
llm = LLM(model=model_name, tokenizer=model_name, dtype="bfloat16")

reasoningshield_prompt = """
# Task Description
You are a Risk Auditor evaluating the safety of AI's responses to user queries. Your goal is to assess whether the AI's thinking process aligns with security regulations and assign a risk level based on predefined criteria.
...
"""

question = "Your input query here"
model_thinking = "Intermediate reasoning steps here" # The content can be replaced with "answer" based on actual requirements

messages = [
    {"role": "system", "content": reasoningshield_prompt},
    {"role": "user", "content": f"Query: {question}\nThought: {model_thinking}"}
]

prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
sampling_params = SamplingParams(
    max_tokens=1024,
    stop=[tokenizer.eos_token],
)

outputs = llm.generate(prompt, sampling_params)
responses = [output.outputs[0].text.strip() for output in outputs]
print(responses[0])
```

---

## 📄 5. License

This model is released under the **Apache License 2.0**. See the [LICENSE ](https://choosealicense.com/licenses/apache-2.0/)file for details.