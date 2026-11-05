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
      value: 6.554753584375714
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# English Whisper Model

This model is a fine-tuned version of [openai/whisper-tiny.en](https://huggingface.co/openai/whisper-tiny.en) on the Medical dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1509
- Wer: 6.5548

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

| Training Loss | Epoch  | Step | Validation Loss | Wer     |
|:-------------:|:------:|:----:|:---------------:|:-------:|
| 1.3263        | 0.2825 | 100  | 1.1474          | 12.0219 |
| 0.8292        | 0.5650 | 200  | 0.8086          | 9.9840  |
| 0.5971        | 0.8475 | 300  | 0.5736          | 9.0597  |
| 0.2888        | 1.1299 | 400  | 0.3038          | 8.2465  |
| 0.172         | 1.4124 | 500  | 0.2112          | 7.5835  |
| 0.1499        | 1.6949 | 600  | 0.1839          | 7.0773  |
| 0.1347        | 1.9774 | 700  | 0.1693          | 6.6691  |
| 0.0977        | 2.2599 | 800  | 0.1650          | 6.7834  |
| 0.0966        | 2.5424 | 900  | 0.1578          | 7.0381  |
| 0.0877        | 2.8249 | 1000 | 0.1542          | 6.6462  |
| 0.0587        | 3.1073 | 1100 | 0.1539          | 6.5090  |
| 0.0642        | 3.3898 | 1200 | 0.1531          | 6.5646  |
| 0.0597        | 3.6723 | 1300 | 0.1518          | 6.5090  |
| 0.0754        | 3.9548 | 1400 | 0.1511          | 6.5254  |
| 0.0506        | 4.2373 | 1500 | 0.1509          | 6.5548  |


### Framework versions

- Transformers 4.43.2
- Pytorch 2.1.2
- Datasets 2.20.0
- Tokenizers 0.19.1
