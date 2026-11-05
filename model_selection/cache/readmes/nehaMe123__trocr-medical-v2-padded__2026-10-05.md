---
library_name: transformers
base_model: microsoft/trocr-small-handwritten
tags:
- generated_from_trainer
model-index:
- name: trocr-medical-v2-padded
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# trocr-medical-v2-padded

This model is a fine-tuned version of [microsoft/trocr-small-handwritten](https://huggingface.co/microsoft/trocr-small-handwritten) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2892
- Cer: 0.3485

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 15
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Cer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 2.7747        | 1.0   | 166  | 2.8512          | 0.8883 |
| 2.1227        | 2.0   | 332  | 2.4945          | 0.8846 |
| 1.9645        | 3.0   | 498  | 2.3030          | 0.8507 |
| 1.5736        | 4.0   | 664  | 1.8213          | 0.8279 |
| 1.1897        | 5.0   | 830  | 1.2490          | 0.7454 |
| 0.8294        | 6.0   | 996  | 0.9490          | 0.5703 |
| 0.549         | 7.0   | 1162 | 0.6554          | 0.5129 |
| 0.387         | 8.0   | 1328 | 0.5487          | 0.4914 |
| 0.3109        | 9.0   | 1494 | 0.5268          | 0.4428 |
| 0.2238        | 10.0  | 1660 | 0.4383          | 0.4076 |
| 0.1751        | 11.0  | 1826 | 0.3658          | 0.3945 |
| 0.1141        | 12.0  | 1992 | 0.3795          | 0.3804 |
| 0.0954        | 13.0  | 2158 | 0.3162          | 0.3640 |
| 0.0691        | 14.0  | 2324 | 0.3186          | 0.3462 |
| 0.0589        | 15.0  | 2490 | 0.2892          | 0.3485 |


### Framework versions

- Transformers 4.57.1
- Pytorch 2.8.0+cu126
- Datasets 4.4.2
- Tokenizers 0.22.1
