---
language: vi
license: mit
tags:
- text-classification
- sentiment-analysis
pipeline_tag: text-classification
widget:
- text: "Video này thật tuyệt vời!"
- text: "Tôi không thích nội dung này."
---


<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# LVC_Phobert

This model is a fine-tuned version of [vinai/phobert-large](https://huggingface.co/vinai/phobert-large) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0760

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.2878        | 1.0   | 347  | 1.1734          |
| 0.9926        | 2.0   | 694  | 1.0603          |
| 0.7133        | 3.0   | 1041 | 1.0150          |
| 0.4261        | 4.0   | 1388 | 1.2528          |
| 0.357         | 5.0   | 1735 | 1.4177          |
| 0.1385        | 6.0   | 2082 | 1.8420          |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.5.1+cu121
- Datasets 2.16.1
- Tokenizers 0.15.2