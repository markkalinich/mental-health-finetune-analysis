---
library_name: transformers
base_model: yikuan8/Clinical-Longformer
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: finetuned_ClinicalLongformer_CAT
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_ClinicalLongformer_CAT

This model is a fine-tuned version of [yikuan8/Clinical-Longformer](https://huggingface.co/yikuan8/Clinical-Longformer) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5686
- F1: 0.6565

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 30

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.7643        | 1.0   | 88   | 0.6880          | 0.4545 |
| 0.5304        | 2.0   | 176  | 0.5686          | 0.6565 |
| 0.4965        | 3.0   | 264  | 0.5383          | 0.6333 |
| 0.5511        | 4.0   | 352  | 0.5025          | 0.6387 |
| 0.4464        | 5.0   | 440  | 0.8222          | 0.6324 |
| 0.524         | 6.0   | 528  | 0.5835          | 0.6387 |
| 0.5914        | 7.0   | 616  | 0.5681          | 0.6333 |
| 0.4904        | 8.0   | 704  | 0.7025          | 0.6190 |
| 0.368         | 9.0   | 792  | 1.0666          | 0.5984 |
| 0.5524        | 10.0  | 880  | 0.9018          | 0.5909 |
| 0.4279        | 11.0  | 968  | 1.4256          | 0.5672 |
| 0.423         | 12.0  | 1056 | 1.4379          | 0.5571 |
| 0.437         | 13.0  | 1144 | 1.8244          | 0.5507 |
| 0.3844        | 14.0  | 1232 | 1.7702          | 0.5455 |
| 0.4193        | 15.0  | 1320 | 2.4407          | 0.5412 |
| 0.3736        | 16.0  | 1408 | 2.1648          | 0.5369 |
| 0.3675        | 17.0  | 1496 | 2.1035          | 0.5306 |
| 0.2557        | 18.0  | 1584 | 2.3772          | 0.5430 |
| 0.2683        | 19.0  | 1672 | 2.4857          | 0.5430 |
| 0.251         | 20.0  | 1760 | 2.5679          | 0.5306 |
| 0.2913        | 21.0  | 1848 | 2.5935          | 0.5395 |
| 0.2671        | 22.0  | 1936 | 2.6229          | 0.5430 |
| 0.3045        | 23.0  | 2024 | 2.7196          | 0.5430 |
| 0.2878        | 24.0  | 2112 | 2.7983          | 0.5333 |
| 0.388         | 25.0  | 2200 | 2.9204          | 0.5325 |
| 0.308         | 26.0  | 2288 | 2.9649          | 0.5395 |
| 0.3096        | 27.0  | 2376 | 2.9466          | 0.5430 |
| 0.339         | 28.0  | 2464 | 2.9776          | 0.5290 |
| 0.1394        | 29.0  | 2552 | 2.9992          | 0.5290 |
| 0.2073        | 30.0  | 2640 | 3.0120          | 0.5290 |


### Framework versions

- Transformers 4.48.0
- Pytorch 2.5.1+cu124
- Datasets 3.2.0
- Tokenizers 0.21.0
