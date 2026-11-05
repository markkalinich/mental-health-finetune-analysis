---
library_name: transformers
license: other
base_model: Qwen/Qwen3-32B
tags:
- llama-factory
- full
- generated_from_trainer
model-index:
- name: fleet-sft-full
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# fleet-sft-full

This model is a fine-tuned version of [Qwen/Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B) on the fleet_trajectories_train dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6703

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- gradient_accumulation_steps: 8
- total_train_batch_size: 64
- total_eval_batch_size: 8
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.05
- num_epochs: 2.0

### Training results

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| No log        | 0      | 0    | 1.0427          |
| 0.9312        | 0.0714 | 10   | 0.8903          |
| 0.8495        | 0.1427 | 20   | 0.7987          |
| 0.8165        | 0.2141 | 30   | 0.7599          |
| 0.7885        | 0.2855 | 40   | 0.7384          |
| 0.7654        | 0.3568 | 50   | 0.7236          |
| 0.7662        | 0.4282 | 60   | 0.7133          |
| 0.7065        | 0.4996 | 70   | 0.7057          |
| 0.7348        | 0.5709 | 80   | 0.7000          |
| 0.7067        | 0.6423 | 90   | 0.6951          |
| 0.745         | 0.7136 | 100  | 0.6905          |
| 0.7613        | 0.7850 | 110  | 0.6870          |
| 0.7349        | 0.8564 | 120  | 0.6837          |
| 0.7261        | 0.9277 | 130  | 0.6811          |
| 0.7158        | 0.9991 | 140  | 0.6788          |
| 0.705         | 1.0642 | 150  | 0.6800          |
| 0.6893        | 1.1356 | 160  | 0.6777          |
| 0.6718        | 1.2070 | 170  | 0.6759          |
| 0.6664        | 1.2783 | 180  | 0.6747          |
| 0.6906        | 1.3497 | 190  | 0.6736          |
| 0.6984        | 1.4211 | 200  | 0.6728          |
| 0.6925        | 1.4924 | 210  | 0.6721          |
| 0.695         | 1.5638 | 220  | 0.6715          |
| 0.6995        | 1.6351 | 230  | 0.6710          |
| 0.7153        | 1.7065 | 240  | 0.6707          |
| 0.7119        | 1.7779 | 250  | 0.6705          |
| 0.6479        | 1.8492 | 260  | 0.6703          |
| 0.6582        | 1.9206 | 270  | 0.6703          |
| 0.729         | 1.9920 | 280  | 0.6703          |


### Framework versions

- Transformers 4.52.4
- Pytorch 2.10.0+cu128
- Datasets 3.6.0
- Tokenizers 0.21.1
