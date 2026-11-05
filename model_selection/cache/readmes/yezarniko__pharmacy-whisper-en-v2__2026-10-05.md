---
library_name: transformers
language:
- en
license: apache-2.0
base_model: openai/whisper-small.en
tags:
- generated_from_trainer
datasets:
- yezarniko/medicines-asr2
metrics:
- wer
model-index:
- name: Pharmacy ASR Whisper Base Model
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Medicines ASR Dataset
      type: yezarniko/medicines-asr2
      args: 'config: en, split: test'
    metrics:
    - name: Wer
      type: wer
      value: 0.0
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Pharmacy ASR Whisper Base Model

This model is a fine-tuned version of [openai/whisper-small.en](https://huggingface.co/openai/whisper-small.en) on the Medicines ASR Dataset dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0001
- Wer: 0.0

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
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 5000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer    |
|:-------------:|:------:|:----:|:---------------:|:------:|
| 0.035         | 1.0905 | 1000 | 0.0312          | 6.5282 |
| 0.0042        | 2.1810 | 2000 | 0.0018          | 0.5935 |
| 0.0083        | 3.2715 | 3000 | 0.0007          | 0.0    |
| 0.0003        | 4.3621 | 4000 | 0.0001          | 0.0    |
| 0.0002        | 5.4526 | 5000 | 0.0001          | 0.0    |


### Framework versions

- Transformers 4.50.3
- Pytorch 2.6.0+cu124
- Datasets 2.14.4
- Tokenizers 0.21.2
