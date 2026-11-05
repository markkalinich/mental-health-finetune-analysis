---
base_model:
- winninghealth/WiNGPT2-Llama-3-8B-Base
- johnsnowlabs/JSL-MedLlama-3-8B-v1.0
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
* [winninghealth/WiNGPT2-Llama-3-8B-Base](https://huggingface.co/winninghealth/WiNGPT2-Llama-3-8B-Base)
* [johnsnowlabs/JSL-MedLlama-3-8B-v1.0](https://huggingface.co/johnsnowlabs/JSL-MedLlama-3-8B-v1.0)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
slices:
  - sources:
      - model: johnsnowlabs/JSL-MedLlama-3-8B-v1.0
        layer_range: [0, 32]
      - model: winninghealth/WiNGPT2-Llama-3-8B-Base
        layer_range: [0, 32]
merge_method: slerp
base_model: johnsnowlabs/JSL-MedLlama-3-8B-v1.0
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5
dtype: bfloat16
```
