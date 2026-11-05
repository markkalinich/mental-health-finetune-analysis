---
language:
- es
license: apache-2.0
base_model: openai/whisper-medium
tags:
- generated_from_trainer
datasets:
- Mezosky/es_clinical_assistance_10k
metrics:
- wer
model-index:
- name: Whisper Chilean Spanish Medium
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Mezosky/es_clinical_assistance_10k
      type: Mezosky/es_clinical_assistance_10k
    metrics:
    - name: Wer
      type: wer
      value: 7.774513918030494
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Chilean Spanish Medium

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the Mezosky/es_clinical_assistance_10k dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1058
- Wer: 7.7745

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

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.6275        | 0.17  | 100  | 0.5455          | 13.3333 |
| 0.185         | 0.34  | 200  | 0.1782          | 10.7316 |
| 0.1523        | 0.51  | 300  | 0.1539          | 10.9106 |
| 0.1373        | 0.69  | 400  | 0.1399          | 10.1329 |
| 0.1538        | 0.86  | 500  | 0.1322          | 17.5493 |
| 0.1007        | 1.03  | 600  | 0.1238          | 8.4963  |
| 0.0782        | 1.2   | 700  | 0.1187          | 8.4599  |
| 0.0722        | 1.37  | 800  | 0.1128          | 7.8137  |
| 0.0715        | 1.54  | 900  | 0.1081          | 7.6934  |
| 0.0927        | 1.72  | 1000 | 0.1058          | 7.7745  |


### Framework versions

- Transformers 4.39.3
- Pytorch 2.2.2+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2
