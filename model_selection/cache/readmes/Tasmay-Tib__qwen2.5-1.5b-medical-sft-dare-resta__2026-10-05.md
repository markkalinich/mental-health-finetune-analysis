---
base_model:
- Qwen/Qwen2.5-1.5B-Instruct
- Tasmay-Tib/qwen2.5-1.5b-medical-sft-dare-p03
library_name: transformers
tags:
- mergekit
- merge

---
# model_sft_dare_resta

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [Task Arithmetic](https://arxiv.org/abs/2212.04089) merge method using [Qwen/Qwen2.5-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct) as a base.

### Models Merged

The following models were included in the merge:
* outputs/part2/model_harmful_full
* [Tasmay-Tib/qwen2.5-1.5b-medical-sft-dare-p03](https://huggingface.co/Tasmay-Tib/qwen2.5-1.5b-medical-sft-dare-p03)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
- model: Qwen/Qwen2.5-1.5B-Instruct
- model: Tasmay-Tib/qwen2.5-1.5b-medical-sft-dare-p03
  parameters:
    weight: 1.0
- model: outputs/part2/model_harmful_full
  parameters:
    weight: -1.0
merge_method: task_arithmetic
base_model: Qwen/Qwen2.5-1.5B-Instruct
parameters:
  normalize: false
dtype: bfloat16

```
