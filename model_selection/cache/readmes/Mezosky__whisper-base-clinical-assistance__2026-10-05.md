---
language:
- es
license: apache-2.0
base_model: openai/whisper-base
tags:
- generated_from_trainer
datasets:
- Mezosky/es_clinical_assistance
metrics:
- wer
model-index:
- name: Whisper Chilean Spanish Small
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Mezosky/es_clinical_assistance
      type: Mezosky/es_clinical_assistance
    metrics:
    - name: Wer
      type: wer
      value: 204.97553017944537
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Chilean Spanish Small

This model is a fine-tuned version of [openai/whisper-base](https://huggingface.co/openai/whisper-base) on the Mezosky/es_clinical_assistance dataset.
It achieves the following results on the evaluation set:
- Loss: 4.4659
- Wer: 204.9755

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
- training_steps: 1000

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer      |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 4.6451        | 6.25  | 100  | 4.5135          | 105.7912 |
| 3.2485        | 12.5  | 200  | 3.3821          | 126.5905 |
| 2.3839        | 18.75 | 300  | 2.9779          | 215.0897 |
| 1.6538        | 25.0  | 400  | 3.0304          | 212.1533 |
| 0.887         | 31.25 | 500  | 3.4092          | 221.3703 |
| 0.3317        | 37.5  | 600  | 3.7754          | 191.3540 |
| 0.1065        | 43.75 | 700  | 4.0480          | 235.1550 |
| 0.0374        | 50.0  | 800  | 4.2473          | 185.4812 |
| 0.0173        | 56.25 | 900  | 4.4145          | 187.5204 |
| 0.014         | 62.5  | 1000 | 4.4659          | 204.9755 |


### Framework versions

- Transformers 4.39.3
- Pytorch 2.2.2+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2
