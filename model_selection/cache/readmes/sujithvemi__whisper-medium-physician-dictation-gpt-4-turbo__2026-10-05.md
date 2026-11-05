---
language:
- en
license: apache-2.0
base_model: openai/whisper-medium
tags:
- generated_from_trainer
datasets:
- physician_dictation_gpt_4_turbo
metrics:
- wer
model-index:
- name: Whisper Large v3 Physician Dictation GPT 4 turbo
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Physician Dictation GPT 4 Turbo
      type: physician_dictation_gpt_4_turbo
      config: default
      split: None
      args: 'config: en, split: test'
    metrics:
    - name: Wer
      type: wer
      value: 5.349683331087454
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Large v3 Physician Dictation GPT 4 turbo

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the Physician Dictation GPT 4 Turbo dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1660
- Wer: 5.3497

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
- train_batch_size: 8
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 8500
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch   | Step | Validation Loss | Wer    |
|:-------------:|:-------:|:----:|:---------------:|:------:|
| 0.0143        | 3.9683  | 500  | 0.1068          | 4.9948 |
| 0.0023        | 7.9365  | 1000 | 0.1287          | 5.0757 |
| 0.0026        | 11.9048 | 1500 | 0.1254          | 4.9409 |
| 0.0003        | 15.8730 | 2000 | 0.1298          | 4.7298 |
| 0.001         | 19.8413 | 2500 | 0.1312          | 5.0173 |
| 0.0001        | 23.8095 | 3000 | 0.1405          | 5.2374 |
| 0.0001        | 27.7778 | 3500 | 0.1454          | 4.9903 |
| 0.0001        | 31.7460 | 4000 | 0.1497          | 5.2104 |
| 0.0           | 35.7143 | 4500 | 0.1531          | 5.1835 |
| 0.0           | 39.6825 | 5000 | 0.1558          | 5.1431 |
| 0.0           | 43.6508 | 5500 | 0.1581          | 5.1296 |
| 0.0           | 47.6190 | 6000 | 0.1601          | 5.1700 |
| 0.0           | 51.5873 | 6500 | 0.1619          | 5.1925 |
| 0.0           | 55.5556 | 7000 | 0.1635          | 5.2329 |
| 0.0           | 59.5238 | 7500 | 0.1648          | 5.2733 |
| 0.0           | 63.4921 | 8000 | 0.1656          | 5.3362 |
| 0.0           | 67.4603 | 8500 | 0.1660          | 5.3497 |


### Framework versions

- Transformers 4.40.2
- Pytorch 2.0.1+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
