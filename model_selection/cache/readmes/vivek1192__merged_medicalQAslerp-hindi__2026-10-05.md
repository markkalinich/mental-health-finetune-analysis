---
base_model:
- OdiaGenAI/mistral_hindi_7b_base_v1
- BioMistral/BioMistral-7B
library_name: transformers
tags:
- mergekit
- merge

---
# merged_models

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [SLERP](https://en.wikipedia.org/wiki/Slerp) merge method.

### Models Merged

The following models were included in the merge:
* [OdiaGenAI/mistral_hindi_7b_base_v1](https://huggingface.co/OdiaGenAI/mistral_hindi_7b_base_v1)
* [BioMistral/BioMistral-7B](https://huggingface.co/BioMistral/BioMistral-7B)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
base_model: OdiaGenAI/mistral_hindi_7b_base_v1
dtype: float16
merge_method: slerp
modules:
  default:
    slices:
    - sources:
      - layer_range: [0, 32]
        model: BioMistral/BioMistral-7B
        parameters:
          density: 0.5
          weight: 0.5
      - layer_range: [0, 32]
        model: OdiaGenAI/mistral_hindi_7b_base_v1
        parameters:
          density: 0.5
          weight: 0.5
parameters:
  t:
  - filter: self_attn
    value: [0.0, 0.5, 0.3, 0.7, 1.0]
  - filter: mlp
    value: [1.0, 0.5, 0.7, 0.3, 0.0]
  - value: 0.5
```
