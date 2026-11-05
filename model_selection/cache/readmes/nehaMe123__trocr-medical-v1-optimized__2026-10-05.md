---
library_name: transformers
base_model: microsoft/trocr-small-handwritten
tags:
- generated_from_trainer
model-index:
- name: trocr-medical-v1-optimized
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# trocr-medical-v1-optimized

This model is a fine-tuned version of [microsoft/trocr-small-handwritten](https://huggingface.co/microsoft/trocr-small-handwritten) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0500
- Cer: 0.3118

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 15
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Cer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 1.1384        | 1.0   | 176  | 0.8087          | 0.2478 |
| 0.2974        | 2.0   | 352  | 0.2246          | 0.2590 |
| 0.1963        | 3.0   | 528  | 0.1778          | 0.2712 |
| 0.1206        | 4.0   | 704  | 0.1506          | 0.2616 |
| 0.0706        | 5.0   | 880  | 0.1275          | 0.2052 |
| 0.0413        | 6.0   | 1056 | 0.1201          | 0.2565 |
| 0.0291        | 7.0   | 1232 | 0.0987          | 0.2397 |
| 0.0136        | 8.0   | 1408 | 0.0723          | 0.2641 |
| 0.01          | 9.0   | 1584 | 0.0643          | 0.3012 |
| 0.0026        | 10.0  | 1760 | 0.0630          | 0.2641 |
| 0.0049        | 11.0  | 1936 | 0.0618          | 0.3586 |
| 0.0008        | 12.0  | 2112 | 0.0486          | 0.3118 |
| 0.0008        | 13.0  | 2288 | 0.0426          | 0.3255 |
| 0.0004        | 14.0  | 2464 | 0.0487          | 0.3098 |
| 0.0013        | 15.0  | 2640 | 0.0500          | 0.3118 |


### Framework versions

- Transformers 4.57.1
- Pytorch 2.8.0+cu126
- Datasets 4.4.2
- Tokenizers 0.22.1
