---
base_model:
- maywell/Synatra-7B-v0.3-RP
- stephenlzc/Mistral-7B-v0.3-Chinese-Chat-uncensored
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
* [maywell/Synatra-7B-v0.3-RP](https://huggingface.co/maywell/Synatra-7B-v0.3-RP)
* [stephenlzc/Mistral-7B-v0.3-Chinese-Chat-uncensored](https://huggingface.co/stephenlzc/Mistral-7B-v0.3-Chinese-Chat-uncensored)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
slices:
  - sources:
      - model: maywell/Synatra-7B-v0.3-RP
        layer_range: [0, 32]
      - model: stephenlzc/Mistral-7B-v0.3-Chinese-Chat-uncensored
        layer_range: [0, 32]
merge_method: slerp
base_model: stephenlzc/Mistral-7B-v0.3-Chinese-Chat-uncensored
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5
dtype: bfloat16

```
