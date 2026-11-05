---
library_name: transformers
license: cc-by-nc-nd-4.0
base_model: iiiorg/piiranha-v1-detect-personal-information
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: piiranha-my-v3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# piiranha-my-v3

This model is a fine-tuned version of [iiiorg/piiranha-v1-detect-personal-information](https://huggingface.co/iiiorg/piiranha-v1-detect-personal-information) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0613
- Accuracy: 0.9961
- F1: 0.9919

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
- eval_batch_size: 64
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 128
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 0.15
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 26.3191       | 1.0   | 118  | 1.6362          | 0.7844   | 0.6952 |
| 5.1317        | 2.0   | 236  | 0.2855          | 0.9603   | 0.9567 |
| 1.9508        | 3.0   | 354  | 0.0897          | 0.9894   | 0.9759 |
| 1.4124        | 4.0   | 472  | 0.0599          | 0.9916   | 0.9782 |
| 1.1169        | 5.0   | 590  | 0.0479          | 0.9936   | 0.9844 |
| 0.8100        | 6.0   | 708  | 0.0475          | 0.9943   | 0.9867 |
| 0.6853        | 7.0   | 826  | 0.0426          | 0.9946   | 0.9870 |
| 0.5779        | 8.0   | 944  | 0.0436          | 0.9951   | 0.9881 |
| 0.5129        | 9.0   | 1062 | 0.0426          | 0.9952   | 0.9877 |
| 0.4607        | 10.0  | 1180 | 0.0405          | 0.9954   | 0.9884 |
| 0.2784        | 11.0  | 1298 | 0.0437          | 0.9958   | 0.9900 |
| 0.2591        | 12.0  | 1416 | 0.0447          | 0.9959   | 0.9903 |
| 0.2794        | 13.0  | 1534 | 0.0526          | 0.9950   | 0.9877 |
| 0.2377        | 14.0  | 1652 | 0.0500          | 0.9956   | 0.9908 |
| 0.1475        | 15.0  | 1770 | 0.0571          | 0.9952   | 0.9900 |
| 0.1174        | 16.0  | 1888 | 0.0591          | 0.9954   | 0.9906 |
| 0.1026        | 17.0  | 2006 | 0.0523          | 0.9959   | 0.9915 |
| 0.1846        | 18.0  | 2124 | 0.0577          | 0.9959   | 0.9911 |
| 0.1288        | 19.0  | 2242 | 0.0608          | 0.9954   | 0.9896 |
| 0.1284        | 20.0  | 2360 | 0.0574          | 0.9962   | 0.9914 |
| 0.0978        | 21.0  | 2478 | 0.0621          | 0.9956   | 0.9904 |
| 0.1150        | 22.0  | 2596 | 0.0597          | 0.9960   | 0.9912 |
| 0.1008        | 23.0  | 2714 | 0.0623          | 0.9959   | 0.9912 |
| 0.0595        | 24.0  | 2832 | 0.0612          | 0.9961   | 0.9919 |
| 0.0405        | 25.0  | 2950 | 0.0640          | 0.9958   | 0.9910 |
| 0.0677        | 26.0  | 3068 | 0.0643          | 0.9957   | 0.9907 |
| 0.0496        | 27.0  | 3186 | 0.0638          | 0.9958   | 0.9906 |
| 0.0863        | 28.0  | 3304 | 0.0637          | 0.9958   | 0.9910 |
| 0.0638        | 29.0  | 3422 | 0.0640          | 0.9958   | 0.9911 |
| 0.0503        | 30.0  | 3540 | 0.0640          | 0.9958   | 0.9911 |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 4.8.3
- Tokenizers 0.22.2
