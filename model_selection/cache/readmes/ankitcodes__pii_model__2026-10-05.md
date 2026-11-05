---
license: apache-2.0
base_model: bert-base-cased
tags:
- PII
- NER
- Bert
- Token Classification
datasets:
- generator
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: pii_model
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: generator
      type: generator
      config: default
      split: train
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.954751
    - name: Recall
      type: recall
      value: 0.965233
    - name: F1
      type: f1
      value: 0.959964
    - name: Accuracy
      type: accuracy
      value: 0.991199
pipeline_tag: token-classification
language:
- en
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->



## Model can Detect Following Entity Group

- ACCOUNTNUMBER
- FIRSTNAME
- ACCOUNTNAME
- PHONENUMBER
- CREDITCARDCVV
- CREDITCARDISSUER
- PREFIX
- LASTNAME
- AMOUNT
- DATE
- DOB
- COMPANYNAME
- BUILDINGNUMBER
- STREET
- SECONDARYADDRESS
- STATE
- EMAIL
- CITY
- CREDITCARDNUMBER
- SSN
- URL
- USERNAME
- PASSWORD
- COUNTY
- PIN
- MIDDLENAME
- IBAN
- GENDER
- AGE
- ZIPCODE
- SEX










### Framework versions

- Transformers 4.38.2
- Pytorch 2.1.0+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2