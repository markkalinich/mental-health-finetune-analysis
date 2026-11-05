---
library_name: transformers
license: mit
base_model: microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: cellate2.0-tapt_base-LR_5e-05
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# cellate2.0-tapt_base-LR_5e-05

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1527
- Accuracy: 0.7405

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 3407
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-06 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.06
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.385         | 1.0   | 4    | 1.3146          | 0.7350   |
| 1.4161        | 2.0   | 8    | 1.2337          | 0.7449   |
| 1.3044        | 3.0   | 12   | 1.2215          | 0.7331   |
| 1.3033        | 4.0   | 16   | 1.3410          | 0.7153   |
| 1.2797        | 5.0   | 20   | 1.2776          | 0.7228   |
| 1.265         | 6.0   | 24   | 1.2818          | 0.7273   |
| 1.2078        | 7.0   | 28   | 1.2216          | 0.7442   |
| 1.1611        | 8.0   | 32   | 1.3203          | 0.7321   |
| 1.1928        | 9.0   | 36   | 1.2691          | 0.7335   |
| 1.1883        | 10.0  | 40   | 1.2359          | 0.7408   |
| 1.1549        | 11.0  | 44   | 1.2654          | 0.7350   |
| 1.1768        | 12.0  | 48   | 1.2919          | 0.7224   |
| 1.1169        | 13.0  | 52   | 1.2514          | 0.7263   |
| 1.1635        | 14.0  | 56   | 1.2352          | 0.7324   |
| 1.0975        | 15.0  | 60   | 1.2906          | 0.7385   |
| 1.0897        | 16.0  | 64   | 1.2099          | 0.7337   |
| 0.9993        | 17.0  | 68   | 1.2057          | 0.7395   |
| 1.0331        | 18.0  | 72   | 1.2895          | 0.7347   |
| 1.1321        | 19.0  | 76   | 1.2824          | 0.7386   |
| 1.083         | 20.0  | 80   | 1.1527          | 0.7405   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
