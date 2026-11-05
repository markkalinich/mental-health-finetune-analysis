---
language:
- ko
license: apache-2.0
base_model: openai/whisper-small
tags:
- hf-asr-leaderboard
- generated_from_trainer
datasets:
- Yettiesoft/voice_medical_origin_small_vector
model-index:
- name: jazzhong1_medical_whisper_small
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# jazzhong1_medical_whisper_small

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the voice_medical_origin_small_vector dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2648
- Cer: 10.1284

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

| Training Loss | Epoch  | Step | Validation Loss | Cer     |
|:-------------:|:------:|:----:|:---------------:|:-------:|
| 0.2886        | 0.4342 | 1000 | 0.3111          | 11.4993 |
| 0.3306        | 0.8684 | 2000 | 0.2815          | 10.8260 |
| 0.215         | 1.3026 | 3000 | 0.2702          | 10.0223 |
| 0.2068        | 1.7369 | 4000 | 0.2648          | 10.1284 |


### Framework versions

- Transformers 4.42.0.dev0
- Pytorch 2.3.0+cu121
- Datasets 2.19.1
- Tokenizers 0.19.1
