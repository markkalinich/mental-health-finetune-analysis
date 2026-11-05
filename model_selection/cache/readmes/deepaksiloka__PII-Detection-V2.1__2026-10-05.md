---
library_name: transformers
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- generated_from_trainer
model-index:
- name: PII-Detection-V2.1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# PII-Detection-V2.1

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0331
- Overall Precision: 0.9482
- Overall Recall: 0.9574
- Overall F1: 0.9528
- Overall Accuracy: 0.9926
- Accountname F1: 0.9939
- Accountnumber F1: 0.9879
- Buildingnumber F1: 0.8059
- City F1: 0.9729
- Companyname F1: 0.9773
- County F1: 0.9463
- Creditcardcvv F1: 0.8970
- Creditcardissuer F1: 0.9565
- Creditcardnumber F1: 0.8770
- Email F1: 0.9981
- Firstname F1: 0.9324
- Fullname F1: 0.9851
- Iban F1: 0.9834
- Lastname F1: 0.8744
- Middlename F1: 0.8390
- Name F1: 0.9972
- Number F1: 0.9684
- Phonenumber F1: 0.9788
- Pin F1: 0.9017
- Secondaryaddress F1: 0.9892
- State F1: 0.9421
- Street F1: 0.8617
- Streetaddress F1: 0.7533
- Url F1: 0.9977
- Username F1: 0.9654

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
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Overall Precision | Overall Recall | Overall F1 | Overall Accuracy | Accountname F1 | Accountnumber F1 | Buildingnumber F1 | City F1 | Companyname F1 | County F1 | Creditcardcvv F1 | Creditcardissuer F1 | Creditcardnumber F1 | Email F1 | Firstname F1 | Fullname F1 | Iban F1 | Lastname F1 | Middlename F1 | Name F1 | Number F1 | Phonenumber F1 | Pin F1 | Secondaryaddress F1 | State F1 | Street F1 | Streetaddress F1 | Url F1 | Username F1 |
|:-------------:|:-----:|:-----:|:---------------:|:-----------------:|:--------------:|:----------:|:----------------:|:--------------:|:----------------:|:-----------------:|:-------:|:--------------:|:---------:|:----------------:|:-------------------:|:-------------------:|:--------:|:------------:|:-----------:|:-------:|:-----------:|:-------------:|:-------:|:---------:|:--------------:|:------:|:-------------------:|:--------:|:---------:|:----------------:|:------:|:-----------:|
| 0.0445        | 1.0   | 2031  | 0.0375          | 0.8924            | 0.9268         | 0.9093     | 0.9885           | 0.9781         | 0.9675           | 0.7260            | 0.9391  | 0.9347         | 0.8747    | 0.8221           | 0.8962              | 0.8239              | 0.9948   | 0.8764       | 0.9804      | 0.9528  | 0.7683      | 0.6548        | 0.9889  | 0.8223    | 0.9277         | 0.7938 | 0.9853              | 0.8633   | 0.7646    | 0.4597           | 0.9937 | 0.9427      |
| 0.0266        | 2.0   | 4062  | 0.0296          | 0.9245            | 0.9455         | 0.9349     | 0.9908           | 0.9900         | 0.9810           | 0.7546            | 0.9639  | 0.9574         | 0.9085    | 0.8370           | 0.9375              | 0.8809              | 0.9979   | 0.9094       | 0.9824      | 0.9785  | 0.8299      | 0.8111        | 0.9938  | 0.9247    | 0.9523         | 0.8640 | 0.9826              | 0.9163   | 0.7605    | 0.6372           | 0.9977 | 0.9599      |
| 0.0148        | 3.0   | 6093  | 0.0277          | 0.9414            | 0.9529         | 0.9471     | 0.9921           | 0.9948         | 0.9863           | 0.7876            | 0.9689  | 0.9624         | 0.9324    | 0.8883           | 0.9537              | 0.8795              | 0.9979   | 0.9252       | 0.9849      | 0.9840  | 0.8515      | 0.8310        | 0.9946  | 0.9506    | 0.9675         | 0.8685 | 0.9875              | 0.9325   | 0.8355    | 0.7560           | 0.9973 | 0.9685      |
| 0.0095        | 4.0   | 8124  | 0.0301          | 0.9438            | 0.9536         | 0.9487     | 0.9921           | 0.9913         | 0.9859           | 0.8018            | 0.9742  | 0.9652         | 0.9443    | 0.8982           | 0.9508              | 0.8784              | 0.9986   | 0.9281       | 0.9842      | 0.9828  | 0.8584      | 0.8294        | 0.9952  | 0.9681    | 0.9629         | 0.8889 | 0.9875              | 0.9374   | 0.8430    | 0.7522           | 0.9980 | 0.9457      |
| 0.0038        | 5.0   | 10155 | 0.0331          | 0.9482            | 0.9574         | 0.9528     | 0.9926           | 0.9939         | 0.9879           | 0.8059            | 0.9729  | 0.9773         | 0.9463    | 0.8970           | 0.9565              | 0.8770              | 0.9981   | 0.9324       | 0.9851      | 0.9834  | 0.8744      | 0.8390        | 0.9972  | 0.9684    | 0.9788         | 0.9017 | 0.9892              | 0.9421   | 0.8617    | 0.7533           | 0.9977 | 0.9654      |


### Framework versions

- Transformers 4.45.2
- Pytorch 2.2.0
- Datasets 3.0.1
- Tokenizers 0.20.1
