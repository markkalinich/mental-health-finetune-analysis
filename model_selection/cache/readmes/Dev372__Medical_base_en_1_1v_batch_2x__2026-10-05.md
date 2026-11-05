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
      value: 6.580881152225743
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# English Whisper Model

This model is a fine-tuned version of [openai/whisper-tiny.en](https://huggingface.co/openai/whisper-tiny.en) on the Medical dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1386
- Wer: 6.5809

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
- train_batch_size: 36
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 1500
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer     |
|:-------------:|:------:|:----:|:---------------:|:-------:|
| 1.1731        | 0.5650 | 100  | 0.9844          | 10.2812 |
| 0.6483        | 1.1299 | 200  | 0.6288          | 9.3047  |
| 0.3802        | 1.6949 | 300  | 0.3554          | 7.8938  |
| 0.1437        | 2.2599 | 400  | 0.1702          | 7.1230  |
| 0.1136        | 2.8249 | 500  | 0.1415          | 6.5841  |
| 0.0752        | 3.3898 | 600  | 0.1336          | 6.0616  |
| 0.0713        | 3.9548 | 700  | 0.1257          | 6.1236  |
| 0.0373        | 4.5198 | 800  | 0.1279          | 5.8526  |
| 0.0311        | 5.0847 | 900  | 0.1283          | 5.8003  |
| 0.03          | 5.6497 | 1000 | 0.1303          | 6.1171  |
| 0.0166        | 6.2147 | 1100 | 0.1314          | 6.0845  |
| 0.0241        | 6.7797 | 1200 | 0.1339          | 6.3588  |
| 0.0164        | 7.3446 | 1300 | 0.1368          | 6.3555  |
| 0.0178        | 7.9096 | 1400 | 0.1380          | 6.4764  |
| 0.0099        | 8.4746 | 1500 | 0.1386          | 6.5809  |


### Framework versions

- Transformers 4.44.0
- Pytorch 2.1.2
- Datasets 2.20.0
- Tokenizers 0.19.1
