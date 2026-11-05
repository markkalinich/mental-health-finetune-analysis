---
base_model: []
library_name: transformers
tags:
- mergekit
- merge

---
# final_merge_medical

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [DARE](https://arxiv.org/abs/2311.03099) [TIES](https://arxiv.org/abs/2306.01708) merge method using ./evol_merge_storage_medical/input_models/Llama-2-7b-hf_1207016536 as a base.

### Models Merged

The following models were included in the merge:
* ./evol_merge_storage_medical/input_models/meditron-7b_535713315

### Configuration

The following YAML configuration was used to produce this model:

```yaml
base_model: ./evol_merge_storage_medical/input_models/Llama-2-7b-hf_1207016536
dtype: bfloat16
merge_method: dare_ties
parameters:
  int8_mask: 1.0
  normalize: 1.0
slices:
- sources:
  - layer_range: [0, 4]
    model: ./evol_merge_storage_medical/input_models/meditron-7b_535713315
    parameters:
      density: 0.992384363500622
      weight: 0.12828024613059025
  - layer_range: [0, 4]
    model: ./evol_merge_storage_medical/input_models/Llama-2-7b-hf_1207016536
    parameters:
      density: 1.0
      weight: 0.2043801834581346
- sources:
  - layer_range: [4, 8]
    model: ./evol_merge_storage_medical/input_models/meditron-7b_535713315
    parameters:
      density: 0.8166617869585223
      weight: 0.5073401926353303
  - layer_range: [4, 8]
    model: ./evol_merge_storage_medical/input_models/Llama-2-7b-hf_1207016536
    parameters:
      density: 0.9502278365422492
      weight: 0.9538077350045424
- sources:
  - layer_range: [8, 12]
    model: ./evol_merge_storage_medical/input_models/meditron-7b_535713315
    parameters:
      density: 0.9729859873278464
      weight: 0.24983126895812832
  - layer_range: [8, 12]
    model: ./evol_merge_storage_medical/input_models/Llama-2-7b-hf_1207016536
    parameters:
      density: 1.0
      weight: 0.36977171041903323
- sources:
  - layer_range: [12, 16]
    model: ./evol_merge_storage_medical/input_models/meditron-7b_535713315
    parameters:
      density: 0.942566643987019
      weight: 0.25604084632369556
  - layer_range: [12, 16]
    model: ./evol_merge_storage_medical/input_models/Llama-2-7b-hf_1207016536
    parameters:
      density: 1.0
      weight: 0.3479493989699756
- sources:
  - layer_range: [16, 20]
    model: ./evol_merge_storage_medical/input_models/meditron-7b_535713315
    parameters:
      density: 0.9937376494167793
      weight: 0.18395490495846406
  - layer_range: [16, 20]
    model: ./evol_merge_storage_medical/input_models/Llama-2-7b-hf_1207016536
    parameters:
      density: 1.0
      weight: 0.11572624333070619
- sources:
  - layer_range: [20, 24]
    model: ./evol_merge_storage_medical/input_models/meditron-7b_535713315
    parameters:
      density: 0.784005177941743
      weight: 0.5101432868743351
  - layer_range: [20, 24]
    model: ./evol_merge_storage_medical/input_models/Llama-2-7b-hf_1207016536
    parameters:
      density: 0.7983003243622248
      weight: 0.6687460577953303
- sources:
  - layer_range: [24, 28]
    model: ./evol_merge_storage_medical/input_models/meditron-7b_535713315
    parameters:
      density: 0.5794040987288581
      weight: 0.5522697341347537
  - layer_range: [24, 28]
    model: ./evol_merge_storage_medical/input_models/Llama-2-7b-hf_1207016536
    parameters:
      density: 1.0
      weight: 0.8057676781293861
- sources:
  - layer_range: [28, 32]
    model: ./evol_merge_storage_medical/input_models/meditron-7b_535713315
    parameters:
      density: 0.960066282337993
      weight: 0.6270458624800975
  - layer_range: [28, 32]
    model: ./evol_merge_storage_medical/input_models/Llama-2-7b-hf_1207016536
    parameters:
      density: 0.9877495522716813
      weight: 0.15281690912944845
```
