---
library_name: transformers
license: cc-by-nc-4.0
base_model: MCG-NJU/videomae-base
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: videomae-base-finetuned-ucf101-subset
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# videomae-base-finetuned-ucf101-subset

This model is a fine-tuned version of [MCG-NJU/videomae-base](https://huggingface.co/MCG-NJU/videomae-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2697
- Accuracy: 0.9286

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- training_steps: 300

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.7277        | 0.25  | 75   | 1.3769          | 0.5571   |
| 0.8952        | 1.25  | 150  | 0.8913          | 0.6571   |
| 0.3108        | 2.25  | 225  | 0.3952          | 0.8857   |
| 0.2449        | 3.25  | 300  | 0.2697          | 0.9286   |


### Framework versions

- Transformers 4.48.3
- Pytorch 2.0.0+cu117
- Datasets 3.3.2
- Tokenizers 0.21.0
