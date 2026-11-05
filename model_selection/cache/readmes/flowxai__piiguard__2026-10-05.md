---
license: apache-2.0
library_name: onnx
pipeline_tag: text-classification
tags:
  - guardrails
  - onnx
  - multilingual
  - piiguard
language:
  - az
  - bg
  - cs
  - da
  - de
  - el
  - en
  - es
  - et
  - fi
  - fr
  - ga
  - hr
  - hu
  - it
  - lt
  - lv
  - mt
  - nl
  - pl
  - pt
  - ro
  - sk
  - sl
  - sv
  - tr
---

# piiguard[border]

The `piiguard` detector for [border](https://github.com/flowx-ai/border), an embeddable library that inspects the text going into and coming out of an LLM and returns a structured decision plus an audit-grade evidence record.

`flowxai/piiguard` on the hub. It is one detector of 28, and it is not a general purpose piiguard classifier: it was trained for this library's policy, is read at the operating point below, and reports through the evidence record rather than returning a bare score.

This card is generated from the evaluation and export artifacts of the training run, so every number on it is reproducible from this repository rather than asserted.

## What it is

- **Base model**: FacebookAI/xlm-roberta-base
- **Head**: token classification, BIO tags
- **Labels**: `O`, `B-PERSON`, `I-PERSON`, `B-EMAIL`, `I-EMAIL`, `B-PHONE`, `I-PHONE`, `B-NATIONAL_ID`, `I-NATIONAL_ID`, `B-IBAN`, `I-IBAN`, `B-CARD`, `I-CARD`, `B-DATE`, `I-DATE`, `B-LOCATION`, `I-LOCATION`
- **Artifact**: `onnx/model.fp16.onnx`, 555 MB, opset 17
- **Trained at**: 96 tokens

## Operating point

This head is read with argmax and has no threshold.

## How to use it

Through the library, which is what this model is for. It loads the artifact below, applies the operating point above, and returns a decision with an evidence record rather than a bare score.

```sh
pip install flowx-border
```

```yaml
# policy.yaml
policy_id: default
version: 1

detectors:
  piiguard:
    enabled: true
    on_fail: flag
```

```python
from flowx_border import load_policy, scan_input, scan_output

policy = load_policy("policy.yaml")

decision = scan_input(user_text, policy)
decision = scan_output(model_answer, policy)

print(decision.verdict)      # allow | flag | redact | block
print([f.label for f in decision.findings if f.detector_id == "piiguard"])
print(decision.evidence.record_id)
```

This detector reads the input and output side, so `scan_input` and `scan_output` is where it fires. It is T2, so it runs on the standard path and can be disabled per policy.

The weights are fetched once and cached, and a scan needs no network after that. Nothing here calls out to a hosted model, and the evidence record carries hashes rather than your text.

### Without the library

The artifact is plain ONNX, so it will load in `onnxruntime` directly. Two things you then own yourself, and they are the reason the library exists: the operating point above is not in the graph, and neither is the chunking. Inputs longer than the trained window have to be split and recombined, or the scores past it are extrapolation.

```python
import onnxruntime as ort
from huggingface_hub import hf_hub_download
from tokenizers import Tokenizer

repo = "flowxai/piiguard"
session = ort.InferenceSession(hf_hub_download(repo, "onnx/model.int8.onnx"))
tokenizer = Tokenizer.from_file(hf_hub_download(repo, "tokenizer.json"))
```

## Per entity

**Read this before the per-language table below.** The language axis asks whether a span was
found in a given language. It does not ask whether the right label was put on it, and label
assignment is where this model's failures are. Two were reported from a deployment in
September 2026, `Kubernetes` tagged `LOCATION` at 0.97 and a founding year tagged `IBAN` at
1.00, and neither could appear in a per-language score however carefully it was computed.

Measured by `border_train.heldout_ner_eval` on frames written to remove each type's habitual
neighbour, so it is deliberately harder than the training distribution: the generator always
puts a card after an IBAN and a person first, and this asks what happens when it does not.

| entity | F1 | precision | recall | gold spans | spurious | mislabelled | leaked tokens |
|---|---|---|---|---|---|---|---|
| `PERSON` | 1.0000 | 1.0000 | 1.0000 | 1040 | 0 | 0 | 0 |
| `EMAIL` | 1.0000 | 1.0000 | 1.0000 | 416 | 0 | 0 | 0 |
| `IBAN` | 1.0000 | 1.0000 | 1.0000 | 416 | 0 | 0 | 0 |
| `PHONE` | 1.0000 | 1.0000 | 1.0000 | 312 | 0 | 0 | 0 |
| `DATE` | 1.0000 | 1.0000 | 1.0000 | 208 | 0 | 0 | 0 |
| `CARD` | 0.8170 | 0.6906 | 1.0000 | 520 | 233 | 0 | 0 |
| `NATIONAL_ID` | 0.1429 | 1.0000 | 0.0769 | 208 | 0 | 151 | 0 |
| `LOCATION` | 0.0000 | 0.0000 | 1.0000 | **0** | 2 | 0 | 0 |

**`LOCATION` has zero gold spans in this harness, so it has never been scored.** It is the
newest of the eight types and the harness has no frames for it. An F1 of 0.0000 on a support
of 0 is not a score, it is a division by nothing, and the two spurious spans are the only
thing this row actually reports. Treat `LOCATION` as unevaluated.

**The last column is the one to keep, and it is zero throughout.** Not one sensitive token
went unredacted across any frame. `NATIONAL_ID` recalling 0.0769 means 151 of its 208 spans
came back under a different type's name, and `CARD`'s 0.6906 precision means a spurious span
on 192 of 520 rows. Both are wrong names on covered spans rather than text reaching a caller.
A redactor still removes the span; the evidence record gets the type wrong. If you depend on
the label rather than on the redaction, depend on the top five rows.

## Per language

Per language rather than an aggregate, because an aggregate across 26 languages hides the tail and the tail is the point.

**What this table is, stated plainly because 21 of its 26 rows read exactly 1.000.** It is the
corpus test split, drawn from the same generator as the training split, so a rule of the form
"the entity sits at position N of template T" is sufficient to score on it. It shows that no
language was starved of data. It is not evidence that the model is right about a given entity
in a given language, and a row reading 1.000 should be read as "this language was trained"
rather than as "this language is solved".

| Language | Support | P | R | F1 | Note |
|---|---|---|---|---|---|
| `az` Azerbaijani | 164 | 1.000 | 1.000 | 1.000 |  |
| `bg` Bulgarian | 180 | 1.000 | 1.000 | 1.000 |  |
| `da` Danish | 124 | 1.000 | 1.000 | 1.000 |  |
| `de` German | 212 | 1.000 | 1.000 | 1.000 |  |
| `el` Greek | 144 | 1.000 | 1.000 | 1.000 |  |
| `en` English | 180 | 1.000 | 1.000 | 1.000 |  |
| `es` Spanish | 180 | 1.000 | 1.000 | 1.000 |  |
| `et` Estonian | 188 | 1.000 | 1.000 | 1.000 |  |
| `fi` Finnish | 164 | 1.000 | 1.000 | 1.000 |  |
| `hr` Croatian | 152 | 1.000 | 1.000 | 1.000 |  |
| `hu` Hungarian | 224 | 1.000 | 1.000 | 1.000 |  |
| `lt` Lithuanian | 148 | 1.000 | 1.000 | 1.000 |  |
| `lv` Latvian | 156 | 1.000 | 1.000 | 1.000 |  |
| `mt` Maltese | 164 | 1.000 | 1.000 | 1.000 | not in base model pretraining |
| `nl` Dutch | 160 | 1.000 | 1.000 | 1.000 |  |
| `pl` Polish | 180 | 1.000 | 1.000 | 1.000 |  |
| `pt` Portuguese | 172 | 1.000 | 1.000 | 1.000 |  |
| `ro` Romanian | 192 | 1.000 | 1.000 | 1.000 |  |
| `sk` Slovak | 188 | 1.000 | 1.000 | 1.000 |  |
| `sl` Slovenian | 152 | 1.000 | 1.000 | 1.000 |  |
| `sv` Swedish | 132 | 1.000 | 1.000 | 1.000 |  |
| `tr` Turkish | 172 | 0.994 | 0.994 | 0.994 |  |
| `it` Italian | 172 | 0.988 | 0.988 | 0.988 |  |
| `cs` Czech | 164 | 0.976 | 1.000 | 0.988 |  |
| `ga` Irish | 160 | 0.976 | 1.000 | 0.988 |  |
| `fr` French | 148 | 0.987 | 0.987 | 0.987 |  |

### Weakest languages

Published rather than dropped. A coverage table with the bad rows removed is not a coverage table.

- `fr` French: F1 0.987
- `ga` Irish: F1 0.988
- `cs` Czech: F1 0.988

## Quantisation

The published artifact is fp16, halving every weight rather than quantising a subset. Used where INT8 moved decisions on this base model and fp16 did not.

For this artifact specifically: **0 of 300 decisions differ** from the fp32 checkpoint, read as `character spans`: 0 spans added and 0 characters no longer covered. A quantised model that answers differently is a different detector, so this is measured rather than assumed.

## Limitations

- **Synthetic training data.** Generated natively per language, never translated from English, so the sentence structure is the target language's own. It is still synthetic, and a production distribution will differ.
- **Maltese is absent from XLM-RoBERTa's pretraining set.** That is a fact about the base model, and it is not an explanation for a weak score. This card said "no amount of data fixes that" until 2026-08-14, which this project's own measurement disproves: the `nsfw` detector scored 0.000 in Maltese, was blamed on the base model, and went to 1.000 with perfect precision and recall when its corpus went from 2 positives per language to 10. Nothing about the model changed. So where a language scores badly here, read the support column first.
- **`LOCATION` is unevaluated.** It has zero gold spans in the held-out harness, so no number on this card describes it. See the per-entity table.
- **Two of the eight types are weak on label assignment.** `NATIONAL_ID` and `CARD`, both with zero leaked tokens, so the cost is a wrong type in the record rather than text reaching a caller.
- **This is not a compliance product.** It produces evidence about controls that were applied. It does not make anyone compliant with anything, and the obligations under the EU AI Act sit with the provider or deployer of a system, not with a model or a library.

## Licence

Apache-2.0, declared in the metadata above as well as here, so that a tool reading the repository can attest it rather than a human having to read prose.
