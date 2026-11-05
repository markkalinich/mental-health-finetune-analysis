---
library_name: transformers
license: apache-2.0
base_model: d4data/biomedical-ner-all
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: ner-biomedical-maccrobat2018
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ner-biomedical-maccrobat2018

This model is a fine-tuned version of [d4data/biomedical-ner-all](https://huggingface.co/d4data/biomedical-ner-all) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7250
- Accuracy: 0.7665

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 2.6575        | 1.0   | 10   | 1.7587          | 0.2575   |
| 1.4576        | 2.0   | 20   | 1.1109          | 0.5523   |
| 0.9363        | 3.0   | 30   | 0.8227          | 0.6823   |
| 0.6519        | 4.0   | 40   | 0.7157          | 0.7200   |
| 0.4871        | 5.0   | 50   | 0.6950          | 0.7298   |
| 0.3808        | 6.0   | 60   | 0.6697          | 0.7455   |
| 0.3106        | 7.0   | 70   | 0.6761          | 0.7481   |
| 0.2558        | 8.0   | 80   | 0.6697          | 0.7568   |
| 0.2151        | 9.0   | 90   | 0.6689          | 0.7546   |
| 0.1856        | 10.0  | 100  | 0.6743          | 0.7587   |
| 0.1617        | 11.0  | 110  | 0.7075          | 0.7569   |
| 0.1426        | 12.0  | 120  | 0.7087          | 0.7561   |
| 0.1282        | 13.0  | 130  | 0.6996          | 0.7624   |
| 0.1163        | 14.0  | 140  | 0.7200          | 0.7646   |
| 0.1068        | 15.0  | 150  | 0.7044          | 0.7673   |
| 0.0968        | 16.0  | 160  | 0.7150          | 0.7641   |
| 0.0934        | 17.0  | 170  | 0.7239          | 0.7673   |
| 0.0871        | 18.0  | 180  | 0.7264          | 0.7652   |
| 0.085         | 19.0  | 190  | 0.7269          | 0.7655   |
| 0.083         | 20.0  | 200  | 0.7250          | 0.7665   |


### Framework versions

- Transformers 4.50.3
- Pytorch 2.6.0+cu124
- Tokenizers 0.21.1
