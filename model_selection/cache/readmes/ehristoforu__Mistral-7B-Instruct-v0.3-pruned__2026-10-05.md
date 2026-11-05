---
base_model:
- mistralai/Mistral-7B-Instruct-v0.3
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
* [mistralai/Mistral-7B-Instruct-v0.3](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
slices:
  - sources:
      - model: mistralai/Mistral-7B-Instruct-v0.3
        layer_range: [0, 21]
  - sources:
      - model: mistralai/Mistral-7B-Instruct-v0.3
        layer_range: [29,32]
            
merge_method: passthrough
dtype: bfloat16
```
