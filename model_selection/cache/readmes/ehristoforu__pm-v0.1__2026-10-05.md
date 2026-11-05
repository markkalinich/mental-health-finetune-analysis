---
base_model:
- David-Xu/Mistral-7B-Instruct-v0.2
- ajibawa-2023/Code-Mistral-7B
- OpenBuddy/openbuddy-mistral-7b-v13.1
- NousResearch/Yarn-Mistral-7b-128k
- meta-math/MetaMath-Mistral-7B
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
* [ajibawa-2023/Code-Mistral-7B](https://huggingface.co/ajibawa-2023/Code-Mistral-7B)
* [OpenBuddy/openbuddy-mistral-7b-v13.1](https://huggingface.co/OpenBuddy/openbuddy-mistral-7b-v13.1)
* [NousResearch/Yarn-Mistral-7b-128k](https://huggingface.co/NousResearch/Yarn-Mistral-7b-128k)
* [meta-math/MetaMath-Mistral-7B](https://huggingface.co/meta-math/MetaMath-Mistral-7B)

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
  - model: NousResearch/Yarn-Mistral-7b-128k
    parameters:
      density: 0.5
      weight: 0.5
  - model: ajibawa-2023/Code-Mistral-7B
    parameters:
      density: 0.5
      weight: 0.5
  - model: meta-math/MetaMath-Mistral-7B
    parameters:
      density: 0.5
      weight: 0.5


merge_method: ties
base_model: David-Xu/Mistral-7B-Instruct-v0.2
parameters:
  normalize: true
  int8_mask: true
dtype: bfloat16
```
