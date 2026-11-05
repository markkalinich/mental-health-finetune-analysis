---
library_name: transformers
base_model: aubmindlab/bert-base-arabertv02
tags:
- generated_from_trainer
model-index:
- name: arabert-mental-health-finetuned-final
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# arabert-mental-health-finetuned-final

This model is a fine-tuned version of [aubmindlab/bert-base-arabertv02](https://huggingface.co/aubmindlab/bert-base-arabertv02) on the [Arabic Mental Health QA (MentalQA) dataset](https://github.com/hasanhuz/MentalQA).
It achieves the following results on the evaluation set:
- Loss: 0.2212
- F1 Weighted: 0.6045
- Jaccard Weighted: 0.4540

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
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1 Weighted | Jaccard Weighted |
|:-------------:|:-----:|:----:|:---------------:|:-----------:|:----------------:|
| No log        | 1.0   | 38   | 0.2513          | 0.4951      | 0.4109           |
| No log        | 2.0   | 76   | 0.2260          | 0.6044      | 0.4600           |
| No log        | 3.0   | 114  | 0.2245          | 0.6101      | 0.4588           |
| No log        | 4.0   | 152  | 0.2212          | 0.6045      | 0.4540           |


### Framework versions

- Transformers 4.53.2
- Pytorch 2.6.0+cu124
- Datasets 2.14.4
- Tokenizers 0.21.2
