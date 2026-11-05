---
base_model:
- BioMistral/BioMistral-7B
- mistralai/Mistral-7B-v0.1
- OdiaGenAI/mistral_hindi_7b_base_v1
library_name: transformers
tags:
- mergekit
- merge

---
# merged_models

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [DELLA](https://arxiv.org/abs/2406.11617) merge method using [mistralai/Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1) as a base.

### Models Merged

The following models were included in the merge:
* [BioMistral/BioMistral-7B](https://huggingface.co/BioMistral/BioMistral-7B)
* [OdiaGenAI/mistral_hindi_7b_base_v1](https://huggingface.co/OdiaGenAI/mistral_hindi_7b_base_v1)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
base_model: mistralai/Mistral-7B-v0.1
dtype: float16
merge_method: della
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
      - layer_range: [0, 32]
        model: mistralai/Mistral-7B-v0.1
parameters:
  int8_mask: 1.0
  normalize: 0.0
```
