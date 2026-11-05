---
base_model:
- vihangd/Llama-3-8B-Hindi-Sathi-v0.1
- johnsnowlabs/JSL-MedLlama-3-8B-v1.0
library_name: transformers
tags:
- mergekit
- merge
license: other
---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [DARE TIES](https://arxiv.org/abs/2311.03099) merge method using [johnsnowlabs/JSL-MedLlama-3-8B-v1.0](https://huggingface.co/johnsnowlabs/JSL-MedLlama-3-8B-v1.0) as a base.

### Models Merged

The following models were included in the merge:
* [vihangd/Llama-3-8B-Hindi-Sathi-v0.1](https://huggingface.co/vihangd/Llama-3-8B-Hindi-Sathi-v0.1)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: johnsnowlabs/JSL-MedLlama-3-8B-v1.0
    # No parameters necessary for base model
  - model: vihangd/Llama-3-8B-Hindi-Sathi-v0.1
    parameters:
      density: 0.5
      weight: 0.5
merge_method: dare_ties
base_model: johnsnowlabs/JSL-MedLlama-3-8B-v1.0
parameters:
  int8_mask: true
dtype: bfloat16

```