---
library_name: transformers
language:
- en
license: apache-2.0
base_model: openai/whisper-base.en
tags:
- generated_from_trainer
datasets:
- yezarniko/medicines-asr
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
      type: yezarniko/medicines-asr
      args: 'config: en, split: test'
    metrics:
    - name: Wer
      type: wer
      value: 7.71513353115727
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Pharmacy ASR Whisper Base Model

This model is a fine-tuned version of [openai/whisper-base.en](https://huggingface.co/openai/whisper-base.en) on the Medicines ASR Dataset dataset [yezarniko/medicines](https://huggingface.co/datasets/yezarniko/medicines) which contains real-world drug names and pharmacy-friendly pronunciations.
It achieves the following results on the evaluation set:
- Loss: 0.0008
- Wer: 7.7151

## Model description

The goal of this model is to provide fast and accurate transcription of medicinal terms, improving speech recognition for healthcare and pharmacy applications.

## Intended uses & limitations

- Medicine search systems
- Prescription reading
- Voice-based pharmacy automation
- Speech-driven drug inventory/apps

The base model is Whisper-base.en, meaning it only supports English. 
It cannot recognize medicine names spoken in other languages.
The dataset may not represent all drug names available in real pharmacies. 

## Training and evaluation data

[yezarniko/medicines](https://huggingface.co/datasets/yezarniko/medicines) 
- Total Dataset:  14669
- Total Duration (second)s:  15853.571
- No. of Agents:  10
- No. of VoiceLines:  1466

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

| Training Loss | Epoch  | Step | Validation Loss | Wer     |
|:-------------:|:------:|:----:|:---------------:|:-------:|
| 0.0803        | 1.0905 | 1000 | 0.0566          | 21.6617 |
| 0.012         | 2.1810 | 2000 | 0.0073          | 11.2760 |
| 0.0046        | 3.2715 | 3000 | 0.0016          | 8.6053  |
| 0.0015        | 4.3621 | 4000 | 0.0010          | 8.0119  |
| 0.0014        | 5.4526 | 5000 | 0.0008          | 7.7151  |


### Framework versions

- Transformers 4.50.3
- Pytorch 2.6.0+cu124
- Datasets 2.14.4
- Tokenizers 0.21.2
