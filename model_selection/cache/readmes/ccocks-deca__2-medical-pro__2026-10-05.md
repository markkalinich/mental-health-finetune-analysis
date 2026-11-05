---
base_model:
- aaditya/Llama3-OpenBioLLM-70B
- deepseek-ai/DeepSeek-R1-Distill-Llama-70B
library_name: transformers
tags:
- mergekit
- merge

---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [SLERP](https://en.wikipedia.org/wiki/Slerp) merge method.

### Models Merged

The following models were included in the merge:
* [aaditya/Llama3-OpenBioLLM-70B](https://huggingface.co/aaditya/Llama3-OpenBioLLM-70B)
* [deepseek-ai/DeepSeek-R1-Distill-Llama-70B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-70B)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: deepseek-ai/DeepSeek-R1-Distill-Llama-70B
    #no parameters necessary for base model
  - model: aaditya/Llama3-OpenBioLLM-70B
    parameters:
      density: 0.6
      weight: 0.6

merge_method: slerp
base_model: deepseek-ai/DeepSeek-R1-Distill-Llama-70B
parameters:
  t: [0, 0, 0.5, 1]
dtype: bfloat16
```
