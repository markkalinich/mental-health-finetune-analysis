---
base_model:
- soob3123/GrayLine-Qwen3-8B
- mlxha/Qwen3-8B-grpo-medmcqa
- ValiantLabs/Qwen3-8B-Esper3
- Goekdeniz-Guelmez/Josiefied-Qwen3-8B-abliterated-v1
tags:
- merge
- mergekit
- lazymergekit
- soob3123/GrayLine-Qwen3-8B
- mlxha/Qwen3-8B-grpo-medmcqa
- ValiantLabs/Qwen3-8B-Esper3
- Goekdeniz-Guelmez/Josiefied-Qwen3-8B-abliterated-v1
---

# Qwen3-8B-medmcqa-GrayLine

Qwen3-8B-medmcqa-GrayLine is a merge of the following models using [LazyMergekit](https://colab.research.google.com/drive/1obulZ1ROXHjYLn6PPZJwRR6GzgQogxxb?usp=sharing):
* [soob3123/GrayLine-Qwen3-8B](https://huggingface.co/soob3123/GrayLine-Qwen3-8B)
* [mlxha/Qwen3-8B-grpo-medmcqa](https://huggingface.co/mlxha/Qwen3-8B-grpo-medmcqa)
* [ValiantLabs/Qwen3-8B-Esper3](https://huggingface.co/ValiantLabs/Qwen3-8B-Esper3)
* [Goekdeniz-Guelmez/Josiefied-Qwen3-8B-abliterated-v1](https://huggingface.co/Goekdeniz-Guelmez/Josiefied-Qwen3-8B-abliterated-v1)

## 🧩 Configuration

```yaml
slices:
  - sources:
      - model: soob3123/GrayLine-Qwen3-8B
        layer_range: [0, 36]
      - model: mlxha/Qwen3-8B-grpo-medmcqa
        layer_range: [0, 36]
      - model: ValiantLabs/Qwen3-8B-Esper3
        layer_range: [0, 36]
      - model: Goekdeniz-Guelmez/Josiefied-Qwen3-8B-abliterated-v1
        layer_range: [0, 36]
merge_method: multislerp
base_model: soob3123/GrayLine-Qwen3-8B
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5
dtype: bfloat16
```

## 💻 Usage

```python
!pip install -qU transformers accelerate

from transformers import AutoTokenizer
import transformers
import torch

model = "leegang/Qwen3-8B-medmcqa-GrayLine"
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