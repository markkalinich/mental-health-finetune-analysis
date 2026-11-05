---
base_model:
- NousResearch/Meta-Llama-3-8B
- gradientai/Llama-3-8B-Instruct-Gradient-4194k
- refuelai/Llama-3-Refueled
library_name: transformers
tags:
- mergekit
- merge

---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [DARE](https://arxiv.org/abs/2311.03099) [TIES](https://arxiv.org/abs/2306.01708) merge method using [NousResearch/Meta-Llama-3-8B](https://huggingface.co/NousResearch/Meta-Llama-3-8B) as a base.

### Models Merged

The following models were included in the merge:
* [gradientai/Llama-3-8B-Instruct-Gradient-4194k](https://huggingface.co/gradientai/Llama-3-8B-Instruct-Gradient-4194k)
* [refuelai/Llama-3-Refueled](https://huggingface.co/refuelai/Llama-3-Refueled)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: NousResearch/Meta-Llama-3-8B
    # No parameters necessary for base model
  - model: gradientai/Llama-3-8B-Instruct-Gradient-4194k
    parameters:
      density: 0.6
      weight: 0.5
  - model: refuelai/Llama-3-Refueled
    parameters:
      density: 0.55
      weight: 0.05
merge_method: dare_ties
base_model: NousResearch/Meta-Llama-3-8B
parameters:
  int8_mask: true
dtype: bfloat16
```
