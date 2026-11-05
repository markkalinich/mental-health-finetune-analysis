---
library_name: transformers
license: apache-2.0
base_model: openai/whisper-tiny
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: whisper-tiny-medical
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# whisper-tiny-medical

This model is a fine-tuned version of [openai/whisper-tiny](https://huggingface.co/openai/whisper-tiny) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5555
- Wer: 0.3282

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
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.4277        | 1.0   | 204  | 0.6119          | 0.2787 |
| 0.3418        | 2.0   | 408  | 0.5642          | 0.2541 |
| 0.2761        | 3.0   | 612  | 0.5533          | 0.3720 |
| 0.1849        | 4.0   | 816  | 0.5534          | 0.3361 |
| 0.1760        | 5.0   | 1020 | 0.5555          | 0.3282 |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.5.1+cu121
- Datasets 4.8.3
- Tokenizers 0.22.2
