---
base_model:
- Gaivoronsky/Mistral-7B-Saiga
- cognitivecomputations/dolphin-2.2.1-mistral-7b
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
* [Gaivoronsky/Mistral-7B-Saiga](https://huggingface.co/Gaivoronsky/Mistral-7B-Saiga)
* [cognitivecomputations/dolphin-2.2.1-mistral-7b](https://huggingface.co/cognitivecomputations/dolphin-2.2.1-mistral-7b)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
slices:
- sources:
  - model: Gaivoronsky/Mistral-7B-Saiga
    layer_range:
    - 0
    - 32
  - model: cognitivecomputations/dolphin-2.2.1-mistral-7b
    layer_range:
    - 0
    - 32
merge_method: slerp
base_model: Gaivoronsky/Mistral-7B-Saiga
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
