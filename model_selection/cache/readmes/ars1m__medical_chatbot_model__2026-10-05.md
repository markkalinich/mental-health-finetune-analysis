---
library_name: transformers
license: mit
base_model: microsoft/biogpt
tags:
- generated_from_trainer
model-index:
- name: medical_chatbot_model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medical_chatbot_model

This model is a fine-tuned version of [microsoft/biogpt](https://huggingface.co/microsoft/biogpt) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0033

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 4
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 200
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 2.1439        | 0.1686 | 500  | 1.9988          |
| 1.919         | 0.3372 | 1000 | 1.7011          |
| 1.6665        | 0.5057 | 1500 | 1.5434          |
| 1.4834        | 0.6743 | 2000 | 1.4272          |
| 1.4149        | 0.8429 | 2500 | 1.3405          |
| 1.3279        | 1.0115 | 3000 | 1.2766          |
| 1.1643        | 1.1800 | 3500 | 1.2236          |
| 1.151         | 1.3486 | 4000 | 1.1806          |
| 1.1403        | 1.5172 | 4500 | 1.1421          |
| 1.0784        | 1.6858 | 5000 | 1.1136          |
| 1.0303        | 1.8543 | 5500 | 1.0795          |
| 0.8385        | 2.0229 | 6000 | 1.0726          |
| 0.8542        | 2.1915 | 6500 | 1.0580          |
| 0.7797        | 2.3601 | 7000 | 1.0466          |
| 0.8073        | 2.5287 | 7500 | 1.0307          |
| 0.7923        | 2.6972 | 8000 | 1.0134          |
| 0.7565        | 2.8658 | 8500 | 1.0069          |


### Framework versions

- Transformers 4.51.3
- Pytorch 2.6.0+cu124
- Datasets 2.14.4
- Tokenizers 0.21.1
