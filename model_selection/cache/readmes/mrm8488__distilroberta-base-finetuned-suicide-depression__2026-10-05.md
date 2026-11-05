---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
widget:
- text: "It's in the back of my mind. I'm not sure I'll be ok. Not sure I can deal with this. I'll try...I will try. Even though it's hard to see the point. But...this still isn't off the table."
model-index:
- name: distilroberta-base-finetuned-suicide-depression
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilroberta-base-finetuned-suicide-depression

This model is a fine-tuned version of [distilroberta-base](https://huggingface.co/distilroberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6622
- Accuracy: 0.7158

## Model description

Just a **POC** of a Transformer fine-tuned on [SDCNL](https://github.com/ayaanzhaque/SDCNL) dataset for suicide (label 1) or depression (label 0) detection in tweets.
**DO NOT use it in production**

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
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 214  | 0.6204          | 0.6632   |
| No log        | 2.0   | 428  | 0.6622          | 0.7158   |
| 0.5244        | 3.0   | 642  | 0.7312          | 0.6684   |
| 0.5244        | 4.0   | 856  | 0.9711          | 0.7105   |
| 0.2876        | 5.0   | 1070 | 1.1620          | 0.7      |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.9.0+cu111
- Datasets 1.13.0
- Tokenizers 0.10.3
