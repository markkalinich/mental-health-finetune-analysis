---
library_name: transformers
license: apache-2.0
base_model:
- answerdotai/ModernBERT-large
tags:
- climate
- ModernBERT
- toxic
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: climate-guard-classifier
  results: []
datasets:
- QuotaClimat/frugalaichallenge-text-train
- tdiggelm/climate_fever
- takara-ai/QuotaClimat
- Tonic/Climate-Guard-Toxic-Agent
language:
- en
---

# Climate Guard Toxic Agent - ModernBERT Classifier for Climate Disinformation

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on the [Tonic/climate-guard-toxic-agent](https://huggingface.co/datasets/Tonic/Climate-Guard-Toxic-Agent) dataset.
It achieves the following results on the evaluation set:
- Loss: 4.9405
- Accuracy: 0.4774
- F1: 0.4600
- Precision: 0.6228
- Recall: 0.4774
- F1 0 Not Relevant: 0.5064
- F1 1 Not Happening: 0.6036
- F1 2 Not Human: 0.3804
- F1 3 Not Bad: 0.4901
- F1 4 Solutions Harmful Unnecessary: 0.3382
- F1 5 Science Is Unreliable: 0.4126
- F1 6 Proponents Biased: 0.4433
- F1 7 Fossil Fuels Needed: 0.4752

## Model description

This model implements a novel approach to classifying climate change skepticism arguments 
    by using only synthetic data. The base architecture uses ModernBERT with an accuracy of 99.45% on the validation dataset which is the entire [QuotaClimat](QuotaClimat/frugalaichallenge-text-train) dataset.

    The model categorizes text into the following climate change denial types:

- `label`: Following categories:
  - `0_not_relevant`: No relevant claim detected or claims that don't fit other categories
  - `1_not_happening`: Claims denying the occurrence of global warming and its effects - Global warming is not happening. Climate change is NOT leading to melting ice (such as glaciers, sea ice, and permafrost), increased extreme weather, or rising sea levels. Cold weather also shows that climate change is not happening
  - `2_not_human`: Claims denying human responsibility in climate change - Greenhouse gases from humans are not the causing climate change.
  - `3_not_bad`: Claims minimizing or denying negative impacts of climate change - The impacts of climate change will not be bad and might even be beneficial.
  - `4_solutions_harmful_unnecessary`: Claims against climate solutions - Climate solutions are harmful or unnecessary
  - `5_science_is_unreliable`: Claims questioning climate science validity - Climate science is uncertain, unsound, unreliable, or biased.
  - `6_proponents_biased`: Claims attacking climate scientists and activists - Climate scientists and proponents of climate action are alarmist, biased, wrong, hypocritical, corrupt, and/or politically motivated.
  - `7_fossil_fuels_needed`: Claims promoting fossil fuel necessity - We need fossil fuels for economic growth, prosperity, and to maintain our standard of living.    

## Intended uses & limitations

This model can be used for multi-class text classification tasks where the input text needs to be categorized into one of the eight predefined classes. It is particularly suited for datasets with class imbalance, thanks to its weighted loss function.

## Training and evaluation data


### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 32
- seed: 22
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 7
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step  | Validation Loss | Accuracy | F1     | Precision | Recall | F1 0 Not Relevant | F1 1 Not Happening | F1 2 Not Human | F1 3 Not Bad | F1 4 Solutions Harmful Unnecessary | F1 5 Science Is Unreliable | F1 6 Proponents Biased | F1 7 Fossil Fuels Needed |
|:-------------:|:------:|:-----:|:---------------:|:--------:|:------:|:---------:|:------:|:-----------------:|:------------------:|:--------------:|:------------:|:----------------------------------:|:--------------------------:|:----------------------:|:------------------------:|
| 0.4502        | 1.0    | 2324  | 0.2539          | 0.9214   | 0.9208 | 0.9256    | 0.9214 | 0.8674            | 0.8627             | 0.9116         | 0.9473       | 0.9461                             | 0.9092                     | 0.9277                 | 0.9683                   |
| 0.3061        | 2.0    | 4648  | 0.1701          | 0.9446   | 0.9447 | 0.9461    | 0.9446 | 0.8858            | 0.9185             | 0.9295         | 0.9574       | 0.9628                             | 0.9450                     | 0.9446                 | 0.9750                   |
| 0.1339        | 3.0    | 6972  | 0.2239          | 0.9499   | 0.9499 | 0.9502    | 0.9499 | 0.8900            | 0.9412             | 0.9506         | 0.9469       | 0.9611                             | 0.9506                     | 0.9364                 | 0.9786                   |
| 0.0217        | 4.0    | 9296  | 0.3198          | 0.9517   | 0.9517 | 0.9520    | 0.9517 | 0.9073            | 0.9430             | 0.9520         | 0.9561       | 0.9542                             | 0.9537                     | 0.9369                 | 0.9771                   |
| 0.0032        | 5.0    | 11620 | 0.3009          | 0.9530   | 0.9530 | 0.9531    | 0.9530 | 0.9007            | 0.9408             | 0.9553         | 0.9565       | 0.9602                             | 0.9525                     | 0.9388                 | 0.9815                   |
| 0.0001        | 6.0    | 13944 | 0.3055          | 0.9538   | 0.9537 | 0.9537    | 0.9538 | 0.9055            | 0.9424             | 0.9536         | 0.9590       | 0.9589                             | 0.9540                     | 0.9413                 | 0.9802                   |
| 0.0028        | 6.9972 | 16261 | 0.3108          | 0.9529   | 0.9529 | 0.9529    | 0.9529 | 0.9055            | 0.9413             | 0.9541         | 0.9574       | 0.9564                             | 0.9541                     | 0.9403                 | 0.9792                   |


### Framework versions

- Transformers 4.48.3
- Pytorch 2.6.0+cu124
- Datasets 3.2.0
- Tokenizers 0.21.0