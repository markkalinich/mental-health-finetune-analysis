---
language:
  - en
library_name: transformers
license: apache-2.0
pipeline_tag: text-classification
tags:
  - text-classification
  - prompt-injection-detection
  - jailbreak-detection
  - security
metrics:
  - accuracy
base_model: distilbert-base-uncased
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_prompt_guard

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1045
- Accuracy: 0.9795
- Macro Precision: 0.9863
- Macro Recall: 0.9728
- Macro F1: 0.9791

## Model description

This is a 3-class DistilBERT classifier fine-tuned for:
- benign
- prompt_injection
- jailbreak

Base model: {BASE_MODEL}

Datasets used:
- wambosec/prompt-injections
- jackhhao/jailbreak-classification

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 16
- eval_batch_size: 32
- seed: 17
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 0.1
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Macro Precision | Macro Recall | Macro F1 |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------------:|:------------:|:--------:|
| 0.5076        | 1.0   | 47   | 0.2579          | 0.9315   | 0.9356          | 0.9246       | 0.9291   |
| 0.1328        | 2.0   | 94   | 0.1055          | 0.9726   | 0.9820          | 0.9633       | 0.9717   |
| 0.0280        | 3.0   | 141  | 0.1045          | 0.9795   | 0.9863          | 0.9728       | 0.9791   |


### Framework versions

- Transformers 5.5.4
- Pytorch 2.10.0+cu128
- Datasets 4.8.4
- Tokenizers 0.22.2
