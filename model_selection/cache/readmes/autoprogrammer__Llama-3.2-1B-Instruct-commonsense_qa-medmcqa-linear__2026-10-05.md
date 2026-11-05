---
base_model:
- ank028/Llama-3.2-1B-Instruct-medmcqa
- ank028/Llama-3.2-1B-Instruct-commonsense_qa
library_name: transformers
tags:
- mergekit
- merge

---
# outputmodels

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [linear](https://arxiv.org/abs/2203.05482) merge method.

### Models Merged

The following models were included in the merge:
* [ank028/Llama-3.2-1B-Instruct-medmcqa](https://huggingface.co/ank028/Llama-3.2-1B-Instruct-medmcqa)
* [ank028/Llama-3.2-1B-Instruct-commonsense_qa](https://huggingface.co/ank028/Llama-3.2-1B-Instruct-commonsense_qa)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: ank028/Llama-3.2-1B-Instruct-commonsense_qa
    parameters:
      weight: 1.0
  - model: ank028/Llama-3.2-1B-Instruct-medmcqa
    parameters:
      weight: 1.0
merge_method: linear
dtype: float16

```
