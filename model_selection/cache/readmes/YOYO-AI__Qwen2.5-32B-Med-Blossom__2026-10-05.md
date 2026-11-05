---
base_model:
- arcee-ai/Virtuoso-Medium-v2
- Qwen/Qwen2.5-32B
- Azure99/Blossom-V6-32B
library_name: transformers
tags:
- mergekit
- merge

---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [DELLA](https://arxiv.org/abs/2406.11617) merge method using [Qwen/Qwen2.5-32B](https://huggingface.co/Qwen/Qwen2.5-32B) as a base.

### Models Merged

The following models were included in the merge:
* [arcee-ai/Virtuoso-Medium-v2](https://huggingface.co/arcee-ai/Virtuoso-Medium-v2)
* [Azure99/Blossom-V6-32B](https://huggingface.co/Azure99/Blossom-V6-32B)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:  
  - model: Azure99/Blossom-V6-32B  
    parameters:  
      density: 1  
      weight: 1  
      lambda: 0.9
  - model: arcee-ai/Virtuoso-Medium-v2  
    parameters:  
      density: 1  
      weight: 1  
      lambda: 0.9  
merge_method: della  
base_model: Qwen/Qwen2.5-32B  
parameters:  
  density: 1  
  weight: 1  
  lambda: 0.9  
  normalize: true  
  int8_mask: true  
dtype: bfloat16  
tokenizer_source: base  
```
