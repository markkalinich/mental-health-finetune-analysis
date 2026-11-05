---
license: apache-2.0
base_model: facebook/wav2vec2-large
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: wav2vec2-base-medical-demo2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-medical-demo2

This model is a fine-tuned version of [facebook/wav2vec2-large](https://huggingface.co/facebook/wav2vec2-large) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4790
- Wer: 0.1988

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
| 3.8755        | 3.97  | 500  | 1.4725          | 0.9722 |
| 0.8476        | 7.94  | 1000 | 0.5328          | 0.3881 |
| 0.4148        | 11.9  | 1500 | 0.5005          | 0.2710 |
| 0.259         | 15.87 | 2000 | 0.5133          | 0.2376 |
| 0.1795        | 19.84 | 2500 | 0.4084          | 0.2239 |
| 0.1323        | 23.81 | 3000 | 0.4588          | 0.2067 |
| 0.1015        | 27.78 | 3500 | 0.4790          | 0.1988 |


### Framework versions

- Transformers 4.34.1
- Pytorch 2.1.0
- Datasets 2.14.6
- Tokenizers 0.14.1
