---
base_model:
- google/gemma-3-27b-it
- google/medgemma-27b-it
library_name: transformers
tags:
- mergekit
- merge

---
# medgemma-nuslerp-27b

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the NuSLERP merge method.

### Models Merged

The following models were included in the merge:
* [google/gemma-3-27b-it](https://huggingface.co/google/gemma-3-27b-it)
* [google/medgemma-27b-it](https://huggingface.co/google/medgemma-27b-it)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: google/gemma-3-27b-it
    parameters:
      weight: 1.0
  - model: google/medgemma-27b-it
    parameters: 
      weight: 1.618033988749
merge_method: nuslerp
tokenizer_source: google/gemma-3-27b-it

```
