---
license: mit
tags:
- token_cls
- generated_from_trainer
base_model: broadfield-dev/bert-mini-ner-pii-training-tuned-12270113-tuned-12271020-tuned-12271353
datasets:
- ai4privacy/pii-masking-400k
model-index:
- name: bert-mini-ner-pii-training-tuned-12270113-tuned-12271020-tuned-12271353-tuned-12271913
  results: []
---

# bert-mini-ner-pii-training-tuned-12270113-tuned-12271020-tuned-12271353-tuned-12271913

This model is a fine-tuned version of [broadfield-dev/bert-mini-ner-pii-training-tuned-12270113-tuned-12271020-tuned-12271353](https://huggingface.co/broadfield-dev/bert-mini-ner-pii-training-tuned-12270113-tuned-12271020-tuned-12271353) on the [ai4privacy/pii-masking-400k](https://huggingface.co/ai4privacy/pii-masking-400k) dataset.

## Training Details
- **Task:** TOKEN_CLS
- **Columns:** Input: source_text  Output: privacy_mask
- **Rows:** Start: 3  End: 10000
- **Epochs:** 4
- **Learning Rate:** 2e-05
- **Gradient Accumulation Steps:** 4

## Entity Labels
`['ACCOUNTNUM', 'BUILDINGNUM', 'CITY', 'CREDITCARDNUMBER', 'DATEOFBIRTH', 'DRIVERLICENSENUM', 'EMAIL', 'GIVENNAME', 'IDCARDNUM', 'O', 'PASSWORD', 'SOCIALNUM', 'STREET', 'SURNAME', 'TAXNUM', 'TELEPHONENUM', 'USERNAME', 'ZIPCODE']`
