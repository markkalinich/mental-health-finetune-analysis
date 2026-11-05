---
license: cc-by-nc-4.0
base_model: facebook/mms-1b-all
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: mms-1b-lg-mentalhealth
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mms-1b-lg-mentalhealth

This model is a fine-tuned version of [facebook/mms-1b-all](https://huggingface.co/facebook/mms-1b-all) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6196
- Wer: 0.5037
- Cer: 0.1895

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
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 400
- num_epochs: 40

### Training results

| Training Loss | Epoch   | Step | Validation Loss | Wer    | Cer    |
|:-------------:|:-------:|:----:|:---------------:|:------:|:------:|
| 1.0605        | 27.1186 | 200  | 0.6196          | 0.5037 | 0.1895 |


### Framework versions

- Transformers 4.40.2
- Pytorch 2.3.1+cu121
- Datasets 2.19.2
- Tokenizers 0.19.1
