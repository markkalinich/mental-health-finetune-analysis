---
base_model:
- Vezora/Mistral-22B-v0.2
- Vezora/Mistral-22B-v0.1
library_name: transformers
tags:
- mergekit
- merge

---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the passthrough merge method.

### Models Merged

The following models were included in the merge:
* [Vezora/Mistral-22B-v0.2](https://huggingface.co/Vezora/Mistral-22B-v0.2)
* [Vezora/Mistral-22B-v0.1](https://huggingface.co/Vezora/Mistral-22B-v0.1)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
slices:
  - sources:
    - model: Vezora/Mistral-22B-v0.2
      layer_range: [0, 24]
  - sources:
    - model:  Vezora/Mistral-22B-v0.1
      layer_range: [8, 32]
merge_method: passthrough
dtype: bfloat16
```
