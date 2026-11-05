---
base_model:
- gradientai/Llama-3-8B-Instruct-Gradient-4194k
- OpenBuddy/openbuddy-llama3-8b-v21.1-8k
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
* [gradientai/Llama-3-8B-Instruct-Gradient-4194k](https://huggingface.co/gradientai/Llama-3-8B-Instruct-Gradient-4194k)
* [OpenBuddy/openbuddy-llama3-8b-v21.1-8k](https://huggingface.co/OpenBuddy/openbuddy-llama3-8b-v21.1-8k)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
slices:
  - sources:
    - model: gradientai/Llama-3-8B-Instruct-Gradient-4194k
      layer_range: [0, 24]
  - sources:
    - model:  OpenBuddy/openbuddy-llama3-8b-v21.1-8k
      layer_range: [8, 32]
merge_method: passthrough
dtype: bfloat16
```
