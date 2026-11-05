---
license: mit
tags:
- token_cls
- generated_from_trainer
base_model: broadfield-dev/bert-mini-ner-pii-training-tuned-12270113-tuned-12271020
datasets:
- ai4privacy/pii-masking-400k
model-index:
- name: bert-mini-ner-pii-training-tuned-12270113-tuned-12271020-tuned-12271353
  results:
  - task:
      type: token-classification  # Common type for NER/PII tasks
      name: Named Entity Recognition
    dataset:
      name: "ai4privacy/pii-masking-400k"
      type: "dataset-id"         
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9714 
    - name: F1
      type: f1
      value: 0.8764
    - name: Precision
      type: precision
      value: 0.8748
    - name: Recall
      type: recall
      value: 0.8781

---

# bert-mini-ner-pii-training-tuned-12270113-tuned-12271020-tuned-12271353

This model is a fine-tuned version of [broadfield-dev/bert-mini-ner-pii-training-tuned-12270113-tuned-12271020](https://huggingface.co/broadfield-dev/bert-mini-ner-pii-training-tuned-12270113-tuned-12271020) on the [ai4privacy/pii-masking-400k](https://huggingface.co/ai4privacy/pii-masking-400k) dataset.

## Training Details
- **Task:** TOKEN_CLS
- **Columns:** Input: source_text  Output: privacy_mask
- **Rows:** Start: 2  End: 320000
- **Epochs:** 1
- **Learning Rate:** 2e-05
- **Gradient Accumulation Steps:** 4

## Entity Labels
`['ACCOUNTNUM', 'BUILDINGNUM', 'CITY', 'CREDITCARDNUMBER', 'DATEOFBIRTH', 'DRIVERLICENSENUM', 'EMAIL', 'GIVENNAME', 'IDCARDNUM', 'O', 'PASSWORD', 'SOCIALNUM', 'STREET', 'SURNAME', 'TAXNUM', 'TELEPHONENUM', 'USERNAME', 'ZIPCODE']`
