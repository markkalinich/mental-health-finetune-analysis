---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
- text-classification
- emotion
- pytorch
datasets:
- emotion
metrics:
- accuracy
- f1
- precision
- recall
base_model: distilbert-base-cased
model-index:
- name: distilbert-base-cased-emotion
  results:
  - task:
      type: text-classification
      name: text-classification
    dataset:
      name: emotion
      type: emotion
      config: default
      split: validation
    metrics:
    - type: accuracy
      value: 0.9235
      name: accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOTI0NGY1MTgwMzViYzY2NzdmOTk2NGM0YjRjMDExYjRkNDY3YmQzZmY4Y2JlMGQ3ZThlNjNjMjQ1OTI4MjdlOSIsInZlcnNpb24iOjF9.jJ8RC2HTtWrq3_b592HIFBlKuGavgSMrp--gwLFLZ66Uuz44gnouotoYpsqMtgUt-S3lkcCUs2ZFOPo6xR2EAA
    - type: accuracy
      value: 0.938
      name: Accuracy
      verified: true
    - type: precision
      value: 0.9281100797474869
      name: Precision Macro
      verified: true
    - type: precision
      value: 0.938
      name: Precision Micro
      verified: true
    - type: precision
      value: 0.9376891512759605
      name: Precision Weighted
      verified: true
    - type: recall
      value: 0.9029821552608664
      name: Recall Macro
      verified: true
    - type: recall
      value: 0.938
      name: Recall Micro
      verified: true
    - type: recall
      value: 0.938
      name: Recall Weighted
      verified: true
    - type: f1
      value: 0.9147207975135915
      name: F1 Macro
      verified: true
    - type: f1
      value: 0.938
      name: F1 Micro
      verified: true
    - type: f1
      value: 0.9373403463117288
      name: F1 Weighted
      verified: true
    - type: loss
      value: 0.23682540655136108
      name: loss
      verified: true
    - type: accuracy
      value: 0.938
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYTUwM2MxN2Q0MGY2MjM5N2IyNjM1Y2Q5ZTM3YzRjYzU1NWQ3MGM1M2E2OWY5YTYyOGVjNTRmODc2ZDkxYzRlMyIsInZlcnNpb24iOjF9.vUgzbI8tmXYBL4OmW3y9GJx_J_j_o6hs1fmxgc-SgaF7B6Qr0qxVwTahvxKnJjad8KnA-aEfQWRYhwVpAr44Dw
    - type: precision
      value: 0.9281100797474869
      name: Precision Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMjQ1Mzg5NmI2MjU0MjA1N2EzNmQ1MGVhYjgyYTg5YmVjMGY5ZDhkMmJmNmVhZDI0ZDNmZDJhZjg0NDUzNzEzMiIsInZlcnNpb24iOjF9.kK_Lg1Vy1dXCSzEik-0vfP15icUf1RNYNs_dcXc46PAXU1TWF1t4CKUXmu6FFyRyAWKMp90dH_Ss7VIMj1-OAw
    - type: precision
      value: 0.938
      name: Precision Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOTdiNWE1ZmFmYmE3NDc0YmUyYjRiNGZmMDk5NTg5YWUyOTQyYmNkOWM3M2Y4ZjI4ZWU3Mzk2NTU1YjQxM2QzMiIsInZlcnNpb24iOjF9.9UVnzkkjthoZML84FS8cWbr88JPgG2RQtC7k_I4a3rCC0T6LMsJSoMWCOIz6a6tnpO26q-_x-wM70GzzSanmCg
    - type: precision
      value: 0.9376891512759605
      name: Precision Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNTU2ZDVjYjk5YTMwYWY2YmZjNDdkMTFkMWI5NjI3YjQ3Njk2NWQ0OGM2ZjYyZWRhZjE2YzM5YjA3NjU1YmFlNiIsInZlcnNpb24iOjF9.fixCk6zcIOYsk3LgfCHeSQ5YNoJ-ZWxvvW76g1-s2yjrI5Qmf_VQcNlyDr_pmHtZ7mc3yykCPaD6k2oMKZ5QBw
    - type: recall
      value: 0.9029821552608664
      name: Recall Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZjA0NTc4MGExMmExNWZjNjc1MDA3MDI4MmMwMTNjYWQ0YmVkZjExNzdkZTJkNmMwZWIyNjA4MTNlMDRmODkwNiIsInZlcnNpb24iOjF9.rAq4wFgCo6Q3mxElGdnbXlzVyUvSYOFW-m1KHzDFTydt-4Re-SUVjeh2y8HFf5H0Te5Jj5SiXfszJUmwFXh1Ag
    - type: recall
      value: 0.938
      name: Recall Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMDk4NTE4YjZmZDdlNmI1NDkxYmU4ZjAzODhiNGFhYTAxNGEyNjY2MGE3MWQwNGFkMDhkZjNkYjkzNWQxZDQ1YiIsInZlcnNpb24iOjF9.l2JP6XY0XWRFB6G5A82CQy9-Isn48vAGickkwvhMhcW7cZsPjDTLHg2wyBjD8etcYzU99RdfR9nusSnWxBvxAQ
    - type: recall
      value: 0.938
      name: Recall Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMTEwNGQ0NDc0NWE2OGUzMjkwMWM2MGRhODViNmIwMDU1NDk3OTdlOWI1N2VlN2JmY2MzYWI4YjJhNDFhYWVhNCIsInZlcnNpb24iOjF9.IV35Ctc1lhxXGP5J3PQxWi6IpWH1ZyZ95yrrca6-EzlF0w3AYL1Bk8q_glolpmrBqUBrJH8AJ07MFN3g77UzCA
    - type: f1
      value: 0.9147207975135915
      name: F1 Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZDFlNDk2OWUxOWQ5MTY1MTg3MDU2MzA5OGVmYTk2ODgyNDRiNWU5ZDZmYWYzYmMyMTcyZGExMWE1MGQ2Mzk2MyIsInZlcnNpb24iOjF9.GdxhM7wmt4DQucMB21z0ZZx-iOSlf7wYIs01U6dERhXHX4gsDaFIuIFCVNPFZpwerUYUz6Xtsl6jK1v9kkjqBA
    - type: f1
      value: 0.938
      name: F1 Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMTFlM2JlYWFhZjQzNGVjNjhhMTQ3MWZlNGFlMDI5YjEyYWQzMmY3MzQ4MmEzYzg0ZjIyZTZlODNmMTRlZWI5OSIsInZlcnNpb24iOjF9.EKJExY6JPzTwnnPzBPTCoDTowYYly6jKw4Qypsj3GKEpzwmqG-hoo5yhyZaoWsRL2hb1W6eHbsZtPdy1HqGLDQ
    - type: f1
      value: 0.9373403463117288
      name: F1 Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYzU1MjI3NTc4N2MxYTI5MjI1OTc3YjFhYjdkZDZmY2MxOTkyYzMzMWIxY2JmNGRkNDg2MTk0YTRiOWJhMTBhNCIsInZlcnNpb24iOjF9.bqFLqztywdiWTm-r7oeQ_R3_VKOTBkyxbL_sZktEE3hsJHYhwLOEVeKD7sqt56gQu_JNYMCz6WGWKRECFKH3Cw
    - type: loss
      value: 0.23682540655136108
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOWZlZjkwNmJjYjAzYzk4ZjU4NzNiYzg1NTU1MGQ3OTFjYmE4MjE5NzNkYzZiZDI0ZmNkM2Y2NGU4ZjJlOThlOSIsInZlcnNpb24iOjF9.mYcz4sdJOmXXMBGW01OSJiKCouKh28AuExj1E7JiPCz-9ri3oRXPkT2fBHgrf0I2ifVEGVSFYckoC8Ymg-cMAw
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: emotion
      type: emotion
      config: default
      split: test
    metrics:
    - type: accuracy
      value: 0.9235
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNDdiOWE5ZjI4NmVjN2Y0OWFmNGI2NWU4MTYwMTA5MTFmMjEzOTkyODhhOTEzMzg0OTJmOTM2NGM3YzMxMDAyNCIsInZlcnNpb24iOjF9.SzWJe5bMitRlUb4d0gIX49k_mTC1ADWKDOLdS6TMx3ZGmkMdD6F9-IlmmTunbfVEDQSjweVpv7H7TUcHsBeIBQ
    - type: precision
      value: 0.89608475565062
      name: Precision Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYjZlMjk2ZTZkNzJiZTgwNDczNzRjMDkzYTcwNmM2YjdjODE1NzI2NTFmNjRkYTBjMDg2NzMzNmE0MGY1NWRiYyIsInZlcnNpb24iOjF9.qlIfR61-QTw9M71mMGOjN2UPs3Pjz-DVtq094BFtVkFQVllN5vPZLkkqVTkQlX1WdnY70JHpYv-qM_Kpv1h3Cw
    - type: precision
      value: 0.9235
      name: Precision Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZjUwMDIwMGEwMmE2NmEzMjQxMjM5MWI5MDRlYjhmODE1NjliMjkwMTU5YTg3ZWJiMjI2MGQxMWU4MmJiYTljNiIsInZlcnNpb24iOjF9.rFJQ1Q6aPlncwReXR2jciz3UEIArJS_nTwHAuTNXZKKQSvTM1zBN7x7EdSDeEIf8JDFfEimvv282wgnCPVmkAw
    - type: precision
      value: 0.9224273416855945
      name: Precision Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNDNmYWE4MTQxY2FkNTcxMzMyMmQyNmViN2FhMGQxOWYzNGU0MmIyMjhiZmE5ZmYyOWQwMzExZWRiMjRkNzliMyIsInZlcnNpb24iOjF9.6kD-hmPbjJrpAHZY-tFULnufxw118PfMCwj8PBjDKTtSQ_MCTP7iU3KtNe5essy5vDpdBFuA9E9SbrtjW3vnBA
    - type: recall
      value: 0.8581097243584549
      name: Recall Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNjZjMGJlZmI2NGVmYWIxZjdlYzg1ZjAyNmYwOWQ0NGE2OWI5OGIzMzE5Zjg5Yzg2NTlhZjRkMzE0ZTZjOGUyMCIsInZlcnNpb24iOjF9._r5lQK7hSPCyM9Bz9H5AVactjXzpF3hKW-iB5dco_kmVMhdy_-N00aFQg8XMKa4sL9lmJs0svINUwL5q55vmCw
    - type: recall
      value: 0.9235
      name: Recall Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOTQyMmZiNDQ1ZDMyZGY5ZWVlOGM0OWMzODhiNWI1NGUzNDJmOWEyM2VjYjhkNGQ4Y2ZmYzMwYjc1NTU4YjY0ZCIsInZlcnNpb24iOjF9.N7SJCOKlRa_3sRFYqiuPZpXmikQ9xuA4uDsKldGVNG6Tg6dffT2fLE9kkTCOQmG3BQzoP-xxjbhjG1gDPe_KCw
    - type: recall
      value: 0.9235
      name: Recall Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNGZkZmU4OTRhNDc3MzdiMDQwYzg4NmI5MTNlOWNjODk1ZGNmODZmZjk2MmY2NmU1Y2QyNGExNTkyNDUyZWJhYyIsInZlcnNpb24iOjF9.SvIJpc0dCvtMeaRZ0yQinV3FKftMiHLbhvalrVDT0uLnQ-wGL3HOkj9i9lO53kLrunxbswPjhKmR4bY1P6LUCQ
    - type: f1
      value: 0.8746813002250796
      name: F1 Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZDcxMTE4YzIyOWM5YmU0YTI4NzliMjM5YzBkYTJjODY3NjdkOWMwNmJhOTJiY2Y3MDM4NDNkYjljOGMxN2I2YyIsInZlcnNpb24iOjF9.41XMqnkXPjeoKiUmOuMhitX-624vXLmz6QMeNsOx_yFDhkugYP5ox5xq9PhC3cQIxn0SD71AusaN7YOnfKOaDA
    - type: f1
      value: 0.9235
      name: F1 Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZjE0MDU4YjY4MzlkMjQyZmI3ODUwODUyYzIyMDFhNjIyZjcwZjNkZTI0NmFiYTA4YWJlMzdmNDMxZGY0MTVhZCIsInZlcnNpb24iOjF9.a1Nh5T-g74Ol-ElZhu2O7yg4tJrBRGCJYeVYUsZd7AkXPR_e0jyOwVx16J2t7gOVTp512HEK5u2wIpns8qWrAA
    - type: f1
      value: 0.9217456925724525
      name: F1 Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiN2YyODE0NjIzOGI4OTExYTlhMTUxNzBkZWE5ZGIzZTNkOThjZTRiYmM5NDEzYjZlYTY2MzY1ZmVkY2IyZDA4MyIsInZlcnNpb24iOjF9.XEhuUaY3E5FwXunSiRNMW_Rnu9B176mu7wr8jXvISdPovno1ANhliK276GeLgS_suAjjpPQPTwMK-ntJ9PHuCA
    - type: loss
      value: 0.32714536786079407
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZDdhOTRiNjI5Y2FmYmQ0MGNmNjM5NWQzN2Y0ZWJhNmYyZDgwYzRhOWE0YmNiMjIyNjYyMWE2NTczMTA3NDM1YiIsInZlcnNpb24iOjF9.tmWAsH0fU7QUztbh3PfbBL1aSigZge0iQgYQIHsULZMCD9M98l8DXeLpZl-dehWruVY9Lkr4PJKTn9ba35vKCg
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-cased-emotion

**Training:** The model has been trained using the script provided in the following repository https://github.com/MorenoLaQuatra/transformers-tasks-templates

This model is a fine-tuned version of [distilbert-base-cased](https://huggingface.co/distilbert-base-cased) on [emotion](https://huggingface.co/datasets/emotion) dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3272
- Accuracy: 0.9235
- F1: 0.9217
- Precision: 0.9224
- Recall: 0.9235

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
- lr_scheduler_warmup_steps: 500
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:---------:|:------:|
| 0.2776        | 1.0   | 500  | 0.2954          | 0.9      | 0.8957 | 0.9031    | 0.9    |
| 0.1887        | 2.0   | 1000 | 0.1716          | 0.934    | 0.9344 | 0.9370    | 0.934  |
| 0.119         | 3.0   | 1500 | 0.1614          | 0.9345   | 0.9342 | 0.9377    | 0.9345 |
| 0.1001        | 4.0   | 2000 | 0.2018          | 0.936    | 0.9353 | 0.9359    | 0.936  |
| 0.0704        | 5.0   | 2500 | 0.1925          | 0.935    | 0.9349 | 0.9354    | 0.935  |
| 0.0471        | 6.0   | 3000 | 0.2369          | 0.938    | 0.9373 | 0.9377    | 0.938  |
| 0.0322        | 7.0   | 3500 | 0.2693          | 0.938    | 0.9382 | 0.9392    | 0.938  |
| 0.0137        | 8.0   | 4000 | 0.2926          | 0.937    | 0.9371 | 0.9372    | 0.937  |
| 0.0099        | 9.0   | 4500 | 0.2964          | 0.9365   | 0.9362 | 0.9362    | 0.9365 |
| 0.0114        | 10.0  | 5000 | 0.3044          | 0.935    | 0.9349 | 0.9350    | 0.935  |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.11.0+cu113
- Datasets 2.0.0
- Tokenizers 0.11.6
