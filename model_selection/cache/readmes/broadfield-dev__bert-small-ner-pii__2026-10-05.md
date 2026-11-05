---
license: mit
tags:
- token_cls
- generated_from_trainer
base_model: prajjwal1/bert-small
datasets:
- ai4privacy/pii-masking-400k
model-index:
- name: bert-small-tuned-12260932
  results: []
---

# bert-small-tuned-12260932

This model is a fine-tuned version of [prajjwal1/bert-small](https://huggingface.co/prajjwal1/bert-small) on the [ai4privacy/pii-masking-400k](https://huggingface.co/ai4privacy/pii-masking-400k) dataset.

## Training Details
- **Task:** TOKEN_CLS
- **Columns:** Input: source_text  Output: privacy_mask
- **Rows:** Start: 0  End: 10000
- **Epochs:** 4
- **Learning Rate:** 2e-05
- **Gradient Accumulation Steps:** 4

## Entity Labels
`['ACCOUNTNUM', 'BUILDINGNUM', 'CITY', 'CREDITCARDNUMBER', 'DATEOFBIRTH', 'DRIVERLICENSENUM', 'EMAIL', 'GIVENNAME', 'IDCARDNUM', 'O', 'PASSWORD', 'SOCIALNUM', 'STREET', 'SURNAME', 'TAXNUM', 'TELEPHONENUM', 'USERNAME', 'ZIPCODE']`
