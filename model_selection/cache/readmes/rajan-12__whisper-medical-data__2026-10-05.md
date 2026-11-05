---
license: apache-2.0
base_model: openai/whisper-small.en
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: whisper-medical-data
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# whisper-medical-data

This model is a fine-tuned version of [openai/whisper-small.en](https://huggingface.co/openai/whisper-small.en) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7069
- Wer: 23.3573

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
- lr_scheduler_warmup_steps: 100
- training_steps: 1000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 1.0106        | 4.17  | 100  | 1.1117          | 24.8717 |
| 0.043         | 8.33  | 200  | 0.5784          | 28.0287 |
| 0.0049        | 12.5  | 300  | 0.6418          | 23.7936 |
| 0.001         | 16.67 | 400  | 0.6730          | 23.2290 |
| 0.0005        | 20.83 | 500  | 0.6854          | 23.3573 |
| 0.0004        | 25.0  | 600  | 0.6938          | 23.3316 |
| 0.0003        | 29.17 | 700  | 0.6996          | 23.4343 |
| 0.0003        | 33.33 | 800  | 0.7034          | 23.3830 |
| 0.0002        | 37.5  | 900  | 0.7061          | 23.3573 |
| 0.0002        | 41.67 | 1000 | 0.7069          | 23.3573 |


### Framework versions

- Transformers 4.38.2
- Pytorch 2.1.0+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2
