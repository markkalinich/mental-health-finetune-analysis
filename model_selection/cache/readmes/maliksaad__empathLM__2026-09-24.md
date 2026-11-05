---
license: mit
base_model: HuggingFaceTB/SmolLM2-135M-Instruct
tags:
  - empathy
  - mental-health
  - motivational-interviewing
  - cognitive-behavioral-therapy
  - fine-tuned
  - emotional-support
  - empathLM
language:
  - en
---

# 🧠 EmpathLM

**Fine-tuned for Psychologically Safe & Persuasive Emotional Support**

EmpathLM is a fine-tuned version of [SmolLM2-135M-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-135M-Instruct) 
trained to generate responses that combine **Motivational Interviewing (MI)** and **Cognitive Behavioral Therapy (CBT)** principles.

## What Makes EmpathLM Unique

Unlike general-purpose language models, EmpathLM is specifically optimized to:
- ✅ **Validate emotions** without judgment
- ✅ **Reflect feelings** back to the person warmly  
- ✅ **Gently shift perspective** without being manipulative
- ✅ **Ask powerful open questions** that encourage self-reflection
- ❌ **Never give unsolicited advice**

## Benchmark Results

EmpathLM was benchmarked against GPT-4o-mini and a Groq baseline on 20 unseen test situations,
scored across: emotional_validation, advice_avoidance, perspective_shift, and overall_empathy.

*See the [GitHub repository](https://github.com/maliksaad/empathLM) for full benchmark results.*

## Usage

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("maliksaad/empathLM")
model = AutoModelForCausalLM.from_pretrained("maliksaad/empathLM")

SYSTEM_PROMPT = """You are EmpathLM — an emotionally intelligent AI trained in Motivational Interviewing 
and Cognitive Behavioral Therapy. When someone shares emotional pain:
- Validate their feelings without judgment
- Reflect their emotions back to them
- Ask one powerful open-ended question
- NEVER give unsolicited advice"""

messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": "I failed my exam again. I feel like I'm just not smart enough."},
]

inputs = tokenizer.apply_chat_template(messages, return_tensors="pt", add_generation_prompt=True)
outputs = model.generate(inputs, max_new_tokens=200, temperature=0.7)
print(tokenizer.decode(outputs[0][inputs.shape[1]:], skip_special_tokens=True))
```

## Training Details

| Parameter | Value |
|-----------|-------|
| Base Model | SmolLM2-135M-Instruct |
| Training Examples | ~180 (90% of 200) |
| Epochs | 3 |
| Batch Size | 8 |
| Learning Rate | 2e-5 |
| Max Sequence Length | 512 |
| Training Platform | Kaggle (Free GPU) |

## Dataset

Trained on [maliksaad/empathLM-dataset](https://huggingface.co/datasets/maliksaad/empathLM-dataset)

## Citation

```bibtex
@model{saad2025empathLM,
  title  = {EmpathLM: A Psychologically-Grounded Empathetic Response Model},
  author = {Muhammad Saad},
  year   = {2025},
  url    = {https://huggingface.co/maliksaad/empathLM}
}
```
