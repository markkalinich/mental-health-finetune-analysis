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
      value: 6.283680067931677
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# English Whisper Model

This model is a fine-tuned version of [openai/whisper-tiny.en](https://huggingface.co/openai/whisper-tiny.en) on the Medical dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1252
- Wer: 6.2837

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
- training_steps: 1500
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer     |
|:-------------:|:------:|:----:|:---------------:|:-------:|
| 1.2359        | 0.2825 | 100  | 1.0423          | 10.4935 |
| 0.6633        | 0.5650 | 200  | 0.6451          | 9.5072  |
| 0.4199        | 0.8475 | 300  | 0.3864          | 8.5078  |
| 0.1541        | 1.1299 | 400  | 0.1895          | 7.4202  |
| 0.1228        | 1.4124 | 500  | 0.1642          | 6.8781  |
| 0.1132        | 1.6949 | 600  | 0.1471          | 6.8422  |
| 0.1076        | 1.9774 | 700  | 0.1356          | 6.3261  |
| 0.0717        | 2.2599 | 800  | 0.1333          | 6.1334  |
| 0.0682        | 2.5424 | 900  | 0.1284          | 6.3947  |
| 0.0627        | 2.8249 | 1000 | 0.1265          | 6.5972  |
| 0.0367        | 3.1073 | 1100 | 0.1261          | 6.2478  |
| 0.0452        | 3.3898 | 1200 | 0.1265          | 6.3784  |
| 0.0374        | 3.6723 | 1300 | 0.1257          | 6.3980  |
| 0.0523        | 3.9548 | 1400 | 0.1248          | 6.1596  |
| 0.031         | 4.2373 | 1500 | 0.1252          | 6.2837  |


### Framework versions

- Transformers 4.43.3
- Pytorch 2.1.2
- Datasets 2.20.0
- Tokenizers 0.19.1
