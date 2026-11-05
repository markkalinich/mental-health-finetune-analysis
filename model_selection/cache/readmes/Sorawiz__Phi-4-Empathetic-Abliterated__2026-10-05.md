---
base_model:
- prithivMLmods/Phi-4-Empathetic
- ngxson/LoRA-phi-4-abliterated
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
* [prithivMLmods/Phi-4-Empathetic](https://huggingface.co/prithivMLmods/Phi-4-Empathetic) + [ngxson/LoRA-phi-4-abliterated](https://huggingface.co/ngxson/LoRA-phi-4-abliterated)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: prithivMLmods/Phi-4-Empathetic+ngxson/LoRA-phi-4-abliterated
merge_method: passthrough
dtype: bfloat16
```
