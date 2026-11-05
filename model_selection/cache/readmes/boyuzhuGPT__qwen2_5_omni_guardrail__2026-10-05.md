---
library_name: transformers
tags:
- generated_from_trainer
model-index:
- name: qwen2_5_omni_guardrail
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# qwen2_5_omni_guardrail

This model was trained from scratch on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6665
- Token Acc: 0.7955

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 2
- eval_batch_size: 1
- seed: 42
- distributed_type: multi-GPU
- num_devices: 7
- gradient_accumulation_steps: 4
- total_train_batch_size: 56
- total_eval_batch_size: 7
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.95) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.05
- num_epochs: 3.0

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Token Acc |
|:-------------:|:------:|:----:|:---------------:|:---------:|
| 0.9021        | 0.1039 | 50   | 0.9205          | 0.7297    |
| 0.9695        | 0.2078 | 100  | 0.9952          | 0.7195    |
| 0.9601        | 0.3117 | 150  | 0.9734          | 0.7263    |
| 0.9378        | 0.4156 | 200  | 0.9595          | 0.7289    |
| 0.9390        | 0.5195 | 250  | 0.9449          | 0.7318    |
| 0.8926        | 0.6234 | 300  | 0.9310          | 0.7358    |
| 0.9051        | 0.7273 | 350  | 0.9156          | 0.7394    |
| 0.8859        | 0.8312 | 400  | 0.8981          | 0.7417    |
| 0.8712        | 0.9351 | 450  | 0.8760          | 0.7477    |
| 0.7780        | 1.0374 | 500  | 0.8808          | 0.7480    |
| 0.7604        | 1.1413 | 550  | 0.8487          | 0.7548    |
| 0.7572        | 1.2452 | 600  | 0.8360          | 0.7574    |
| 0.7331        | 1.3491 | 650  | 0.8217          | 0.7601    |
| 0.7224        | 1.4530 | 700  | 0.8031          | 0.7632    |
| 0.7041        | 1.5569 | 750  | 0.7866          | 0.7666    |
| 0.7000        | 1.6608 | 800  | 0.7697          | 0.7708    |
| 0.6760        | 1.7647 | 850  | 0.7534          | 0.7746    |
| 0.6628        | 1.8686 | 900  | 0.7397          | 0.7772    |
| 0.6366        | 1.9725 | 950  | 0.7249          | 0.7802    |
| 0.5454        | 2.0748 | 1000 | 0.7189          | 0.7826    |
| 0.5519        | 2.1787 | 1050 | 0.7049          | 0.7860    |
| 0.5499        | 2.2826 | 1100 | 0.6966          | 0.7884    |
| 0.5468        | 2.3865 | 1150 | 0.6902          | 0.7904    |
| 0.5225        | 2.4904 | 1200 | 0.6791          | 0.7925    |
| 0.5161        | 2.5943 | 1250 | 0.6749          | 0.7939    |
| 0.5306        | 2.6982 | 1300 | 0.6707          | 0.7944    |
| 0.4990        | 2.8021 | 1350 | 0.6682          | 0.7950    |
| 0.5109        | 2.9060 | 1400 | 0.6666          | 0.7954    |
| 0.5278        | 3.0    | 1446 | 0.6665          | 0.7955    |


### Framework versions

- Transformers 4.57.0.dev0
- Pytorch 2.8.0+cu128
- Datasets 4.1.1
- Tokenizers 0.22.1
