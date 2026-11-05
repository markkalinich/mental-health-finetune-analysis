---
library_name: transformers
license: other
base_model: Qwen/Qwen3-1.7B
tags:
- llama-factory
- full
- generated_from_trainer
model-index:
- name: medical-o1-sft-full
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medical-o1-sft-full

This model is a fine-tuned version of [Qwen/Qwen3-1.7B](https://huggingface.co/Qwen/Qwen3-1.7B) on the medical_o1_train dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4089

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
| 1.4962        | 0.3419 | 50   | 1.4686          |
| 1.4215        | 0.6838 | 100  | 1.4337          |
| 1.3304        | 1.0205 | 150  | 1.4194          |
| 1.3097        | 1.3624 | 200  | 1.4159          |
| 1.3175        | 1.7043 | 250  | 1.4089          |
| 1.2195        | 2.0410 | 300  | 1.4176          |
| 1.2726        | 2.3829 | 350  | 1.4229          |
| 1.1895        | 2.7248 | 400  | 1.4216          |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2
