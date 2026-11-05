---
language:
- en
license: llama3.1
tags:
- text-generation-inference
- transformers
- unsloth
- llama
- trl
base_model: unsloth/deepseek-r1-distill-llama-8b-unsloth-bnb-4bit
model-index:
- name: Fireball-R1-Llama-3.1-8B
  results:
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: IFEval (0-Shot)
      type: HuggingFaceH4/ifeval
      args:
        num_few_shot: 0
    metrics:
    - type: inst_level_strict_acc and prompt_level_strict_acc
      value: 44.27
      name: strict accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=EpistemeAI/Fireball-R1-Llama-3.1-8B
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: BBH (3-Shot)
      type: BBH
      args:
        num_few_shot: 3
    metrics:
    - type: acc_norm
      value: 10.27
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=EpistemeAI/Fireball-R1-Llama-3.1-8B
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: MATH Lvl 5 (4-Shot)
      type: hendrycks/competition_math
      args:
        num_few_shot: 4
    metrics:
    - type: exact_match
      value: 31.12
      name: exact match
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=EpistemeAI/Fireball-R1-Llama-3.1-8B
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: GPQA (0-shot)
      type: Idavidrein/gpqa
      args:
        num_few_shot: 0
    metrics:
    - type: acc_norm
      value: 0.0
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=EpistemeAI/Fireball-R1-Llama-3.1-8B
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: MuSR (0-shot)
      type: TAUR-Lab/MuSR
      args:
        num_few_shot: 0
    metrics:
    - type: acc_norm
      value: 1.43
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=EpistemeAI/Fireball-R1-Llama-3.1-8B
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: MMLU-PRO (5-shot)
      type: TIGER-Lab/MMLU-Pro
      config: main
      split: test
      args:
        num_few_shot: 5
    metrics:
    - type: acc
      value: 1.28
      name: accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=EpistemeAI/Fireball-R1-Llama-3.1-8B
      name: Open LLM Leaderboard
---

**Upgrade** version: [EpistemeAI/Fireball-R1-Llama-3.1-8B-Medical-COT](https://huggingface.co/EpistemeAI/Fireball-R1-Llama-3.1-8B-Medical-COT)

## Model Information


# Fireball-R1-LLama-3.1-8B

![License](https://img.shields.io/badge/License-Apache%202.0-blue)  ![Version](https://img.shields.io/badge/Version-1.0.0-green)

This is a state-of-the-art language model optimized for **neutrality**, **STEM proficiency**, and **ethical alignment**. Fine-tuned Deepseek-R1-distill-llama-8b-unsloth-bnb-4bit for science, chemistry, and mathematics with reduced cultural/political bias.
This large language model is open source.  

---

## Table of Contents  
- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Training Details](#training-details)  
- [Ethical Considerations](#ethical-considerations)  
- [License](#license)  
- [Citation](#citation)  
- [Contact](#contact)  

---

## Features  
- **Neutral Worldview**: Minimizes political/cultural bias via globally diverse training data and human feedback.  
- **STEM Specialization**: Enhanced performance in:  
  - **Chemistry**: Reaction mechanisms, periodic trends, spectroscopy.  
  - **Mathematics**: Equation solving, proofs, calculus.  
  - **General Science**: Hypothesis generation, research summarization.  
- **Ethical Guardrails**: Filters sensitive content and flags uncertain outputs.  

---

## Installation  
```bash  
pip install transformers torch
pip install accelerate
pip install -U transformers
```

### Basic Inference
```bash  

from transformers import AutoTokenizer, AutoModelForCausalLM  

tokenizer = AutoTokenizer.from_pretrained("EpistemeAI/Fireball-R1-Llama-3.1-8B")  
model = AutoModelForCausalLM.from_pretrained("EpistemeAI/Fireball-R1-Llama-3.1-8B")  

prompt = "Calculate the molar mass of sulfuric acid (H₂SO₄)."  
inputs = tokenizer(prompt, return_tensors="pt")  
outputs = model.generate(**inputs, max_length=200)  
print(tokenizer.decode(outputs[0], skip_special_tokens=True))


##advance inference
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("EpistemeAI/Fireball-R1-Llama-3.1-8B")

# Load the model in 8-bit precision using bitsandbytes (requires a CUDA GPU)
model = AutoModelForCausalLM.from_pretrained(
    "EpistemeAI/Fireball-R1-Llama-3.1-8B",
    load_in_8bit=True,      # Enable 8-bit loading to reduce memory usage
    device_map="auto"       # Automatically map model layers to the available device(s)
)

# Define the system prompt and the user prompt
system_prompt = "You are a highly knowledgeable assistant with expertise in chemistry and physics. <think>"
user_prompt = "Calculate the molar mass of sulfuric acid (H₂SO₄)."

# Combine the system prompt with the user prompt. The format here follows a common convention for chat-like interactions.
full_prompt = f"System: {system_prompt}\nUser: {user_prompt}\nAssistant:"

# Tokenize the combined prompt and move the inputs to the GPU
inputs = tokenizer(full_prompt, return_tensors="pt").to("cuda")

# Generate output text from the model
outputs = model.generate(**inputs, max_length=12200)

# Decode and print the result, skipping special tokens
result = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(result)

```



### Recommended Parameters

```bash  
outputs = model.generate(  
  **inputs,  
  max_length=300,  
  temperature=0.7,  
  top_p=0.95,  
  repetition_penalty=1.2  
)  
```

# Uploaded  model

- **Developed by:** EpistemeAI
- **License:** apache-2.0
- **Finetuned from model :** unsloth/deepseek-r1-distill-llama-8b-unsloth-bnb-4bit

# Ethical Considerations
Do Not Use For:

- Medical/legal advice without expert oversight.
- Generating partisan or culturally insensitive content.

## Limitations:
- May occasionally produce plausible but incorrect scientific explanations.
- Not fully immune to subtle biases.

## Thank you
We appreciate the companies as following: Unsloth, Meta and Deepseek. 

## License
This model is licensed under [apache-2.0] - see LICENSE for details.

## Citation

```
@misc{Fireball-R1-Llama-3.1-8B,  
  author = {EpistemeAI},  
  title = {Fireball-R1-8B: A Neutral, Science-Optimized Language Model},  
  year = {2025},  
  url = {https://huggingface.co/EpistemeAI/Fireball-R1-Llama-3.1-8B}  
}
```

For support or feedback: contact us at episteme.ai@proton.me

This llama model was trained 2x faster with [Unsloth](https://github.com/unslothai/unsloth) and Huggingface's TRL library.

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/EpistemeAI__Fireball-R1-Llama-3.1-8B-details)

|      Metric       |Value|
|-------------------|----:|
|Avg.               |14.73|
|IFEval (0-Shot)    |44.27|
|BBH (3-Shot)       |10.27|
|MATH Lvl 5 (4-Shot)|31.12|
|GPQA (0-shot)      | 0.00|
|MuSR (0-shot)      | 1.43|
|MMLU-PRO (5-shot)  | 1.28|

