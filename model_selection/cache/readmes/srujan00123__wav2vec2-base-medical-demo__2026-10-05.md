---
license: apache-2.0
base_model: facebook/wav2vec2-base
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: wav2vec2-base-medical-demo
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-medical-demo

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4566
- Wer: 0.2256

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
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 30

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 4.045         | 3.97  | 500  | 3.0058          | 0.9895 |
| 1.762         | 7.94  | 1000 | 0.5449          | 0.3923 |
| 0.3363        | 11.9  | 1500 | 0.3889          | 0.2890 |
| 0.173         | 15.87 | 2000 | 0.3992          | 0.2524 |
| 0.1127        | 19.84 | 2500 | 0.4172          | 0.2375 |
| 0.0805        | 23.81 | 3000 | 0.4576          | 0.2291 |
| 0.0648        | 27.78 | 3500 | 0.4566          | 0.2256 |


### Framework versions

- Transformers 4.35.0.dev0
- Pytorch 2.0.1+cpu
- Datasets 2.14.6.dev0
- Tokenizers 0.14.1
