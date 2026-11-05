---
language:
- en
license: apache-2.0
base_model: openai/whisper-small.en
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
      value: 4.889121133936445
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# English Whisper Model

This model is a fine-tuned version of [openai/whisper-small.en](https://huggingface.co/openai/whisper-small.en) on the Medical dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0952
- Wer: 4.8891

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
- training_steps: 1000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer    |
|:-------------:|:------:|:----:|:---------------:|:------:|
| 0.7956        | 0.2825 | 100  | 0.7275          | 8.0048 |
| 0.5277        | 0.5650 | 200  | 0.5046          | 6.2706 |
| 0.2247        | 0.8475 | 300  | 0.1916          | 6.1988 |
| 0.0883        | 1.1299 | 400  | 0.1251          | 5.5880 |
| 0.0735        | 1.4124 | 500  | 0.1173          | 5.0883 |
| 0.0752        | 1.6949 | 600  | 0.1080          | 4.9120 |
| 0.0689        | 1.9774 | 700  | 0.0975          | 4.5233 |
| 0.0401        | 2.2599 | 800  | 0.0992          | 4.4613 |
| 0.0364        | 2.5424 | 900  | 0.0966          | 4.7291 |
| 0.0345        | 2.8249 | 1000 | 0.0952          | 4.8891 |


### Framework versions

- Transformers 4.43.3
- Pytorch 2.1.2
- Datasets 2.20.0
- Tokenizers 0.19.1
