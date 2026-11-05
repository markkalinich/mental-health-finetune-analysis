---
language:
- en
license: apache-2.0
base_model: openai/whisper-tiny.en
tags:
- generated_from_trainer
datasets:
- Dev372/Medical_STT_Dataset_1.1
metrics:
- wer
model-index:
- name: English Whisper Model
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Medical
      type: Dev372/Medical_STT_Dataset_1.1
      args: 'split: test'
    metrics:
    - name: Wer
      type: wer
      value: 6.286946013912929
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# English Whisper Model

This model is a fine-tuned version of [openai/whisper-tiny.en](https://huggingface.co/openai/whisper-tiny.en) on the Medical dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1269
- Wer: 6.2869

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
- train_batch_size: 18
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 1100
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer     |
|:-------------:|:------:|:----:|:---------------:|:-------:|
| 1.2361        | 0.2825 | 100  | 1.0425          | 10.4870 |
| 0.6631        | 0.5650 | 200  | 0.6451          | 9.4908  |
| 0.419         | 0.8475 | 300  | 0.3854          | 8.5535  |
| 0.1538        | 1.1299 | 400  | 0.1895          | 7.2635  |
| 0.1234        | 1.4124 | 500  | 0.1644          | 6.8454  |
| 0.1134        | 1.6949 | 600  | 0.1470          | 6.6201  |
| 0.1071        | 1.9774 | 700  | 0.1358          | 6.0289  |
| 0.0721        | 2.2599 | 800  | 0.1329          | 6.1302  |
| 0.0693        | 2.5424 | 900  | 0.1299          | 6.3065  |
| 0.0635        | 2.8249 | 1000 | 0.1275          | 6.5025  |
| 0.0441        | 3.1073 | 1100 | 0.1269          | 6.2869  |


### Framework versions

- Transformers 4.43.3
- Pytorch 2.1.2
- Datasets 2.20.0
- Tokenizers 0.19.1
