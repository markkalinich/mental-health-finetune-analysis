---
base_model:
- allura-org/Gemma-3-Glitter-27B
- allura-forge/gemma-3-27b-medglitter-ero
library_name: transformers
tags:
- mergekit
- merge

---
# merged

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [Linear](https://arxiv.org/abs/2203.05482) merge method.

### Models Merged

The following models were included in the merge:
* [allura-org/Gemma-3-Glitter-27B](https://huggingface.co/allura-org/Gemma-3-Glitter-27B)
* [allura-forge/gemma-3-27b-medglitter-ero](https://huggingface.co/allura-forge/gemma-3-27b-medglitter-ero)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: allura-forge/gemma-3-27b-medglitter-ero
    parameters:
      weight: 0.5
  - model: allura-org/Gemma-3-Glitter-27B
    parameters: 
      weight: 0.5
merge_method: linear 
dtype: bfloat16
```
