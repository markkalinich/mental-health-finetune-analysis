---
license: apache-2.0
tags:
- merge
- mergekit
- chaoyi-wu/MedLLaMA_13B
- lmsys/vicuna-13b-v1.3
---

# arcee-ai/MedLLaMA-Vicuna-13B-Slerp

arcee-ai/MedLLaMA-Vicuna-13B-Slerp is a merge of the following models using [mergekit](https://github.com/cg123/mergekit):
* [chaoyi-wu/MedLLaMA_13B](https://huggingface.co/chaoyi-wu/MedLLaMA_13B)
* [lmsys/vicuna-13b-v1.3](https://huggingface.co/lmsys/vicuna-13b-v1.3)

## 🧩 Configuration

```yaml
slices:
  - sources:
      - model: chaoyi-wu/MedLLaMA_13B
        layer_range: [0, 40]
      - model: lmsys/vicuna-13b-v1.3
        layer_range: [0, 40]
merge_method: slerp
base_model: lmsys/vicuna-13b-v1.3
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5
dtype: bfloat16

```