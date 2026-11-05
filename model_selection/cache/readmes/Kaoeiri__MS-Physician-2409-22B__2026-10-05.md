---
base_model:
- unsloth/Mistral-Small-Instruct-2409
- benhaotang/mistral-small-physics-finetuned-adapter
library_name: transformers
tags:
- mergekit
- merge

---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [task arithmetic](https://arxiv.org/abs/2212.04089) merge method using [unsloth/Mistral-Small-Instruct-2409](https://huggingface.co/unsloth/Mistral-Small-Instruct-2409) + [benhaotang/mistral-small-physics-finetuned-adapter](https://huggingface.co/benhaotang/mistral-small-physics-finetuned-adapter) as a base.

### Models Merged

The following models were included in the merge:


### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
 - model: unsloth/Mistral-Small-Instruct-2409+benhaotang/mistral-small-physics-finetuned-adapter

base_model: unsloth/Mistral-Small-Instruct-2409+benhaotang/mistral-small-physics-finetuned-adapter
merge_method: task_arithmetic
parameters:
  normalize: false

dtype: bfloat16
tokenizer_source: union
```
