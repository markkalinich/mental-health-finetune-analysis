---
library_name: transformers
license: apache-2.0
base_model: openai/whisper-large-v3
tags:
- whisper-event
- generated_from_trainer
datasets:
- OUTCOMESAI/medical_speech_corpus
metrics:
- wer
model-index:
- name: Whisper Small Medical
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: OUTCOMESAI/medical_speech_corpus zh-en
      type: OUTCOMESAI/medical_speech_corpus
    metrics:
    - name: Wer
      type: wer
      value: 44.25531914893617
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small Medical

This model is a fine-tuned version of [openai/whisper-large-v3](https://huggingface.co/openai/whisper-large-v3) on the OUTCOMESAI/medical_speech_corpus zh-en dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6201
- Wer: 44.2553

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-07
- train_batch_size: 32
- eval_batch_size: 16
- seed: 42
- distributed_type: multi-GPU
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 50
- training_steps: 100
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 7.4337        | 25.0  | 50   | 0.6201          | 44.2553 |
| 5.7447        | 50.0  | 100  | 0.6113          | 51.2340 |


### Framework versions

- Transformers 4.48.0.dev0
- Pytorch 2.1.0+cu118
- Datasets 3.1.1.dev0
- Tokenizers 0.21.0
