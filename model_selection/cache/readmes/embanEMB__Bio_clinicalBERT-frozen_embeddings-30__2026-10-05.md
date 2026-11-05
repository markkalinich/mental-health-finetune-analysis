---
library_name: transformers
license: mit
base_model: emilyalsentzer/Bio_ClinicalBERT
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: Bio_clinicalBERT-frozen_embeddings-30
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Bio_clinicalBERT-frozen_embeddings-30

This model is a fine-tuned version of [emilyalsentzer/Bio_ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2236
- Accuracy: 0.5153

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.03
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 30

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 115  | 2.2869          | 0.3712   |
| No log        | 2.0   | 230  | 2.0574          | 0.3930   |
| No log        | 3.0   | 345  | 3.3676          | 0.3886   |
| No log        | 4.0   | 460  | 2.4398          | 0.3581   |
| 2.2747        | 5.0   | 575  | 1.8722          | 0.4410   |
| 2.2747        | 6.0   | 690  | 2.1077          | 0.3231   |
| 2.2747        | 7.0   | 805  | 1.9363          | 0.5109   |
| 2.2747        | 8.0   | 920  | 3.5410          | 0.2882   |
| 2.0667        | 9.0   | 1035 | 2.8723          | 0.2795   |
| 2.0667        | 10.0  | 1150 | 2.0155          | 0.4148   |
| 2.0667        | 11.0  | 1265 | 2.4170          | 0.4105   |
| 2.0667        | 12.0  | 1380 | 2.8414          | 0.3188   |
| 2.0667        | 13.0  | 1495 | 1.9712          | 0.4367   |
| 1.9756        | 14.0  | 1610 | 1.8535          | 0.4323   |
| 1.9756        | 15.0  | 1725 | 1.8735          | 0.5109   |
| 1.9756        | 16.0  | 1840 | 1.7002          | 0.4629   |
| 1.9756        | 17.0  | 1955 | 1.4065          | 0.4716   |
| 1.7396        | 18.0  | 2070 | 2.0771          | 0.3799   |
| 1.7396        | 19.0  | 2185 | 2.8953          | 0.3100   |
| 1.7396        | 20.0  | 2300 | 1.5128          | 0.4847   |
| 1.7396        | 21.0  | 2415 | 1.3819          | 0.4629   |
| 1.5953        | 22.0  | 2530 | 1.7965          | 0.4236   |
| 1.5953        | 23.0  | 2645 | 1.4167          | 0.4847   |
| 1.5953        | 24.0  | 2760 | 1.3443          | 0.4891   |
| 1.5953        | 25.0  | 2875 | 1.5971          | 0.4410   |
| 1.5953        | 26.0  | 2990 | 1.4340          | 0.4847   |
| 1.3758        | 27.0  | 3105 | 1.3012          | 0.5022   |
| 1.3758        | 28.0  | 3220 | 1.3027          | 0.4978   |
| 1.3758        | 29.0  | 3335 | 1.3025          | 0.4803   |
| 1.3758        | 30.0  | 3450 | 1.2236          | 0.5153   |


### Framework versions

- Transformers 4.48.3
- Pytorch 2.5.1+cu124
- Tokenizers 0.21.0
