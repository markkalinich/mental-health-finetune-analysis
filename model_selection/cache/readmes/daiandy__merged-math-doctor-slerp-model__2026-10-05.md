---
base_model:
- daiandy/math-model
- daiandy/doctor-model
library_name: transformers
tags:
- mergekit
- merge

---

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the SLERP merge method.

### Models Merged

The following models were included in the merge:
* [daiandy/math-model](https://huggingface.co/daiandy/math-model)
* [daiandy/doctor-model](https://huggingface.co/daiandy/doctor-model)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
slices:
  - sources:
      - model: daiandy/math-model
        layer_range: [0, 31]
      - model: daiandy/doctor-model
        layer_range: [0, 31]
# or, the equivalent models: syntax:
# models:
#   - model: psmathur/orca_mini_v3_13b
#   - model: garage-bAInd/Platypus2-13B
merge_method: slerp
base_model: daiandy/math-model
parameters:
  t:
    - filter: self_attn
      value: [0.5, 0.5, 0.5, 0.5, 0.5]
    - filter: mlp
      value: [0.5, 0.5, 0.5, 0.5, 0.5]
    - value: 0.5 # fallback for rest of tensors
dtype: float16

```
