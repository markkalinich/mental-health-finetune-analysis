---
base_model:
- autoprogrammer/Llama-3.2-1B-Instruct-MGSM8K-sft1
- ank028/Llama-3.2-1B-Instruct-medmcqa
library_name: transformers
tags:
- mergekit
- merge

---
# m_l

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the SLERP merge method.

### Models Merged

The following models were included in the merge:
* [autoprogrammer/Llama-3.2-1B-Instruct-MGSM8K-sft1](https://huggingface.co/autoprogrammer/Llama-3.2-1B-Instruct-MGSM8K-sft1)
* [ank028/Llama-3.2-1B-Instruct-medmcqa](https://huggingface.co/ank028/Llama-3.2-1B-Instruct-medmcqa)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
slices:
  - sources:
      - model: ank028/Llama-3.2-1B-Instruct-medmcqa
        layer_range: [0, 16]
      - model: autoprogrammer/Llama-3.2-1B-Instruct-MGSM8K-sft1
        layer_range: [0, 16]
merge_method: slerp
base_model: ank028/Llama-3.2-1B-Instruct-medmcqa
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5 # fallback for rest of tensors
dtype: float16
name: Llama-3.2-1B-Instruct-medmcqa-MGSM8K-sft1-slerp
```
