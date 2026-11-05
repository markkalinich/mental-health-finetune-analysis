---
base_model:
- tiiuae/Falcon3-10B-Instruct
- tiiuae/Falcon3-10B-Base
library_name: transformers
tags:
- mergekit
- merge

---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the SLERP merge method.

### Models Merged

The following models were included in the merge:
* [tiiuae/Falcon3-10B-Instruct](https://huggingface.co/tiiuae/Falcon3-10B-Instruct)
* [tiiuae/Falcon3-10B-Base](https://huggingface.co/tiiuae/Falcon3-10B-Base)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
slices:
- sources:
  - model: tiiuae/Falcon3-10B-Instruct
    layer_range:
    - 0
    - 32
  - model: tiiuae/Falcon3-10B-Base
    layer_range:
    - 0
    - 32
merge_method: slerp
base_model: tiiuae/Falcon3-10B-Instruct
parameters:
  t:
  - filter: self_attn
    value:
    - 0
    - 0.5
    - 0.3
    - 0.7
    - 1
  - filter: mlp
    value:
    - 1
    - 0.5
    - 0.7
    - 0.3
    - 0
  - value: 0.5
dtype: bfloat16
```
