---
base_model:
- NeverSleep/Noromaid-13b-v0.2
- AdaptLLM/medicine-LLM-13B
tags:
- mergekit
- merge
license: openrail
language:
- en
library_name: transformers
pipeline_tag: text-generation
---

![NOrmaid](6f304230-fa4f-4fdf-9600-1df14b3982f4.png)
# merged

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the SLERP merge method.

### Models Merged

The following models were included in the merge:
* [NeverSleep/Noromaid-13b-v0.2](https://huggingface.co/NeverSleep/Noromaid-13b-v0.2)
* [AdaptLLM/medicine-LLM-13B](https://huggingface.co/AdaptLLM/medicine-LLM-13B)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
base_model: AdaptLLM/medicine-LLM-13B
dtype: bfloat16
merge_method: slerp
parameters:
  t:
  - filter: self_attn
    value: [0.0, 0.5, 0.3, 0.7, 1.0]
  - filter: mlp
    value: [1.0, 0.5, 0.7, 0.3, 0.0]
  - value: 0.5
slices:
- sources:
  - layer_range: [0, 32]
    model: NeverSleep/Noromaid-13b-v0.2
```