---
license: mit
tags:
- token_cls
- generated_from_trainer
base_model: broadfield-dev/bert-small-ner-pii-tuned-12261022-tuned-12272248
datasets:
- ai4privacy/pii-masking-400k
model-index:
- name: bert-small-ner-pii-tuned-12261022-tuned-12272248-tuned-12280500
  results: []
---

# bert-small-ner-pii-tuned-12261022-tuned-12272248-tuned-12280500

This model is a fine-tuned version of [broadfield-dev/bert-small-ner-pii-tuned-12261022-tuned-12272248](https://huggingface.co/broadfield-dev/bert-small-ner-pii-tuned-12261022-tuned-12272248) on the [ai4privacy/pii-masking-400k](https://huggingface.co/ai4privacy/pii-masking-400k) dataset.

## Training Details
- **Task:** TOKEN_CLS
- **Columns:** Input: source_text  Output: privacy_mask
- **Rows:** Start: 2  End: 320000
- **Epochs:** 1
- **Learning Rate:** 2e-05
- **Gradient Accumulation Steps:** 8

## Entity Labels
`['ACCOUNTNUM', 'BUILDINGNUM', 'CITY', 'CREDITCARDNUMBER', 'DATEOFBIRTH', 'DRIVERLICENSENUM', 'EMAIL', 'GIVENNAME', 'IDCARDNUM', 'O', 'PASSWORD', 'SOCIALNUM', 'STREET', 'SURNAME', 'TAXNUM', 'TELEPHONENUM', 'USERNAME', 'ZIPCODE']`
