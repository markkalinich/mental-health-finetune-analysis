---
library_name: transformers
language:
- hi
license: apache-2.0
base_model: openai/whisper-small
tags:
- generated_from_trainer
datasets:
- DereAbdulhameed/Pharma-Speak
metrics:
- wer
model-index:
- name: 'Whisper Small Medication Corpus '
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Pharma-Speak
      type: DereAbdulhameed/Pharma-Speak
      args: 'config: en, split: test'
    metrics:
    - name: Wer
      type: wer
      value: 20.0
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small Medication Corpus 

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the Pharma-Speak dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6189
- Wer: 20.0

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
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 4000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer     |
|:-------------:|:------:|:----:|:---------------:|:-------:|
| 0.0           | 500.0  | 1000 | 0.5205          | 18.6047 |
| 0.0           | 1000.0 | 2000 | 0.5735          | 20.9302 |
| 0.0           | 1500.0 | 3000 | 0.6033          | 21.8605 |
| 0.0           | 2000.0 | 4000 | 0.6189          | 20.0    |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.4.0+cu121
- Datasets 2.21.0
- Tokenizers 0.19.1
