---
library_name: transformers
base_model: openai/whisper-large-turbo
tags:
- generated_from_trainer
datasets:
- Farhang87/whisperlargeturbo-Medical-ASR-Data
metrics:
- wer
model-index:
- name: Whisper Large Turbo Medical
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Medical ASR
      type: Farhang87/whisperlargeturbo-Medical-ASR-Data
    metrics:
    - name: Wer
      type: wer
      value: 4.344677769732078
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Large Turbo Medical

This model is a fine-tuned version of [openai/whisper-large-turbo](https://huggingface.co/openai/whisper-large-turbo) on the Medical ASR dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0672
- Wer: 4.3447

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
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 50
- training_steps: 500
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer    |
|:-------------:|:------:|:----:|:---------------:|:------:|
| 0.2994        | 0.5405 | 100  | 0.2101          | 9.9928 |
| 0.1405        | 1.0811 | 200  | 0.1212          | 5.7929 |
| 0.0859        | 1.6216 | 300  | 0.0929          | 4.4895 |
| 0.044         | 2.1622 | 400  | 0.0739          | 3.9585 |
| 0.0248        | 2.7027 | 500  | 0.0672          | 4.3447 |


### Framework versions

- Transformers 4.49.0
- Pytorch 2.4.0+cu121
- Datasets 3.3.2
- Tokenizers 0.21.0
