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

This model was merged using the Passthrough merge method.

### Models Merged

The following models were included in the merge:
* [OdiaGenAI/mistral_hindi_7b_base_v1](https://huggingface.co/OdiaGenAI/mistral_hindi_7b_base_v1)
* [BioMistral/BioMistral-7B](https://huggingface.co/BioMistral/BioMistral-7B)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
dtype: float16
merge_method: passthrough
modules:
  default:
    slices:
    - sources:
      - layer_range: [0, 24]
        model: BioMistral/BioMistral-7B
    - sources:
      - layer_range: [20, 32]
        model: OdiaGenAI/mistral_hindi_7b_base_v1
```
