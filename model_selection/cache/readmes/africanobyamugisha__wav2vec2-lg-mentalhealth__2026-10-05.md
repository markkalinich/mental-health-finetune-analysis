---
license: apache-2.0
base_model: africanobyamugisha/luganda-asr-wav2vec2-ab1
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: wav2vec2-lg-mentalhealth
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-lg-mentalhealth

This model is a fine-tuned version of [africanobyamugisha/luganda-asr-wav2vec2-ab1](https://huggingface.co/africanobyamugisha/luganda-asr-wav2vec2-ab1) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.5107
- Wer: 0.7015
- Cer: 0.4277

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 15

### Training results

| Training Loss | Epoch   | Step | Validation Loss | Wer    | Cer    |
|:-------------:|:-------:|:----:|:---------------:|:------:|:------:|
| 2.5265        | 5.5556  | 50   | 2.5725          | 0.7067 | 0.4281 |
| 2.4892        | 11.1111 | 100  | 2.5107          | 0.7015 | 0.4277 |


### Framework versions

- Transformers 4.40.2
- Pytorch 2.3.1+cu121
- Datasets 2.19.2
- Tokenizers 0.19.1
