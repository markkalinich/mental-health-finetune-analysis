---
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
      value: 16.051170649287954
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

[<img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-28.svg" alt="Visualize in Weights & Biases" width="200" height="32"/>](https://wandb.ai/jutsu-labs/huggingface/runs/nnp3wvhl)
# Whisper Medium Medical

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the Medical ASR dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0567
- Wer: 16.0512

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
- train_batch_size: 32
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
| 0.4817        | 0.5405 | 100  | 0.1982          | 12.8651 |
| 0.104         | 1.0811 | 200  | 0.0839          | 10.3065 |
| 0.0549        | 1.6216 | 300  | 0.0643          | 15.9063 |
| 0.0245        | 2.1622 | 400  | 0.0610          | 14.0961 |
| 0.012         | 2.7027 | 500  | 0.0567          | 16.0512 |


### Framework versions

- Transformers 4.42.4
- Pytorch 2.2.0+cu121
- Datasets 2.20.0
- Tokenizers 0.19.1
