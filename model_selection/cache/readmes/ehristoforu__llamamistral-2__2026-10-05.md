---
base_model:
- OpenBuddy/openbuddy-mistral-7b-v13.1
- David-Xu/Mistral-7B-Instruct-v0.2
- NousResearch/Meta-Llama-3-8B-Instruct
library_name: transformers
tags:
- mergekit
- merge

---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [TIES](https://arxiv.org/abs/2306.01708) merge method using [David-Xu/Mistral-7B-Instruct-v0.2](https://huggingface.co/David-Xu/Mistral-7B-Instruct-v0.2) as a base.

### Models Merged

The following models were included in the merge:
* [OpenBuddy/openbuddy-mistral-7b-v13.1](https://huggingface.co/OpenBuddy/openbuddy-mistral-7b-v13.1)
* [NousResearch/Meta-Llama-3-8B-Instruct](https://huggingface.co/NousResearch/Meta-Llama-3-8B-Instruct)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: David-Xu/Mistral-7B-Instruct-v0.2
    #no parameters necessary for base model
  - model: OpenBuddy/openbuddy-mistral-7b-v13.1
    parameters:
      density: 0.5
      weight: 0.5
  - model: NousResearch/Meta-Llama-3-8B-Instruct
    parameters:
      density: 0.5
      weight: 0.5
      weight: 0.5

merge_method: ties
base_model: David-Xu/Mistral-7B-Instruct-v0.2
parameters:
  normalize: true
  int8_mask: true
dtype: bfloat16

```
