---
base_model:
- Qwen/Qwen2.5-32B-Instruct
- shaafsalman/qwen-2.5-32B
library_name: transformers
pipeline_tag: text-generation
tags:
- mergekit
- merge
- medical
- clinical
- qwen2
language:
- en
---

# MedQWEN-2.5-32B

A 32B medical language model created by SLERP-merging **Qwen2.5-32B-Instruct** with a medical domain fine-tune ([shaafsalman/qwen-2.5-32B](https://huggingface.co/shaafsalman/qwen-2.5-32B)), using [mergekit](https://github.com/cg123/mergekit).

The merge retains the instruction-following capability of the base instruct model while blending in clinical domain knowledge from the fine-tuned variant.

## Model Details

| Field | Value |
|-------|-------|
| Architecture | Qwen2.5 (64 layers, 32B parameters) |
| Merge Method | SLERP |
| Base Model | [Qwen/Qwen2.5-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct) |
| Domain Fine-tune | [shaafsalman/qwen-2.5-32B](https://huggingface.co/shaafsalman/qwen-2.5-32B) |
| Dtype | bfloat16 |
| Library | Transformers |

## Merge Configuration

```yaml
slices:
  - sources:
      - model: Qwen/Qwen2.5-32B-Instruct
        layer_range: [0, 64]
      - model: shaafsalman/qwen-2.5-32B
        layer_range: [0, 64]
merge_method: slerp
base_model: Qwen/Qwen2.5-32B-Instruct
tokenizer_source: Qwen/Qwen2.5-32B-Instruct
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5
dtype: bfloat16
```

**SLERP interpolation weights by layer type:**

| Layer type | Interpolation pattern |
|------------|-----------------------|
| Self-attention | `[0, 0.5, 0.3, 0.7, 1]` — sweeps from base to fine-tune |
| MLP | `[1, 0.5, 0.7, 0.3, 0]` — inverse sweep |
| Other (norms, embeddings) | `0.5` — equal blend |

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "shaafsalman/MedQWEN-2.5-32B"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype="bfloat16",
    device_map="auto",
)

messages = [{"role": "user", "content": "What are the symptoms of hypomagnesemia?"}]
text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(text, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=512)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## Evaluation

Evaluated on [MedAgentBench](https://huggingface.co/datasets/shaafsalman/MedAgentBench-Tasks) — a FHIR-based clinical agentic benchmark covering 300 tasks across 10 clinical task types including lab retrieval, medication ordering, and referral management.
