---
language:
- en
license: apache-2.0
base_model: openai/whisper-large-v3
tags:
- generated_from_trainer
datasets:
- medical_data
- Na0s/Primock_med
model-index:
- name: Final_Medical_whisper
  results: []
metrics:
- cer
- wer
pipeline_tag: automatic-speech-recognition
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

<a href="https://ibb.co/4YRxh82"><img src="https://i.ibb.co/wwh15S7/DALL-E-2024-10-05-20-47-54-A-doctor-in-a-modern-clinical-setting-carefully-listening-to-a-patient-s.webp" alt="DALL-E-2024-10-05-20-47-54-A-doctor-in-a-modern-clinical-setting-carefully-listening-to-a-patient-s" border="0"></a>

# med-whisper-large-final

This model is a fine-tuned version of [openai/whisper-large-v3](https://huggingface.co/openai/whisper-large-v3) on the primock_data dataset.

## Model description

Fine tuned version of whisper-large-v3 through transfer learning on Doctor/Patient consultations

## Intended uses & limitations

Medical transcription

## Training and evaluation data

Na0s/Medical_Augmented_data

## Training procedure

Exhaustive transfer learning 


### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 6
- eval_batch_size: 6
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 24
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: constant_with_warmup
- lr_scheduler_warmup_steps: 50
- training_steps: 500
- mixed_precision_training: Native AMP

### Performance Overview:

\| Model Name         | WER  | CER  | Number of Parameters |
|--------------------|------|------|----------------------|
| Whisper Tiny       | 0.46 | 0.27 | 39M                  |
| Whisper Base       | 0.42 | 0.26 | 74M                  |
| Whisper Small      | 0.39 | 0.26 | 244M                 |
| Whisper Medium     | 0.37 | 0.23 | 769M                 |
| Whisper Large v3   | 0.33 | 0.18 | 1.55B                |
| **Whisper Medical**| **0.19** | **0.10** | **1.55B**      |

**Performance of foundation Whispers vs Medical Whisper on the Validation set.**

| Model Name         | WER  | CER  | Number of Parameters |
|--------------------|------|------|----------------------|
| **Whisper Medical**| **0.24** | **0.13** | **1.55B**    |

**Table: Performance of Whisper Medical on the Test set.**


### Framework versions

- Transformers 4.42.4
- Pytorch 2.3.1+cu121
- Datasets 2.20.0
- Tokenizers 0.19.1