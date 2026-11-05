---
base_model:
- David-Xu/Mistral-7B-Instruct-v0.2
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
* [David-Xu/Mistral-7B-Instruct-v0.2](https://huggingface.co/David-Xu/Mistral-7B-Instruct-v0.2)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
slices:
  - sources:
    - model: David-Xu/Mistral-7B-Instruct-v0.2
      layer_range: [0, 24]
  - sources:
    - model:  David-Xu/Mistral-7B-Instruct-v0.2
      layer_range: [8, 32]
merge_method: passthrough
dtype: bfloat16
```
