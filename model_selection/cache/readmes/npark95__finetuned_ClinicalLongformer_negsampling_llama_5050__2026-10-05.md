---
library_name: transformers
base_model: yikuan8/Clinical-Longformer
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: finetuned_ClinicalLongformer_negsampling_llama_5050
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_ClinicalLongformer_negsampling_llama_5050

This model is a fine-tuned version of [yikuan8/Clinical-Longformer](https://huggingface.co/yikuan8/Clinical-Longformer) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3217
- F1: 0.8889

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
| 0.6739        | 1.0   | 38   | 0.3638          | 0.8346 |
| 0.3866        | 2.0   | 76   | 0.3469          | 0.8710 |
| 0.2627        | 3.0   | 114  | 0.3217          | 0.8889 |
| 0.2636        | 4.0   | 152  | 0.3962          | 0.88   |
| 0.1862        | 5.0   | 190  | 0.5527          | 0.8403 |
| 0.2031        | 6.0   | 228  | 0.5769          | 0.8548 |
| 0.1784        | 7.0   | 266  | 0.5310          | 0.8819 |
| 0.1762        | 8.0   | 304  | 0.5902          | 0.8889 |
| 0.1089        | 9.0   | 342  | 0.7058          | 0.8594 |
| 0.0828        | 10.0  | 380  | 0.6648          | 0.8661 |
| 0.0573        | 11.0  | 418  | 0.7363          | 0.8730 |
| 0.0417        | 12.0  | 456  | 0.7568          | 0.8730 |
| 0.0727        | 13.0  | 494  | 0.8009          | 0.8618 |
| 0.0198        | 14.0  | 532  | 0.7883          | 0.8730 |
| 0.098         | 15.0  | 570  | 0.7891          | 0.8730 |


### Framework versions

- Transformers 4.48.0
- Pytorch 2.5.1+cu124
- Datasets 3.2.0
- Tokenizers 0.21.0
