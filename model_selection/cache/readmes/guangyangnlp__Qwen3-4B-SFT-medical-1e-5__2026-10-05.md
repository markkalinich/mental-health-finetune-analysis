---
library_name: transformers
license: other
base_model: Qwen/Qwen3-4B
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

This model is a fine-tuned version of [Qwen/Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B) on the medical_o1_train dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3088

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
| 1.3952        | 0.3009 | 44   | 1.3628          |
| 1.3153        | 0.6017 | 88   | 1.3319          |
| 1.3174        | 0.9026 | 132  | 1.3175          |
| 1.1758        | 1.1983 | 176  | 1.3184          |
| 1.2047        | 1.4991 | 220  | 1.3131          |
| 1.1961        | 1.8    | 264  | 1.3088          |
| 1.1401        | 2.0957 | 308  | 1.3254          |
| 1.1144        | 2.3966 | 352  | 1.3240          |
| 1.1196        | 2.6974 | 396  | 1.3236          |
| 1.0940        | 2.9983 | 440  | 1.3234          |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2
