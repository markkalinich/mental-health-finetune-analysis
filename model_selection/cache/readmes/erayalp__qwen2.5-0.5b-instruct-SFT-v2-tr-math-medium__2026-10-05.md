---
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct/blob/main/LICENSE
language:
- tr
- en
datasets:
- erayalp/medium_turkish_math_reasoning
base_model:
- erayalp/qwen2.5-0.5b-instruct-sft-v1-tr-math-easy
pipeline_tag: text-generation
library_name: transformers
tags:
- curriculum-learning
- math
- supervised-fine-tuning
- turkish
---
## Objective
This model is the **second phase** of a multi-stage training pipeline designed to improve the Turkish mathematical reasoning capabilities of the compact [Qwen2.5-0.5B](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct) model.

Starting from [`erayalp/qwen2.5-0.5b-instruct-sft-v1-tr-math-easy`](https://huggingface.co/erayalp/qwen2.5-0.5b-instruct-sft-v1-tr-math-easy), which was fine-tuned on simple Turkish math problems, this version continues training using **moderately difficult** examples to improve the model’s step-by-step reasoning and generalization before advancing to full-complexity GSM8K-TR tasks.

#### This model is intended for:
- Research on curriculum learning in small models
- Evaluating Turkish math reasoning tasks of moderate complexity

### Limitations
- Still not robust on **multi-step, abstract**, or **edge-case** problems.
- May hallucinate or give overconfident answers to complex prompts.
- Prompt sensitivity and reasoning depth are **in progress** — expect improvements in later phases.

### Roadmap
1. ~~Phase 1: SFT with basic arithmatic and math problems~~
2. **Phase 2: SFT with moderately difficult math problems**
3. Phase 3: SFT with full-scale GSM8K-TR complexity
4. Phase 4: GRPO-based training to optimize multi-step reasoning and reduce hallucinations

## How to Use

You can easily run inference using the Transformers library:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
model_name = "erayalp/qwen2.5-0.5b-instruct-sft-v2-tr-math-medium"
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