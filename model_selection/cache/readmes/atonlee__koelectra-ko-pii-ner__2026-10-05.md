---
library_name: transformers
tags:
- ner
- pii
- korean
- token-classification
- on-device
- privacy
pipeline_tag: token-classification
model_type: electra
language:
- ko
datasets:
- BCCard/pii-masking-openpii-finance
- townboy/korean-pii-dataset
base_model:
- monologg/koelectra-small-v3-discriminator
license: apache-2.0
---

# koelectra-ko-pii-ner · Korean PII Detection Model

A 14M-parameter NER model that detects personal data in Korean text and returns its
**position and type**.

Used for masking personal data, or for identifying it before text is sent to an
external LLM or to the cloud.

| tier | criterion | recommended action | main labels |
| --- | --- | --- | --- |
| `tier1` | identifies a person on its own | do not send off-device | resident registration number · alien registration number · passport · driver's licence · card number · account number · password |
| `tier2` | identifies a person in combination with other data | mask, then send | name · phone · email · address · date of birth · user id · employee id · vehicle plate · IP |
| `none` | entity that is not treated as personal data | send as-is | date · time · quantity · place · organisation |

`none` does not mean the sentence contains no personal data. It means an entity that
is detected but not treated as personal data, such as `PLACE` or `ORGANIZATION`.

## Usage

```python
import torch
from transformers import AutoModelForTokenClassification, AutoTokenizer

MODEL_ID = "atonlee/koelectra-ko-pii-ner"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForTokenClassification.from_pretrained(MODEL_ID).eval()

text = "김민준 씨한테 010-1234-5678로 연락해줘"

inputs = tokenizer(
    text,
    return_offsets_mapping=True,
    return_tensors="pt",
    truncation=True,
    max_length=512,
)

offsets = inputs.pop("offset_mapping")[0]

with torch.no_grad():
    logits = model(**inputs).logits

predictions = logits.argmax(dim=-1)[0]

for pred, (start, end) in zip(predictions, offsets):
    if start == end:
        continue

    label = model.config.id2label[pred.item()]

    if label != "O":
        print(label, repr(text[start:end]), f"[{start}:{end}]")
```

Output:

```text
B-NAME  '김민'  [0:2]
I-NAME  '준'    [2:3]
B-PHONE '010'   [8:11]
I-PHONE '-'     [11:12]
I-PHONE '123'   [12:15]
I-PHONE '4'     [15:16]
I-PHONE '-'     [16:17]
I-PHONE '56'    [17:19]
I-PHONE '78'    [19:21]
```

The model predicts personal data using the BIO scheme.

* `B-` — start of a region
* `I-` — continuation of the same region
* `O` — token that is not a target

Tokens are subword units, so consecutive BIO tags have to be joined to recover the
actual region.

```text
김민준                          NAME
010-1234-5678                   PHONE
900101-1234567                  RRN
5310-99**-****-1122             CARD_NUMBER
서울시 강남구 테헤란로 152 3층      ADDRESS
```

One joined region is **one entity**. `김민준 = NAME (0, 3)` is one. A sentence can
contain several, and the evaluation below counts entities, not sentences.

## Labels

29 labels.

### `tier1` — do not send off-device

Identifies a person on its own.

| label | description | example |
| --- | --- | --- |
| `RRN` | resident registration number | `900101-1234567` |
| `ALIEN_ID` | alien registration number | `920414-6613077` |
| `PASSPORT` | passport number | `W858W0028` |
| `DRIVER_LICENSE` | driver's licence number | `19-61-620553-00` |
| `IPIN` | i-PIN · connecting information | `7275209485124` |
| `CARD_NUMBER` | card number | `4594-1722-2866-5259` |
| `CARD_EXPIRY` | card expiry date | `10/2028` |
| `CVC` | card security code | `488` |
| `ACCOUNT_NUMBER` | bank account number | `719-938-027247` |
| `SECRET` | password · credential | `A2UfgtKg!W1x` |

### `tier2` — mask, then send

Identifies a person in combination with other data.

| label | description | example |
| --- | --- | --- |
| `NAME` | person's name | `김민준` |
| `PHONE` | phone number | `010-6517-8506` |
| `EMAIL` | email address | `jkim899@example.com` |
| `ADDRESS` | address with a building or unit number | `인천광역시 연수구 송도동 6` |
| `ZIPCODE` | postal code | `55857` |
| `BIRTHDATE` | date of birth | `2001년 5월 25일` |
| `USER_ID` | account id | `quiet_owl22` |
| `GENERIC_ID` | assigned number — employee id, membership id | `MEM-865502` |
| `VEHICLE_NUMBER` | vehicle plate | `89라 8008` |
| `IP_ADDRESS` | IP address | `221.139.235.53` |
| `URL` | link containing a personal identifier | `https://example.co.kr/account/9uemxnc5l` |
| `DEPARTMENT` | department | `인사팀` |
| `POSITION` | job title | `팀장` |
| `ATTRIBUTE` | personal attribute — blood type, religion, major | `A형` · `천주교` |

### `none` — send as-is

Detected, but not treated as personal data.

| label | description | example |
| --- | --- | --- |
| `PLACE` | place name without a building number | `강릉시` · `메가박스 강남` |
| `ORGANIZATION` | institution · company · group | `환경부` · `NAVER` |
| `DATE` | date | `1939-10-14` |
| `TIME` | time | `오전` |
| `QUANTITY` | quantity | `40%` |

`ADDRESS` and `PLACE` are split by form. With a building or unit number it is
`ADDRESS` (tier2); without one it is `PLACE` (none).

## ONNX

ONNX models are included.

| file | size |
| --- | ---: |
| `model.onnx` | 56.6 MB |
| `model_fp16.onnx` | 28.5 MB |
| `model_int8.onnx` | 14.7 MB |
| `model_uint8.onnx` | 14.7 MB |
| `model_quantized.onnx` | 14.7 MB |
| `model_q4f16.onnx` | 15.0 MB |

`model_quantized.onnx` is the uint8 model under the name Transformers.js looks for.

## Training

| | |
| --- | --- |
| Base model | `monologg/koelectra-small-v3-discriminator` |
| Parameters | 14.1M |
| Tokenizer | Korean WordPiece |
| Task | Token Classification |
| Tagging | BIO |
| Max input | 512 tokens |

Training used public datasets and hand-written PII examples.

| source | licence | contribution |
| --- | --- | --- |
| [`BCCard/pii-masking-openpii-finance`](https://huggingface.co/datasets/BCCard/pii-masking-openpii-finance) | CC BY 4.0 | financial and administrative prose, structured identifiers |
| [`townboy/korean-pii-dataset`](https://huggingface.co/datasets/townboy/korean-pii-dataset) | CC BY 4.0 | Korean names, affiliations, personal-data expressions |

The following were written for this model and added to the training data.

* masked identifiers
* partially revealed identifiers
* ordinary sentences containing no personal data
* strings shaped like identifiers but not personal data

Neither the source datasets nor the merged training corpus is redistributed here.

## Evaluation

5,171 test sentences carry ground-truth annotations — 17,537 entities in total,
personal data included. Predictions were compared against those annotations.

Three criteria, differing in how much has to match.

| criterion | counts as correct when | needed for |
| --- | --- | --- |
| position | it overlaps the ground truth | deciding whether personal data is present |
| type | it overlaps and the label matches | tier routing |
| boundary | start and end character positions match too | masking |

| criterion | Precision | Recall | F1 |
| --- | ---: | ---: | ---: |
| position | 93.8% | 98.4% | 96.1% |
| type | 92.0% | 96.5% | 94.2% |
| boundary | 86.1% | 90.3% | 88.1% |

By tier, on the **type** criterion.

| tier | ground truth | Precision | Recall | F1 |
| --- | ---: | ---: | ---: | ---: |
| `tier1` | 1,979 | 84.8% | 94.3% | 89.3% |
| `tier2` | 8,975 | 94.9% | 98.5% | 96.7% |
| `none` | 6,583 | 90.2% | 94.3% | 92.2% |

## Licence

Model weights: Apache-2.0

Inherited from the base model. Each external dataset used in training keeps its own
licence.

* `BCCard/pii-masking-openpii-finance` — CC BY 4.0
* `townboy/korean-pii-dataset` — CC BY 4.0

This repository does not relicense or redistribute the source datasets.
