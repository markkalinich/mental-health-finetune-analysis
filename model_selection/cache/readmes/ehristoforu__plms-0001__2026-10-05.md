---
base_model:
- openchat/openchat
- CarperAI/stable-vicuna-13b-delta
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
* [openchat/openchat](https://huggingface.co/openchat/openchat)
* [CarperAI/stable-vicuna-13b-delta](https://huggingface.co/CarperAI/stable-vicuna-13b-delta)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
slices:
- sources:
  - model: openchat/openchat
    layer_range:
    - 0
    - 32
  - model: CarperAI/stable-vicuna-13b-delta
    layer_range:
    - 0
    - 32
merge_method: slerp
base_model: CarperAI/stable-vicuna-13b-delta
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
