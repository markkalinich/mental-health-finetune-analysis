---
library_name: transformers
license: apache-2.0
base_model: jonatasgrosman/wav2vec2-large-xlsr-53-english
tags:
- generated_from_trainer
datasets:
- afrispeech-200
metrics:
- wer
model-index:
- name: wav2vec2-xlsr-afrispeech-clinical
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
      value: 0.295
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-xlsr-afrispeech-clinical

This model is a fine-tuned version of [jonatasgrosman/wav2vec2-large-xlsr-53-english](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-english) on the afrispeech-200 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3815
- Model Preparation Time: 0.003
- Wer: 0.295

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2239
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Model Preparation Time | Wer   |
|:-------------:|:-----:|:-----:|:---------------:|:----------------------:|:-----:|
| 1.3513        | 1.0   | 2240  | 0.5410          | 0.003                  | 0.391 |
| 1.0632        | 2.0   | 4480  | 0.4555          | 0.003                  | 0.351 |
| 0.9540        | 3.0   | 6720  | 0.4268          | 0.003                  | 0.334 |
| 0.8654        | 4.0   | 8960  | 0.4057          | 0.003                  | 0.328 |
| 0.7554        | 5.0   | 11200 | 0.3871          | 0.003                  | 0.316 |
| 0.6892        | 6.0   | 13440 | 0.3936          | 0.003                  | 0.312 |
| 0.6096        | 7.0   | 15680 | 0.3836          | 0.003                  | 0.303 |
| 0.5333        | 8.0   | 17920 | 0.3859          | 0.003                  | 0.298 |
| 0.5335        | 9.0   | 20160 | 0.3858          | 0.003                  | 0.296 |
| 0.5038        | 10.0  | 22400 | 0.3815          | 0.003                  | 0.295 |


### Framework versions

- Transformers 5.3.0
- Pytorch 2.12.0.dev20260307+cu128
- Datasets 2.19.0
- Tokenizers 0.22.2
