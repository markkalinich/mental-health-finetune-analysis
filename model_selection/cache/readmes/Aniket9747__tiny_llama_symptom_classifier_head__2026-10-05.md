---
library_name: transformers
license: apache-2.0
base_model: TinyLlama/TinyLlama-1.1B-Chat-v1.0
tags:
- generated_from_trainer
model-index:
- name: tiny_llama_symptom_classifier_head
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# tiny_llama_symptom_classifier_head

This model is a fine-tuned version of [TinyLlama/TinyLlama-1.1B-Chat-v1.0](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0006

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.0122        | 0.8   | 100  | 0.0118          |
| 0.0046        | 1.6   | 200  | 0.0045          |
| 0.0017        | 2.4   | 300  | 0.0018          |
| 0.0008        | 3.2   | 400  | 0.0009          |
| 0.0005        | 4.0   | 500  | 0.0007          |
| 0.0004        | 4.8   | 600  | 0.0006          |


### Framework versions

- Transformers 5.1.0
- Pytorch 2.9.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.2
