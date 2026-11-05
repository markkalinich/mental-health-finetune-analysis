---
base_model:
- unsloth/Mistral-Nemo-Instruct-2407
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
* [unsloth/Mistral-Nemo-Instruct-2407](https://huggingface.co/unsloth/Mistral-Nemo-Instruct-2407)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
slices:
  - sources:
      - model: unsloth/Mistral-Nemo-Instruct-2407
        layer_range: [0, 21]
  - sources:
      - model: unsloth/Mistral-Nemo-Instruct-2407
        layer_range: [22, 25]
merge_method: passthrough
dtype: bfloat16

```
