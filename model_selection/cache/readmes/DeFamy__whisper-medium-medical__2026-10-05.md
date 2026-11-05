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
      value: 19.526912865073616
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Medium Medical

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the Medical ASR dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0829
- Wer: 19.5269

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
| 0.3456        | 0.5405 | 100  | 0.2379          | 17.6684 |
| 0.1514        | 1.0811 | 200  | 0.1298          | 15.7615 |
| 0.0846        | 1.6216 | 300  | 0.0976          | 19.7924 |
| 0.0479        | 2.1622 | 400  | 0.0881          | 19.3338 |
| 0.0272        | 2.7027 | 500  | 0.0829          | 19.5269 |


### Framework versions

- Transformers 4.45.1
- Pytorch 2.4.0
- Datasets 3.0.1
- Tokenizers 0.20.0
