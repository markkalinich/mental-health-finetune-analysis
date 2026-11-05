---
library_name: transformers
license: apache-2.0
base_model: distilgpt2
tags:
- generated_from_trainer
model-index:
- name: distilgpt2-finetuned-wellness
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilgpt2-finetuned-wellness

This model is a fine-tuned version of [distilgpt2](https://huggingface.co/distilgpt2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.6526

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 3.0101        | 1.0   | 158  | 2.1220          |
| 2.0886        | 2.0   | 316  | 1.9541          |
| 1.9941        | 3.0   | 474  | 1.8785          |
| 1.8701        | 4.0   | 632  | 1.8243          |
| 1.8238        | 5.0   | 790  | 1.7894          |
| 1.743         | 6.0   | 948  | 1.7593          |
| 1.699         | 7.0   | 1106 | 1.7376          |
| 1.6606        | 8.0   | 1264 | 1.7188          |
| 1.6345        | 9.0   | 1422 | 1.7027          |
| 1.6208        | 10.0  | 1580 | 1.6914          |
| 1.5896        | 11.0  | 1738 | 1.6830          |
| 1.5694        | 12.0  | 1896 | 1.6722          |
| 1.5468        | 13.0  | 2054 | 1.6671          |
| 1.5311        | 14.0  | 2212 | 1.6663          |
| 1.5172        | 15.0  | 2370 | 1.6602          |
| 1.51          | 16.0  | 2528 | 1.6544          |
| 1.4916        | 17.0  | 2686 | 1.6555          |
| 1.4782        | 18.0  | 2844 | 1.6529          |
| 1.4829        | 19.0  | 3002 | 1.6532          |
| 1.4639        | 20.0  | 3160 | 1.6526          |


### Framework versions

- Transformers 4.45.1
- Pytorch 2.4.1+cu124
- Datasets 3.0.1
- Tokenizers 0.20.0
