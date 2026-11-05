---
language:
- es
license: apache-2.0
base_model: openai/whisper-large-v3
tags:
- generated_from_trainer
datasets:
- Mezosky/es_clinical_assistance_10k
metrics:
- wer
model-index:
- name: Whisper Chilean Spanish Large v3
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
      value: 6.935235697300322
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Chilean Spanish Large v3

This model is a fine-tuned version of [openai/whisper-large-v3](https://huggingface.co/openai/whisper-large-v3) on the Mezosky/es_clinical_assistance_10k dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0961
- Wer: 6.9352

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
- training_steps: 2000

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.2816        | 0.17  | 100  | 0.2250          | 11.2827 |
| 0.1505        | 0.34  | 200  | 0.1479          | 9.8196  |
| 0.1293        | 0.51  | 300  | 0.1350          | 72.1192 |
| 0.1221        | 0.69  | 400  | 0.1292          | 9.6825  |
| 0.141         | 0.86  | 500  | 0.1194          | 53.0899 |
| 0.0922        | 1.03  | 600  | 0.1150          | 12.0380 |
| 0.0773        | 1.2   | 700  | 0.1079          | 12.8661 |
| 0.0745        | 1.37  | 800  | 0.1036          | 67.3017 |
| 0.0699        | 1.54  | 900  | 0.1016          | 8.2697  |
| 0.0917        | 1.72  | 1000 | 0.0956          | 8.6334  |
| 0.0716        | 1.89  | 1100 | 0.0968          | 7.7997  |
| 0.0441        | 2.06  | 1200 | 0.0946          | 8.3760  |
| 0.0377        | 2.23  | 1300 | 0.0963          | 7.6178  |
| 0.0417        | 2.4   | 1400 | 0.0951          | 7.5703  |
| 0.0409        | 2.57  | 1500 | 0.0926          | 7.2681  |
| 0.0356        | 2.74  | 1600 | 0.0912          | 6.8933  |
| 0.0361        | 2.92  | 1700 | 0.0918          | 7.0835  |
| 0.0215        | 3.09  | 1800 | 0.0938          | 6.9548  |
| 0.018         | 3.26  | 1900 | 0.0960          | 6.6415  |
| 0.0196        | 3.43  | 2000 | 0.0961          | 6.9352  |


### Framework versions

- Transformers 4.39.3
- Pytorch 2.2.2+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2
