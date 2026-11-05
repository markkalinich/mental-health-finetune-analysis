---
library_name: transformers
license: apache-2.0
base_model: Falconsai/medical_summarization
tags:
- generated_from_trainer
model-index:
- name: Falconsai_medical_finetuned1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Falconsai_medical_finetuned1

This model is a fine-tuned version of [Falconsai/medical_summarization](https://huggingface.co/Falconsai/medical_summarization) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8915

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 8
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 200
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 2.52          | 1.6420 | 300  | 2.2277          |
| 2.2193        | 3.2798 | 600  | 1.9523          |
| 2.1492        | 4.9218 | 900  | 1.8915          |


### Framework versions

- Transformers 4.51.3
- Pytorch 2.5.1+cu121
- Datasets 2.14.4
- Tokenizers 0.21.1
