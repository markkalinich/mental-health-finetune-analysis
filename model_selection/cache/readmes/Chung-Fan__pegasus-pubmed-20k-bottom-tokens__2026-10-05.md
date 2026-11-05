---
license: apache-2.0
base_model: tuner007/pegasus_summarizer
tags:
- generated_from_trainer
model-index:
- name: pegasus-pubmed-20k-bottom-tokens
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pegasus-pubmed-20k-bottom-tokens

This model is a fine-tuned version of [tuner007/pegasus_summarizer](https://huggingface.co/tuner007/pegasus_summarizer) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3139

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 1

### Training results

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 1.6173        | 0.7477 | 500  | 1.3139          |


### Framework versions

- Transformers 4.40.0
- Pytorch 2.2.1+cu121
- Datasets 2.19.0
- Tokenizers 0.19.1
