---
license: apache-2.0
base_model: allenai/longformer-base-4096
tags:
- generated_from_trainer
model-index:
- name: clinical_longformer_same_tokens_cc
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# clinical_longformer_same_tokens_cc

This model is a fine-tuned version of [allenai/longformer-base-4096](https://huggingface.co/allenai/longformer-base-4096) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.7387

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
- train_batch_size: 2
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 64
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1500
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 3.578         | 0.28  | 2    | 2.5967          |
| 2.8262        | 0.57  | 4    | 2.6161          |
| 2.6404        | 0.85  | 6    | 2.7073          |
| 2.5883        | 1.14  | 8    | 2.7756          |
| 2.7661        | 1.42  | 10   | 2.6908          |
| 2.695         | 1.71  | 12   | 2.5367          |
| 3.3694        | 1.99  | 14   | 2.6043          |
| 2.6329        | 2.28  | 16   | 2.5741          |
| 2.5998        | 2.56  | 18   | 2.6167          |
| 2.7418        | 2.84  | 20   | 2.5720          |
| 2.7355        | 3.13  | 22   | 2.5241          |
| 2.7436        | 3.41  | 24   | 2.6759          |
| 2.7103        | 3.7   | 26   | 2.6468          |
| 2.7274        | 3.98  | 28   | 2.7387          |


### Framework versions

- Transformers 4.35.0
- Pytorch 2.1.0+cu118
- Datasets 2.14.6
- Tokenizers 0.14.1
