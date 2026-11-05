---
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct/blob/main/LICENSE
language:
- tr
- en
datasets:
- erayalp/easy_turkish_math_reasoning
base_model:
- Qwen/Qwen2.5-0.5B-Instruct
pipeline_tag: text-generation
library_name: transformers
tags:
- curriculum-learning
- math
- supervised-fine-tuning
- turkish
---

## Objective
The goal of this project is to enhance the reasoning ability of the compact Qwen2.5-0.5B model on Turkish math questions. Using supervised fine-tuning (SFT) on simpler examples as a starting point, the model will be progressively improved through curriculum learning, and later refined using Group Relative Policy Optimization (GRPO) to boost multi-step reasoning performance.

#### This model is intended for:
- Research on curriculum learning in small models
- Evaluating Turkish math reasoning tasks

### Limitations
- Currently only trained on simpler math examples — lacks robustness for multi-step or abstract reasoning.
- May produce incorrect or overconfident answers on complex tasks.
- Performance may be sensitive to prompt phrasing.

### Roadmap
1. **Phase 1: SFT with basic arithmatic and math problems**
2. Phase 2: SFT with moderately difficult math problems
3. Phase 3: SFT with full-scale GSM8K-TR complexity
4. Phase 4: GRPO-based training to optimize multi-step reasoning and reduce hallucinations

## How to Use

You can easily run inference using the Transformers library:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_name = "erayalp/qwen2.5-0.5b-instruct-sft-v1-tr-math-easy"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)

prompt = "Ali’nin 3 kalemi vardı. 2 kalem daha aldı. Ali’nin şimdi kaç kalemi var?"

inputs = tokenizer(prompt, return_tensors="pt")
output = model.generate(**inputs, max_new_tokens=256)

print(tokenizer.decode(output[0], skip_special_tokens=True))