---
library_name: transformers
license: other
base_model: Qwen/Qwen3-4B
tags:
- llama-factory
- full
- generated_from_trainer
model-index:
- name: medical-o1-sft-full-2e-5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medical-o1-sft-full-2e-5

This model is a fine-tuned version of [Qwen/Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B) on the medical_o1_train dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3128

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
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 32
- total_train_batch_size: 128
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 0.05
- num_epochs: 3.0

### Training results

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 1.3878        | 0.3009 | 44   | 1.3555          |
| 1.3129        | 0.6017 | 88   | 1.3286          |
| 1.3143        | 0.9026 | 132  | 1.3146          |
| 1.1074        | 1.1983 | 176  | 1.3256          |
| 1.1358        | 1.4991 | 220  | 1.3180          |
| 1.1299        | 1.8    | 264  | 1.3128          |
| 1.0013        | 2.0957 | 308  | 1.3543          |
| 0.9818        | 2.3966 | 352  | 1.3585          |
| 0.9763        | 2.6974 | 396  | 1.3566          |
| 0.9635        | 2.9983 | 440  | 1.3570          |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2
