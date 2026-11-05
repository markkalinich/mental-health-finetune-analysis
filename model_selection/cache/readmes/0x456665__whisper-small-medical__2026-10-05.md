---
library_name: transformers
license: apache-2.0
base_model: openai/whisper-small
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: whisper-small-medical
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# whisper-small-medical

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0998
- Wer: 7.4577

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 4
- eval_batch_size: 2
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 5000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch   | Step | Validation Loss | Wer     |
|:-------------:|:-------:|:----:|:---------------:|:-------:|
| 0.0846        | 2.7056  | 500  | 0.2339          | 19.7460 |
| 0.0383        | 5.4071  | 1000 | 0.1777          | 14.1061 |
| 0.0223        | 8.1085  | 1500 | 0.1673          | 13.3342 |
| 0.0127        | 10.8141 | 2000 | 0.1469          | 10.5204 |
| 0.0041        | 13.5156 | 2500 | 0.1398          | 9.0388  |
| 0.0025        | 16.2171 | 3000 | 0.1240          | 9.4746  |
| 0.0           | 18.9227 | 3500 | 0.0997          | 7.8063  |
| 0.0           | 21.6242 | 4000 | 0.0997          | 7.6693  |
| 0.0           | 24.3256 | 4500 | 0.0998          | 7.4452  |
| 0.0           | 27.0271 | 5000 | 0.0998          | 7.4577  |


### Framework versions

- Transformers 4.56.2
- Pytorch 2.8.0+cu128
- Datasets 4.1.1
- Tokenizers 0.22.1
