---
language:
- en
license: apache-2.0
base_model: openai/whisper-tiny.en
tags:
- generated_from_trainer
datasets:
- Dev372/Medical_STT_Dataset_1_0_check_training
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
      type: Dev372/Medical_STT_Dataset_1_0_check_training
      args: 'split: test'
    metrics:
    - name: Wer
      type: wer
      value: 6.0845332094751505
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# English Whisper Model

This model is a fine-tuned version of [openai/whisper-tiny.en](https://huggingface.co/openai/whisper-tiny.en) on the Medical dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1019
- Wer: 6.0845

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
- training_steps: 1500
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch   | Step | Validation Loss | Wer    |
|:-------------:|:-------:|:----:|:---------------:|:------:|
| 1.8606        | 1.0101  | 100  | 1.6059          | 9.1965 |
| 1.0954        | 2.0202  | 200  | 1.0513          | 6.2935 |
| 0.6627        | 3.0303  | 300  | 0.6161          | 6.6187 |
| 0.1747        | 4.0404  | 400  | 0.1527          | 4.2034 |
| 0.0554        | 5.0505  | 500  | 0.0924          | 5.3182 |
| 0.028         | 6.0606  | 600  | 0.0819          | 4.0641 |
| 0.0132        | 7.0707  | 700  | 0.0835          | 5.6897 |
| 0.0085        | 8.0808  | 800  | 0.0913          | 5.5504 |
| 0.0056        | 9.0909  | 900  | 0.0932          | 5.8059 |
| 0.0043        | 10.1010 | 1000 | 0.0982          | 5.8059 |
| 0.0023        | 11.1111 | 1100 | 0.0990          | 5.8755 |
| 0.0016        | 12.1212 | 1200 | 0.1005          | 6.0149 |
| 0.0015        | 13.1313 | 1300 | 0.1015          | 6.0613 |
| 0.0016        | 14.1414 | 1400 | 0.1017          | 6.0613 |
| 0.0015        | 15.1515 | 1500 | 0.1019          | 6.0845 |


### Framework versions

- Transformers 4.42.4
- Pytorch 2.1.2
- Datasets 2.20.0
- Tokenizers 0.19.1
