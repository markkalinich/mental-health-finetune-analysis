---
base_model:
- Nexusflow/Athene-V2-Chat
- Qwen/Qwen2.5-72B-Instruct
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
* [Nexusflow/Athene-V2-Chat](https://huggingface.co/Nexusflow/Athene-V2-Chat)
* [Qwen/Qwen2.5-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
slices:
- sources:
  - layer_range: [0, 40]
    model: Qwen/Qwen2.5-72B-Instruct
- sources:
  - layer_range: [30, 40]
    model: Nexusflow/Athene-V2-Chat
- sources:
  - layer_range: [40, 80]
    model: Qwen/Qwen2.5-72B-Instruct
merge_method: passthrough
dtype: bfloat16
tokenizer_source: "Qwen/Qwen2.5-72B-Instruct"
```
