---
library_name: transformers
tags:
- sft
- lora
- unsloth
- reasoning
- medical
license: apache-2.0
datasets:
- mamachang/medical-reasoning
language:
- en
base_model:
- unsloth/Qwen3-1.7B
pipeline_tag: text-generation
---

## Model Card: khazarai/ClinicalReasoning-0.6B

### Model Description 

- **Model Name:** ClinicalReasoning-0.6B
- **Base Model:** Qwen-3 0.6B
- **Fine-Tuning Dataset:** 4,000 examples of medical reasoning clinical vignettes including multiple-choice questions, with step-by-step reasoning and answer labels.
- **Task:** Multiple-choice medical reasoning with reasoning explanation. The model provides reasoning in <analysis></analysis> tags and the final answer in <answer></answer> tags.


## Intended Use:

- Assisting medical students and professionals in practicing clinical reasoning.
- Educational tools for medical multiple-choice question solving.
- Research purposes in medical NLP and reasoning tasks.

Not Intended For:
- Direct medical diagnosis or patient care. Outputs should not replace professional medical advice.


## Limitations:

- Limited to the scope of the training dataset (4K examples).
- May not generalize to rare or complex medical scenarios.
- Should not be used as a substitute for professional medical advice.

## How to Get Started with the Model

Use the code below to get started with the model.

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("khazarai/ClinicalReasoning-0.6B")
model = AutoModelForCausalLM.from_pretrained(
    "khazarai/ClinicalReasoning-0.6B",
    device_map={"": 0}
)

system = "Please answer with one of the option in the bracket. Write reasoning in between <analysis></analysis>. Write answer in between <answer></answer>."

question = """
A 44-year-old female is admitted to the neurological service. You examine her chart and note that after admission she was started on nimodipine. Which of the following pathologies would benefit from this pharmacologic therapy??
{'A': 'Pseudotumor cerebri', 'B': 'Thromboembolic stroke', 'C': 'Epidural hematoma', 'D': 'Subdural hematoma', 'E': 'Subarachnoid hemorrhage'}
"""

messages = [
    {"role" : "system", "content" : system},
    {"role" : "user",   "content" : question}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize = False,
    add_generation_prompt = True, 
    enable_thinking = False,
)

from transformers import TextStreamer
_ = model.generate(
    **tokenizer(text, return_tensors = "pt").to("cuda"),
    max_new_tokens = 512,
    temperature = 0.6,
    top_p = 0.95,
    top_k = 20,
    streamer = TextStreamer(tokenizer, skip_prompt = True),
)
```