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
metrics:
- rouge
inference: false
base_model: pszemraj/long-t5-tglobal-large-pubmed-3k-booksum-16384-WIP13
model-index:
- name: pszemraj/long-t5-tglobal-large-pubmed-3k-booksum-16384-WIP15
  results:
  - task:
      type: summarization
      name: Summarization
    dataset:
      name: samsum
      type: samsum
      config: samsum
      split: test
    metrics:
    - type: rouge
      value: 24.5482
      name: ROUGE-1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiM2U3MGNlNzI0MGNiYWQ2NGRhYzg5M2Y3NjhjYTdhZmVlYWNmM2Y0YTFhN2I2ZmI5NDVkY2I2M2MxMjM5ZDIwOSIsInZlcnNpb24iOjF9.tHnV8ofGr9jbx0fHm3cDL6p8nqXZITS1H6XLjW-iWaNFuQJ7Qfs7E0uYNf2haQP6Mu5K5eWWGdg54KtMi1N9DA
    - type: rouge
      value: 4.811
      name: ROUGE-2
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYzE1ODYzOGFhMDE4ZGU1OTM0OTM5NDBkNjEwODQzY2I1NzRhYTc0NDJjZmM5YzI4ZGZmZGNkZjljYmNlYTQ1YyIsInZlcnNpb24iOjF9.n7tOZFKEePwSEqM7a0Y-fBiEEi3jZL7QwP0MCQNun5yKsd2OIkTlruuauV3h8yHN5yKxg33CUfpzS2B44kGjBg
    - type: rouge
      value: 17.2505
      name: ROUGE-L
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMjM3YTYwNjAyYzY5MmZjMzI1MmYwNzI2OWNmMzJiNzk3MTY5Y2E4ZmM1OTIyYjQ1NTkxMjI1ZGMwYmRiYzg5NiIsInZlcnNpb24iOjF9.1VQIehrugMj213RavmSAf1qsKTG3Jmj6DAJGi3KOeOYrJpKeLBQ6ftQZ_wSje8UiyR9uekne1wTd256sr61DBQ
    - type: rouge
      value: 20.906
      name: ROUGE-LSUM
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNDdhNjJlOTY3ZjgxOGMzYjkzOGI2NGJlZDY0MDk0NmE5ZDcyMzIyNTA1M2ZhNmMyOTFlODJjZWJkY2ZjMTQ3NCIsInZlcnNpb24iOjF9.SLAdCUY_9PFb7BrvvpN2ABDU9uvy7EIMEHKtnlpH94nZbv2G2sj74tWLcIQstuTkmXmLTk6_HvdZTEaoUc-5CA
    - type: loss
      value: 3.3002164363861084
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNDFkM2UyOWQ5YzM2ZDIwZGRmNTY2YTRlMzUzY2QxZDhkNGFmODljNjIxNWQxZjFhM2E2YjM4ZWRjZDUzNWQxNyIsInZlcnNpb24iOjF9.HUYhxEAGbZS8J76Zt9k5KNFt6dx_vdoqf34k5ht3X0BTB4u2WiYwVS9O0ka2ExCynIODo9OMWLcMG2CW-xnjBA
    - type: gen_len
      value: 52
      name: gen_len
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZTkxMWQ0ZWVlNWUxNjYwNTU3MTQzYjRhZGI1YjQ1ODYxOGRlNTU0ZjlkOGZiN2UzM2I5MjU3Y2QxODU3MTJmZCIsInZlcnNpb24iOjF9.9iDB-q3h2qYZIRHLKryZIjYYUeN_4_9hr5miRgmJl8TYB1Prf69NNziW7QPOkMXMOM-5-xvRVKmx-JqZQSkcDg
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
      value: 35.3305
      name: ROUGE-1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiY2Q0NWU1Mjc0ZTYxOGM5NjI3NTlmODYwMmU4ODE3Y2VjYjdmNTRhOWI2MDdlM2U3OTk5N2Q3YTcyYTViYzIwMiIsInZlcnNpb24iOjF9.ScFds-4QZgG0Wro-w0qnoaQSoXXMpWOTEE4zYrvA9k2lew965geaqeBVAt7QQxwchuB9q26hSGYCEqLMdX3EBw
    - type: rouge
      value: 5.8001
      name: ROUGE-2
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYjFiNjU2ZjI1YmE2NDViZjUwMjI1ZWFiNDkyMjExZjJjMjBmN2I5ZmYyYjE0MGEzNzk3ZGE4YTMzNzA0M2NjNSIsInZlcnNpb24iOjF9.H4r1JTjEC3ABkgVIi8i3TRxQ1gMsYoQR8qCBbJVkdWJQwECzWGZRw6QIaWz0kZv73nQ890kf90JE6FKeD2MpAg
    - type: rouge
      value: 16.0557
      name: ROUGE-L
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNjBjNTBiYmM3OWM3ZjFkN2FjZTBiMGJkMTg4MTYxYzRjNWUzNWE2YWVjOWJiMzRkZTMxMGFkYThlYmZiN2UwNSIsInZlcnNpb24iOjF9.mLij-24wue3udXSS5H3kBniefh7NDTmNf3bxacq7UinFkbTtqx9OvS6Ywun4LfJj_Ufn9-uTMR2VbaoIIQKkBA
    - type: rouge
      value: 32.3409
      name: ROUGE-LSUM
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZjg3ODliOTAzYzg4Y2NhNzI4M2I4OGM1ZGQwMWE5ZjBiZGQyNTNhMDQxZDllMzgxOGM0NWZjZTJjMzFkZGVkZSIsInZlcnNpb24iOjF9.LpNcyf7HNaL_xwb4zqrBgOPoTBWFaBN0AgSbzsgfsQ7J12CIi7s0UoBhxg_c8UYwNuqFOZouYIq78r1PM81RCA
    - type: loss
      value: 3.0063540935516357
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMTJmMGM2Y2U0MDU0OTFlMzJlNTNlZjViYTAyYjE4YTVkOWJhMmQxZjc3MjM4ZGNkNTNmOTViNDYwZjg0MWI0YyIsInZlcnNpb24iOjF9.VLKkHEjp4Iq1r3-CXSABBzgPJFx1sbjRt5KbbKe_AEuKuJtXI6rRWPuBjudOLB-CHBvutDzVS9wR60pGaQ5jCg
    - type: gen_len
      value: 268.4032
      name: gen_len
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYjJmYjZhOGFkMGNkZjEzOTA0Y2RjNWU3Yjc2ZGI5NWU1MTNjZjY5NzFiZjI0YjBhZjUxMDFlMjBmZTYxMWE0ZCIsInZlcnNpb24iOjF9.vnImpJVQBidfhKVOzEYuA2okKgbTvB0bkc4GNmvkTlxXdZlsqg1KuevQa587lmy0LQOZk1_pYWz0aVJ4VQQQAA
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
      value: 37.0412
      name: ROUGE-1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOTQ0NzdhYjdlNDNhYjJmNzQwM2E1OWQ3ZTQxMTZiY2IwNjJkMzE0YzNmMWZjZTI0NGI2NWYzNTU0ODM0OTVmMCIsInZlcnNpb24iOjF9.1Gf6zoMOLmf71bkW9RdiXJPDms-vfc0hu0jJehdb7XCjW-hPcmLxdk8ALwWi9knBmeHZ18GHHSJklgU_maFoAA
    - type: rouge
      value: 8.519
      name: ROUGE-2
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiN2M0MTE2YTE5NmE1NjhkMGM0ZjYxMzJiOTFjZGNmOTdlZWFhOTExZTAzOGUyOWE4Yjg4MTE3NDcwZTg5ZDk0MCIsInZlcnNpb24iOjF9.6EeSA2FzddyK5EfHhBViKNDXIZp9svVTpvSi4O_9YULWX6Gs4bZYcGRQATGLS6Pfvh1swky1ZXXR5GpX4tN-Ag
    - type: rouge
      value: 17.8685
      name: ROUGE-L
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNTZmMWRhZmNmZDY5MzYzM2JhNDc5NzdiMWI3MmRlYWViZjA0NGQxZDJhNjIxZTY3ZTM2NTJjYjI0ODE5MGFlYiIsInZlcnNpb24iOjF9.Tz6vT3YFZO5Hd8BySoXmtcwDQMSvr4DLGvKYpTeH7L0iZOaIFr8XILCPbLV6ZxjglSgFwMzcwsjN1d032mEqBA
    - type: rouge
      value: 33.5036
      name: ROUGE-LSUM
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYzgzNGQyMTIxYWUwMDlkMjQwZDE5ZDRmYzczODJkZTIxOGE5MTEyZDNjYzMzZWFhMGUyMjljNDQ5NGQ4ZGRkOCIsInZlcnNpb24iOjF9.oR8vSpgDjMskRmcImHV4E5dkXbP74BKNYXmfpkpO5zIHIJWNNyJvUSKurDDy5rhbhbkI98kF5GmOcLlfghyrDA
    - type: loss
      value: 3.628979444503784
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMTNkY2E0Y2Q1YjA3Y2VhYTAyOGE1NmQyYWQ0YzM5NzczOTBkYThiYzNjMDljY2YzZGYzMGQ3NGQ5YzRhN2M5OCIsInZlcnNpb24iOjF9.kD1yDRyt6PR5wKBHvsU4l6stGmcsvPbkGB1dMgSfvMWV0LjjSc3MaXUS2ykNciLdnJK_aSqIjSUbUDyO0e4oDA
    - type: gen_len
      value: 219.3885
      name: gen_len
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYzI2MjIyZWViY2I0NTE0YWMxYTE3OTAyODdhOTNlZDZkOTIyMjQ1NzdkMmU5YTY5NmNjYTNkOGI0ODk4YzE2OSIsInZlcnNpb24iOjF9.sqlm-kWBzo-sJ4PaelnJWeQ1usF3nM5ZJP8igXE2GhWNhAQVsST3tlvcA8GwRtfbVCAy_x7Ex9iOuYqpccdbDA
---

# long-t5-tglobal-large-pubmed-3k-booksum-16384-WIP15

This model is a fine-tuned version of [pszemraj/long-t5-tglobal-large-pubmed-3k-booksum-16384-WIP13](https://huggingface.co/pszemraj/long-t5-tglobal-large-pubmed-3k-booksum-16384-WIP13.5) on the `kmfoda/booksum` dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0004
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- distributed_type: multi-GPU
- gradient_accumulation_steps: 64
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.01
- num_epochs: 1.4

### Framework versions

- Transformers 4.23.0.dev0
- Pytorch 1.10.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
