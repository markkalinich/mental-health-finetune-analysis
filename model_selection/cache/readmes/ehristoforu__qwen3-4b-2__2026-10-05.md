---
base_model:
- Qwen/Qwen3-4B
- Menlo/Jan-nano
- POLARIS-Project/Polaris-4B-Preview
library_name: transformers
tags:
- mergekit
- merge

---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [Model Stock](https://arxiv.org/abs/2403.19522) merge method using [Qwen/Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B) as a base.

### Models Merged

The following models were included in the merge:
* [Menlo/Jan-nano](https://huggingface.co/Menlo/Jan-nano)
* [POLARIS-Project/Polaris-4B-Preview](https://huggingface.co/POLARIS-Project/Polaris-4B-Preview)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: Menlo/Jan-nano
  - model: POLARIS-Project/Polaris-4B-Preview
merge_method: model_stock
base_model: Qwen/Qwen3-4B
normalize: true
int8_mask: true
dtype: bfloat16
```
