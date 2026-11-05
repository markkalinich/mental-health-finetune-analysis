---
license: apache-2.0
base_model: facebook/wav2vec2-base
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: mood_box
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mood_box

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5115
- Accuracy: 0.3802

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 4    | 1.6030          | 0.2231   |
| No log        | 2.0   | 8    | 1.5976          | 0.3223   |
| 1.6018        | 3.0   | 12   | 1.5936          | 0.2893   |
| 1.6018        | 4.0   | 16   | 1.5849          | 0.2810   |
| 1.5765        | 5.0   | 20   | 1.5733          | 0.3636   |
| 1.5765        | 6.0   | 24   | 1.5557          | 0.3884   |
| 1.5765        | 7.0   | 28   | 1.5360          | 0.3719   |
| 1.5323        | 8.0   | 32   | 1.5246          | 0.3554   |
| 1.5323        | 9.0   | 36   | 1.5152          | 0.3719   |
| 1.4909        | 10.0  | 40   | 1.5115          | 0.3802   |


### Framework versions

- Transformers 4.38.1
- Pytorch 2.1.0+cu121
- Datasets 2.17.1
- Tokenizers 0.15.2
