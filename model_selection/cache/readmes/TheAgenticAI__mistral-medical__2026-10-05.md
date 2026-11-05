---
library_name: transformers
tags:
- generated_from_trainer
model-index:
- name: mistral-medical
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mistral-medical

This model was trained from scratch on an [TheAgenticAI/medical-o1-reasoning-SFT](https://huggingface.co/datasets/TheAgenticAI/medical-o1-reasoning-SFT) dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2238
- Token Acc: 0.6780

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

[TheAgenticAI/medical-o1-reasoning-SFT](https://huggingface.co/datasets/TheAgenticAI/medical-o1-reasoning-SFT)

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-06
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- gradient_accumulation_steps: 16
- total_train_batch_size: 128
- total_eval_batch_size: 8
- optimizer: Use adamw_torch with betas=(0.9,0.95) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.05
- num_epochs: 3.0

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Token Acc |
|:-------------:|:------:|:----:|:---------------:|:---------:|
| 1.0816        | 0.6841 | 100  | 1.0844          | 0.6876    |
| 0.8230        | 1.3625 | 200  | 1.1134          | 0.6851    |
| 0.5641        | 2.0410 | 300  | 1.1864          | 0.6809    |
| 0.5385        | 2.7251 | 400  | 1.2243          | 0.6781    |
| 0.4993        | 2.9850 | 438  | 1.2238          | 0.6780    |


### Framework versions

- Transformers 4.51.3
- Pytorch 2.6.0+cu124
- Datasets 3.2.0
- Tokenizers 0.21.1
