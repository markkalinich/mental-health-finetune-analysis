---
tags:
- merge
- mergekit
- lazymergekit
---

# tts-1111

tts-1111 is a merge of the following models using [LazyMergekit](https://colab.research.google.com/drive/1obulZ1ROXHjYLn6PPZJwRR6GzgQogxxb?usp=sharing):

## 🧩 Configuration

```yaml
models:
  - model: canopylabs/orpheus-3b-0.1-ft
  - model: kadirnar/orpheus-tts-tr-full
  - model: VAGOsolutions/SauerkrautTTS-Preview-0.1
  - model: maya-research/Veena
merge_method: model_stock
base_model: canopylabs/orpheus-3b-0.1-ft
normalize: true
int8_mask: true
dtype: float16
```

## 💻 Usage

```python
!pip install -qU transformers accelerate

from transformers import AutoTokenizer
import transformers
import torch

model = "ehristoforu/tts-1111"
messages = [{"role": "user", "content": "What is a large language model?"}]

tokenizer = AutoTokenizer.from_pretrained(model)
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
)

outputs = pipeline(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])
```