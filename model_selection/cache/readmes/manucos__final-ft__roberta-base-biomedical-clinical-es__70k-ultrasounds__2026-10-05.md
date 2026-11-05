---
license: apache-2.0
base_model: BSC-LT/roberta-base-biomedical-clinical-es
tags:
- generated_from_trainer
model-index:
- name: final-ft__roberta-base-biomedical-clinical-es__70k-ultrasounds
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# final-ft__roberta-base-biomedical-clinical-es__70k-ultrasounds

This model is a fine-tuned version of [BSC-LT/roberta-base-biomedical-clinical-es](https://huggingface.co/BSC-LT/roberta-base-biomedical-clinical-es) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5971

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 256
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch   | Step | Validation Loss |
|:-------------:|:-------:|:----:|:---------------:|
| No log        | 0.9978  | 229  | 0.9388          |
| No log        | 2.0     | 459  | 0.8139          |
| No log        | 2.9978  | 688  | 0.7544          |
| 0.9622        | 4.0     | 918  | 0.7302          |
| 0.9622        | 4.9978  | 1147 | 0.6878          |
| 0.9622        | 6.0     | 1377 | 0.6754          |
| 0.9622        | 6.9978  | 1606 | 0.6625          |
| 0.715         | 8.0     | 1836 | 0.6431          |
| 0.715         | 8.9978  | 2065 | 0.6278          |
| 0.715         | 10.0    | 2295 | 0.6361          |
| 0.715         | 10.9978 | 2524 | 0.6296          |
| 0.6597        | 12.0    | 2754 | 0.6164          |
| 0.6597        | 12.9978 | 2983 | 0.6117          |
| 0.6597        | 14.0    | 3213 | 0.6052          |
| 0.6597        | 14.9978 | 3442 | 0.6064          |
| 0.6354        | 16.0    | 3672 | 0.6225          |
| 0.6354        | 16.9978 | 3901 | 0.5974          |
| 0.6354        | 18.0    | 4131 | 0.6010          |
| 0.6354        | 18.9978 | 4360 | 0.5816          |
| 0.6354        | 19.9564 | 4580 | 0.5971          |


### Framework versions

- Transformers 4.40.0
- Pytorch 2.2.1+cu121
- Datasets 2.19.0
- Tokenizers 0.19.1
