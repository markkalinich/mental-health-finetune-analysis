---
base_model:
- ank028/Llama-3.2-1B-Instruct-medmcqa
- autoprogrammer/Llama-3.2-1B-Instruct-MGSM8K-sft1
library_name: transformers
tags:
- mergekit
- merge

---
# m_l

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [linear](https://arxiv.org/abs/2203.05482) merge method.

### Models Merged

The following models were included in the merge:
* [ank028/Llama-3.2-1B-Instruct-medmcqa](https://huggingface.co/ank028/Llama-3.2-1B-Instruct-medmcqa)
* [autoprogrammer/Llama-3.2-1B-Instruct-MGSM8K-sft1](https://huggingface.co/autoprogrammer/Llama-3.2-1B-Instruct-MGSM8K-sft1)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: ank028/Llama-3.2-1B-Instruct-medmcqa
    parameters:
      weight: 0.5
  - model: autoprogrammer/Llama-3.2-1B-Instruct-MGSM8K-sft1
    parameters:
      weight: 0.5
merge_method: linear
dtype: float16
name: Llama-3.2-1B-Instruct-medmcqa-MGSM8K-sft1-linear
```
