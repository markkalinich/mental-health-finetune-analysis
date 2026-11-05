---
library_name: transformers
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- generated_from_trainer
model-index:
- name: PII-Detection
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# PII-Detection

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0643
- Overall Precision: 0.9370
- Overall Recall: 0.9502
- Overall F1: 0.9436
- Overall Accuracy: 0.9823
- Accountname F1: 0.9835
- Accountnumber F1: 0.9792
- Amount F1: 0.9439
- Bic F1: 0.8741
- Bitcoinaddress F1: 0.9478
- Buildingnumber F1: 0.6465
- City F1: 0.9865
- Company Name F1: 0.9583
- County F1: 0.9811
- Creditcardcvv F1: 0.9007
- Creditcardissuer F1: 0.9302
- Creditcardnumber F1: 0.8662
- Currency F1: 0.7101
- Currencycode F1: 0.7445
- Currencyname F1: 0.4375
- Currencysymbol F1: 0.5600
- Date F1: 0.9873
- Displayname F1: 0.4706
- Email F1: 0.9991
- Ethereumaddress F1: 0.9808
- Firstname F1: 0.8912
- Fullname F1: 0.9867
- Gender F1: 0.8462
- Iban F1: 0.9947
- Ip F1: 0.2642
- Ipv4 F1: 0.8165
- Ipv6 F1: 0.6330
- Jobarea F1: 0.9734
- Jobdescriptor F1: 0.8723
- Jobtitle F1: 0.9760
- Jobtype F1: 0.9150
- Lastname F1: 0.7589
- Litecoinaddress F1: 0.9123
- Mac F1: 1.0
- Maskednumber F1: 0.8000
- Middlename F1: 0.8033
- Name F1: 0.9966
- Nearbygpscoordinate F1: 1.0
- Number F1: 0.9159
- Ordinaldirection F1: 0.0
- Password F1: 0.9497
- Phoneimei F1: 0.9756
- Phone Number F1: 0.9244
- Pin F1: 0.8889
- Prefix F1: 0.9009
- Secondaryaddress F1: 0.9939
- Sex F1: 0.9032
- Sextype F1: 0.0
- Ssn F1: 0.8992
- State F1: 0.9931
- Street F1: 0.6906
- Streetaddress F1: 0.8523
- Suffix F1: 0.9026
- Time F1: 0.9796
- Url F1: 0.9973
- Useragent F1: 0.9839
- Username F1: 0.8900
- Vehiclevin F1: 0.9612
- Vehiclevrm F1: 0.9697
- Zipcode F1: 0.9387

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

| Training Loss | Epoch | Step | Validation Loss | Overall Precision | Overall Recall | Overall F1 | Overall Accuracy | Accountname F1 | Accountnumber F1 | Amount F1 | Bic F1 | Bitcoinaddress F1 | Buildingnumber F1 | City F1 | Company Name F1 | County F1 | Creditcardcvv F1 | Creditcardissuer F1 | Creditcardnumber F1 | Currency F1 | Currencycode F1 | Currencyname F1 | Currencysymbol F1 | Date F1 | Displayname F1 | Email F1 | Ethereumaddress F1 | Firstname F1 | Fullname F1 | Gender F1 | Iban F1 | Ip F1  | Ipv4 F1 | Ipv6 F1 | Jobarea F1 | Jobdescriptor F1 | Jobtitle F1 | Jobtype F1 | Lastname F1 | Litecoinaddress F1 | Mac F1 | Maskednumber F1 | Middlename F1 | Name F1 | Nearbygpscoordinate F1 | Number F1 | Ordinaldirection F1 | Password F1 | Phoneimei F1 | Phone Number F1 | Pin F1 | Prefix F1 | Secondaryaddress F1 | Sex F1 | Sextype F1 | Ssn F1 | State F1 | Street F1 | Streetaddress F1 | Suffix F1 | Time F1 | Url F1 | Useragent F1 | Username F1 | Vehiclevin F1 | Vehiclevrm F1 | Zipcode F1 |
|:-------------:|:-----:|:----:|:---------------:|:-----------------:|:--------------:|:----------:|:----------------:|:--------------:|:----------------:|:---------:|:------:|:-----------------:|:-----------------:|:-------:|:---------------:|:---------:|:----------------:|:-------------------:|:-------------------:|:-----------:|:---------------:|:---------------:|:-----------------:|:-------:|:--------------:|:--------:|:------------------:|:------------:|:-----------:|:---------:|:-------:|:------:|:-------:|:-------:|:----------:|:----------------:|:-----------:|:----------:|:-----------:|:------------------:|:------:|:---------------:|:-------------:|:-------:|:----------------------:|:---------:|:-------------------:|:-----------:|:------------:|:---------------:|:------:|:---------:|:-------------------:|:------:|:----------:|:------:|:--------:|:---------:|:----------------:|:---------:|:-------:|:------:|:------------:|:-----------:|:-------------:|:-------------:|:----------:|
| 0.1445        | 1.0   | 1337 | 0.0873          | 0.8766            | 0.9038         | 0.8900     | 0.9710           | 0.9132         | 0.9245           | 0.8316    | 0.6260 | 0.7211            | 0.5392            | 0.9670  | 0.8041          | 0.9658    | 0.6462           | 0.7333              | 0.6833              | 0.5885      | 0.4341          | 0.016           | 0.0513            | 0.9726  | 0.0            | 0.9986   | 0.8778             | 0.7974       | 0.9812      | 0.5905    | 0.8744  | 0.0405 | 0.7125  | 0.7616  | 0.9148     | 0.0              | 0.7961      | 0.5644     | 0.5821      | 0.6442             | 0.9573 | 0.2375          | 0.1486        | 0.9865  | 0.3077                 | 0.7009    | 0.0                 | 0.8883      | 0.9697       | 0.7985          | 0.6387 | 0.8256    | 0.8772              | 0.8742 | 0.0        | 0.8593 | 0.9870   | 0.5492    | 0.8496           | 0.4966    | 0.9632  | 0.9754 | 0.9370       | 0.8839      | 0.8857        | 0.8           | 0.8691     |
| 0.0599        | 2.0   | 2674 | 0.0573          | 0.9218            | 0.9369         | 0.9293     | 0.9786           | 0.9669         | 0.9679           | 0.9179    | 0.8429 | 0.78              | 0.4982            | 0.9831  | 0.9375          | 0.9774    | 0.8873           | 0.9153              | 0.8418              | 0.7326      | 0.6621          | 0.1102          | 0.5634            | 0.975   | 0.0            | 0.9972   | 0.9202             | 0.8603       | 0.9859      | 0.7925    | 0.9684  | 0.1164 | 0.7847  | 0.7129  | 0.9626     | 0.6752           | 0.9445      | 0.8734     | 0.6809      | 0.6931             | 0.9811 | 0.7468          | 0.6905        | 0.9943  | 1.0                    | 0.8165    | 0.0                 | 0.9385      | 0.9756       | 0.8465          | 0.8190 | 0.8899    | 0.9878              | 0.8861 | 0.0        | 0.8769 | 0.9905   | 0.6496    | 0.8784           | 0.8513    | 0.9662  | 0.9932 | 0.9490       | 0.9149      | 0.9394        | 0.9265        | 0.8732     |
| 0.0411        | 3.0   | 4011 | 0.0517          | 0.9146            | 0.9444         | 0.9292     | 0.9804           | 0.9703         | 0.9837           | 0.9269    | 0.8939 | 0.8806            | 0.615             | 0.9837  | 0.9220          | 0.9811    | 0.8742           | 0.9249              | 0.8497              | 0.6351      | 0.6970          | 0.4037          | 0.5195            | 0.9824  | 0.3956         | 0.9989   | 0.9761             | 0.8779       | 0.9851      | 0.8081    | 0.9894  | 0.1043 | 0.8622  | 0.5398  | 0.9655     | 0.8333           | 0.9742      | 0.92       | 0.7368      | 0.8432             | 0.9905 | 0.7389          | 0.7661        | 0.9947  | 1.0                    | 0.8505    | 0.0                 | 0.9435      | 1.0          | 0.9204          | 0.8491 | 0.8920    | 0.9878              | 0.8889 | 0.0        | 0.9538 | 0.9896   | 0.6269    | 0.7057           | 0.8900    | 0.9796  | 0.9945 | 0.9641       | 0.8623      | 0.9606        | 0.9143        | 0.9672     |
| 0.0226        | 4.0   | 5348 | 0.0599          | 0.9349            | 0.9482         | 0.9415     | 0.9824           | 0.9835         | 0.9746           | 0.9041    | 0.8939 | 0.8963            | 0.6707            | 0.9871  | 0.9141          | 0.9848    | 0.8707           | 0.9302              | 0.8702              | 0.6916      | 0.6618          | 0.3830          | 0.5195            | 0.9848  | 0.4651         | 0.9986   | 0.9581             | 0.8872       | 0.9862      | 0.8776    | 0.9892  | 0.2561 | 0.8682  | 0.7172  | 0.9726     | 0.8763           | 0.9814      | 0.9322     | 0.7266      | 0.7826             | 0.9952 | 0.8193          | 0.7256        | 0.9960  | 1.0                    | 0.9014    | 0.0                 | 0.9494      | 0.9816       | 0.9238          | 0.8462 | 0.9002    | 0.9939              | 0.8987 | 0.0        | 0.9091 | 0.9922   | 0.6997    | 0.8472           | 0.8821    | 0.9796  | 0.9973 | 0.9758       | 0.8940      | 0.9538        | 0.9624        | 0.9485     |
| 0.0129        | 5.0   | 6685 | 0.0643          | 0.9370            | 0.9502         | 0.9436     | 0.9823           | 0.9835         | 0.9792           | 0.9439    | 0.8741 | 0.9478            | 0.6465            | 0.9865  | 0.9583          | 0.9811    | 0.9007           | 0.9302              | 0.8662              | 0.7101      | 0.7445          | 0.4375          | 0.5600            | 0.9873  | 0.4706         | 0.9991   | 0.9808             | 0.8912       | 0.9867      | 0.8462    | 0.9947  | 0.2642 | 0.8165  | 0.6330  | 0.9734     | 0.8723           | 0.9760      | 0.9150     | 0.7589      | 0.9123             | 1.0    | 0.8000          | 0.8033        | 0.9966  | 1.0                    | 0.9159    | 0.0                 | 0.9497      | 0.9756       | 0.9244          | 0.8889 | 0.9009    | 0.9939              | 0.9032 | 0.0        | 0.8992 | 0.9931   | 0.6906    | 0.8523           | 0.9026    | 0.9796  | 0.9973 | 0.9839       | 0.8900      | 0.9612        | 0.9697        | 0.9387     |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.1
- Tokenizers 0.19.1
