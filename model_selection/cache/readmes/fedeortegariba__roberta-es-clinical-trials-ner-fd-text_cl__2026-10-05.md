---
library_name: transformers
license: cc-by-nc-4.0
base_model: lcampillos/roberta-es-clinical-trials-ner
tags:
- generated_from_trainer
metrics:
- accuracy
- recall
- precision
- f1
model-index:
- name: roberta-es-clinical-trials-ner-fd-text_cl
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-es-clinical-trials-ner-fd-text_cl

This model is a fine-tuned version of [lcampillos/roberta-es-clinical-trials-ner](https://huggingface.co/lcampillos/roberta-es-clinical-trials-ner) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0955
- Accuracy: 0.8961
- Recall: 0.9353
- Precision: 0.8926
- F1: 0.9134

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
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 30

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Recall | Precision | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:---------:|:------:|
| No log        | 1.0   | 231  | 0.2599          | 0.9107   | 0.9273 | 0.9209    | 0.9241 |
| No log        | 2.0   | 462  | 0.4050          | 0.9008   | 0.9482 | 0.8897    | 0.9180 |
| 0.1696        | 3.0   | 693  | 0.5082          | 0.8944   | 0.9412 | 0.8857    | 0.9126 |
| 0.1696        | 4.0   | 924  | 0.7025          | 0.8821   | 0.9323 | 0.8748    | 0.9026 |
| 0.0363        | 5.0   | 1155 | 0.6880          | 0.9026   | 0.9432 | 0.8959    | 0.9190 |
| 0.0363        | 6.0   | 1386 | 0.6909          | 0.9096   | 0.9263 | 0.9199    | 0.9231 |
| 0.0051        | 7.0   | 1617 | 0.8435          | 0.8938   | 0.9462 | 0.8813    | 0.9126 |
| 0.0051        | 8.0   | 1848 | 0.9259          | 0.8891   | 0.9452 | 0.8755    | 0.9090 |
| 0.0085        | 9.0   | 2079 | 0.7661          | 0.9043   | 0.9253 | 0.9126    | 0.9189 |
| 0.0085        | 10.0  | 2310 | 0.8466          | 0.8915   | 0.9452 | 0.8787    | 0.9107 |
| 0.0063        | 11.0  | 2541 | 0.8288          | 0.9043   | 0.9183 | 0.9183    | 0.9183 |
| 0.0063        | 12.0  | 2772 | 0.9942          | 0.8827   | 0.9472 | 0.8653    | 0.9044 |
| 0.009         | 13.0  | 3003 | 0.5731          | 0.9294   | 0.9223 | 0.9556    | 0.9387 |
| 0.009         | 14.0  | 3234 | 0.7689          | 0.9084   | 0.9402 | 0.9068    | 0.9232 |
| 0.009         | 15.0  | 3465 | 1.2144          | 0.8687   | 0.9532 | 0.8432    | 0.8948 |
| 0.0017        | 16.0  | 3696 | 0.9313          | 0.8956   | 0.9283 | 0.8970    | 0.9124 |
| 0.0017        | 17.0  | 3927 | 0.8994          | 0.9049   | 0.9213 | 0.9167    | 0.9190 |
| 0.001         | 18.0  | 4158 | 0.9995          | 0.8956   | 0.9323 | 0.8940    | 0.9127 |
| 0.001         | 19.0  | 4389 | 1.0237          | 0.8932   | 0.9333 | 0.8898    | 0.9110 |
| 0.0007        | 20.0  | 4620 | 1.0355          | 0.8938   | 0.9373 | 0.8877    | 0.9118 |
| 0.0007        | 21.0  | 4851 | 1.0372          | 0.8944   | 0.9343 | 0.8908    | 0.9120 |
| 0.0006        | 22.0  | 5082 | 1.0451          | 0.8944   | 0.9343 | 0.8908    | 0.9120 |
| 0.0006        | 23.0  | 5313 | 1.0461          | 0.8944   | 0.9343 | 0.8908    | 0.9120 |
| 0.0004        | 24.0  | 5544 | 1.0582          | 0.8932   | 0.9343 | 0.8891    | 0.9111 |
| 0.0004        | 25.0  | 5775 | 1.0680          | 0.8944   | 0.9373 | 0.8886    | 0.9123 |
| 0.0008        | 26.0  | 6006 | 1.0828          | 0.8921   | 0.9343 | 0.8874    | 0.9102 |
| 0.0008        | 27.0  | 6237 | 1.0875          | 0.8932   | 0.9442 | 0.8819    | 0.9120 |
| 0.0008        | 28.0  | 6468 | 1.0394          | 0.8961   | 0.9223 | 0.9025    | 0.9123 |
| 0.0022        | 29.0  | 6699 | 1.0938          | 0.8961   | 0.9353 | 0.8926    | 0.9134 |
| 0.0022        | 30.0  | 6930 | 1.0955          | 0.8961   | 0.9353 | 0.8926    | 0.9134 |


### Framework versions

- Transformers 4.51.3
- Pytorch 2.6.0+cu124
- Datasets 3.5.0
- Tokenizers 0.21.1
