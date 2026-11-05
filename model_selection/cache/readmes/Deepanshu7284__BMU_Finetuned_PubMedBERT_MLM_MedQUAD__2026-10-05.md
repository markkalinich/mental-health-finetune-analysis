---
library_name: transformers
license: mit
base_model: microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext
tags:
- generated_from_trainer
model-index:
- name: BMU_Finetuned_PubMedBERT_MLM_MedQUAD
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BMU_Finetuned_PubMedBERT_MLM_MedQUAD

This model is a fine-tuned version of [microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5522

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2.2672        | 1.0   | 616  | 1.9948          |
| 2.0847        | 2.0   | 1232 | 1.8343          |
| 1.7977        | 3.0   | 1848 | 1.7409          |
| 1.5881        | 4.0   | 2464 | 1.6755          |
| 1.6609        | 5.0   | 3080 | 1.6300          |
| 1.7369        | 6.0   | 3696 | 1.6144          |
| 1.721         | 7.0   | 4312 | 1.5940          |
| 1.6352        | 8.0   | 4928 | 1.5743          |
| 1.4389        | 9.0   | 5544 | 1.5766          |
| 1.387         | 10.0  | 6160 | 1.5522          |


### Framework versions

- Transformers 4.47.0
- Pytorch 2.5.1+cu121
- Datasets 3.3.1
- Tokenizers 0.21.0
