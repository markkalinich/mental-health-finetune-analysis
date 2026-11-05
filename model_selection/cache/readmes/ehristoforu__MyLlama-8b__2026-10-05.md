---
base_model:
- NousResearch/Meta-Llama-3-8B-Instruct
- Muhammad2003/Llama3-8B-OpenHermes-DPO
- Kukedlc/LLama-3-8b-Maths
- IlyaGusev/saiga_llama3_8b
- ruslanmv/Medical-Llama3-8B
library_name: transformers
tags:
- mergekit
- merge

---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [TIES](https://arxiv.org/abs/2306.01708) merge method using [NousResearch/Meta-Llama-3-8B-Instruct](https://huggingface.co/NousResearch/Meta-Llama-3-8B-Instruct) as a base.

### Models Merged

The following models were included in the merge:
* [Muhammad2003/Llama3-8B-OpenHermes-DPO](https://huggingface.co/Muhammad2003/Llama3-8B-OpenHermes-DPO)
* [Kukedlc/LLama-3-8b-Maths](https://huggingface.co/Kukedlc/LLama-3-8b-Maths)
* [IlyaGusev/saiga_llama3_8b](https://huggingface.co/IlyaGusev/saiga_llama3_8b)
* [ruslanmv/Medical-Llama3-8B](https://huggingface.co/ruslanmv/Medical-Llama3-8B)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: NousResearch/Meta-Llama-3-8B-Instruct
    # no parameters necessary for base model
  - model: IlyaGusev/saiga_llama3_8b
    parameters:
      density: 0.5
      weight: 0.5
  - model: Muhammad2003/Llama3-8B-OpenHermes-DPO
    parameters:
      density: 0.5
      weight: 0.5
  - model: ruslanmv/Medical-Llama3-8B
    parameters:
      density: 0.5
      weight: 0.5
  - model: Kukedlc/LLama-3-8b-Maths
    parameters:
      density: 0.5
      weight: 0.5
merge_method: ties
base_model: NousResearch/Meta-Llama-3-8B-Instruct
parameters:
  normalize: true
dtype: bfloat16

```
