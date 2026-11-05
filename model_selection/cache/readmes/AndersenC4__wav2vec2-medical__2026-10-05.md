---
library_name: transformers
license: apache-2.0
base_model: facebook/wav2vec2-base
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: wav2vec2-medical
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-medical

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1992
- Wer: 0.1411
- Cer: 0.0495

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- training_steps: 3500
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch   | Step | Validation Loss | Wer    | Cer    |
|:-------------:|:-------:|:----:|:---------------:|:------:|:------:|
| 0.16          | 2.7056  | 500  | 0.2363          | 0.1710 | 0.0594 |
| 0.1467        | 5.4071  | 1000 | 0.2485          | 0.1882 | 0.0678 |
| 0.1392        | 8.1085  | 1500 | 0.2382          | 0.1650 | 0.0568 |
| 0.11          | 10.8141 | 2000 | 0.2240          | 0.1623 | 0.0568 |
| 0.1006        | 13.5156 | 2500 | 0.1995          | 0.1510 | 0.0519 |
| 0.0788        | 16.2171 | 3000 | 0.2202          | 0.1454 | 0.0507 |
| 0.0678        | 18.9227 | 3500 | 0.1992          | 0.1411 | 0.0495 |


### Framework versions

- Transformers 4.52.4
- Pytorch 2.6.0+cu124
- Datasets 2.14.4
- Tokenizers 0.21.1
