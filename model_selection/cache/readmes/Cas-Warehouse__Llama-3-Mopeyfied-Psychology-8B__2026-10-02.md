---
base_model:
- Casual-Autopsy/Llama-3-Psychology-LoRA-Stock-8B
- Casual-Autopsy/Llama-3-SOVL-MopeyMule-8B
- Casual-Autopsy/Llama-3-MopeyMule-Blackroot-8B
library_name: transformers
tags:
- mergekit
- merge

---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [task arithmetic](https://arxiv.org/abs/2212.04089) merge method using [Casual-Autopsy/Llama-3-Psychology-LoRA-Stock-8B](https://huggingface.co/Casual-Autopsy/Llama-3-Psychology-LoRA-Stock-8B) as a base.

### Models Merged

The following models were included in the merge:
* [Casual-Autopsy/Llama-3-SOVL-MopeyMule-8B](https://huggingface.co/Casual-Autopsy/Llama-3-SOVL-MopeyMule-8B)
* [Casual-Autopsy/Llama-3-MopeyMule-Blackroot-8B](https://huggingface.co/Casual-Autopsy/Llama-3-MopeyMule-Blackroot-8B)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
slices:
- sources:
  - model: Casual-Autopsy/Llama-3-Psychology-LoRA-Stock-8B
    layer_range: [0, 32]
    parameters:
      weight: 0.6
  - model: Casual-Autopsy/Llama-3-MopeyMule-Blackroot-8B
    layer_range: [0, 32]
    parameters:
      weight: 0.25
  - model: Casual-Autopsy/Llama-3-SOVL-MopeyMule-8B
    layer_range: [0, 32]
    parameters:
      weight: 0.15
merge_method: task_arithmetic
base_model: Casual-Autopsy/Llama-3-Psychology-LoRA-Stock-8B
normalize: False
dtype: bfloat16

```
