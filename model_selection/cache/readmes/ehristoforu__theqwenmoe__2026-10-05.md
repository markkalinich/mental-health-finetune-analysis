---
license: mit
pipeline_tag: text-generation
language:
- en
- ru
- code
base_model:
- Qwen/Qwen2.5-7B-Instruct
tags:
- qwen2.5
---

### theqwenmoe
- 18.3B parametrs
- English & Russian
- Math & Logic
- Code: Python, Javascript, Java, PHP, C++, C#, ...

This is experimental model. Can be bugs and various problems.

Made with mergekit and unsloth apps by ehristoforu.

Code usage example:
```py
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "ehristoforu/theqwenmoe"

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

prompt = "Give me a short introduction to large language model."
messages = [
    {"role": "system", "content": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."},
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=512
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
```