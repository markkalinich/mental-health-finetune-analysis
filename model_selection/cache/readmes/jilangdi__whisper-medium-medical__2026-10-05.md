---
library_name: transformers
license: apache-2.0
base_model: openai/whisper-medium
tags:
- generated_from_trainer
datasets:
- yashtiwari/PaulMooney-Medical-ASR-Data
metrics:
- wer
model-index:
- name: Whisper Medium Medical
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Medical ASR
      type: yashtiwari/PaulMooney-Medical-ASR-Data
    metrics:
    - name: Wer
      type: wer
      value: 12.406468742457157
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Medium Medical

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the Medical ASR dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0995
- Wer: 12.4065

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
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 50
- training_steps: 500
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer     |
|:-------------:|:------:|:----:|:---------------:|:-------:|
| 0.7532        | 0.1357 | 100  | 0.2695          | 13.0099 |
| 0.2155        | 0.2714 | 200  | 0.2053          | 9.8238  |
| 0.2392        | 0.4071 | 300  | 0.1567          | 8.9549  |
| 0.151         | 0.5427 | 400  | 0.1159          | 6.9273  |
| 0.1439        | 0.6784 | 500  | 0.0995          | 12.4065 |


### Framework versions

- Transformers 4.45.1
- Pytorch 2.4.1+cu121
- Datasets 3.0.1
- Tokenizers 0.20.0
