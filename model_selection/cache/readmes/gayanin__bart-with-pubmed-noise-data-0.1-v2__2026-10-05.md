---
license: apache-2.0
base_model: facebook/bart-base
tags:
- generated_from_trainer
model-index:
- name: bart-with-pubmed-noise-data-0.1-v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-with-pubmed-noise-data-0.1-v2

This model is a fine-tuned version of [facebook/bart-base](https://huggingface.co/facebook/bart-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2115

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 10
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 0.4161        | 0.11  | 500   | 0.3441          |
| 0.342         | 0.21  | 1000  | 0.3091          |
| 0.2694        | 0.32  | 1500  | 0.2969          |
| 0.3792        | 0.43  | 2000  | 0.2712          |
| 0.3219        | 0.54  | 2500  | 0.2601          |
| 0.3001        | 0.64  | 3000  | 0.2574          |
| 0.2606        | 0.75  | 3500  | 0.2489          |
| 0.2716        | 0.86  | 4000  | 0.2415          |
| 0.2714        | 0.96  | 4500  | 0.2382          |
| 0.2072        | 1.07  | 5000  | 0.2429          |
| 0.2111        | 1.18  | 5500  | 0.2377          |
| 0.1977        | 1.28  | 6000  | 0.2455          |
| 0.2171        | 1.39  | 6500  | 0.2309          |
| 0.1853        | 1.5   | 7000  | 0.2314          |
| 0.2436        | 1.61  | 7500  | 0.2269          |
| 0.171         | 1.71  | 8000  | 0.2220          |
| 0.2032        | 1.82  | 8500  | 0.2226          |
| 0.2028        | 1.93  | 9000  | 0.2175          |
| 0.1448        | 2.03  | 9500  | 0.2227          |
| 0.1447        | 2.14  | 10000 | 0.2216          |
| 0.1516        | 2.25  | 10500 | 0.2200          |
| 0.1294        | 2.35  | 11000 | 0.2197          |
| 0.1569        | 2.46  | 11500 | 0.2157          |
| 0.1505        | 2.57  | 12000 | 0.2160          |
| 0.152         | 2.68  | 12500 | 0.2151          |
| 0.1588        | 2.78  | 13000 | 0.2117          |
| 0.1451        | 2.89  | 13500 | 0.2134          |
| 0.1644        | 3.0   | 14000 | 0.2115          |


### Framework versions

- Transformers 4.37.2
- Pytorch 2.1.2+cu121
- Datasets 2.17.0
- Tokenizers 0.15.1
