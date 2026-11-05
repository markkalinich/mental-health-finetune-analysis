---
license: apache-2.0
base_model: distilgpt2
tags:
- generated_from_trainer
model-index:
- name: symptom-check-april-4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# symptom-check-april-4

This model is a fine-tuned version of [distilgpt2](https://huggingface.co/distilgpt2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7701

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 12

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.6832        | 1.0   | 760  | 1.0709          |
| 1.0634        | 2.0   | 1520 | 0.9318          |
| 0.9903        | 3.0   | 2280 | 0.8711          |
| 0.9194        | 4.0   | 3040 | 0.8364          |
| 0.8973        | 5.0   | 3800 | 0.8148          |
| 0.8668        | 6.0   | 4560 | 0.8001          |
| 0.8552        | 7.0   | 5320 | 0.7892          |
| 0.8389        | 8.0   | 6080 | 0.7811          |
| 0.8333        | 9.0   | 6840 | 0.7770          |
| 0.8251        | 10.0  | 7600 | 0.7728          |
| 0.8233        | 11.0  | 8360 | 0.7711          |
| 0.8177        | 12.0  | 9120 | 0.7701          |


### Framework versions

- Transformers 4.38.2
- Pytorch 2.2.1+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2
