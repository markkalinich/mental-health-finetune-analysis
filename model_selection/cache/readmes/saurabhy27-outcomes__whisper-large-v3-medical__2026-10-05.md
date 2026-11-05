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
- name: Whisper Large V3 Medical
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: OUTCOMESAI/medical_speech_corpus en
      type: OUTCOMESAI/medical_speech_corpus
    metrics:
    - name: Wer
      type: wer
      value: 3.2635854592980795
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Large V3 Medical

This model is a fine-tuned version of [openai/whisper-large-v3](https://huggingface.co/openai/whisper-large-v3) on the OUTCOMESAI/medical_speech_corpus en dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1453
- Wer: 3.2636

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
- train_batch_size: 64
- eval_batch_size: 32
- seed: 42
- distributed_type: multi-GPU
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 200
- training_steps: 5000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer    |
|:-------------:|:------:|:----:|:---------------:|:------:|
| 4.2439        | 0.1530 | 200  | 0.2935          | 4.5078 |
| 3.3374        | 0.3060 | 400  | 0.2734          | 4.6961 |
| 3.0833        | 0.4591 | 600  | 0.2673          | 4.2733 |
| 1.8243        | 0.6121 | 800  | 0.2681          | 4.4373 |
| 1.1288        | 0.7651 | 1000 | 0.2549          | 4.2771 |
| 0.8199        | 0.9181 | 1200 | 0.2412          | 4.2041 |
| 0.681         | 1.0712 | 1400 | 0.2311          | 4.1054 |
| 0.5798        | 1.2242 | 1600 | 0.2192          | 4.0093 |
| 0.5233        | 1.3772 | 1800 | 0.2072          | 3.8927 |
| 0.463         | 1.5302 | 2000 | 0.1992          | 3.8197 |
| 0.428         | 1.6832 | 2200 | 0.1951          | 3.7748 |
| 0.3944        | 1.8363 | 2400 | 0.1866          | 3.6775 |
| 0.3682        | 1.9893 | 2600 | 0.1792          | 3.6044 |
| 0.3543        | 2.1423 | 2800 | 0.1725          | 3.5301 |
| 0.3368        | 2.2953 | 3000 | 0.1714          | 3.4904 |
| 0.3136        | 2.4484 | 3200 | 0.1648          | 3.4571 |
| 0.3121        | 2.6014 | 3400 | 0.1604          | 3.4238 |
| 0.2959        | 2.7544 | 3600 | 0.1561          | 3.3956 |
| 0.2912        | 2.9074 | 3800 | 0.1538          | 3.3738 |
| 0.2767        | 3.0604 | 4000 | 0.1511          | 3.3456 |
| 0.2848        | 3.2135 | 4200 | 0.1487          | 3.3200 |
| 0.274         | 3.3665 | 4400 | 0.1475          | 3.2841 |
| 0.2694        | 3.5195 | 4600 | 0.1464          | 3.2828 |
| 0.2731        | 3.6725 | 4800 | 0.1455          | 3.2687 |
| 0.2677        | 3.8256 | 5000 | 0.1453          | 3.2636 |


### Framework versions

- Transformers 4.48.0.dev0
- Pytorch 2.1.0+cu118
- Datasets 3.1.1.dev0
- Tokenizers 0.21.0
