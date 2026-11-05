---
license: mit
base_model: FacebookAI/xlm-roberta-large
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: roberta-suicide-detection-hk
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-suicide-detection-hk

This model is a fine-tuned version of [FacebookAI/xlm-roberta-large](https://huggingface.co/FacebookAI/xlm-roberta-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1628
- Accuracy: 0.9608

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.6783        | 0.19  | 20   | 0.5885          | 0.7451   |
| 0.7304        | 0.37  | 40   | 0.6978          | 0.7059   |
| 0.6086        | 0.56  | 60   | 0.4823          | 0.7255   |
| 0.5071        | 0.74  | 80   | 0.5564          | 0.7059   |
| 0.5933        | 0.93  | 100  | 0.5993          | 0.6667   |
| 0.6311        | 1.11  | 120  | 0.6531          | 0.7059   |
| 0.5867        | 1.3   | 140  | 0.6158          | 0.4510   |
| 0.6845        | 1.48  | 160  | 0.5851          | 0.7059   |
| 0.7479        | 1.67  | 180  | 0.6134          | 0.7059   |
| 0.573         | 1.85  | 200  | 0.5972          | 0.7059   |
| 0.6183        | 2.04  | 220  | 0.5631          | 0.7059   |
| 0.657         | 2.22  | 240  | 0.6166          | 0.7059   |
| 0.7293        | 2.41  | 260  | 0.5851          | 0.7059   |
| 0.6215        | 2.59  | 280  | 0.4603          | 0.7647   |
| 0.3509        | 2.78  | 300  | 0.6292          | 0.7647   |
| 0.3484        | 2.96  | 320  | 0.6770          | 0.8431   |
| 0.3279        | 3.15  | 340  | 0.1123          | 0.9608   |
| 0.4096        | 3.33  | 360  | 0.1380          | 0.9804   |
| 0.3626        | 3.52  | 380  | 0.4317          | 0.9216   |
| 0.2809        | 3.7   | 400  | 0.1681          | 0.9804   |
| 0.5547        | 3.89  | 420  | 0.1194          | 0.9804   |
| 0.3751        | 4.07  | 440  | 0.2943          | 0.9216   |
| 0.1131        | 4.26  | 460  | 0.0558          | 0.9804   |
| 0.182         | 4.44  | 480  | 0.1463          | 0.9608   |
| 0.2991        | 4.63  | 500  | 0.2800          | 0.9608   |
| 0.2471        | 4.81  | 520  | 0.2261          | 0.9608   |
| 0.1022        | 5.0   | 540  | 0.1628          | 0.9608   |


### Framework versions

- Transformers 4.39.3
- Pytorch 2.1.2
- Datasets 2.18.0
- Tokenizers 0.15.2
