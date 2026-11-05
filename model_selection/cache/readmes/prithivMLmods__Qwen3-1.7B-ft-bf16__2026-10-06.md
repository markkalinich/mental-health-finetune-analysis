---
license: apache-2.0
language:
- en
base_model:
- Qwen/Qwen3-1.7B
pipeline_tag: text-generation
library_name: transformers
tags:
- text-generation-inference
- moe
- moderately abliterated variant
---

![FMjPew6Vjrp4FvKe1Uz_T.png](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/sdq94NXg-BEF9xbxauq1W.png)

# **Qwen3-1.7B-ft-bf16**

> **Qwen3-1.7B-ft-bf16** is a fine-tuned, moderately abliterated variant of the Qwen3-1.7B model. Built upon the robust Qwen3 architecture, this version emphasizes **improved context awareness** and **moderate behavioral flexibility**, while maintaining high standards in reasoning, instruction-following, and multilingual performance. It is designed to perform consistently across general-purpose dialogue, technical reasoning, creative writing, and multilingual tasks.

### Key Highlights:

- **Improved Context Awareness**: Retains and utilizes long-span contextual information effectively, making it suitable for long conversations, document analysis, and summarization.
- **Moderate Abliteration**: Introduces controlled experimental freedoms for enhanced expressiveness and adaptability, while preserving safety and alignment.
- **Dual-Mode Thinking Support**: Supports dynamic switching between deep logical reasoning and efficient casual dialogue, making it task-aware and context-adaptive.
- **Multilingual Excellence**: Robust across 100+ languages, handling translation, multilingual instruction, and language-specific tasks seamlessly.
- **Tool and Agent Integration**: Performs well in agent-driven scenarios and can interface with tools and APIs in both thinking and non-thinking modes.

---

## Quickstart with 🤗 Transformers

```bash
pip install transformers==4.51.3
pip install huggingface_hub[hf_xet]
```

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "prithivMLmods/Qwen3-1.7B-ft-bf16"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)

# Define prompt and apply chat template
prompt = "Explain why the sky appears blue during the day and red at sunset."
messages = [{"role": "user", "content": prompt}]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=True
)

# Tokenize input
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

# Generate response
generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=32768
)
output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist()

# Optional: Separate thinking content
try:
    index = len(output_ids) - output_ids[::-1].index(151668)  # token ID for </think>
except ValueError:
    index = 0

thinking_content = tokenizer.decode(output_ids[:index], skip_special_tokens=True).strip("\n")
content = tokenizer.decode(output_ids[index:], skip_special_tokens=True).strip("\n")

print("thinking content:", thinking_content)
print("content:", content)
```

---

## Recommended Settings

- **Sampling Parameters**:
  - Thinking Mode: `temperature=0.6`, `top_p=0.95`, `top_k=20`, `min_p=0.0`
  - Non-Thinking Mode: `temperature=0.7`, `top_p=0.8`, `top_k=20`, `min_p=0.0`
- **Max Token Length**:
  - Standard Tasks: `32768`
  - Complex/Extended Tasks: `38912`

---

## Prompting Guidelines

- **Math Problems**:  
  `"Please reason step by step, and put your final answer within \boxed{}."`
- **MCQs**:  
  Format: `{"answer": "C"}`
- **Dialogues**:  
  Include only final responses in history; omit internal thinking logs for efficiency. 