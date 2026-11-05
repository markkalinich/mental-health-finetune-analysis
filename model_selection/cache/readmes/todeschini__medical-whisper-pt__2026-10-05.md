---
library_name: transformers
license: mit
base_model: openai/whisper-large-v3-turbo
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: medical-whisper-pt
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Medical Whisper - Portuguese

This model is a fine-tuned version of [openai/whisper-large-v3-turbo](https://huggingface.co/openai/whisper-large-v3-turbo) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3011
- Wer: 30.6945

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 9e-06
- train_batch_size: 4
- eval_batch_size: 16
- seed: 42
- distributed_type: multi-GPU
- num_devices: 4
- gradient_accumulation_steps: 8
- total_train_batch_size: 128
- total_eval_batch_size: 64
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 6000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer     |
|:-------------:|:------:|:----:|:---------------:|:-------:|
| 0.3654        | 0.3680 | 500  | 0.3516          | 35.6868 |
| 0.3355        | 0.7360 | 1000 | 0.3341          | 35.0002 |
| 0.2826        | 1.1041 | 1500 | 0.3248          | 34.6635 |
| 0.2763        | 1.4721 | 2000 | 0.3171          | 33.6200 |
| 0.2715        | 1.8401 | 2500 | 0.3101          | 33.1267 |
| 0.2203        | 2.2081 | 3000 | 0.3071          | 31.3256 |
| 0.2202        | 2.5761 | 3500 | 0.3019          | 30.5031 |
| 0.2169        | 2.9442 | 4000 | 0.2975          | 30.7246 |
| 0.1765        | 3.3122 | 4500 | 0.3002          | 31.2968 |
| 0.1768        | 3.6802 | 5000 | 0.2985          | 30.5046 |
| 0.1594        | 4.0482 | 5500 | 0.3003          | 30.5781 |
| 0.1603        | 4.4162 | 6000 | 0.3011          | 30.6945 |


### Framework versions

- Transformers 4.46.0.dev0
- Pytorch 2.1.0+cu118
- Datasets 3.0.2.dev0
- Tokenizers 0.20.0
