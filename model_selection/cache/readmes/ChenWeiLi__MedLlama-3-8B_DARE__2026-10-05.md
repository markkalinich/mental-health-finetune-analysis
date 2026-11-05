---
base_model:
- sethuiyer/Medichat-Llama3-8B
- mlabonne/ChimeraLlama-3-8B-v3
- johnsnowlabs/JSL-MedLlama-3-8B-v2.0
library_name: transformers
tags:
- mergekit
- merge
license: llama3
---
# medLlama-3-8B_DARE

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [DARE](https://arxiv.org/abs/2311.03099) [TIES](https://arxiv.org/abs/2306.01708) merge method using [mlabonne/ChimeraLlama-3-8B-v3](https://huggingface.co/mlabonne/ChimeraLlama-3-8B-v3) as a base.

### Models Merged

The following models were included in the merge:
* [sethuiyer/Medichat-Llama3-8B](https://huggingface.co/sethuiyer/Medichat-Llama3-8B)
* [johnsnowlabs/JSL-MedLlama-3-8B-v2.0](https://huggingface.co/johnsnowlabs/JSL-MedLlama-3-8B-v2.0)

### Evaluation

- multimedq (0 shot) </br>
  
|             Tasks             |Version|Filter|n-shot| Metric |Value |   |Stderr|
|-------------------------------|-------|------|-----:|--------|-----:|---|-----:|
| - medmcqa                     |Yaml   |none  |     0|acc     |0.5728|±  |0.0076|
|                               |       |none  |     0|acc_norm|0.5728|±  |0.0076|
| - medqa_4options              |Yaml   |none  |     0|acc     |0.5923|±  |0.0138|
|                               |       |none  |     0|acc_norm|0.5923|±  |0.0138|
| - anatomy (mmlu)              |      0|none  |     0|acc     |0.7111|±  |0.0392|
| - clinical_knowledge (mmlu)   |      0|none  |     0|acc     |0.7547|±  |0.0265|
| - college_biology (mmlu)      |      0|none  |     0|acc     |0.7917|±  |0.0340|
| - college_medicine (mmlu)     |      0|none  |     0|acc     |0.6647|±  |0.0360|
| - medical_genetics (mmlu)     |      0|none  |     0|acc     |0.8200|±  |0.0386|
| - professional_medicine (mmlu)|      0|none  |     0|acc     |0.7426|±  |0.0266|
|stem                           |N/A    |none  |     0|acc_norm|0.5773|±  |0.0067|
|                               |       |none  |     0|acc     |0.6145|±  |0.0057|
| - pubmedqa                    |      1|none  |     0|acc     |0.7400|±  |0.0196|

|Groups|Version|Filter|n-shot| Metric |Value |   |Stderr|
|------|-------|------|-----:|--------|-----:|---|-----:|
|stem  |N/A    |none  |     0|acc_norm|0.5773|±  |0.0067|
|      |       |none  |     0|acc     |0.6145|±  |0.0057|

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: mlabonne/ChimeraLlama-3-8B-v3
    # No parameters necessary for base model

  - model: sethuiyer/Medichat-Llama3-8B
    parameters:
      density: 0.53
      weight: 0.5
  - model: johnsnowlabs/JSL-MedLlama-3-8B-v2.0
    parameters:
      density: 0.53
      weight: 0.5
      
merge_method: dare_ties
base_model: mlabonne/ChimeraLlama-3-8B-v3
parameters:
  int8_mask: true
dtype: float16

```