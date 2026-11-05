---
license: apache-2.0
tags:
- merge
- mergekit
- llamas-community/LlamaGuard-7b
- ParthasarathyShanmugam/llama-2-7b-samantha
---

# Guardian-Samantha-7b-slerp

Guardian-Samantha-7b-slerp is a merge of the following models using [mergekit](https://github.com/cg123/mergekit):
* [llamas-community/LlamaGuard-7b](https://huggingface.co/llamas-community/LlamaGuard-7b)
* [ParthasarathyShanmugam/llama-2-7b-samantha](https://huggingface.co/ParthasarathyShanmugam/llama-2-7b-samantha)

## 🧩 Configuration

\```yaml{'slices': [{'sources': [{'model': 'llamas-community/LlamaGuard-7b', 'layer_range': [0, 32]}, {'model': 'ParthasarathyShanmugam/llama-2-7b-samantha', 'layer_range': [0, 32]}]}], 'merge_method': 'slerp', 'base_model': 'llamas-community/LlamaGuard-7b', 'parameters': {'t': [{'filter': 'self_attn', 'value': [0, 0.5, 0.3, 0.7, 1]}, {'filter': 'mlp', 'value': [1, 0.5, 0.7, 0.3, 0]}, {'value': 0.5}]}, 'dtype': 'float16'}\```