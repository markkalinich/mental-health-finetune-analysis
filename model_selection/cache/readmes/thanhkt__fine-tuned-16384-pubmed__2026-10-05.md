---
tags:
- generated_from_trainer
- summarize
- pubmed
- med
datasets:
- pubmed-summarization
metrics:
- rouge
model-index:
- name: fine-tuned-16384-pubmed
  results: []
language:
- en
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# fine-tuned-16384-pubmed

This model is fine-tuned  on the pubmed-summarization dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3719
- Rouge1: 0.4602
- Rouge2: 0.2253
- Rougel: 0.2911
- Rougelsum: 0.4283

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 50
- num_epochs: 2

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum |
|:-------------:|:------:|:----:|:---------------:|:------:|:------:|:------:|:---------:|
| 12.7776       | 0.2667 | 50   | 9.5450          | 0.4552 | 0.2219 | 0.2848 | 0.4234    |
| 7.2062        | 0.5333 | 100  | 4.6159          | 0.4564 | 0.2215 | 0.2874 | 0.4241    |
| 4.0511        | 0.8    | 150  | 2.7224          | 0.4615 | 0.2222 | 0.2914 | 0.4287    |
| 2.657         | 1.0667 | 200  | 1.7347          | 0.4597 | 0.2226 | 0.2921 | 0.4273    |
| 1.7104        | 1.3333 | 250  | 1.0021          | 0.4583 | 0.2231 | 0.2918 | 0.4261    |
| 0.9336        | 1.6    | 300  | 0.5423          | 0.4586 | 0.2228 | 0.2905 | 0.4259    |
| 0.4902        | 1.8667 | 350  | 0.3719          | 0.4602 | 0.2253 | 0.2911 | 0.4283    |
| 0.4032        | 2      | 400  | 0.2967          | 0.4718 | 0.2203 | 0.2871 | 0.4243    |


### Framework versions

- Transformers 4.43.3
- Pytorch 2.0.0
- Datasets 2.15.0
- Tokenizers 0.19.1