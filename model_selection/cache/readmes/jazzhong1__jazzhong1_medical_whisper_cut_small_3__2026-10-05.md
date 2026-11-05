---
language:
- ko
license: apache-2.0
tags:
- hf-asr-leaderboard
- generated_from_trainer
base_model: openai/whisper-small
datasets:
- Yettiesoft/voice_medical_cut_small_vector
model-index:
- name: jazzhong1/jazzhong1_medical_whisper_cut_small_3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# jazzhong1/jazzhong1_medical_whisper_cut_small_3

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the Yettiesoft/voice_medical_cut_small_vector dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2959
- Cer: 8.2065

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4e-05
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 5000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Cer     |
|:-------------:|:------:|:----:|:---------------:|:-------:|
| 0.3011        | 0.9381 | 1000 | 0.3146          | 11.6877 |
| 0.2058        | 1.8762 | 2000 | 0.2831          | 9.7311  |
| 0.1046        | 2.8143 | 3000 | 0.2834          | 8.9407  |
| 0.0364        | 3.7523 | 4000 | 0.2867          | 8.5658  |
| 0.0111        | 4.6904 | 5000 | 0.2959          | 8.2065  |


### Framework versions

- Transformers 4.41.2
- Pytorch 2.3.0+cu121
- Datasets 2.19.2
- Tokenizers 0.19.1
