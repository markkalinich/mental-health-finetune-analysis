---
library_name: transformers
language:
- yo
license: apache-2.0
base_model: openai/whisper-small
tags:
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_17_0
metrics:
- wer
model-index:
- name: Whisper Small yo - harcuracy model
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 17.0
      type: mozilla-foundation/common_voice_17_0
      config: yo
      split: test
      args: 'config: yo, split: test'
    metrics:
    - name: Wer
      type: wer
      value: 75.33815964945704
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small yo - harcuracy model

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the Common Voice 17.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2762
- Wer: 75.3382

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
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- training_steps: 1500
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch   | Step | Validation Loss | Wer     |
|:-------------:|:-------:|:----:|:---------------:|:-------:|
| 0.1066        | 5.5556  | 500  | 0.9370          | 76.7003 |
| 0.0053        | 11.1111 | 1000 | 1.1919          | 74.9571 |
| 0.0012        | 16.6667 | 1500 | 1.2762          | 75.3382 |


### Framework versions

- Transformers 4.47.0
- Pytorch 2.4.0
- Datasets 3.2.0
- Tokenizers 0.21.0
