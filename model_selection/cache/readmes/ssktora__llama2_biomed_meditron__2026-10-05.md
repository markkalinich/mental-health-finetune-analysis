---
base_model: []
library_name: transformers
tags:
- mergekit
- merge

---
# final_merge_medical2

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [DARE](https://arxiv.org/abs/2311.03099) [TIES](https://arxiv.org/abs/2306.01708) merge method using ./evol_merge_storage_medical2/input_models/Llama-2-7b-hf_1207016536 as a base.

### Models Merged

The following models were included in the merge:
* ./evol_merge_storage_medical2/input_models/meditron-7b_535713315
* ./evol_merge_storage_medical2/input_models/BioMedGPT-LM-7B_1321966785

### Configuration

The following YAML configuration was used to produce this model:

```yaml
base_model: ./evol_merge_storage_medical2/input_models/Llama-2-7b-hf_1207016536
dtype: bfloat16
merge_method: dare_ties
parameters:
  int8_mask: 1.0
  normalize: 1.0
slices:
- sources:
  - layer_range: [0, 4]
    model: ./evol_merge_storage_medical2/input_models/BioMedGPT-LM-7B_1321966785
    parameters:
      density: 1.0
      weight: 0.17884011663118993
  - layer_range: [0, 4]
    model: ./evol_merge_storage_medical2/input_models/Llama-2-7b-hf_1207016536
    parameters:
      density: 0.8890748672494518
      weight: 0.8456004469240137
  - layer_range: [0, 4]
    model: ./evol_merge_storage_medical2/input_models/meditron-7b_535713315
    parameters:
      density: 0.8353965535147524
      weight: 0.39636256675038484
- sources:
  - layer_range: [4, 8]
    model: ./evol_merge_storage_medical2/input_models/BioMedGPT-LM-7B_1321966785
    parameters:
      density: 1.0
      weight: 1.020532319785238
  - layer_range: [4, 8]
    model: ./evol_merge_storage_medical2/input_models/Llama-2-7b-hf_1207016536
    parameters:
      density: 1.0
      weight: 0.40553667157598416
  - layer_range: [4, 8]
    model: ./evol_merge_storage_medical2/input_models/meditron-7b_535713315
    parameters:
      density: 0.8955950669638045
      weight: 0.1256681933865999
- sources:
  - layer_range: [8, 12]
    model: ./evol_merge_storage_medical2/input_models/BioMedGPT-LM-7B_1321966785
    parameters:
      density: 0.8698472775356287
      weight: 0.712509376634506
  - layer_range: [8, 12]
    model: ./evol_merge_storage_medical2/input_models/Llama-2-7b-hf_1207016536
    parameters:
      density: 1.0
      weight: 0.09302230163177483
  - layer_range: [8, 12]
    model: ./evol_merge_storage_medical2/input_models/meditron-7b_535713315
    parameters:
      density: 1.0
      weight: -0.05614416786806742
- sources:
  - layer_range: [12, 16]
    model: ./evol_merge_storage_medical2/input_models/BioMedGPT-LM-7B_1321966785
    parameters:
      density: 1.0
      weight: 0.39694054142633234
  - layer_range: [12, 16]
    model: ./evol_merge_storage_medical2/input_models/Llama-2-7b-hf_1207016536
    parameters:
      density: 1.0
      weight: 0.2626803763724651
  - layer_range: [12, 16]
    model: ./evol_merge_storage_medical2/input_models/meditron-7b_535713315
    parameters:
      density: 0.9657199816167481
      weight: 0.2153132357599829
- sources:
  - layer_range: [16, 20]
    model: ./evol_merge_storage_medical2/input_models/BioMedGPT-LM-7B_1321966785
    parameters:
      density: 0.8289285693717532
      weight: 0.34481743191831266
  - layer_range: [16, 20]
    model: ./evol_merge_storage_medical2/input_models/Llama-2-7b-hf_1207016536
    parameters:
      density: 0.7115155293484904
      weight: 0.03210636463921337
  - layer_range: [16, 20]
    model: ./evol_merge_storage_medical2/input_models/meditron-7b_535713315
    parameters:
      density: 1.0
      weight: 0.23727760414855137
- sources:
  - layer_range: [20, 24]
    model: ./evol_merge_storage_medical2/input_models/BioMedGPT-LM-7B_1321966785
    parameters:
      density: 0.9992577736634561
      weight: 0.33608731549782594
  - layer_range: [20, 24]
    model: ./evol_merge_storage_medical2/input_models/Llama-2-7b-hf_1207016536
    parameters:
      density: 1.0
      weight: 0.2672857028656318
  - layer_range: [20, 24]
    model: ./evol_merge_storage_medical2/input_models/meditron-7b_535713315
    parameters:
      density: 1.0
      weight: 0.4567325333292645
- sources:
  - layer_range: [24, 28]
    model: ./evol_merge_storage_medical2/input_models/BioMedGPT-LM-7B_1321966785
    parameters:
      density: 1.0
      weight: -0.061310476755757834
  - layer_range: [24, 28]
    model: ./evol_merge_storage_medical2/input_models/Llama-2-7b-hf_1207016536
    parameters:
      density: 1.0
      weight: 0.23902257193439966
  - layer_range: [24, 28]
    model: ./evol_merge_storage_medical2/input_models/meditron-7b_535713315
    parameters:
      density: 0.5322311277242968
      weight: 0.37656791069123563
- sources:
  - layer_range: [28, 32]
    model: ./evol_merge_storage_medical2/input_models/BioMedGPT-LM-7B_1321966785
    parameters:
      density: 1.0
      weight: -0.018284769401157808
  - layer_range: [28, 32]
    model: ./evol_merge_storage_medical2/input_models/Llama-2-7b-hf_1207016536
    parameters:
      density: 1.0
      weight: 0.5831277146552916
  - layer_range: [28, 32]
    model: ./evol_merge_storage_medical2/input_models/meditron-7b_535713315
    parameters:
      density: 0.8437643378550103
      weight: 0.1599917740219515
```
