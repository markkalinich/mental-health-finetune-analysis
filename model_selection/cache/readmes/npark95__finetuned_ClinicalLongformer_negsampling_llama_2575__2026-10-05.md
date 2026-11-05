---
library_name: transformers
base_model: yikuan8/Clinical-Longformer
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: finetuned_ClinicalLongformer_negsampling_llama_2575
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_ClinicalLongformer_negsampling_llama_2575

This model is a fine-tuned version of [yikuan8/Clinical-Longformer](https://huggingface.co/yikuan8/Clinical-Longformer) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1546
- F1: 0.9281

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.2101        | 1.0   | 76   | 0.2707          | 0.825  |
| 0.2161        | 2.0   | 152  | 0.1818          | 0.9178 |
| 0.372         | 3.0   | 228  | 0.1546          | 0.9281 |
| 0.1678        | 4.0   | 304  | 0.1724          | 0.9054 |
| 0.1615        | 5.0   | 380  | 0.2070          | 0.9079 |
| 0.1595        | 6.0   | 456  | 0.2347          | 0.9103 |
| 0.0517        | 7.0   | 532  | 0.2861          | 0.8936 |
| 0.08          | 8.0   | 608  | 0.3332          | 0.8732 |
| 0.1124        | 9.0   | 684  | 0.3660          | 0.8767 |
| 0.0279        | 10.0  | 760  | 0.2867          | 0.9028 |
| 0.0043        | 11.0  | 836  | 0.3631          | 0.8889 |
| 0.0299        | 12.0  | 912  | 0.3500          | 0.9041 |
| 0.0005        | 13.0  | 988  | 0.3502          | 0.9041 |
| 0.0027        | 14.0  | 1064 | 0.3698          | 0.8966 |
| 0.0004        | 15.0  | 1140 | 0.3696          | 0.9041 |


### Framework versions

- Transformers 4.48.0
- Pytorch 2.5.1+cu124
- Datasets 3.2.0
- Tokenizers 0.21.0
