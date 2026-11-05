---
language:
- en
license: apache-2.0
base_model: openai/whisper-small.en
tags:
- generated_from_trainer
datasets:
- HarshDev_custom_dataset
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
      type: HarshDev_custom_dataset
      args: 'split: test'
    metrics:
    - name: Wer
      type: wer
      value: 1.2965964343598055
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# English Whisper Model

This model is a fine-tuned version of [openai/whisper-small.en](https://huggingface.co/openai/whisper-small.en) on the Medical dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0236
- Wer: 1.2966

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
- train_batch_size: 15
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 1500
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch   | Step | Validation Loss | Wer    |
|:-------------:|:-------:|:----:|:---------------:|:------:|
| 0.0026        | 6.0976  | 500  | 0.0240          | 1.6613 |
| 0.0002        | 12.1951 | 1000 | 0.0234          | 1.2966 |
| 0.0002        | 18.2927 | 1500 | 0.0236          | 1.2966 |


### Framework versions

- Transformers 4.42.4
- Pytorch 2.1.2
- Datasets 2.20.0
- Tokenizers 0.19.1
