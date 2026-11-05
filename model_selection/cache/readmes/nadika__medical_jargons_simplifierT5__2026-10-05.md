---
base_model: luqh/ClinicalT5-base
tags:
- generated_from_trainer
model-index:
- name: medical_jargons_simplifierT5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medical_jargons_simplifierT5

This model is a fine-tuned version of [luqh/ClinicalT5-base](https://huggingface.co/luqh/ClinicalT5-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4734

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
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 50
- num_epochs: 5

### Training results

| Training Loss | Epoch  | Step  | Validation Loss |
|:-------------:|:------:|:-----:|:---------------:|
| 3.3369        | 0.2198 | 500   | 0.5700          |
| 0.601         | 0.4396 | 1000  | 0.5279          |
| 0.572         | 0.6593 | 1500  | 0.5137          |
| 0.5556        | 0.8791 | 2000  | 0.5051          |
| 0.5132        | 1.0989 | 2500  | 0.4991          |
| 0.5406        | 1.3187 | 3000  | 0.4941          |
| 0.513         | 1.5385 | 3500  | 0.4909          |
| 0.5328        | 1.7582 | 4000  | 0.4880          |
| 0.5304        | 1.9780 | 4500  | 0.4846          |
| 0.5215        | 2.1978 | 5000  | 0.4825          |
| 0.5296        | 2.4176 | 5500  | 0.4811          |
| 0.5143        | 2.6374 | 6000  | 0.4799          |
| 0.4768        | 2.8571 | 6500  | 0.4780          |
| 0.513         | 3.0769 | 7000  | 0.4775          |
| 0.4933        | 3.2967 | 7500  | 0.4761          |
| 0.4891        | 3.5165 | 8000  | 0.4761          |
| 0.5022        | 3.7363 | 8500  | 0.4749          |
| 0.523         | 3.9560 | 9000  | 0.4743          |
| 0.5233        | 4.1758 | 9500  | 0.4742          |
| 0.5004        | 4.3956 | 10000 | 0.4738          |
| 0.4817        | 4.6154 | 10500 | 0.4733          |
| 0.4848        | 4.8352 | 11000 | 0.4734          |


### Framework versions

- Transformers 4.41.2
- Pytorch 2.1.2
- Datasets 2.19.2
- Tokenizers 0.19.1
