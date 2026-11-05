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
- name: jazzhong1_medical_whisper_cut_small_1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# jazzhong1_medical_whisper_cut_small_1

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the voice_medical_cut_small_vector dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2648
- Cer: 9.1909

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 4000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Cer     |
|:-------------:|:------:|:----:|:---------------:|:-------:|
| 0.3922        | 0.2346 | 1000 | 0.4451          | 14.6184 |
| 0.3506        | 0.4693 | 2000 | 0.3587          | 13.0215 |
| 0.3206        | 0.7039 | 3000 | 0.2984          | 10.8546 |
| 0.2721        | 0.9385 | 4000 | 0.2648          | 9.1909  |


### Framework versions

- Transformers 4.41.1
- Pytorch 2.3.0+cu121
- Datasets 2.19.1
- Tokenizers 0.19.1
