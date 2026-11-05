---
base_model:
- victunes/TherapyLlama-8B-v1
- herisan/llama-3-8b_mental_health_counseling_conversations
- TheSkullery/llama-3-cat-8b-instruct-v1
library_name: transformers
tags:
- mergekit
- merge

---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [task arithmetic](https://arxiv.org/abs/2212.04089) merge method using [TheSkullery/llama-3-cat-8b-instruct-v1](https://huggingface.co/TheSkullery/llama-3-cat-8b-instruct-v1) as a base.

### Models Merged

The following models were included in the merge:
* [victunes/TherapyLlama-8B-v1](https://huggingface.co/victunes/TherapyLlama-8B-v1)
* [herisan/llama-3-8b_mental_health_counseling_conversations](https://huggingface.co/herisan/llama-3-8b_mental_health_counseling_conversations)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
slices:
- sources:
  - model: TheSkullery/llama-3-cat-8b-instruct-v1
    layer_range: [0, 32]
  - model: victunes/TherapyLlama-8B-v1
    layer_range: [0, 32]
    parameters:
      weight: 0.25
  - model: herisan/llama-3-8b_mental_health_counseling_conversations
    layer_range: [0, 32]
    parameters:
      weight: 0.25
merge_method: task_arithmetic
base_model: TheSkullery/llama-3-cat-8b-instruct-v1
dtype: bfloat16
```
