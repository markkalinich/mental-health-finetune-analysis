---
license: bsd-3-clause
base_model: LA1512/led-pubmed-20K-ORC-4096
tags:
- generated_from_trainer
model-index:
- name: results
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# results

This model is a fine-tuned version of [LA1512/led-pubmed-20K-ORC-4096](https://huggingface.co/LA1512/led-pubmed-20K-ORC-4096) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 3.2494

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 400
- num_epochs: 1
- label_smoothing_factor: 0.1

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 3.2974        | 0.16  | 200  | 3.2981          |
| 3.1752        | 0.32  | 400  | 3.3060          |
| 3.1366        | 0.48  | 600  | 3.3115          |
| 3.1612        | 0.64  | 800  | 3.2834          |
| 3.172         | 0.8   | 1000 | 3.2593          |
| 3.2953        | 0.96  | 1200 | 3.2494          |


### Framework versions

- Transformers 4.39.3
- Pytorch 2.1.2
- Datasets 2.18.0
- Tokenizers 0.15.2
