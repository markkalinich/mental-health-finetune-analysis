---
base_model:
- prithivMLmods/Phi-4-Empathetic
- prithivMLmods/Megatron-Opus-14B-2.0
library_name: transformers
tags:
- mergekit
- merge

---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [SLERP](https://en.wikipedia.org/wiki/Slerp) merge method.

### Models Merged

The following models were included in the merge:
* [prithivMLmods/Phi-4-Empathetic](https://huggingface.co/prithivMLmods/Phi-4-Empathetic)
* [prithivMLmods/Megatron-Opus-14B-2.0](https://huggingface.co/prithivMLmods/Megatron-Opus-14B-2.0)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
slices:
  - sources:
      - model: prithivMLmods/Phi-4-Empathetic
        layer_range: [0, 40]
      - model: prithivMLmods/Megatron-Opus-14B-2.0
        layer_range: [0, 40]
merge_method: slerp
base_model: prithivMLmods/Megatron-Opus-14B-2.0
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5
dtype: bfloat16
```
