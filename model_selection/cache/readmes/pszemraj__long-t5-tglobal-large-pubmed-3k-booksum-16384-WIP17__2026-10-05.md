---
license:
- apache-2.0
- bsd-3-clause
tags:
- summarization
- summary
- booksum
- long-document
- long-form
datasets:
- kmfoda/booksum
inference: false
base_model: pszemraj/long-t5-tglobal-large-pubmed-3k-booksum-16384-WIP16
model-index:
- name: pszemraj/long-t5-tglobal-large-pubmed-3k-booksum-16384-WIP17
  results:
  - task:
      type: summarization
      name: Summarization
    dataset:
      name: launch/gov_report
      type: launch/gov_report
      config: plain_text
      split: test
    metrics:
    - type: rouge
      value: 36.8427
      name: ROUGE-1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiODY2YTBkOTUxZjRlOWYwNWI1OWM2ZDMwOTFjMGIzNjc5YzgwMWE2ZDJiNzY5YTZlZTZiZmNlYzNiYjc5NWZiMiIsInZlcnNpb24iOjF9.Jf41H9W-V6vbLXloL3XUtvKG2Uieoeijzean8Ns4AKRgX6OMeAaWpqoOG4Umpb1JsjtXvbSYdqwTlQVm0IAABQ
    - type: rouge
      value: 8.4234
      name: ROUGE-2
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNTY2MzQ1OTM1ZDM1OGU0OTliZGQ0Y2QzZDExZWQ2NzAwNzlhZThjYjc3ZmU1NDZiNTZjZmZiMTA1NjlhNGU1YyIsInZlcnNpb24iOjF9.etPfWSu1mxR5RN-9rq_F5FFi0IXPe81yGZWbpb6yDzZjAoiSTq4RCmaEUlt8JFXkoLJS3pP9JgjSr7Cg4dl2CQ
    - type: rouge
      value: 17.774
      name: ROUGE-L
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZjRkYTcyMzJiNzY5NWMwYzg2YmFkYTZiMzgxMzJjZDcwOTg3MWZmNTk3OTYzNzFkOGEyNTg4NmU0MjJlZDRlOCIsInZlcnNpb24iOjF9.Cd4LtEHKbEp-n42rDJb7KFqNlCUBKgCTz8sTNgkZVYJqY-rV5JGZtDz5mawNSbJTMn7rNnBNmaU4V99MGQyiBw
    - type: rouge
      value: 33.2901
      name: ROUGE-LSUM
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZTI4M2RhNzQ5OWM4ZmExZjU1NDU0MDliZTM1YTgxODczMTFjNWFiNmJlNjc1YzEyY2FjZTJiNmFiZmNjNTc2MyIsInZlcnNpb24iOjF9.b52vREVLI3DgfDkku8lzi2KDWLiN9TvNENCjFAKmrifMDxpsjTPGn6qf0csvU6_kgjWkHKFO53VkLr-XFazPBg
    - type: loss
      value: 3.765686511993408
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYTJjNzU1OWEwOWZiYzM2Zjk0ZjZhYmRmYjczMTJlZGFjOTNjZTY4Mjg3NTRiMTAzN2NlYTEyNjU2YWY5M2E5NiIsInZlcnNpb24iOjF9.Q4FFH8cbGLzaZWJUrSKeZl1os7h9S12v8a__oIoeeWL-c9GXVyNdtb5q-eb7r-4G5i9ytBc9NM6n90nuO353Aw
    - type: gen_len
      value: 213.8849
      name: gen_len
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYTg3NGMwMTY0M2Y0M2JiOTFhNTQ2ODgxNzZjNTAwNjI4YmRhZTllNTU5ZjE5OGE2Y2EwZmI2YTQ3ZTQxNTFkNiIsInZlcnNpb24iOjF9.8yc25qbswrqJa56hlM1vvlD-Re7R1n3Q9_3U4c9OEzC9XIf8ir3zUQOrEZUb9vm5_H9a8QoiEXUcZG6Bq4fTAQ
  - task:
      type: summarization
      name: Summarization
    dataset:
      name: kmfoda/booksum
      type: kmfoda/booksum
      config: kmfoda--booksum
      split: test
    metrics:
    - type: rouge
      value: 35.4324
      name: ROUGE-1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZTkyOTU5M2ZiYzc4NzU0Nzg3NzI2MDE3MTVkZGRlYzVlNWFlYzJlYjA3ZGNhYzIyYmM1NzVkZWEzMTRhMGRhNCIsInZlcnNpb24iOjF9.TGS-ZF3MKg0cbgpPm2wz7Y8KarRGvBNyfaaDHFpUesYCR5pcz3a_ojRAGXOTIek-fcS--ZvADjEz8by9GYBOAQ
    - type: rouge
      value: 5.9586
      name: ROUGE-2
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYTIzZGRkMTc3MmUxOGRhMzI2NjAzNGYxYjY4YTM5N2QxNDJiZTJlMmRiNzY3NTFmZDg2NzAzMWI1ZTA5ZmY4YiIsInZlcnNpb24iOjF9.1fyZffIo-wDg85krXWGgc90SlFLIU_v7URS-14zNEHZSe4kmbcdGmW963WKAEI2v2oRXU7uQ3BsgDS3d30KzDQ
    - type: rouge
      value: 16.134
      name: ROUGE-L
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiODI4Mzc1YTY3ZDBmYTMxZTJkMmU3YWI4OGE3NGVkODk1NDQ5NThlZTM0NmM5ZGEwODFjZWI5ODQ5YzAxYmMzOCIsInZlcnNpb24iOjF9.KzQLzOXFjJv_tRzKPnkp2AA_8u_aZtI2GQQeavB3L4ksmX-aOnlVu9-fXktfOCiXmmJCbyZfS3uicdyLgqyhBw
    - type: rouge
      value: 32.4141
      name: ROUGE-LSUM
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMTFhNDQ1Y2YyMThjMzBmY2EzM2MxNzNkYTE1MDYxNzAwOWQxNDdlNjljZWE4ZWRiZmUxODkyOGM3ZDZiN2I3NyIsInZlcnNpb24iOjF9.YYxCtJlNax15r4oY_IikY1MmaU05WCD_JtTMKt5Jdb9Tco2KOPQ9z6Vc6AlGEJNaXVNRm-ROS7CKCDkC55B_Bg
    - type: loss
      value: 3.050943374633789
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNDllNjgzMWZjNzNhZmFlZWQ4OTY3MTVjY2FkOGEzYjFkOGNhNzM3MjhhNTUyNWI5ODhhNTk2MDhlODNhNGMxOCIsInZlcnNpb24iOjF9.5S2y4SbzKWu6BHlnyUH2R9jwO780INnzqQbdKHXizkJKvX8g9qpuYB0Iu41e1aWqmePdY0JbVUqhG3Xfo2otBA
    - type: gen_len
      value: 279.8735
      name: gen_len
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNmRhZTY2MDMwMTk2ZGFjNTJhN2Q4NmNjYjRjNjgzMzljNzBiYjEwNTgzZGNhYmY5MGNhYTY2MzE0OTlhNGNhZSIsInZlcnNpb24iOjF9.epjIxFmPlfDHJc--eJIo8AgnkjQBDLokICjxVqwyHiE6T0Hlj8D69RhOplEIDwMQyXC5usfkF0zW7ib8JuhyCg
  - task:
      type: summarization
      name: Summarization
    dataset:
      name: billsum
      type: billsum
      config: default
      split: test
    metrics:
    - type: rouge
      value: 38.066
      name: ROUGE-1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNGJlYjZhMDIzZTAyNzU3MGFhYmIwZTBjNTViZTQ5MjFjODcyNTUzNDg5MWVlNzMxZTQ0NjA5ZjJlYWYxZDk4ZiIsInZlcnNpb24iOjF9.g-Ppx-hZPJBQM160VSDZWLFt0WEv5WbBiOpwQlbFnQ12QSezZiu-NR2wsaZeNLIVWaeEDVTCVpVcHf0-YymYAA
    - type: rouge
      value: 12.5289
      name: ROUGE-2
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZjlkNjY3OGE4YWIxMjEzZmQyMDg5ZjMxNjhhMzBlMDQ1NDgwZGQ0NWUyYmFhZTY0Mzc4MWQ0NTJjZmE4MmZiOCIsInZlcnNpb24iOjF9.X-rXBFAXTJXVmihkVHdqdpm6QCHbuI4Ligd2SsmvVcpMux6ep2EoBKd4xuTW4WCr6Qjsa7tZ7kJM-1pu9kKSDw
    - type: rouge
      value: 22.3393
      name: ROUGE-L
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiN2E1NGM1YmMyYTc5NTkxNzU3ZWM4OGRmNDBhNDdlZjYwZjBjNWNkNmJkMjkyMDkzNDBlMGIyZDg4ZjBlYTQ3OCIsInZlcnNpb24iOjF9.vZi95CQMrkdETfhQjjgoO2WkpM3Fr4NZCTX7S9q3TnsC9J9KELfcNNXq7rtbWgQndUK74AvBt7G6nG7Qj13nBw
    - type: rouge
      value: 31.9802
      name: ROUGE-LSUM
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYzU3ZTIzZDhiYjc1ODk2ODg4NTI2MDFhZWFhMDRmMTg2OTg0MzkyMjQ0NDkyODI0ZTE1MmM2MzNiODQ2Y2EzZiIsInZlcnNpb24iOjF9.k48PRPLAGKPT-ILO5HbPciwFG9vdR6_ICvUXmOnJI4mz5dIoBLvR0aTdWCU070jyPveDwXisIvE9scK9jWsUCA
    - type: loss
      value: 3.0360958576202393
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOTgzOGRlNmMwZjYyMzNkNjcwNDM4MTYyZjgzODhjYTdhY2JiNWY4ZjMzNWJhZjc1YjNiYjViZDk2ODMzMmI5ZiIsInZlcnNpb24iOjF9.dH1fJs84sTWXqrmdsCMuc6zexedn0uUWd9gmVV2JKzFzpPbTxzIJSNez7jaGz_sgSK8q-AeclWFrBAgPDnM6Bg
    - type: gen_len
      value: 161.4671
      name: gen_len
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYjc5NGM4OWU5ZDM2YTZhZmM2OTgwY2ZiODRmYzE2MWRlMTVhZDBjZTQ3ODJkNjU4NzdkZGZlZDk1YjdkYmE0OCIsInZlcnNpb24iOjF9.OSzFnK9k7IT0cv2qXSVzgjTVLkxkqYnUI9OQqPcoEjBK8nqY0OdMQ8BWq6CN6rt6VmVk111B0TJJCTEfseiHBg
---


# long-t5-tglobal-large-pubmed-3k-booksum-16384-WIP17

This model is a fine-tuned version of [pszemraj/long-t5-tglobal-large-pubmed-3k-booksum-16384-WIP16](https://huggingface.co/pszemraj/long-t5-tglobal-large-pubmed-3k-booksum-16384-WIP16) on the kmfoda/booksum dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- distributed_type: multi-GPU
- gradient_accumulation_steps: 64
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.01
- num_epochs: 3

### Framework versions

- Transformers 4.23.0.dev0
- Pytorch 1.10.0+cu113
- Datasets 2.5.1
- Tokenizers 0.12.1
