---
license: apache-2.0
language:
  - multilingual
  - en
  - zh
  - id
tags:
  - text-classification
  - multi-label-classification
  - pii-detection
  - long-document
  - sliding-window
  - modernbert
pipeline_tag: text-classification
library_name: transformers
base_model: jhu-clsp/mmBERT-base
---

# General PII Detector — 23 labels, document level

Give it text of any length; it returns which of 23 categories of personal or sensitive
information are present. Long inputs are windowed internally, so callers never deal with a
context limit.

## Model Details

### Model Description

A multi-label document classifier: a multilingual encoder with one linear head producing 23
independent probabilities, each compared against its own threshold.

This is a **presence detector**, not an extractor. It reports that a phone number is somewhere in
the text; it does not say where, and it does not return the value.

- **Model type:** multi-label text classification (encoder + linear head)
- **Languages:** multilingual; evaluated on Chinese, English and Indonesian
- **Base model:** [`jhu-clsp/mmBERT-base`](https://huggingface.co/jhu-clsp/mmBERT-base) (ModernBERT architecture)
- **Parameters:** 307M, of which 196.6M are embeddings
- **Licence:** Apache 2.0, inherited from the base encoder

### Measured on real traffic

Training, calibration and evaluation all use **real API traffic** — captured HTTP
request and response bodies, labelled document by document. No synthetic data was used for any
of the numbers below. Splits are grouped by API endpoint, never by row, so near-duplicate
documents from the same endpoint cannot straddle training and evaluation.

Over the 14 labels with enough positives and negatives to measure, on 4,359 held-out real
documents:

| | macro-AP | macro-F1 |
| --- | --- | --- |
| **this model** | **0.930** | **0.891** |
| same encoder without domain-adaptive pretraining | 0.706 | 0.650 |

The strongest labels, with their real precision and recall at the shipped threshold:

| label | eval positives | precision | recall | F1 |
| --- | ---: | ---: | ---: | ---: |
| `email` | 83 | 0.976 | 1.000 | 0.988 |
| `username` | 81 | 0.976 | 0.988 | 0.982 |
| `phone_number` | 72 | 0.971 | 0.931 | 0.950 |
| `product_data` | 1127 | 0.903 | 0.964 | 0.933 |
| `postal_code` | 15 | 1.000 | 0.867 | 0.929 |
| `user_id` | 82 | 0.886 | 0.951 | 0.918 |
| `device_id` | 12 | 0.917 | 0.917 | 0.917 |
| `tax_id` | 13 | 1.000 | 0.846 | 0.917 |
| `street_address` | 39 | 0.900 | 0.923 | 0.911 |

The full 23-label table, including the weak labels and what the pretraining stage bought each of
them, is under [Evaluation](#evaluation).

### Model Sources

- **Windowing and aggregation library:** [sliding-window-transformers](https://github.com/godzeo/sliding-window-transformers)

## Uses

### Direct Use

Flagging which categories of personal information appear in a document, for data-inventory,
routing or triage work: deciding which API endpoints handle sensitive data, which logs need
stricter retention, which records need review.

### Out-of-Scope Use

- **Not an extractor.** No spans, no values, no redaction. Pair it with rules or a token-level
  model if you need the value itself.
- **Not a compliance control.** Two labels are broken and three were never evaluated. Do not make
  it the only safeguard for a regulatory obligation.
- **Not calibrated outside API traffic.** See *Bias, Risks and Limitations*.

## Bias, Risks and Limitations

**What each label is actually worth.** Two things differ and are easy to conflate: whether a
label has *measured accuracy* (enough positives in the evaluation split) and whether its
*threshold was fitted* on the separate calibration split. 14 labels have the first, 13 have the
second. Where a threshold was not fitted, the label keeps the 0.5 default — which is unoptimised,
not automatically bad. Measured at that default:

| label | positives | precision | recall | F1 | verdict |
| --- | --- | --- | --- | --- | --- |
| `ip_address` | 8 | 1.000 | 1.000 | 1.000 | usable |
| `date_of_birth` | 7 | 1.000 | 1.000 | 1.000 | usable |
| `age` | 1 | 1.000 | 1.000 | 1.000 | usable, one sample |
| `payment_card_number` | 12 | 0.846 | 0.917 | 0.880 | usable |
| `password` | 6 | 1.000 | 0.500 | 0.667 | half the positives are missed |
| `biometric_id` | 2 | 0.000 | 0.000 | 0.000 | **broken** |
| `house_number` | 1 | 0.000 | 0.000 | 0.000 | **broken** |
| `passport_number` | 0 | — | — | — | **no evaluation data at all** |
| `social_security_number` | 0 | — | — | — | **no evaluation data at all** |
| `vehicle_plate` | 0 | — | — | — | **no evaluation data at all** |

So: **two labels are broken** (`biometric_id`, `house_number`), **three are entirely unmeasured**
(`passport_number`, `social_security_number`, `vehicle_plate` — the evaluation split contains no
positive example of them), `password` recalls half of what it should, and the remaining 17 work.
Every one of these counts is small, so treat the numbers as indicative rather than tight.

**Labels suppress one another on dense documents.** A card number alone scores 1.000; in a
document that also carries a name, a phone, an address, an e-mail and an IP it falls to 0.008.
The step-by-step measurement is under *Illustrative examples* below. A label reported at 0.82 AP
can be near-zero on a PII-dense document, so aggregate accuracy is not a safe proxy for dense
traffic.

**Distribution.** Trained and calibrated on HTTP request and response bodies from API traffic.
On other shapes (CSV, SQL dumps, logs, e-mail, prose) the high-frequency labels transfer in spot
checks, but the rare ones do not and no threshold is calibrated for them.

**Isolated values are missed.** A bare phone number on its own line scores near zero; the same
number inside a sentence scores 1.000. The model learned "value plus context", not pattern
matching.

**Cross-window association is impossible.** Aggregation across windows is a disjunction, so
evidence more than ~510 tokens apart cannot be combined. Every label here is locally decidable,
so this costs nothing in practice — but a label that needed "A and B hold far apart" would be out
of reach for this architecture.

### Recommendations

Measure per-label recall on your own data before relying on any label, and do it on documents
that are as dense as your real traffic. If you adopt this outside API traffic, refit the
thresholds on a calibration sample of your own distribution; that is far cheaper than retraining
and recovers most of the loss.

## How to Get Started with the Model

```python
from transformers import AutoModel, AutoTokenizer

REPO = "Zeo6/general-pii-detector"
model = AutoModel.from_pretrained(REPO, trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(REPO)

result = model.detect(text, tokenizer=tokenizer)
# {"labels": ["phone_number", "person_name"], "windows": 1, "scores": {...}}
```

`text` is a plain string of any length. That is the whole interface — no chunking, no batching of
windows, no threshold handling on your side. Pass a list to score several documents at once.

If you would rather not enable `trust_remote_code`, download the repo and import the single file
directly; it needs nothing beyond `torch` and `transformers`:

```bash
hf download Zeo6/general-pii-detector --local-dir ./general-pii-detector
```

```python
import sys
sys.path.insert(0, "./general-pii-detector")
from modeling_general_pii import GeneralPIIDetector

detector = GeneralPIIDetector.from_pretrained("./general-pii-detector")
detector.detect("...")                      # the tokenizer loads from the same directory
detector.detect(["doc one", "doc two"])     # a list in, a list out
```

## Training Details

### Training Procedure

Three stages. The base encoder was first fine-tuned on labelled traffic; that checkpoint then
received **domain-adaptive masked-LM pretraining** on unlabelled text of the same distribution
(holdout MLM loss 13.1 → 0.74); the adapted encoder was then fine-tuned with all 22 layers
unfrozen, for three random seeds, and the three resulting checkpoints were averaged uniformly.

Fine-tuning uses multiple-instance learning: a document is a bag of windows, each label
back-propagates through its own single highest-scoring window, and label sampling is weighted by
the square root of each label's positive count so rare labels are not oversampled into
overfitting.

Splits are grouped by API endpoint, never by row, so near-duplicate documents from one endpoint
cannot straddle training and evaluation.

### How a document is scored

Text is cut into 512-token windows that overlap by 128 tokens, so each window advances 382
tokens. Every window is encoded, its token states are averaged under the attention mask, one
linear head produces a logit per label, and the document takes the **maximum over windows** for
each label. There is no cap on the window count, so input length is not limited.

512 is a measured choice, not a capacity limit. The encoder natively supports 8192 positions, but
longer windows scored **worse** — and, against intuition, worst on the long documents they were
supposed to help. Two poolings were tried to separate "dilution" from "length"; both lost, so it
is the length. A single 8192-token pass was also 5.7x slower than the windowed path on an
8.3k-token document, because attention is quadratic.

## Evaluation

### Results, all 23 labels

Real traffic, 4,359 held-out documents, at the shipped threshold. *Baseline AP* is the
same encoder fine-tuned without the domain-adaptive pretraining stage, on the same split, so the
last column shows what that stage bought for each label:

| label | eval positives | AP | precision | recall | F1 | threshold | baseline AP |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `product_data` | 1127 | 0.974 | 0.903 | 0.964 | 0.933 | 0.9112 | 0.976 |
| `phone_number` | 72 | 0.974 | 0.971 | 0.931 | 0.950 | 0.9872 | 0.854 |
| `person_name` | 194 | 0.865 | 0.701 | 0.799 | 0.747 | 0.9560 | 0.755 |
| `street_address` | 39 | 0.906 | 0.900 | 0.923 | 0.911 | 0.3451 | 0.909 |
| `payment_card_number` | 12 | 0.823 | 0.846 | 0.917 | 0.880 | 0.5000 | 0.369 |
| `national_id` | 14 | 0.841 | 0.647 | 0.786 | 0.710 | 0.0619 | 0.530 |
| `passport_number` | 0 | — | — | — | — | 0.5000 | — |
| `ip_address` | 8 | 1.000 | 1.000 | 1.000 | 1.000 | 0.5000 | 0.906 |
| `date_of_birth` | 7 | 1.000 | 1.000 | 1.000 | 1.000 | 0.5000 | 0.844 |
| `employee_id` | 23 | 0.958 | 0.950 | 0.826 | 0.884 | 0.8117 | 0.902 |
| `credential` | 50 | 0.901 | 0.788 | 0.820 | 0.804 | 0.5385 | 0.565 |
| `password` | 6 | 0.839 | 1.000 | 0.500 | 0.667 | 0.5000 | 0.725 |
| `age` | 1 | 1.000 | 1.000 | 1.000 | 1.000 | 0.5000 | 0.111 |
| `biometric_id` | 2 | 0.018 | 0.000 | 0.000 | 0.000 | 0.5000 | 0.174 |
| `username` | 81 | 0.991 | 0.976 | 0.988 | 0.982 | 0.7535 | 0.711 |
| `user_id` | 82 | 0.962 | 0.886 | 0.951 | 0.918 | 0.5761 | 0.326 |
| `social_security_number` | 0 | — | — | — | — | 0.5000 | — |
| `tax_id` | 13 | 0.958 | 1.000 | 0.846 | 0.917 | 0.1200 | 0.705 |
| `device_id` | 12 | 0.898 | 0.917 | 0.917 | 0.917 | 0.0210 | 0.529 |
| `vehicle_plate` | 0 | — | — | — | — | 0.5000 | — |
| `email` | 83 | 0.965 | 0.976 | 1.000 | 0.988 | 0.8387 | 0.979 |
| `postal_code` | 15 | 1.000 | 1.000 | 0.867 | 0.929 | 0.9756 | 0.769 |
| `house_number` | 1 | 0.004 | 0.000 | 0.000 | 0.000 | 0.5000 | 0.022 |

**Read the positive counts alongside the scores.** Several labels rest on a handful of examples:
a 1.000 on `age` means one positive was ranked correctly, not that the label is solved. The
numbers are tight only where the count is large — `product_data` (1127), `person_name` (194),
`email` (83), `user_id` (82), `username` (81), `phone_number` (72), `credential` (50).

Domain-adaptive pretraining helped most where labelled data was scarcest: `user_id` 0.326 → 0.962,
`payment_card_number` 0.369 → 0.823, `device_id` 0.529 → 0.898, `credential` 0.565 → 0.901. It
changed little where data was already plentiful (`product_data`, `email`).

### Labels and thresholds

| label | meaning | threshold | calibrated |
| --- | --- | --- | --- |
| `product_data` | product / catalog / price / inventory content | 0.9112 | yes |
| `phone_number` | phone numbers | 0.9872 | yes |
| `person_name` | natural-person names | 0.9560 | yes |
| `street_address` | street-level address lines | 0.3451 | yes |
| `payment_card_number` | payment card numbers | 0.5000 | **no** |
| `national_id` | national ID numbers | 0.0619 | yes |
| `passport_number` | passport numbers | 0.5000 | **no** |
| `ip_address` | IP addresses | 0.5000 | **no** |
| `date_of_birth` | dates of birth | 0.5000 | **no** |
| `employee_id` | staff numbers | 0.8117 | yes |
| `credential` | credentials, tokens, API keys | 0.5385 | yes |
| `password` | passwords | 0.5000 | **no** |
| `age` | a person's age | 0.5000 | **no** |
| `biometric_id` | biometric identifiers | 0.5000 | **no** |
| `username` | usernames, handles, display names | 0.7535 | yes |
| `user_id` | person / personal-account identifiers | 0.5761 | yes |
| `social_security_number` | social security numbers | 0.5000 | **no** |
| `tax_id` | tax identifiers | 0.1200 | yes |
| `device_id` | device identifiers | 0.0210 | yes |
| `vehicle_plate` | vehicle plate numbers | 0.5000 | **no** |
| `email` | e-mail addresses | 0.8387 | yes |
| `postal_code` | postal codes | 0.9756 | yes |
| `house_number` | house / building numbers | 0.5000 | **no** |

Label names are English identifiers. The training schema was authored in Chinese and
`config.json` carries the mapping under `label_names_zh`, so the original names are
recoverable: `product_data` ↔ `product_data`, `credential` ↔ `credential`, and so on. Renaming them
changed only metadata — the head's 23 outputs keep their order and every score is
bit-identical.
### Speed

CPU, 8 threads, single process, one document at a time:

| windows per document | median tokens | median latency |
| --- | --- | --- |
| 1 | 57 | 44 ms |
| 2–3 | 727 | 352 ms |
| 4–10 | 2,773 | 1.35 s |
| 11–50 | 8,255 | 4.43 s |
| 51+ | 49,446 | 26.8 s |

Overall median 339 ms, p90 16.8 s, p99 73 s. **The distribution is heavily right-skewed** — quote
the median and the p90 together. Peak inference memory 3.4 GiB. Cap the windows per document if
you need bounded latency.

## Illustrative examples

The accuracy numbers above come from real traffic. The snippets below exist only to show the
input and output shape, and to expose one failure mode — they are **not** evidence of accuracy,
and a hand-written snippet is the worst case for this model. Every value in them is fabricated:
`example.com` is reserved by RFC 2606, `203.0.113.0/24` by RFC 5737. The outputs shown are what
the model actually returns for these strings.

### A shipping-address response

Input, exactly as it comes off the wire:

```json
{"code":0,"data":{"addresses":[{"address_id":"778901","receiver_name":"Andi Saputra","phone":"+62 812-3456-7890","detail":"Jl. Melati Raya No. 42, RT.003/RW.005","city":"Jakarta Pusat","province":"DKI Jakarta","post_code":"10510","is_default":true}]}}
```

Output: `["phone_number", "person_name", "street_address", "postal_code"]`, one window.

| label | score | threshold | |
| --- | --- | --- | --- |
| `street_address` | **1.0000** | 0.3451 | ✅ |
| `postal_code` | **0.9999** | 0.9756 | ✅ |
| `person_name` | **0.9997** | 0.9560 | ✅ |
| `phone_number` | **0.9996** | 0.9872 | ✅ |
| `house_number` | 0.0539 | 0.5000 | |
| the other 18 | ≤ 0.0004 | — | |

`address_id` does **not** trigger `user_id`: a record id is not a person id. `province` alone is an
administrative division, which belongs to a label outside this schema, so `street_address` fires on the street
line only.

### Other shapes

| input | output |
| --- | --- |
| `{"X-Forwarded-For":"203.0.113.47","Authorization":"Bearer eyJ…","X-Device-Id":"7a9f3c2e1b8d4056","User-Agent":"Mozilla/5.0 (Linux; Android 13)"}` | `["ip_address","device_id"]` — `device_id` 1.000, `ip_address` 0.985. The bearer token scores 0.250 and is **missed**. `User-Agent` correctly does not trigger `device_id`. |
| `{"user_id":"7495806081620937515","page":1,"lang":"id-ID"}` | `["user_id"]` at 1.000; `page` and `lang` ignored |
| `老王你好，我手机号是13812345678，身份证110101199003074512，晚点联系` | `["phone_number","person_name","national_id"]` — 1.000 / 0.997 / 0.998. Prose is out of distribution, yet the high-frequency labels transfer. `passport_number` stays at 0.258. |
| `这个季度的目标是把平均响应时间从八百毫秒降到三百毫秒以内。` | `[]`, top score `person_name` 0.001 |

### A failure worth understanding

An order-detail response carrying a name, phone, address, e-mail, user id, product line, masked
card number and client IP returns only `["phone_number","person_name","street_address","username","user_id"]`. A human
would also label e-mail, postal code, product data, IP and card number. All five are missed.

It is **not** that the values are unrecognisable. Each of them, alone, scores 1.000. Adding
fields one at a time shows what actually happens:

| document | `email` | `ip_address` | `payment_card_number` | `postal_code` |
| --- | --- | --- | --- | --- |
| `{"email": …}` | **1.000** | 0.000 | 0.000 | 0.000 |
| `+ client_ip` | 0.999 | **1.000** | 0.000 | 0.000 |
| `+ card_no` | 0.997 | 1.000 | **0.121** | 0.000 |
| `+ post_code` | 0.997 | 0.999 | 0.221 | **0.991** |
| `+ name, phone, address` | 0.988 | 0.787 | **0.008** | 0.791 |
| `+ data/buyer/payment nesting` | 0.961 | 0.777 | 0.038 | **0.149** |

**Labels suppress each other.** Nothing about the values changed; only the fields around them did. The
likely mechanism is the training objective: each label back-propagates through its own single
strongest window, and every label reads the same pooled vector for that window, so the
high-frequency labels — `person_name`, `phone_number`, `street_address`, with hundreds to
thousands of training positives — crowd out the rare ones. `payment_card_number` has 83 positives
in the traffic portion of the training data and is the first to collapse.

Field naming, masking and document length are **not** the cause, which is worth stating because
they are the usual suspects: `payment_card_number` scores 1.000 on `4111 **** **** 1234`, on the
unmasked number, and on a last-four-only form; `ip_address` scores 1.000 under `client_ip`, `ip`,
`remote_addr`, `X-Forwarded-For`, as a bare value, and inside a sentence; `email` holds 1.000
with 300 unrelated records and 25 windows appended.

One miss has a different cause: `product_data` goes from 0.079 to **0.997** when 300 order-history
records are added. The label was defined around a document *being* product data, not around a
product name appearing once, so a single line item legitimately does not qualify.

## Technical Specifications

| | |
| --- | --- |
| architecture | ModernBERT encoder + linear head |
| layers / hidden / heads | 22 / 768 / 12 |
| vocabulary | 256,000 (unchanged from the base model) |
| window / overlap | 512 / 128 tokens |
| pooling | attention-masked mean over tokens in a window |
| document aggregation | maximum over windows, per label |
| output | 23 independent sigmoid probabilities |
| composition | uniform weight average of three training seeds |
