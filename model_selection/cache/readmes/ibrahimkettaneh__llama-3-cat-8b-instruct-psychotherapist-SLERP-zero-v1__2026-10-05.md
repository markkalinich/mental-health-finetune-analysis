---
base_model:
- ibrahimkettaneh/llama-3-8B-chat-psychotherapist-merged
- TheSkullery/llama-3-cat-8b-instruct-v1
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
* [ibrahimkettaneh/llama-3-8B-chat-psychotherapist-merged](https://huggingface.co/ibrahimkettaneh/llama-3-8B-chat-psychotherapist-merged)
* [TheSkullery/llama-3-cat-8b-instruct-v1](https://huggingface.co/TheSkullery/llama-3-cat-8b-instruct-v1)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
slices:
- sources:
  - model: TheSkullery/llama-3-cat-8b-instruct-v1
    layer_range:
    - 0
    - 32
  - model: ibrahimkettaneh/llama-3-8B-chat-psychotherapist-merged
    layer_range:
    - 0
    - 32
merge_method: slerp
base_model: TheSkullery/llama-3-cat-8b-instruct-v1
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
