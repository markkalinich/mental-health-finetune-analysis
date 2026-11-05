---
library_name: transformers
language:
- ko
license: mit
base_model: beomi/KcELECTRA-base-v2022
tags:
- absa
- sentiment-analysis
- aspect-based-sentiment-analysis
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: kcELECTRA-absa
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# kcELECTRA-absa

This model is a fine-tuned version of [beomi/KcELECTRA-base-v2022](https://huggingface.co/beomi/KcELECTRA-base-v2022) on the AI Hub Kor ABSA Dataset dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5211
- Accuracy: 0.8060
- F1: 0.6220

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.5858        | 1.0   | 772  | 0.6595          | 0.7101   | 0.4422 |
| 0.426         | 2.0   | 1544 | 0.4981          | 0.7973   | 0.6054 |
| 0.3829        | 3.0   | 2316 | 0.5211          | 0.8060   | 0.6220 |


### Framework versions

- Transformers 4.57.1
- Pytorch 2.8.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.1
