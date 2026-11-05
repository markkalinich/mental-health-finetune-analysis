---
license: mit
language:
  - en
  - ko
base_model: FacebookAI/xlm-roberta-base
pipeline_tag: token-classification
library_name: transformers
tags:
  - pii
  - privacy
  - redaction
  - named-entity-recognition
  - korean
  - bilingual
  - on-premises
---

# pii-xlmr-bilingual — EN/KO PII detection and redaction

A fine-tuned `xlm-roberta-base` span tagger that finds and redacts personal data in **English,
Korean, and code-switched text**, for seven entity types: `PER`, `RRN` (주민등록번호), `PHONE`,
`EMAIL`, `ADDRESS`, `CARD`, `ORG`.

Runs **on CPU at ~15.6 ms/sentence** and makes **no network calls at inference** — both enforced in
code and verified. Trains in ~28 minutes on one consumer GPU (measured on Apple M3 Pro / MPS).

Full training pipeline, evaluation harness, data card and design rationale:
**https://github.com/noczero/security-and-swe-agent-harness**

## Results

Exact-span F1 — a hit counts **only if both the entity type and the exact character boundaries
match**. This is the strict rule; overlap-based scoring reads much higher and is reported separately
in the repo.

| set | what it measures | micro-F1 |
| --- | --- | ---: |
| `gen` | held-out entity pools **and** held-out sentence frames | **0.9711** |
| `test` | a third partition, scored once, nothing tuned against it | **0.9804** |
| `switched` | EN–KO code-switched, held-out pools | **0.9161** |
| `real` | public corpus rows quarantined from training | **0.7356** |
| `dev` | shares pools *and* frames with training | 1.0000 ← *memorisation, not skill* |

`dev` is listed only so nobody can quote it as model quality. **The headline number is 0.9711.**

### Separately for English and Korean

| bucket | `gen` | `test` | `switched` | `real` |
| --- | ---: | ---: | ---: | ---: |
| **English** | **1.000** (235) | 1.000 (244) | — | **0.767** (811) |
| **Korean** | **0.965** (491) | 0.969 (490) | — | **0.707** (890) |
| code-switched | 0.946 (148) | 0.985 (132) | 0.916 (1200) | — |

Support (gold spans) in brackets. **Korean is the harder language** — it carries most of the
held-out spans and essentially all the residual error on synthetic text, because a Korean span must
stop before an attached particle (`김민수` inside `김민수는`).

### Against an off-the-shelf baseline

`fastino/gliner2-privacy-filter-PII-multi`, zero-shot, same sentences and same scorer:

| set | GLiNER2 (strict) | ours (strict) | GLiNER2 (relaxed) | ours (relaxed) |
| --- | ---: | ---: | ---: | ---: |
| `gen` | 0.6130 | **0.9711** | 0.9385 | 0.9904 |
| `switched` | 0.5083 | **0.9161** | 0.9698 | 0.9748 |
| `real` | 0.4778 | **0.7356** | 0.7808 | 0.8363 |

Read the relaxed columns first — they are the honest control. **Most of the advantage is boundaries,
not detection**: on `switched` both models find essentially the same entities, and the strict gap
comes from cutting them in the right place. Word-level span representations cannot express the gold
Korean span at all.

## Usage

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification

tok = AutoTokenizer.from_pretrained("noczero/pii-xlmr-bilingual")
model = AutoModelForTokenClassification.from_pretrained("noczero/pii-xlmr-bilingual")
```

**Use the repo's inference path rather than a naive decode.** Correct spans depend on two things
this model was built around:

- **NFC normalisation, never NFKC.** NFKC turns `㈜한국` from 3 characters into 5 and shifts every
  later offset.
- **Hangul pre-splitting to one tagging unit per syllable**, which raises the exact-span ceiling
  from 97.1% to 100%. Labels ride on units; offsets are *never* read from the tokenizer —
  trusting `return_offsets_mapping` here scored a correct model 0/6 in testing.

The repo ships this as one command:

```bash
python scripts/redact.py --weights <path-to-this-model> \
    --text "김철수는 010-2345-6789 로 연락 주세요"
```

```
김철수는 010-2345-6789 로 연락 주세요
  -> [PER]는 [PHONE] 로 연락 주세요
     [  0:3  ] PER      김철수
     [  5:18 ] PHONE    010-2345-6789
```

Output is the NFC-normalised text, zero or more **non-overlapping** spans with exact `[start, end)`
offsets, and a redacted copy. No confidence scores — the operating point is plain argmax.

## Training data

**Synthesised, not scraped.** Public Korean PII corpora with the entity types this task needs do not
exist at usable licence terms, so the training set is generated: 33,953 examples / 41,806 gold spans,
built from partitioned entity pools and sentence frames, plus real `PER`/`ORG` rows from **KLUE-NER**
and **Few-NERD** (both CC-BY-SA-4.0).

Two design choices carry most of the quality:

- **Type-agnostic frames.** The same sentence frames are shared verbatim across `RRN`, `PHONE` and
  `CARD`, so only a value's *structure* can assign its label — not a nearby cue word. The first
  model had learned "the number after 주민등록번호" and mislabelled 40 of 61 held-out RRNs as
  `PHONE`.
- **Confusable negatives.** Sentences with digits and no PII, deliberately RRN-shaped (order
  numbers). Nothing card-shaped — a Luhn-valid negative would teach the model to miss real cards.
  This, not frame widening, is what fixed RRN to 1.000 precision at 1.000 recall.

Full data card (composition, EN/KO balance, synthesis method, licences, failure modes):
[`DATA_CARD.md`](https://github.com/noczero/security-and-swe-agent-harness/blob/main/DATA_CARD.md).

## Limitations — read before deploying

1. **Real prose is much weaker than synthetic.** `real` is 0.7356, and **`ORG` is the weakest thing
   in the model** (P 0.621 / R 0.667). The strong numbers describe our generator's held-out sets;
   they are not a promise about arbitrary text.
2. **`real` is quarantined by row, not by entity.** A news corpus repeats the same people, so it
   shares 315 entity surfaces with training rows — it measures unseen *sentences* about partly-seen
   *entities*.
3. **`real` covers only `PER` and `ORG`.** The other five types have no real-text measurement at all.
4. **`test` is not calibrated to be as hard as `gen`** and reads slightly higher for that reason.
5. **Trailing digits are noise.** Training on MPS is not bitwise reproducible (max parameter delta
   9.96e-05 over 12 steps; a CPU control reproduces at 0.0). Inference *is* exactly reproducible.
6. **Recall-oriented balance.** For redaction a missed entity is a leak and a false positive is
   cosmetic, but the shipped operating point is plain argmax rather than a tuned threshold — see the
   design doc's precision/recall discussion.
7. **Not a compliance control.** This is a detection aid; it should not be the only thing standing
   between raw text and a disclosure.

## Licence and citation

MIT, following the `xlm-roberta-base` base model. Training corpora (KLUE-NER, Few-NERD) are
CC-BY-SA-4.0 and are cited in the data card.
