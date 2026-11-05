---
library_name: transformers
license: apache-2.0
base_model: bert-base-uncased
tags:
- generated_from_trainer
model-index:
- name: multilabel-mental-health-classifier-v2-iter1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# multilabel-mental-health-classifier-v2-iter1

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0573
- Precision Macro: 0.9964
- Recall Macro: 0.9909
- F1 Macro: 0.9936
- Precision Micro: 0.9923
- Recall Micro: 0.9832
- F1 Micro: 0.9877

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
- seed: 764
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision Macro | Recall Macro | F1 Macro | Precision Micro | Recall Micro | F1 Micro |
|:-------------:|:-----:|:----:|:---------------:|:---------------:|:------------:|:--------:|:---------------:|:------------:|:--------:|
| 1.0673        | 1.0   | 182  | 0.8887          | 0.3631          | 0.7965       | 0.4620   | 0.3957          | 0.7856       | 0.5263   |
| 0.8459        | 2.0   | 364  | 0.6065          | 0.4828          | 0.8962       | 0.6049   | 0.5410          | 0.8629       | 0.6651   |
| 0.5999        | 3.0   | 546  | 0.3847          | 0.6292          | 0.9298       | 0.7352   | 0.6802          | 0.8827       | 0.7684   |
| 0.3859        | 4.0   | 728  | 0.2644          | 0.7463          | 0.9422       | 0.8231   | 0.8018          | 0.8943       | 0.8455   |
| 0.2695        | 5.0   | 910  | 0.1774          | 0.9123          | 0.9639       | 0.9365   | 0.9011          | 0.9300       | 0.9153   |
| 0.1906        | 6.0   | 1092 | 0.1256          | 0.9650          | 0.9739       | 0.9692   | 0.9589          | 0.9491       | 0.9540   |
| 0.1449        | 7.0   | 1274 | 0.0998          | 0.9801          | 0.9782       | 0.9789   | 0.9797          | 0.9584       | 0.9689   |
| 0.1115        | 8.0   | 1456 | 0.0728          | 0.9955          | 0.9860       | 0.9907   | 0.9946          | 0.9732       | 0.9838   |
| 0.0869        | 9.0   | 1638 | 0.0614          | 0.9937          | 0.9896       | 0.9916   | 0.9913          | 0.9802       | 0.9857   |
| 0.0746        | 10.0  | 1820 | 0.0573          | 0.9964          | 0.9909       | 0.9936   | 0.9923          | 0.9832       | 0.9877   |


### Framework versions

- Transformers 4.56.2
- Pytorch 2.8.0
- Tokenizers 0.22.1
