---
library_name: transformers
license: apache-2.0
base_model: openai/whisper-medium
tags:
- generated_from_trainer
datasets:
- afrispeech-200
metrics:
- wer
model-index:
- name: whisper-medium-afrispeech-clinical
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: afrispeech-200
      type: afrispeech-200
      config: all
      split: None
      args: all
    metrics:
    - name: Wer
      type: wer
      value: 0.136
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# whisper-medium-afrispeech-clinical

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the afrispeech-200 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7878
- Model Preparation Time: 0.0098
- Wer: 0.136

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2239
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Model Preparation Time | Wer   |
|:-------------:|:-----:|:-----:|:---------------:|:----------------------:|:-----:|
| 0.4946        | 1.0   | 2240  | 0.5593          | 0.0098                 | 0.157 |
| 0.3420        | 2.0   | 4480  | 0.5074          | 0.0098                 | 0.144 |
| 0.1856        | 3.0   | 6720  | 0.5242          | 0.0098                 | 0.147 |
| 0.1157        | 4.0   | 8960  | 0.5676          | 0.0098                 | 0.142 |
| 0.0364        | 5.0   | 11200 | 0.6216          | 0.0098                 | 0.139 |
| 0.0184        | 6.0   | 13440 | 0.6494          | 0.0098                 | 0.137 |
| 0.0066        | 7.0   | 15680 | 0.6938          | 0.0098                 | 0.137 |
| 0.0021        | 8.0   | 17920 | 0.7283          | 0.0098                 | 0.137 |
| 0.0010        | 9.0   | 20160 | 0.7650          | 0.0098                 | 0.135 |
| 0.0006        | 10.0  | 22400 | 0.7878          | 0.0098                 | 0.136 |


### Framework versions

- Transformers 5.3.0
- Pytorch 2.4.1+cu121
- Datasets 2.19.0
- Tokenizers 0.22.2
