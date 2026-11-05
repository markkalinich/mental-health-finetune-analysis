---
license: apache-2.0
base_model: Helsinki-NLP/opus-mt-en-es
tags:
- translation
- generated_from_trainer
metrics:
- bleu
model-index:
- name: helsinki-biomedical-finetuned
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# helsinki-biomedical-finetuned

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-en-es](https://huggingface.co/Helsinki-NLP/opus-mt-en-es) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0247
- Bleu: 55.6929

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1.5e-05
- train_batch_size: 8
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: reduce_lr_on_plateau
- num_epochs: 25
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch   | Step  | Validation Loss | Bleu    |
|:-------------:|:-------:|:-----:|:---------------:|:-------:|
| 0.0289        | 0.9998  | 3293  | 0.0253          | 52.7060 |
| 0.0255        | 1.9998  | 6587  | 0.0238          | 53.6061 |
| 0.0228        | 2.9999  | 9881  | 0.0231          | 54.1920 |
| 0.0206        | 4.0     | 13175 | 0.0226          | 54.4549 |
| 0.0192        | 4.9998  | 16468 | 0.0224          | 54.5222 |
| 0.0176        | 5.9998  | 19762 | 0.0222          | 54.6624 |
| 0.0167        | 6.9999  | 23056 | 0.0221          | 55.0200 |
| 0.0154        | 8.0     | 26350 | 0.0223          | 53.3307 |
| 0.0147        | 8.9998  | 29643 | 0.0223          | 55.2185 |
| 0.0138        | 9.9998  | 32937 | 0.0224          | 54.9215 |
| 0.0133        | 10.9999 | 36231 | 0.0225          | 55.3672 |
| 0.0122        | 12.0    | 39525 | 0.0229          | 55.2831 |
| 0.0115        | 12.9998 | 42818 | 0.0231          | 55.2310 |
| 0.0108        | 13.9998 | 46112 | 0.0233          | 55.3215 |
| 0.0103        | 14.9999 | 49406 | 0.0234          | 55.3170 |
| 0.0096        | 16.0    | 52700 | 0.0237          | 55.3158 |
| 0.0089        | 16.9998 | 55993 | 0.0242          | 55.0178 |
| 0.0084        | 17.9998 | 59287 | 0.0243          | 55.1974 |
| 0.0072        | 18.9999 | 62581 | 0.0244          | 55.6011 |
| 0.007         | 20.0    | 65875 | 0.0245          | 55.5510 |
| 0.0069        | 20.9998 | 69168 | 0.0246          | 55.6178 |
| 0.0068        | 21.9998 | 72462 | 0.0246          | 55.7191 |
| 0.0068        | 22.9999 | 75756 | 0.0247          | 55.6917 |
| 0.0066        | 24.0    | 79050 | 0.0247          | 55.6962 |
| 0.0067        | 24.9943 | 82325 | 0.0247          | 55.6929 |


### Framework versions

- Transformers 4.40.2
- Pytorch 2.3.0+cu121
- Datasets 2.19.0
- Tokenizers 0.19.1
