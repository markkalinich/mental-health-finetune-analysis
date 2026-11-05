---
library_name: transformers
license: other
base_model: Qwen/Qwen3-1.7B
tags:
- llama-factory
- full
- generated_from_trainer
model-index:
- name: medical-o1-sft-full-1e-5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medical-o1-sft-full-1e-5

This model is a fine-tuned version of [Qwen/Qwen3-1.7B](https://huggingface.co/Qwen/Qwen3-1.7B) on the medical_o1_train dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4197

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
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 128
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 0.05
- num_epochs: 3.0

### Training results

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 1.5150        | 0.3419 | 50   | 1.4871          |
| 1.4362        | 0.6838 | 100  | 1.4490          |
| 1.3921        | 1.0205 | 150  | 1.4327          |
| 1.3675        | 1.3624 | 200  | 1.4269          |
| 1.3790        | 1.7043 | 250  | 1.4203          |
| 1.3200        | 2.0410 | 300  | 1.4197          |
| 1.3762        | 2.3829 | 350  | 1.4212          |
| 1.2864        | 2.7248 | 400  | 1.4206          |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2
