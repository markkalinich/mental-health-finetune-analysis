---
library_name: transformers
license: apache-2.0
base_model: nlpconnect/vit-gpt2-image-captioning
tags:
- generated_from_trainer
metrics:
- bleu
model-index:
- name: medical-caption-model-v1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medical-caption-model-v1

This model is a fine-tuned version of [nlpconnect/vit-gpt2-image-captioning](https://huggingface.co/nlpconnect/vit-gpt2-image-captioning) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 5.0189
- Bleu: 0.0332
- Meteor: 5.8196
- Rougel: 10.2378

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu   | Meteor | Rougel  |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:-------:|
| 5.1913        | 2.0   | 200  | 5.2321          | 0.0396 | 7.0115 | 10.6658 |
| 4.6615        | 4.0   | 400  | 4.9947          | 0.0495 | 6.1088 | 10.9570 |
| 4.3567        | 6.0   | 600  | 4.9261          | 0.0384 | 5.7674 | 11.0691 |
| 4.0884        | 8.0   | 800  | 4.9632          | 0.0344 | 5.9190 | 10.6889 |
| 3.9311        | 10.0  | 1000 | 5.0189          | 0.0332 | 5.8196 | 10.2378 |


### Framework versions

- Transformers 4.56.1
- Pytorch 2.8.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.0
