---
base_model:
- ank028/Llama-3.2-1B-Instruct-medmcqa
- meta-llama/Llama-3.2-1B-Instruct
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

This model was merged using the [TIES](https://arxiv.org/abs/2306.01708) merge method using [meta-llama/Llama-3.2-1B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct) as a base.

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
      density: 0.5 # density gradient
      weight: 1.0
  - model: autoprogrammer/Llama-3.2-1B-Instruct-MGSM8K-sft1
    parameters:
      density: 0.5
      weight: 0.5 # weight gradient
merge_method: ties
base_model: meta-llama/Llama-3.2-1B-Instruct
parameters:
  normalize: true
  int8_mask: false
dtype: float16
name: Llama-3.2-1B-Instruct-medmcqa-MGSM8K-sft1-ties
```
