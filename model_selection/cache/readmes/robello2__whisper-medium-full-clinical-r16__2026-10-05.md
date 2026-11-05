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
- name: whisper-medium-full-clinical-r16
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
      value: 22.403991182271728
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# whisper-medium-full-clinical-r16

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the afrispeech-200 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7557
- Wer: 22.4040
- Cer: 8.9223

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 16
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 200
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step  | Validation Loss | Wer     | Cer     |
|:-------------:|:------:|:-----:|:---------------:|:-------:|:-------:|
| 2.5732        | 1.1047 | 2500  | 0.4727          | 26.4687 | 12.7305 |
| 1.4199        | 2.2095 | 5000  | 0.4792          | 24.9217 | 11.0376 |
| 0.5931        | 3.3142 | 7500  | 0.5210          | 23.6145 | 9.9791  |
| 0.3973        | 4.4189 | 10000 | 0.5586          | 24.2720 | 10.2508 |
| 0.1234        | 5.5237 | 12500 | 0.6029          | 23.0924 | 9.3290  |
| 0.0623        | 6.6284 | 15000 | 0.6551          | 22.9377 | 9.1811  |
| 0.0322        | 7.7331 | 17500 | 0.6905          | 22.4311 | 9.0467  |
| 0.0251        | 8.8379 | 20000 | 0.7327          | 22.5123 | 8.9581  |
| 0.0127        | 9.9426 | 22500 | 0.7556          | 22.4233 | 8.9253  |
| 0.0090        | 10.0   | 22630 | 0.7557          | 22.4040 | 8.9223  |


### Framework versions

- Transformers 5.5.4
- Pytorch 2.11.0+cu130
- Datasets 2.19.0
- Tokenizers 0.22.2
