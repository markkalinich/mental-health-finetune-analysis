---
language: en
license: apache-2.0
tags:
- sagemaker
- bart
- summarization
datasets:
- samsum
widget:
- text: "Jeff: Can I train a \U0001F917 Transformers model on Amazon SageMaker? \n\
    Philipp: Sure you can use the new Hugging Face Deep Learning Container. \nJeff:\
    \ ok.\nJeff: and how can I get started? \nJeff: where can I find documentation?\
    \ \nPhilipp: ok, ok you can find everything here. https://huggingface.co/blog/the-partnership-amazon-sagemaker-and-hugging-face "
model-index:
- name: philschmid/distilbart-cnn-12-6-samsum
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
      value: 41.0895
      name: ROUGE-1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZTBlZmQzZDFmNzY5YTBjMTI3ZjRkNDk4NTI3YzQxOGY4MjlkMTU4ZGJkZWE4YjQ4ZDFhOTIxM2M1YWEyMDQ4MCIsInZlcnNpb24iOjF9.Nw7idRmEmjS-c91HthjVGw6YxttVA_tRB2QRkGwVSVABR3_BY84HvwLOZVstc6a9gUHopMj_W9SRfa_6xTWcBA
    - type: rouge
      value: 20.7459
      name: ROUGE-2
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMjRhN2E4ZDNiNWNkY2RkNjMxMjhiYjcxYjc4OWM4NWQ5MDNjZDMwOGIwNWI2NWJiYzljMzc0NzY1ZDBmMTRmZCIsInZlcnNpb24iOjF9.nYxNimi33AW0T8T1JhqFUukxe4W4niXj4UzLRTuc40NeZveDTSpPS8QzR4rF1gK-r2irqIX5FrvG4dwQHrESBA
    - type: rouge
      value: 31.5952
      name: ROUGE-L
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZjYzYTRjOTU1MDVhN2ZlOGE3YTIxMjk1NDBiY2E2ZWI1MDA5ZTJkOTQ4MzgxNThkOGU4OTUzODU0YWE1OTQ5MiIsInZlcnNpb24iOjF9.G2EtxIlJ86AcNx2bqw2nu1UbdczQ-anl1c02EopQyC81BEcEAbnY-liPvHXLjPVQvP97GGGjqTDLZYjYJ71hDQ
    - type: rouge
      value: 38.3389
      name: ROUGE-LSUM
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOWExZmM2YWI1MDU0ZjE1YWY1NDNiY2E4YTkwZjA5MTE0YmM1NzI4YTc1YjI0MWFmZDlkYTBlZjVlMDk2ZGQxZSIsInZlcnNpb24iOjF9.jjBghJ66Gj_95AdDpWG2TR_MnuUtj8Fzc0M3KS9vqsM0iqtlu9khY8lXrFpMaIeDxVBYKltMMFdZWH8mVv2wCg
    - type: loss
      value: 1.4566329717636108
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZDAyYjFmNzRlYzkyNmUxMWM5YWYxNjgwZGQ1ZDc1Njg0MzU1ZjM4MjI5MTJlODRiNDdiNGRjYTkzZGUxNGMyZiIsInZlcnNpb24iOjF9.2eH5b7DlPeVQ_zFGlvKyRvqrc7yyT8vcf3koJGKGysV00vCQew8sOmFEmDegiBka8gq3UL987Dd2yZCU3b64Cw
    - type: gen_len
      value: 59.6032
      name: gen_len
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNTFkOTlmMjFlODIxZWExZmQyMTQyNDYyY2RmNjY3YmM1NDFlNTI3OTRhZjU0MDQxNGY2NGQ4ZWY2OWFmNDliMyIsInZlcnNpb24iOjF9.K9qwFg3Flnu2-1H-WI9adj7yoBuJ3zBBDyda5BxRpJ1D4L_alLpCweqrVGuynOPl9PAWPuHo7bAG1y2zZNmmDw
  - task:
      type: summarization
      name: Summarization
    dataset:
      name: xsum
      type: xsum
      config: default
      split: test
    metrics:
    - type: rouge
      value: 21.1644
      name: ROUGE-1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYzVjNWI1MWJmOTAzMDYxNjlkYzg4NjM3MzczMDJiYjNjYTg3NjYzNjQ3YTczYzg5MGU2NDcxOWQwZjdlODU4YSIsInZlcnNpb24iOjF9.CqB-ANpnx0GvwhsjeCzLB_RxaKqbnhc_980RG8fqDb2hNTk4LvDhqdDfkLFQMj8kvW4nQLLDSNUENQ7Uni9kCA
    - type: rouge
      value: 4.0659
      name: ROUGE-2
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZjgzYTc5Y2VjZTliNmEwYTZjNTViODdjYTg2MGMyZTFkMjgyMjk0OGIzZjg1ODgzZDJmOTMwNmU4MzdlNTI2OCIsInZlcnNpb24iOjF9.1AfPtrpJ38Khz5vfRsN4Jwb3J_PdycddRH9DJtEccqmEz9BzDo-AO7Ts94sfVlYfSf3srplLHDcd_XFCwQtlBg
    - type: rouge
      value: 13.9414
      name: ROUGE-L
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiODZlZTM2OTM5NzVlNDBjYjc2NDdhNmIxNDZhNGVjOTk4YzIzZmEwYzEwZmQ2ZmNmMjIzNzYwMzkxMjU1ODcxMCIsInZlcnNpb24iOjF9.vvp5PKmEp-Hyt46zgsvzjGOO8wrV0cDG68Z0VPqW2WfY5Sp3k3krEcKLATdQAQjfy96gKCCkQpBFefpjYWcmDA
    - type: rouge
      value: 17.0718
      name: ROUGE-LSUM
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZWEyN2QyOWFhMjAzZTk4NjU5ODU5YjgxMjczNzc1MTM5OTY1OTVjZDMwZDhjODFlZTVmODNkYzFhOTc5NzZhYiIsInZlcnNpb24iOjF9.PwJT3EYTV3KifWaySiwSTxGyBWTB8bHMuaXG3AyRvWkY2xju1BSaBjPGCcfmlZs1yJwghOH7N4dBW5yJBEp5DA
    - type: loss
      value: 3.002755880355835
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZGY0NjgzOGExZWZmNWI3ZTA1ZjRlYTU2OTZkYzk5NDdmOGVmNDdkNWU5YjViMWQyNGE2MTNkODhkZmQ1ZGE2OSIsInZlcnNpb24iOjF9.pWru9Nhl0aZThHz0qveOHmxTOCrZjHu9ySt5wI9MnGQ5ZEpxfufjpI196EMMn-KSSxAl-s7wHygtGC9_WtC1BQ
    - type: gen_len
      value: 71.2969
      name: gen_len
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiY2Q4ODZlZDY4YzE1MDEwNzJjNmNiYjI4NTU5NjRlNmY2NWNjYmUwNzcwZmY3NWVlZDA3NTMxY2Y2NWI1ODYwMCIsInZlcnNpb24iOjF9.0Y_lnTKQ5nmjnwAEju9T7xlLObWgwPLMOxlWDpjPBkDeW0bzHYqJcRADtFcvAhznJ3HktIV830QxjqkRYjZTDw
  - task:
      type: summarization
      name: Summarization
    dataset:
      name: cnn_dailymail
      type: cnn_dailymail
      config: 3.0.0
      split: test
    metrics:
    - type: rouge
      value: 42.9764
      name: ROUGE-1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMzQ0NzAyNDM5YWIyZmY5OTUwNWZjNzRkYTliYWI0YzdmZTg5ZGVhZjJlMDBiZjg2YmE0ZjkxNzU4YjRkYTJjNCIsInZlcnNpb24iOjF9.dymlXdITNpMZpOaYvif-LcxaSRWKh8_RxV6mdBpuvlThPPi3-TwKCW20Fowor8H5RPsC0M1cfvNNzINCyApKCA
    - type: rouge
      value: 19.8711
      name: ROUGE-2
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMTY5ZTI0OTEzNzI1NDRjYWE5MDk2NzVhZDEyNGEzNzU3OTE0NmJmYzhkMTU0MTI2MDVlOTdlNGU0OGI2MTdlNSIsInZlcnNpb24iOjF9.7xN2u4HjPL78CkkihB9I0befTn04IQqimvNlSHpc888arBm_qCtTGl7q7389ArpWUKEdkhvZ94BgB-Z_cXsqCg
    - type: rouge
      value: 29.5196
      name: ROUGE-L
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNGY3YzRiYjljZWJhNGJiMTdhNDY5OTk0ODJhYWMxOGMwYjY4ZTBlNmQ0YTUxMzQ3YmZiNzg0ZDJiNTg4MzdiYyIsInZlcnNpb24iOjF9.Yj0ZaJelYcMJ-8SIon9x7GxRityWR3p0vcLNctTfcg6eCClalTQKBclCVgpDCO8WQyVxSz8EyCDb2qedRgF9CQ
    - type: rouge
      value: 39.959
      name: ROUGE-LSUM
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYmI2MTE3NjQ2M2MwYjJmN2JmMTEwN2JkMDVhMWRiMDBiM2FlMzM5NjAxYWM1N2Q2MTA5MGRhZmI5ZDNjNzMwYSIsInZlcnNpb24iOjF9.A-2Ch4-M691OBAp4KmsYut10K3sF0fjw5ztutK_LTtn68Ne0x8w-u-7pEyjTuWJrJx4Q3Yb1eW3yeHPTnFI0DA
    - type: loss
      value: 3.014679193496704
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMmNiNWZlOGZmOWZhNWZjNTg1ODIzMzY2ZGYxNzBiOWIxMWRiZTQ5MzM5NjRlYTQwMzRjOGI3YzNmZDhmYjQ3MCIsInZlcnNpb24iOjF9.BZkiJxZG0RdFzNgxgcS8U6_zPT1t7rvs-603cnC1tjMMYF3Lbae7rExRb-fVHN_ofZV_w5vl4uRLQ3OxZUY5Ag
    - type: gen_len
      value: 81.956
      name: gen_len
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOTdhNGYxYWRlNTU0MzAxMWU1NzNmMTBjMmY3NzkzODAyYTMzZWYyZmNiMTViMzNmYTE0ZmFmNDdhMzQwMmJkNyIsInZlcnNpb24iOjF9.8lm84JtbCh-diuNQ01oXK6P8vV9CPyA8y-7D9o_OHb9Vk3pNEFM1jMSZVdEG9wFuMpWL3ARbXLadEPQB5HN8AQ
---

## `distilbart-cnn-12-6-samsum`

This model was trained using Amazon SageMaker and the new Hugging Face Deep Learning container.

For more information look at:
- [🤗 Transformers Documentation: Amazon SageMaker](https://huggingface.co/transformers/sagemaker.html)
- [Example Notebooks](https://github.com/huggingface/notebooks/tree/master/sagemaker)
- [Amazon SageMaker documentation for Hugging Face](https://docs.aws.amazon.com/sagemaker/latest/dg/hugging-face.html)
- [Python SDK SageMaker documentation for Hugging Face](https://sagemaker.readthedocs.io/en/stable/frameworks/huggingface/index.html)
- [Deep Learning Container](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#huggingface-training-containers)

## Hyperparameters
```json
{
    "dataset_name": "samsum",
    "do_eval": true,
    "do_train": true,
    "fp16": true,
    "learning_rate": 5e-05,
    "model_name_or_path": "sshleifer/distilbart-cnn-12-6",
    "num_train_epochs": 3,
    "output_dir": "/opt/ml/model",
    "per_device_eval_batch_size": 8,
    "per_device_train_batch_size": 8,
    "seed": 7
}
```

## Train results

| key | value |
| --- | ----- |
| epoch | 3.0 |
| init_mem_cpu_alloc_delta | 180338 |
| init_mem_cpu_peaked_delta | 18282 |
| init_mem_gpu_alloc_delta | 1222242816 |
| init_mem_gpu_peaked_delta | 0 |
| train_mem_cpu_alloc_delta | 6971403 |
| train_mem_cpu_peaked_delta | 640733 |
| train_mem_gpu_alloc_delta | 4910897664 |
| train_mem_gpu_peaked_delta | 23331969536 |
| train_runtime | 155.2034 |
| train_samples | 14732 |
| train_samples_per_second | 2.242 |

## Eval results

| key | value |
| --- | ----- |
| epoch | 3.0 |
| eval_loss | 1.4209576845169067 |
| eval_mem_cpu_alloc_delta | 868003 |
| eval_mem_cpu_peaked_delta | 18250 |
| eval_mem_gpu_alloc_delta | 0 |
| eval_mem_gpu_peaked_delta | 328244736 |
| eval_runtime | 0.6088 |
| eval_samples | 818 |
| eval_samples_per_second | 1343.647 |


## Usage
```python
from transformers import pipeline
summarizer = pipeline("summarization", model="philschmid/distilbart-cnn-12-6-samsum")

conversation = '''Jeff: Can I train a 🤗 Transformers model on Amazon SageMaker? 
Philipp: Sure you can use the new Hugging Face Deep Learning Container. 
Jeff: ok.
Jeff: and how can I get started? 
Jeff: where can I find documentation? 
Philipp: ok, ok you can find everything here. https://huggingface.co/blog/the-partnership-amazon-sagemaker-and-hugging-face                                           
'''
nlp(conversation)
```
