---
library_name: transformers
license: apache-2.0
base_model: google/mt5-base
tags:
- full-finetuning
- amharic
- stance-detection
- sentiment-analysis
- multi-task
- generated_from_trainer
model-index:
- name: MTL-FullFineT-mt5-base-joint
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MTL-FullFineT-mt5-base-joint

This model is a fine-tuned version of [google/mt5-base](https://huggingface.co/google/mt5-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.7186
- Exact Match: 0.5536
- Sentiment Accuracy: 0.6870
- Sentiment Macro F1: 0.6798
- Stance Accuracy: 0.6945
- Stance Macro F1: 0.6957
- Avg Macro F1: 0.6877

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
| 9.6337        | 1.0   | 189  | 2.1926          | 0.0661      | 0.3566             | 0.2667             | 0.3092          | 0.2522          | 0.2595       |
| 1.9636        | 2.0   | 378  | 1.7843          | 0.4626      | 0.6297             | 0.6213             | 0.5761          | 0.5785          | 0.5999       |
| 1.8141        | 3.0   | 567  | 1.7389          | 0.5224      | 0.6571             | 0.6507             | 0.6658          | 0.6694          | 0.6601       |
| 1.7795        | 4.0   | 756  | 1.7315          | 0.5374      | 0.6870             | 0.6850             | 0.6758          | 0.6778          | 0.6814       |
| 1.7752        | 5.0   | 945  | 1.7324          | 0.5337      | 0.6845             | 0.6698             | 0.6584          | 0.6516          | 0.6607       |
| 1.7628        | 6.0   | 1134 | 1.7227          | 0.5424      | 0.6858             | 0.6747             | 0.6746          | 0.6743          | 0.6745       |
| 1.7737        | 7.0   | 1323 | 1.7198          | 0.5461      | 0.6796             | 0.6705             | 0.6920          | 0.6949          | 0.6827       |
| 1.7626        | 8.0   | 1512 | 1.7181          | 0.5511      | 0.6845             | 0.6774             | 0.6958          | 0.6978          | 0.6876       |
| 1.7574        | 9.0   | 1701 | 1.7186          | 0.5561      | 0.6908             | 0.6836             | 0.6970          | 0.6986          | 0.6911       |
| 1.7574        | 10.0  | 1890 | 1.7186          | 0.5536      | 0.6870             | 0.6798             | 0.6945          | 0.6957          | 0.6877       |


### Framework versions

- Transformers 5.17.0
- Pytorch 2.11.0+cu130
- Datasets 4.8.5
- Tokenizers 0.23.2
