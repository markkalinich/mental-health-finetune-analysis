---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: ModerationGPT
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ModerationGPT

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2177
- Rouge1: 81.7742
- Rouge2: 77.8168
- Rougel: 81.7812
- Rougelsum: 81.7593
- Gen Len: 13.6851

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
- train_batch_size: 128
- eval_batch_size: 128
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| No log        | 1.0   | 335  | 1.0577          | 54.2885 | 42.6805 | 54.1114 | 54.2064   | 15.8069 |
| 1.4482        | 2.0   | 670  | 0.5655          | 71.3866 | 65.6295 | 71.3181 | 71.3413   | 13.3214 |
| 0.7111        | 3.0   | 1005 | 0.4278          | 73.535  | 68.2492 | 73.5214 | 73.5207   | 13.3682 |
| 0.7111        | 4.0   | 1340 | 0.3626          | 74.1375 | 69.0355 | 74.1302 | 74.1116   | 13.409  |
| 0.508         | 5.0   | 1675 | 0.3200          | 75.8217 | 69.4616 | 75.8126 | 75.7987   | 13.4467 |
| 0.4281        | 6.0   | 2010 | 0.2923          | 80.1152 | 75.0253 | 80.1019 | 80.0814   | 13.5971 |
| 0.4281        | 7.0   | 2345 | 0.2740          | 81.1188 | 76.4582 | 81.1144 | 81.0866   | 13.6413 |
| 0.3818        | 8.0   | 2680 | 0.2621          | 81.4117 | 76.9557 | 81.4064 | 81.3814   | 13.6591 |
| 0.3505        | 9.0   | 3015 | 0.2521          | 81.5234 | 77.2074 | 81.5176 | 81.4917   | 13.6683 |
| 0.3505        | 10.0  | 3350 | 0.2461          | 81.6226 | 77.3821 | 81.6243 | 81.5999   | 13.6729 |
| 0.3331        | 11.0  | 3685 | 0.2401          | 81.6549 | 77.4807 | 81.6601 | 81.6397   | 13.6769 |
| 0.3176        | 12.0  | 4020 | 0.2341          | 81.7157 | 77.6237 | 81.7192 | 81.6996   | 13.6807 |
| 0.3176        | 13.0  | 4355 | 0.2314          | 81.7288 | 77.6693 | 81.7346 | 81.7125   | 13.6814 |
| 0.3068        | 14.0  | 4690 | 0.2271          | 81.7534 | 77.7293 | 81.758  | 81.7446   | 13.6834 |
| 0.3011        | 15.0  | 5025 | 0.2239          | 81.7569 | 77.7588 | 81.7643 | 81.7426   | 13.6839 |
| 0.3011        | 16.0  | 5360 | 0.2209          | 81.761  | 77.7766 | 81.7681 | 81.7474   | 13.6855 |
| 0.2951        | 17.0  | 5695 | 0.2201          | 81.7483 | 77.7596 | 81.7516 | 81.7331   | 13.6847 |
| 0.2904        | 18.0  | 6030 | 0.2188          | 81.7582 | 77.7865 | 81.7605 | 81.7428   | 13.6842 |
| 0.2904        | 19.0  | 6365 | 0.2179          | 81.7842 | 77.8249 | 81.7899 | 81.7721   | 13.686  |
| 0.2893        | 20.0  | 6700 | 0.2177          | 81.7742 | 77.8168 | 81.7812 | 81.7593   | 13.6851 |


### Framework versions

- Transformers 4.29.2
- Pytorch 2.0.1+cu117
- Datasets 2.12.0
- Tokenizers 0.13.3
