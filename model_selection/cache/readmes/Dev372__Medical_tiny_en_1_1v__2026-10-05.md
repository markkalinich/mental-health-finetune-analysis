---
language:
- en
license: apache-2.0
base_model: openai/whisper-tiny.en
tags:
- generated_from_trainer
datasets:
- Dev372/Medical_STT_Dataset_1.1
metrics:
- wer
model-index:
- name: English Whisper Model
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Medical
      type: Dev372/Medical_STT_Dataset_1.1
      args: 'split: test'
    metrics:
    - name: Wer
      type: wer
      value: 6.5482216924132075
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# English Whisper Model

This model is a fine-tuned version of [openai/whisper-tiny.en](https://huggingface.co/openai/whisper-tiny.en) on the Medical dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1566
- Wer: 6.5482

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
- train_batch_size: 18
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 1100
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer     |
|:-------------:|:------:|:----:|:---------------:|:-------:|
| 1.8857        | 0.1554 | 55   | 1.6694          | 13.1520 |
| 1.3264        | 0.3107 | 110  | 1.0577          | 11.8358 |
| 0.9159        | 0.4661 | 165  | 0.8809          | 10.3857 |
| 0.8292        | 0.6215 | 220  | 0.7654          | 9.8893  |
| 0.641         | 0.7768 | 275  | 0.6364          | 9.2557  |
| 0.5445        | 0.9322 | 330  | 0.4931          | 8.6417  |
| 0.4072        | 1.0876 | 385  | 0.3397          | 8.2759  |
| 0.2378        | 1.2429 | 440  | 0.2414          | 8.1322  |
| 0.2109        | 1.3983 | 495  | 0.2116          | 7.6684  |
| 0.1641        | 1.5537 | 550  | 0.1940          | 7.6423  |
| 0.1498        | 1.7090 | 605  | 0.1819          | 7.1198  |
| 0.1445        | 1.8644 | 660  | 0.1752          | 6.8095  |
| 0.1349        | 2.0198 | 715  | 0.1679          | 6.7181  |
| 0.1032        | 2.1751 | 770  | 0.1661          | 6.7344  |
| 0.0898        | 2.3305 | 825  | 0.1632          | 6.8291  |
| 0.1032        | 2.4859 | 880  | 0.1606          | 6.7278  |
| 0.0845        | 2.6412 | 935  | 0.1592          | 6.7083  |
| 0.0958        | 2.7966 | 990  | 0.1578          | 6.5743  |
| 0.097         | 2.9520 | 1045 | 0.1570          | 6.5515  |
| 0.0689        | 3.1073 | 1100 | 0.1566          | 6.5482  |


### Framework versions

- Transformers 4.43.2
- Pytorch 2.1.2
- Datasets 2.20.0
- Tokenizers 0.19.1
