---
base_model:
- Muhammad2003/Llama3-8B-OpenHermes-DPO
- IlyaGusev/saiga_llama3_8b
- NousResearch/Meta-Llama-3-8B-Instruct
- abacusai/Llama-3-Smaug-8B
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
* [Muhammad2003/Llama3-8B-OpenHermes-DPO](https://huggingface.co/Muhammad2003/Llama3-8B-OpenHermes-DPO)
* [IlyaGusev/saiga_llama3_8b](https://huggingface.co/IlyaGusev/saiga_llama3_8b)
* [NousResearch/Meta-Llama-3-8B-Instruct](https://huggingface.co/NousResearch/Meta-Llama-3-8B-Instruct)
* [abacusai/Llama-3-Smaug-8B](https://huggingface.co/abacusai/Llama-3-Smaug-8B)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
slices:
  - sources:
    - model: IlyaGusev/saiga_llama3_8b
      layer_range: [0, 32]
  - sources:
    - model: Muhammad2003/Llama3-8B-OpenHermes-DPO
      layer_range: [24, 32]
  - sources:
    - model: abacusai/Llama-3-Smaug-8B
      layer_range: [26, 32]
  - sources:
    - model: NousResearch/Meta-Llama-3-8B-Instruct
      layer_range: [28, 32]
merge_method: passthrough
dtype: bfloat16
```
