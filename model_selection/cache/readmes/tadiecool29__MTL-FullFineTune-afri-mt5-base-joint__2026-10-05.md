---
library_name: transformers
license: afl-3.0
base_model: masakhane/afri-mt5-base
tags:
- full-finetuning
- amharic
- stance-detection
- sentiment-analysis
- multi-task
- generated_from_trainer
model-index:
- name: MTL-FullFineTune-afri-mt5-base-joint
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MTL-FullFineTune-afri-mt5-base-joint

This model is a fine-tuned version of [masakhane/afri-mt5-base](https://huggingface.co/masakhane/afri-mt5-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8665
- Exact Match: 0.5536
- Sentiment Accuracy: 0.7082
- Sentiment Macro F1: 0.6990
- Stance Accuracy: 0.7045
- Stance Macro F1: 0.7109
- Avg Macro F1: 0.7050

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 8
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 300
- num_epochs: 10
- label_smoothing_factor: 0.1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Exact Match | Sentiment Accuracy | Sentiment Macro F1 | Stance Accuracy | Stance Macro F1 | Avg Macro F1 |
|:-------------:|:-----:|:----:|:---------------:|:-----------:|:------------------:|:------------------:|:---------------:|:---------------:|:------------:|
| 4.4331        | 1.0   | 189  | 2.5095          | 0.1110      | 0.3130             | 0.1214             | 0.2182          | 0.0750          | 0.0982       |
| 2.2132        | 2.0   | 378  | 1.9743          | 0.4140      | 0.5673             | 0.5116             | 0.5362          | 0.5213          | 0.5165       |
| 1.9958        | 3.0   | 567  | 1.8926          | 0.5374      | 0.6708             | 0.6596             | 0.6983          | 0.7026          | 0.6811       |
| 1.9245        | 4.0   | 756  | 1.8677          | 0.5449      | 0.6908             | 0.6855             | 0.6983          | 0.7036          | 0.6945       |
| 1.9002        | 5.0   | 945  | 1.8702          | 0.5499      | 0.6983             | 0.6880             | 0.6870          | 0.6869          | 0.6874       |
| 1.8719        | 6.0   | 1134 | 1.8703          | 0.5474      | 0.7057             | 0.6939             | 0.6870          | 0.6918          | 0.6928       |
| 1.8554        | 7.0   | 1323 | 1.8652          | 0.5499      | 0.7082             | 0.6998             | 0.7020          | 0.7096          | 0.7047       |
| 1.8604        | 8.0   | 1512 | 1.8656          | 0.5524      | 0.7070             | 0.6982             | 0.7045          | 0.7113          | 0.7047       |
| 1.8424        | 9.0   | 1701 | 1.8664          | 0.5561      | 0.7095             | 0.7001             | 0.7070          | 0.7131          | 0.7066       |
| 1.8492        | 10.0  | 1890 | 1.8665          | 0.5536      | 0.7082             | 0.6990             | 0.7045          | 0.7109          | 0.7050       |


### Framework versions

- Transformers 5.16.1
- Pytorch 2.11.0+cu128
- Datasets 4.8.5
- Tokenizers 0.23.1
