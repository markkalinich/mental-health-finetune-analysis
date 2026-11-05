---
datasets:
- nvidia/HelpSteer3
- Skywork/Skywork-Reward-Preference-80K-v0.2
- Vezora/Code-Preference-Pairs
- xinlai/Math-Step-DPO-10K
language:
- en
base_model:
- Qwen/Qwen3-8B
library_name: transformers
tags:
- reward_model
- nvidia
- qwen3
license: other
license_name: nvidia-internal-scientific-research-and-development-model-license
license_link: >-
  https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-internal-scientific-research-and-development-model-license/

---




# BR-RM: Branch-and-Rethink Reasoning Reward Model

## Model Overview

**BR-RM (Branch-and-Rethink Reasoning Reward Model)** is a reward model that implements a novel two-turn reasoning framework to evaluate LLM-generated responses. Unlike traditional reward models that compress all quality dimensions into a single scalar in one shot, BR-RM performs **adaptive branching** to focus on instance-critical dimensions, followed by **branch-conditioned rethinking** for targeted deep analysis.

This model achieves **state-of-the-art performance** on the average score on three major reward modeling benchmarks (RewardBench, RM-Bench, and RMB) by addressing the "judgment diffusion" problem where models spread attention too thinly across evaluation criteria.

Code Link: https://github.com/yzjiao/BR-RM

### Key Features

- 🎯 **Adaptive Focus**: Dynamically selects 1-3 critical evaluation dimensions per instance
- 🔄 **Two-Turn Reasoning**: First turn branches, second turn performs deep conditioned analysis
- 📊 **SOTA Performance**: Top results on RewardBench (92.1%), RM-Bench (85.9%), and RMB (74.7%)
- 🔧 **RLHF Compatible**: Designed to integrate seamlessly with standard RLHF pipelines

### Model Variants

| Model | Parameters | RewardBench | RM-Bench | RMB | Average |
|-------|-----------|-------------|----------|-----|---------|
| **Qwen3-Nemotron-8B-BRRM** | 8B | 91.0 | 85.0 | 71.8 | 82.6 |
| **Qwen3-Nemotron-14B-BRRM** | 14B | 92.1 | 85.9 | 74.7 | 84.2 |

## How It Works

### Two-Turn Framework

**Turn 1: Adaptive Branching**
```
Input: User query + Two candidate responses
Output: 
  1. Selected critical dimensions (e.g., "Logical Reasoning", "Computational Precision")
  2. Initial issue detection for each response
```

**Turn 2: Branch-Conditioned Rethinking**
```
Input: Turn 1 results + Evaluation hierarchy
Output: Final comparative judgment and preference ranking
```



## Quick Start
```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load model and tokenizer
model_name = "nvidia/Qwen3-Nemotron-8B-BRRM"  # or nvidia/Qwen3-Nemotron-14B-BRRM
model = AutoModelForCausalLM.from_pretrained(
    model_name, 
    torch_dtype=torch.bfloat16,
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Example usage
context = "What is 2+2?"
response1 = "2+2=4"
response2 = "2+2=5"

# Format Turn 1: Adaptive Branching
turn1_prompt = f"""You are a response quality evaluator. Given the context and two responses, select the most important cognitive abilities and analyze critical issues.

**Context:** 
{context}

**Responses:**
[The Begin of Response 1]
{response1}
[The End of Response 1]

[The Begin of Response 2]
{response2}
[The End of Response 2]

**Output Format:**
[Quality Assessment Focus]
Choose 1-3 abilities: Information Accuracy, Computational Precision, Logical Reasoning, Implementation Capability, Safety Awareness, Response Completeness, Instruction Adherence, Communication Clarity.
[End of Quality Assessment Focus]

[Quality Analysis for Response 1]
- Critical Issues: [List specific issues or "None identified"]
[End of Quality Analysis for Response 1]

[Quality Analysis for Response 2]
- Critical Issues: [List specific issues or "None identified"]
[End of Quality Analysis for Response 2]"""

# Generate Turn 1
messages = [{"role": "user", "content": turn1_prompt}]
input_ids = tokenizer.apply_chat_template(
    messages, 
    return_tensors="pt",
    add_generation_prompt=True
).to(model.device)
outputs = model.generate(
    input_ids, 
    max_new_tokens=8192,      
    temperature=1.0,
    top_p=0.95,               
    top_k=20,                 
    do_sample=True,           
    pad_token_id=tokenizer.eos_token_id
)
turn1_response = tokenizer.decode(outputs[0][input_ids.shape[1]:], skip_special_tokens=False)


# Format Turn 2: Branch-Conditioned Rethinking
turn2_prompt = f"""You are making final comparative judgments using established evaluation priorities.

**Evaluation Hierarchies:**
- **Accuracy-Critical**: Correctness > Process > Presentation 
- **Creative/Open-Ended**: User Intent > Content Quality > Creativity 
- **Instruction-Following**: Adherence > Content > Clarity

[The Begin of Analysis on Response 1]
[Apply appropriate evaluation hierarchy]
[The End of Analysis on Response 1]

[The Begin of Analysis on Response 2]
[Apply appropriate evaluation hierarchy]
[The End of Analysis on Response 2]

[The Begin of Ranking Score]
\\boxed{{1 or 2}}
[The End of Ranking Score]"""

# Generate Turn 2
messages.append({"role": "assistant", "content": turn1_response})
messages.append({"role": "user", "content": turn2_prompt})
input_ids = tokenizer.apply_chat_template(
    messages, 
    return_tensors="pt",
    add_generation_prompt=True
).to(model.device)
outputs = model.generate(
    input_ids, 
    max_new_tokens=8192,     
    temperature=1.0,
    top_p=0.95,              
    top_k=20,                
    do_sample=True,          
    pad_token_id=tokenizer.eos_token_id
)
final_response = tokenizer.decode(outputs[0][input_ids.shape[1]:], skip_special_tokens=False)
```


## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their supporting model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse. 
For more detailed information on ethical considerations for this model, please see the Model Card++ [Explainability](explainability.md), [Bias](bias.md), [Safety and Security](safety.md), and [Privacy](privacy.md) Subcards.  

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).


## Citation

If you find this model useful, please cite the following work:

```bibtex
@misc{jiao2025thinktwicebranchandrethinkreasoning,
      title={Think Twice: Branch-and-Rethink Reasoning Reward Model}, 
      author={Yizhu Jiao and Jiaqi Zeng and Julien Veron Vialard and Oleksii Kuchaiev and Jiawei Han and Olivier Delalleau},
      year={2025},
      eprint={2510.23596},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2510.23596}, 
}
```