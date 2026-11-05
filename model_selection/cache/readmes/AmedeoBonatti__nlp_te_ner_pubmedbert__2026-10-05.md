---
license: mit
base_model: AmedeoBonatti/nlp_te_mlm_pubmedbert
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: nlp_te_ner_pubmedbert
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# nlp_te_ner_pubmedbert

This model is a fine-tuned version of [AmedeoBonatti/nlp_te_mlm_pubmedbert](https://huggingface.co/AmedeoBonatti/nlp_te_mlm_pubmedbert) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0181
- Precision: 0.9817
- Recall: 0.9840
- F1: 0.9829
- Accuracy: 0.9959

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 50
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 21   | 0.0206          | 0.9783    | 0.9832 | 0.9808 | 0.9950   |
| No log        | 2.0   | 42   | 0.0209          | 0.9766    | 0.9820 | 0.9793 | 0.9948   |
| No log        | 3.0   | 63   | 0.0206          | 0.9788    | 0.9827 | 0.9807 | 0.9949   |
| No log        | 4.0   | 84   | 0.0181          | 0.9817    | 0.9840 | 0.9829 | 0.9959   |
| No log        | 5.0   | 105  | 0.0200          | 0.9785    | 0.9827 | 0.9806 | 0.9950   |
| No log        | 6.0   | 126  | 0.0231          | 0.9705    | 0.9799 | 0.9752 | 0.9933   |
| No log        | 7.0   | 147  | 0.0227          | 0.9738    | 0.9789 | 0.9764 | 0.9937   |
| No log        | 8.0   | 168  | 0.0234          | 0.9726    | 0.9777 | 0.9751 | 0.9936   |
| No log        | 9.0   | 189  | 0.0213          | 0.9768    | 0.9794 | 0.9781 | 0.9945   |


### Framework versions

- Transformers 4.41.2
- Pytorch 2.2.1
- Datasets 2.19.2
- Tokenizers 0.19.1
