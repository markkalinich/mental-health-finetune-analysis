---
license: apache-2.0
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
model-index:
- name: pszemraj/long-t5-tglobal-large-pubmed-3k-booksum-16384-WIP
  results:
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
      value: 35.9969
      name: ROUGE-1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNzg5ZmI5Y2YzMzdlMjI4N2U1MTE3MDQxNWQyNzkwODFmYzEwNjMwZTU5MTEzOWEwYzdhNWZkMzlkMWI5ZWU3YSIsInZlcnNpb24iOjF9.J56x5lJEDRQzbt3QkmVZn4q5miEpTyCE1rZIiN3xzCDdBL0R5XMhqyqPgbJlJgFcclHHE8mrfjfsj1crV2ygCQ
    - type: rouge
      value: 5.9272
      name: ROUGE-2
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYzg1MzY4OGEwOTRmMGMyOWIyMzkxYzI1YzFiZWZjODUyMDJiMGY0NmMwMzQxNjA1MzhmMDljYzI2MTdhMjljZiIsInZlcnNpb24iOjF9.0rxUBWkRVaPBoUZDFTrjk05AjwJTafxq8AFDGMkDjFx0BfN6rlxENnibj1NP38abysEqlER_gnBz1wjsb4c2Bw
    - type: rouge
      value: 16.0136
      name: ROUGE-L
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMjMwN2YwYzNlZjczZGJhOGExNWJkZTc1OWJiY2YyZmNmZmQ5YTA4ZDA1NmI2ZDM4MmZiN2M3YzFiNDQ1OTk2NiIsInZlcnNpb24iOjF9.oCpGSJwJ0mC_I9Wxw1GaJjus3cjvH2CyW3Lagy8c6GJKd6XPwBcc1CenDp_K3cItAft927iegQbFoYCg8lYgCA
    - type: rouge
      value: 32.941
      name: ROUGE-LSUM
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZmJjZmFlZTUyNjYxMGUxNGNjNzk0MDk5NjYxNGY0NmExMjZhMDViZTcyNmMwZjYwMWQwMmM5ODljZmNjMTgxZiIsInZlcnNpb24iOjF9.uYsoPZNKW3-sUBrcPzAJliY7mCCZA-jGxUbk4aDH-VqLSpEo2HPGbayucDrcUHwrSv7sCihOdHDP2GtxGcPKDg
    - type: loss
      value: 2.9339466094970703
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNDU3NzY4MzJkY2ZmNDc4MDQxZjcyMzE5NTAyMTNlOTczNjBiYjhmODNkMTMwYWZhMjQxM2YzZjhiNGEzODlmZSIsInZlcnNpb24iOjF9.ubsp9ODlTUI6XD9pE310OHswKKd2qCEWacgzXT4P0exypXfqTeKaL9CRCMT9GZf_f8Yg1Zl6FNvSgJoa1T8hCw
    - type: gen_len
      value: 283.7198
      name: gen_len
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNDFlZGZjNWYwYzk3M2E1OGViZWQ1YWY3MDU3MTA0NjI3OWRhZTljMjQ1MjVhYjM3ZGQ2NjFlMzgxZTIzMmViZSIsInZlcnNpb24iOjF9.np0apB8dlENyCSnLtDRYAuo7R5mu7wELjvjeUQPhhT30yUOGCJ1MOt-uE7l0kPqf6v3JYD3KLYB6o-NwnfCHBQ
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
      value: 26.2412
      name: ROUGE-1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNjFlYWRiYzA3NzkxNWQ0NTY3MmY3NGNmYTJhNjBiNDVlZWNjMTliMzQ0YTZiODM2NGNkNWFjMDQ0Y2U1OTIxYiIsInZlcnNpb24iOjF9.VXuruKzSmTj-rc5znqWimqUxFHMq2yi3w958l6rpnEwWzZLki4PaLkmnd000i3WWI1qI8SU-oS5QZ_3BACs4BA
    - type: rouge
      value: 5.9791
      name: ROUGE-2
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZjgyOWNjNmNjMDQ0ZmMwZmQ5ZTAxMTUyNmJhZGQ1NTBkZDI4NzQ3MTYyZDhlNzY5ZGRjZjQ2NWViZmU1MGJhNiIsInZlcnNpb24iOjF9.b0n4KjAbV8K-pcifki4ZtBcyaSTb1zt5NulwQ4eq2ryB1eOktoOvm9BHXH29YcY0vkegoai996azAyhQa64oCw
    - type: rouge
      value: 18.7467
      name: ROUGE-L
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNTU1NmFmZTUxNmFhYTc3OTU3MTk1NTVjOWI2NzAyMTJhZTQ0ZDI0NjhjNzFkZjk3NmNlOTNhMzNlNGM1ZTBlZCIsInZlcnNpb24iOjF9.JDwUXyolkzkUjW52heUuBvfmniToRUwJamq3HXUBPt4eM4RwJCkt9gEqEFwI8enZsHSZV-OrkeYNBBPIGbkHAQ
    - type: rouge
      value: 22.5566
      name: ROUGE-LSUM
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOTFjMWU1YmY5ZDM5OTM0YTliNWE5ZjMyMDk2YTI3MGUyNGFhNGJjZDJhMzA2OTZlODVhODkxYTViZGVjZjk0NiIsInZlcnNpb24iOjF9.UjXKQOz6_4WUM_keDjpZ2JqLk2I_6Qz5sDPn40gTGoShqs-1MdlN2ZD556lg4sASvFhPOgehlocXtkhoVNeDAw
    - type: loss
      value: 2.877626895904541
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNTE1MGE5N2E4MjM4ZjU1NzdkNzVjMzQ2ZTMwZGExZmY2M2NkZmExOGRjN2M0MzNmY2QyMTMxZTA2YWEwZWJlOCIsInZlcnNpb24iOjF9.emXgdp6oFaWXSM_IwWe5f2AuML5q_AF9Fn1uVaLV6oQPQLUUn9kHuJjvhen8rpps3uwV5hlg_FQi1yA0ptg9Bw
    - type: gen_len
      value: 47.6532
      name: gen_len
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOGYwYTA5NjBiMjQ4OTQyZjRjMjAzYWRjYThlZjRiOTAxYTY4YzFmZTY0NzFlZjA4MDY2YzE3M2VjODU3OWNjYyIsInZlcnNpb24iOjF9.VD34TzxOsg5dSxp3o8feeNS_i0jOShKyIgCco6gaI6CV2U2iADzOJRYvTk__il_mnTI8_Q3n5krTq5VBWIrnBg
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
      value: 19.3209
      name: ROUGE-1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYTYwOGVmZDZhNmJlMTk3ZmEzMThjMmJmNDVhMzMyZGYzM2NhMzc5ZDhiY2I0ZGMxZjYzZDBjMmQ0ZTYyZGM3YyIsInZlcnNpb24iOjF9.2CcwX9HsunSocmuXzYeGgUttbxSTJeI3Rd_z8ahVMOVKBU3gy_SFTz4jRAQ-reNpKXcHS-pXBnkrBKF1c909Ag
    - type: rouge
      value: 2.7978
      name: ROUGE-2
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZDRiZjQ5ODRmNDVhNWMwMjBmZjUwNTkwZDU1OGVlZjlhNTIwZTQ1NDkyOTlhMTMwOGU2YjAwYjZjMTM5M2EyZSIsInZlcnNpb24iOjF9.th3dNtUmR9BK_1CErYVLkvp9pjbDEPrYouR_sfTOyHcsiUEnvXWAaHt8VfAjCvZa5GVExIUJ1mU5juWHGgqmCA
    - type: rouge
      value: 12.5816
      name: ROUGE-L
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMTgwNmI1NzRhYzg2MDk2ZmJmYjE4YTNhMjk4OWZiOThjMTBlNmUxMGFjYjYwZjgzNWMwZThlZDIyMjJjZDEzMyIsInZlcnNpb24iOjF9.Px6A7iX1WEX0LkAtRYbgH3bG4ZhR7Qpm0j61SOtCU6tfwIhWjlfndXOB_1f4OM52P38WX17ug3Dbv_fopc4pDw
    - type: rouge
      value: 15.0239
      name: ROUGE-LSUM
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNjhmOWJkNWY0MzkxMDI1NDlkMzhmMzEzOWM1OTE5ZjgwMDhmOGQyOWJkYzI5ODg1NTUzMmNlZDUyZjYyYzEyNyIsInZlcnNpb24iOjF9.wft3QMXCx8d6MLSE6NA4OxJ1Z6BVvpIw-BTtwJR8HZBPEVTrysG9tl3OwJ0oMV3ZvtzozW5WOGJ7sAxTXIqdAA
    - type: loss
      value: 4.483709335327148
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiODYwMDc4MTFmZGRmMjljNzNiN2QxNDNiZWJhZDE3ODcyNDExOTQ1MzhhZTk5MzQ4ZmM1NTUxN2QyMDFkYjZhYiIsInZlcnNpb24iOjF9.NMGHLvhHJwFOKi1aojjHzwslAB-D_TUQmNN1iLpBokcNZjrbgw3qqO2HY2xQn7QEQFZpAy-UD7ptIJ5zpJhSDw
    - type: gen_len
      value: 82.729
      name: gen_len
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMjkzYmI1YWE2MmVkODdjNzU4Y2U3NTgwZjdjYjMxZTBkYmIyODVkNzA0NzEyZjlmOGQ4ODg1ZWE2Mzc1ZDE2MiIsInZlcnNpb24iOjF9.1vDZt_Ujy6kM_VjgA7ZenMjg5UJUI_mXUueB3I1WYhsTOzq_Dib8cjlHejkFuLHbHoKzg4x5WEu90ncEpptIAg
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
      value: 36.5688
      name: ROUGE-1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMDA2MjFkZThjMTk3NGNjNzk3MzdlMjgyMDJkYzA1MGMwYjdkZTZjMzE2NGE1MjM5OTFiOTU3YmVmZTNiNGIzYiIsInZlcnNpb24iOjF9.-1cYB1OAdxdq6bJb1c1xavlHNQxtYcNvf1ro7a5U5zksCBsfufG-B7AWkgxlyfxMMb373bwq4QqbRkk8omiqAw
    - type: rouge
      value: 12.5849
      name: ROUGE-2
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNjMzNDc2NzBjMGY4MTAyNzk3YTlkZDViOWZjNmEzODBhMDI3NTQ2ZDk4YzA2YTA1YmNmOTUwMjZiMjMzZTA0NiIsInZlcnNpb24iOjF9.WOedmezrR8FUpNaoPZEOzF8-m3zr77XoCUmQfw6RNlA_6otM0cQyOy2OZPWHAXv2Q9PLQHX1MntAf9ZLLXCfBQ
    - type: rouge
      value: 22.2461
      name: ROUGE-L
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNDgyM2ZhN2QzMzU0YzY0YzU4MTE4OTQzMGVmNGE4Yjk4NWJlMWUzOWU0ZDY2ZDc0YTI1Y2RjZjA4ODM4YzRlNSIsInZlcnNpb24iOjF9.ApE22RN5wiJt3lo9_VgY7D7OLTC0xWcVZZ7Q2b3Z3qzfFVZnnr7GvOxDgqvKtU5SJEzvqvGUSqTa6pfCbvu7Bg
    - type: rouge
      value: 30.6507
      name: ROUGE-LSUM
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMThmOTQ4N2Q3NTdhNjVkNmUxZmY4MTRhNzYxMmZhMGU0NzJhYWE3YjAwMzE2ZmNiMGY2YzNiZWQ5NWZiMTQxZCIsInZlcnNpb24iOjF9.6gNsS7SASoDHs9nKeluC23FUcaTmo75DM18aRlT1T2HT3J66fuG9fWLpFpL2c1TtJTD_XU2aEnMeQO0VjIaHAQ
    - type: loss
      value: 2.6456267833709717
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMzYxOTkxMDcyMTVkZDI0YWUyNTE5ZTE3YzM5MDc2ZDM5ZWZiNjhiNTBlZjlhNzA3OTQzZWJiZWRmNGFiYTdiYyIsInZlcnNpb24iOjF9.hOVX5_MW58SlQjDbEakqrZvFhmDcJTv3QNyhP7ayd4mOjHg2s8qPJPXQEpSsCNgTjNhd4h0WC3B6-dVXLSLFBw
    - type: gen_len
      value: 139.0398
      name: gen_len
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZDkzMWU4MjZlYWUzZjBmN2ZmMTc4MjEyZDUwYTFhMWY0NTZmZTI4NjYyYzMxZDY5OGY0Y2E3MTA0NmJkYzNlYyIsInZlcnNpb24iOjF9.kJctRHl1hSPEjCO6GpFKTlJ190Mc70NTlGrX0sciIevCSZ8IgzITZEnuR5SP7FgZIcQV82PrGH2RifpD-ImRBA
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
      value: 37.0248
      name: ROUGE-1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYTdmYTU0OWRiNTRlMjFmMzI3N2FjMDIyZmE3ZTMyZDEzZmIzNzRkOWVkZTc5YTg4NTc3ZWIyMDVjY2NlZDhlMSIsInZlcnNpb24iOjF9.-c5dYiAJ7mGXTrP2Q4rzXf3to_gLSicvE2et6NrLIhr4LfdhMWHl1KgOe1nSwkL_rI8pBMDLQ73_LhfjrnWfDQ
    - type: rouge
      value: 9.0446
      name: ROUGE-2
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOGI0Y2JiZWFmNmYwMWYyYzVlZDgyZmZiZDcxZWU4NTgyMzA3MzJmOTM5NmQ1YzBlNTc1MDhiOWU0NWFiOGQ0ZiIsInZlcnNpb24iOjF9._a3fSk8m3-MIkU6EZFhga5_gD5fAkBYInEtGLi6fTkpO-MHCJPJhMKa3abkX7WYOGUWq2boK93LxRSUiJLisDA
    - type: rouge
      value: 18.0521
      name: ROUGE-L
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYTI3OTI5OTBhZTRiOTVlOTM4NTJlNTRhYTAyZjYyY2JiMmNhNWUyY2U0ODcxY2UxYmUwNTdlNmZkMTQ4YjQyYSIsInZlcnNpb24iOjF9.6nfKp5X0L8h6UB7QCyWe9r-yUciqEoH_2MKTcCvJmJIzjyzjsVhwXcUicNvjF7tV2vozv3LTDImoz4RireAbCA
    - type: rouge
      value: 33.4723
      name: ROUGE-LSUM
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNjJkMTU1OTFjZDE1Nzk4MmYzZWQzZmFhZGQ5MWRmNDM0ZGQ2MmNiMDQxOTY5MTNhM2QwZDE2NGViMDkzZTRjNyIsInZlcnNpb24iOjF9.8rwYGzNPFfTE2q0dgifp8z7EjpJt5KGrsfGE2dI8liEVrOziXZZYcY8tgVJldu9CsGpP4nUCMq93BA-ZrwyoBQ
    - type: loss
      value: 3.381495237350464
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMmI0Y2ZmZmVmNDU1MGZlYTZlMDQ5YzY0ZmY1NjNlYzdmN2NmY2ZmZWI5NWJmNjQzNmJiZDUwOWU4YjYzYjFjMCIsInZlcnNpb24iOjF9.CkCmAGRz3s2YXbpqRDJ7bjfEpCllU-AS5QJo1ZznvTkKN4iv7aLHgiXKIkPKSfeO2qWj1zVL_P9NMG0IxBvXBA
    - type: gen_len
      value: 211.2066
      name: gen_len
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMzY2NjQ4ZjBkZWI5MDE2Y2IwMmYxMDc3ZmRlZjk4M2U0MmQ4Mjg3YWZlZmM0ZjdiZDIyZTIxNDViNzExMTEwNiIsInZlcnNpb24iOjF9.hz2qJ2O3Hd6YDLveOZ1yKU7rMRpxs65nNGWaJ3Ln4niQXl_LqXB3em5cbl0FtWS_E9Ptso6o8fGz76mN6hNwDg
---

# long-t5-tglobal-large-pubmed-3k-booksum-16384-WIP

> NOTE: this is still a work-in-progress (WIP) and not completed/converged by any means, but sharing to maybe save some time for others :) 

## Updates

_As I update this WIP checkpoint, I will post a note here._

- July 26, 2022: add two more epochs of training, metrics starting to be _almost_ as good as the more-tuned `base` variant
- July 8, 2022: add checkpoint with ~4 epochs of training on A100, equating to approx 350 steps of functional batch size 128
- July 4, 2022: add checkpoint with six additional epochs of training with the dataset summary outputs filtered to 1024 **tokens**, resolving the prior issue of short summaries.

## About

- a checkpoint of [Stancld/longt5-tglobal-large-16384-pubmed-3k_steps](https://huggingface.co/Stancld/longt5-tglobal-large-16384-pubmed-3k_steps) trained on `kmfoda/booksum` for about 26 epochs 
- max input lengths during training vary between 8192 and 16384 tokens depending on GPU availability. This checkpoint was **trained with 16384 tokens as the max input length for the final 10+ epochs**

  
 ## Comparisons
 
 - compare to [pszemraj/led-large-book-summary](https://huggingface.co/pszemraj/led-large-book-summary). 
   - **inference API has been disabled because it's too compute-intensive :/**
 