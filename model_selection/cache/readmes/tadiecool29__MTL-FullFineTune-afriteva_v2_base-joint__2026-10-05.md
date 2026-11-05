---
library_name: transformers
license: apache-2.0
base_model: castorini/afriteva_v2_base
tags:
- full-finetuning
- amharic
- stance-detection
- sentiment-analysis
- multi-task
- generated_from_trainer
model-index:
- name: MTL-FullFineTune-afriteva_v2_base-joint
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MTL-FullFineTune-afriteva_v2_base-joint

This model is a fine-tuned version of [castorini/afriteva_v2_base](https://huggingface.co/castorini/afriteva_v2_base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.6732
- Exact Match: 0.5736
- Sentiment Accuracy: 0.7145
- Sentiment Macro F1: 0.7071
- Stance Accuracy: 0.7207
- Stance Macro F1: 0.7258
- Avg Macro F1: 0.7165

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
| 3.8675        | 1.0   | 189  | 2.1506          | 0.2643      | 0.4975             | 0.4571             | 0.3304          | 0.2669          | 0.3620       |
| 1.8323        | 2.0   | 378  | 1.7422          | 0.4875      | 0.6758             | 0.6611             | 0.5998          | 0.5779          | 0.6195       |
| 1.7446        | 3.0   | 567  | 1.6980          | 0.5175      | 0.6908             | 0.6812             | 0.6496          | 0.6516          | 0.6664       |
| 1.7116        | 4.0   | 756  | 1.6882          | 0.5474      | 0.7157             | 0.7128             | 0.6820          | 0.6865          | 0.6997       |
| 1.7025        | 5.0   | 945  | 1.6759          | 0.5711      | 0.7082             | 0.6981             | 0.7132          | 0.7144          | 0.7062       |
| 1.6897        | 6.0   | 1134 | 1.6785          | 0.5773      | 0.7195             | 0.7135             | 0.7182          | 0.7204          | 0.7169       |
| 1.6875        | 7.0   | 1323 | 1.6721          | 0.5786      | 0.7157             | 0.7054             | 0.7219          | 0.7266          | 0.7160       |
| 1.6864        | 8.0   | 1512 | 1.6721          | 0.5736      | 0.7132             | 0.7065             | 0.7207          | 0.7263          | 0.7164       |
| 1.6840        | 9.0   | 1701 | 1.6732          | 0.5736      | 0.7145             | 0.7071             | 0.7207          | 0.7258          | 0.7165       |


### Framework versions

- Transformers 5.18.0
- Pytorch 2.11.0+cu130
- Datasets 4.8.5
- Tokenizers 0.23.2
