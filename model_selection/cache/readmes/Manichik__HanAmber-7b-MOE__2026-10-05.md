---
license: apache-2.0
tags:
- moe
- frankenmoe
- merge
- mergekit
- lazymergekit
- LLM360/AmberChat
- wannaphong/han-llm-7b-v2
base_model:
- LLM360/AmberChat
- wannaphong/han-llm-7b-v2
---

# HanAmber-7b-MOE

HanAmber-7b-MOE is a Mixure of Experts (MoE) made with the following models using [LazyMergekit](https://colab.research.google.com/drive/1obulZ1ROXHjYLn6PPZJwRR6GzgQogxxb?usp=sharing):
* [LLM360/AmberChat](https://huggingface.co/LLM360/AmberChat)
* [wannaphong/han-llm-7b-v2](https://huggingface.co/wannaphong/han-llm-7b-v2)

## 🧩 Configuration

```yaml
base_model: LLM360/AmberChat
dtype: float16
gate_mode: cheap_embed
experts:
  - source_model: LLM360/AmberChat
    positive_prompts: ["You are an helpful as general-pupose assistant."]
  - source_model: wannaphong/han-llm-7b-v2
    positive_prompts:
      - "คุณช่วยฉันหน่อยได้ไหม"
      - "คุณช่วยแปลประโยคนี้เป็นภาษาไทยได้ไหม"


```

## 💻 Usage

```python
!pip install -qU transformers bitsandbytes accelerate

from transformers import AutoTokenizer
import transformers
import torch

model = "Manichik/HanAmber-7b-MOE"

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    model_kwargs={"torch_dtype": torch.float16, "load_in_4bit": True},
)

messages = [{"role": "user", "content": "Explain what a Mixture of Experts is in less than 100 words."}]
prompt = pipeline.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
outputs = pipeline(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])
```