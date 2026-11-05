---
library_name: transformers
license: apache-2.0
base_model: bert-base-cased
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: bert-medical-speaker-role
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-medical-speaker-role

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0320
- Accuracy: 0.9952
- Precision Macro: 0.9952
- Recall Macro: 0.9952
- F1 Macro: 0.9952
- Precision Doctor: 0.9964
- Recall Doctor: 0.9939
- F1 Doctor: 0.9952
- Precision Patient: 0.9939
- Recall Patient: 0.9964
- F1 Patient: 0.9951

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 32
- optimizer: Use adamw_torch_fused with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 172
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Accuracy | F1 Doctor | F1 Macro | F1 Patient | Validation Loss | Precision Doctor | Precision Macro | Precision Patient | Recall Doctor | Recall Macro | Recall Patient |
|:-------------:|:------:|:----:|:--------:|:---------:|:--------:|:----------:|:---------------:|:----------------:|:---------------:|:-----------------:|:-------------:|:------------:|:--------------:|
| 1.6221        | 0.2191 | 125  | 0.9632   | 0.9635    | 0.9632   | 0.9629     | 0.1302          | 0.9614           | 0.9632          | 0.9651            | 0.9657        | 0.9632       | 0.9608         |
| 0.1912        | 0.4382 | 250  | 0.9835   | 0.9836    | 0.9835   | 0.9833     | 0.0461          | 0.9800           | 0.9835          | 0.9870            | 0.9872        | 0.9834       | 0.9796         |
| 0.1563        | 0.6573 | 375  | 0.9840   | 0.9840    | 0.9840   | 0.9839     | 0.0669          | 0.9896           | 0.9840          | 0.9784            | 0.9784        | 0.9840       | 0.9896         |
| 0.1186        | 0.8764 | 500  | 0.9911   | 0.9912    | 0.9911   | 0.9911     | 0.0446          | 0.9926           | 0.9911          | 0.9896            | 0.9897        | 0.9911       | 0.9925         |
| 0.1418        | 1.0947 | 625  | 0.0365   | 0.9916    | 0.9917   | 0.9916     | 0.9916          | 0.9985           | 0.9848          | 0.9916            | 0.9848        | 0.9985       | 0.9916         |
| 0.0539        | 1.3138 | 750  | 0.0213   | 0.9958    | 0.9958   | 0.9958     | 0.9958          | 0.9970           | 0.9946          | 0.9958            | 0.9945        | 0.9970       | 0.9958         |
| 0.0181        | 1.5329 | 875  | 0.0365   | 0.9906    | 0.9907   | 0.9907     | 0.9906          | 0.9975           | 0.9838          | 0.9906            | 0.9838        | 0.9975       | 0.9906         |
| 0.0787        | 1.7520 | 1000 | 0.0474   | 0.9894    | 0.9895   | 0.9894     | 0.9894          | 0.9975           | 0.9814          | 0.9894            | 0.9814        | 0.9975       | 0.9894         |
| 0.0830        | 1.9711 | 1125 | 0.0703   | 0.9896    | 0.9897   | 0.9897     | 0.9896          | 0.999            | 0.9804          | 0.9896            | 0.9805        | 0.9990       | 0.9897         |
| 0.0158        | 2.1893 | 1250 | 0.0659   | 0.9891    | 0.9893   | 0.9892     | 0.9891          | 0.9995           | 0.9789          | 0.9891            | 0.9791        | 0.9995       | 0.9892         |
| 0.0600        | 2.4084 | 1375 | 0.0646   | 0.9884    | 0.9885   | 0.9885     | 0.9884          | 0.9975           | 0.9794          | 0.9884            | 0.9795        | 0.9975       | 0.9884         |
| 0.0045        | 2.6275 | 1500 | 0.0571   | 0.9889    | 0.9890   | 0.9890     | 0.9889          | 0.9985           | 0.9794          | 0.9889            | 0.9795        | 0.9985       | 0.9889         |
| 0.0002        | 2.8466 | 1625 | 0.0544   | 0.9894    | 0.9895   | 0.9894     | 0.9894          | 0.9985           | 0.9804          | 0.9894            | 0.9805        | 0.9985       | 0.9894         |
| 0.0433        | 3.0    | 1713 | 0.0563   | 0.9889    | 0.9890   | 0.9890     | 0.9889          | 0.9985           | 0.9794          | 0.9889            | 0.9795        | 0.9985       | 0.9889         |


### Framework versions

- Transformers 5.17.0
- Pytorch 2.14.0+cu126
- Datasets 5.0.1
- Tokenizers 0.23.2
