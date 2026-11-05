---
library_name: transformers
tags:
- router
- pii
- privacy
- korean
- edge-computing
- text-generation
pipeline_tag: text-generation
model_type: llama
language:
- ko
datasets:
- BCCard/pii-masking-openpii-finance
- townboy/korean-pii-dataset
- atonlee/Prompt-Routing-Dataset-ko
base_model:
- SupraLabs/Supra1.5-50M-Base-exp
license: apache-2.0
---

# supra-ko-pii-router · Korean PII Gate

A 51.8M-parameter model that reads one Korean sentence and answers one question:
does it contain personal data?

Used to decide whether text can go to the cloud or to an external LLM as-is, or has
to be inspected first.

This model does not locate personal data and does not mask it. For character spans
use [`atonlee/koelectra-ko-pii-ner`](https://huggingface.co/atonlee/koelectra-ko-pii-ner).

Personal data here means anything that identifies a person, on its own or in
combination with other data — names, phone numbers, email addresses, addresses,
dates of birth, account ids, resident registration numbers, passport numbers, card
numbers, bank account numbers, credentials. Dates, times, quantities, place names
and organisation names are not.

## Performance

On an in-house test split of 602 sentences. Accuracy 97.3%.

| | rows | Precision | Recall | F1 |
| --- | ---: | ---: | ---: | ---: |
| contains personal data | 401 | 96.8% | 99.3% | 98.0% |
| contains none | 201 | 98.4% | 93.5% | 95.9% |

Partially masked identifiers, the form text takes when copied off a screen or out of
a document, still count.

```text
990101-1******     PII
110-***-****90     PII
010-1234-****      PII
```

Sentences that name personal-data terms without containing any do not.

```text
"주민등록번호는 수집하지 않습니다"    none
"개인정보 처리방침을 확인해 주세요"   none
```

## Usage

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_ID = "atonlee/supra-ko-pii-router"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    dtype=torch.float32,
).eval()

PROMPT = "Task: [pii] {q}\nAnalysis:"
LABELS = ["none", "tier2", "tier1"]


def score(text):
    """Return one log-probability per label, in LABELS order."""
    prompt = tokenizer(
        PROMPT.format(q=text),
        return_tensors="pt",
        add_special_tokens=False,
        truncation=True,
        max_length=model.config.max_position_embeddings - 8,
    )["input_ids"]

    start = prompt.shape[1]
    scores = []

    with torch.no_grad():
        for label in LABELS:
            ids = tokenizer(
                " " + label,
                return_tensors="pt",
                add_special_tokens=False,
            )["input_ids"]

            # Score each label from the prompt alone. Sharing one KV cache across
            # the labels would leave the previous label in it.
            logits = model(
                input_ids=torch.cat([prompt, ids], dim=1),
                use_cache=False,
            ).logits[:, start - 1 : start + ids.shape[1] - 1]

            scores.append(
                torch.log_softmax(logits, -1)
                .gather(2, ids.unsqueeze(-1))
                .mean()
                .item()
            )

    return scores


def has_pii(text, margin=0.0):
    """True when the sentence contains personal data.

    Three labels are scored internally and `none` is the first of them. `margin`
    widens the answer toward yes: at 0.0 the highest score wins, above it `none`
    has to win by at least that much.
    """
    scores = score(text)
    ranked = sorted(range(len(LABELS)), key=lambda i: -scores[i])

    if ranked[0] != 0:
        return True

    return scores[0] - scores[ranked[1]] < margin
```

Example:

```python
texts = [
    "주민번호 900101-1234567로 조회해줘",
    "카드 5310-99**-****-1122 결제 취소해줘",
    "김민준 씨한테 010-1234-5678로 연락해줘",
    "서울시 강남구 테헤란로 152 3층으로 보내주세요",
    "이번 주말에 비 오려나",
    "회의 자료 정리하는 방법 알려줘",
]

for text in texts:
    print(f"{'PII ' if has_pii(text) else 'none'}  {text}")
```

```text
PII   주민번호 900101-1234567로 조회해줘
PII   카드 5310-99**-****-1122 결제 취소해줘
PII   김민준 씨한테 010-1234-5678로 연락해줘
PII   서울시 강남구 테헤란로 152 3층으로 보내주세요
none  이번 주말에 비 오려나
none  회의 자료 정리하는 방법 알려줘
```

The labels are scored and compared directly, so there is no generated string to
parse.

## Use with the span tagger

This model decides whether to look; it does not say where. Pair it with
[`atonlee/koelectra-ko-pii-ner`](https://huggingface.co/atonlee/koelectra-ko-pii-ner),
which returns character spans and decides what to do with each one.

```python
spans = tag(text) if has_pii(text, margin=1.2) else []
```

`margin` trades gate calls for coverage: at `0.0` the gate passes 43% of an in-house
87-request set to the tagger, at `1.2` it passes 78%. Raising it costs a tagger call,
which is a 14M model; lowering it risks text never being looked at.

## Training data

Training used public datasets and hand-written examples.

| source | licence | contribution |
| --- | --- | --- |
| [`BCCard/pii-masking-openpii-finance`](https://huggingface.co/datasets/BCCard/pii-masking-openpii-finance) | CC BY 4.0 | financial and administrative prose, personal-data examples |
| [`townboy/korean-pii-dataset`](https://huggingface.co/datasets/townboy/korean-pii-dataset) | CC BY 4.0 | Korean names, affiliations, form and roster text |
| [`atonlee/Prompt-Routing-Dataset-ko`](https://huggingface.co/datasets/atonlee/Prompt-Routing-Dataset-ko) | MIT | general queries as non-personal-data examples. Only the Korean prompt text was used; the routing labels were not |

The following were written for this model.

* masked identifiers
* partially revealed identifiers
* privacy-policy phrasing
* numbers shaped like identifiers but not personal data
* form and roster lines whose only personal data is a name

Neither the source datasets nor the merged training corpus is redistributed here.

The base model is [`SupraLabs/Supra1.5-50M-Base-exp`](https://huggingface.co/SupraLabs/Supra1.5-50M-Base-exp).

## Licence

Model weights: Apache-2.0

Inherited from the base model's Apache-2.0 licence.

Each external dataset used in training keeps its own licence.

* `BCCard/pii-masking-openpii-finance` — CC BY 4.0
* `townboy/korean-pii-dataset` — CC BY 4.0
* `atonlee/Prompt-Routing-Dataset-ko` — MIT, a Korean translation of `SupraLabs/Prompt-Routing-Dataset`

This repository does not relicense or redistribute the source datasets.
