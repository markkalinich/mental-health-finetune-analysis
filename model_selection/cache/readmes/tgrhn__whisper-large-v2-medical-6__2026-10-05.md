---
license: apache-2.0
base_model: openai/whisper-large-v2
tags:
- generated_from_trainer
datasets:
- audiofolder
model-index:
- name: whisper-large-v2-medical-6
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# whisper-large-v2-medical-6

This model is a fine-tuned version of [openai/whisper-large-v2](https://huggingface.co/openai/whisper-large-v2) on the audiofolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1435

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-06
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 0.26  | 20   | 0.6876          |
| 1.0862        | 0.51  | 40   | 0.4528          |
| 0.4702        | 0.77  | 60   | 0.3280          |
| 0.311         | 1.03  | 80   | 0.2105          |
| 0.145         | 1.28  | 100  | 0.1609          |
| 0.145         | 1.54  | 120  | 0.1526          |
| 0.1185        | 1.79  | 140  | 0.1483          |
| 0.1195        | 2.05  | 160  | 0.1449          |
| 0.092         | 2.31  | 180  | 0.1449          |
| 0.0829        | 2.56  | 200  | 0.1441          |
| 0.0829        | 2.82  | 220  | 0.1435          |


### Framework versions

- Transformers 4.39.3
- Pytorch 2.4.0+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2
