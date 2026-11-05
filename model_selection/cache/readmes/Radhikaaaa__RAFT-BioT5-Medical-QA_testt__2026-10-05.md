---
library_name: transformers
license: mit
base_model: QizhiPei/biot5-plus-base
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: RAFT-BioT5-Medical-QA_testt
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# RAFT-BioT5-Medical-QA_testt

This model is a fine-tuned version of [QizhiPei/biot5-plus-base](https://huggingface.co/QizhiPei/biot5-plus-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.5630
- Rouge1: 11.1448
- Rouge2: 3.564
- Rougel: 8.7117
- Meteor: 5.3064
- Bertscore F1: 75.7991

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
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2 | Rougel | Meteor | Bertscore F1 |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:------:|:------:|:------:|:------------:|
| 3.7491        | 1.0   | 12   | 2.5630          | 11.1448 | 3.564  | 8.7117 | 5.3064 | 75.7991      |


### Framework versions

- Transformers 4.55.0
- Pytorch 2.6.0+cu124
- Datasets 4.0.0
- Tokenizers 0.21.2
