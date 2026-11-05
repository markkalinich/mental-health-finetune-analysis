---
language:
- az
license: cc-by-nc-4.0
library_name: transformers
pipeline_tag: token-classification
base_model: LocalDoc/mmBERT-small-en-az
datasets:
- LocalDoc/pii_ner_azerbaijani_extended
tags:
- ner
- pii
- azerbaijani
- privacy
- anonymization
- modernbert
---

# PII NER Azerbaijani v4

Detection of personally identifiable information (PII) in Azerbaijani text: names, addresses, phone numbers,
documents, bank cards, dates. Built on [LocalDoc/mmBERT-small-en-az](https://huggingface.co/LocalDoc/mmBERT-small-en-az)
(ModernBERT, 69M parameters).

On [LocalDoc/pii_benchmark](https://huggingface.co/datasets/LocalDoc/pii_benchmark) (exact span match) v4 reaches
**strict F1 0.851** against 0.640 for [v3](https://huggingface.co/LocalDoc/pii-ner-azerbaijani-v3) used as documented.

> **Use the model with its post-processing** (`pii_ner.py` in this repository). Lowercasing, word-level decoding
> and suffix trimming are part of the result; the plain `transformers` token-classification pipeline gives
> noticeably worse spans.

## What is new compared to v3

- **Validated training data**: [LocalDoc/pii_ner_azerbaijani_extended](https://huggingface.co/datasets/LocalDoc/pii_ner_azerbaijani_extended)
  (current version; the annotations v3 was trained on are under the tag `v1`). Mis-placed spans, nonsense
  template values, missed dates / e-mails / times and truncated spans were fixed.
- **Robust to the way people actually write**: lowercase copies of the data, partial ASCII transliteration
  (`zehmət`, `həle`), all Azerbaijani cities and districts in all case forms (`Culfada`, `Siyezende`, `Şəkidən`).
- **Word-level decoding**: one label per word, spans are never cut in the middle of a word.
- **Azerbaijani morphology**: case suffixes are removed with a dictionary of names/cities plus learned rules
  (`Elçinin` → `Elçin`, `Eldənizi` → `Eldəniz`, `Bakıda` → `Bakı`), following the benchmark's core-span convention.
- **Rule-based filters**: Luhn checksum and 16-digit length for bank cards (tracking codes, IMEI), `10.45` after
  `saat` → TIME, code-like "names" (`ABJQXTLAH`) dropped.
- New label `DRIVERLICENSENUM`.

## Results

[LocalDoc/pii_benchmark](https://huggingface.co/datasets/LocalDoc/pii_benchmark), exact character-span match on
the core NER spans. The benchmark was split in two halves by a hash of `id`; one half was used to select the
checkpoint during training, **the numbers below are on the other half**, which was not used in any way.

| | Precision | Recall | Strict F1 | Macro F1 | Partial F1 | Hard-neg. FP rate | Neg. FP rate |
|---|---|---|---|---|---|---|---|
| **v4** | **0.8435** | **0.8581** | **0.8507** | **0.8543** | **0.8674** | **0.4000** | 0.2805 |
| v3 + v4 post-processing | 0.7928 | 0.7797 | 0.7862 | 0.7706 | 0.8048 | 0.4198 | 0.2950 |
| v3 as documented in its card | 0.6135 | 0.6682 | 0.6397 | 0.6234 | 0.7719 | 0.4198 | 0.2950 |

- *Partial F1*: label correct and spans overlap.
- *Hard-neg. FP rate*: share of hard-negative messages (order ids, tracking codes, prices, …) where anything
  was predicted. *Neg. FP rate*: the same over all messages without PII.
- *v3 + v4 post-processing*: the v3 weights with this repository's decoding and suffix trimming.
- On the full benchmark (both halves) v4 has strict F1 0.8501.
- Measured with word-level decoding and suffix trimming; the rule-based filters (Luhn, card length,
  time with a dot, code-like names) were added afterwards and are not included in these numbers.

F1 per entity (same half):

| entity | v4 | v3 + v4 post-processing | v3 as documented |
|---|---|---|---|
| EMAIL | 1.0000 | 0.9927 | 0.9542 |
| CITY | 0.9762 | 0.8048 | 0.2275 |
| SURNAME | 0.9730 | 0.9424 | 0.7897 |
| PASSPORTNUM | 0.9667 | 0.9333 | 0.8690 |
| AGE | 0.9302 | 0.8294 | 0.7958 |
| GIVENNAME | 0.8956 | 0.8259 | 0.6495 |
| IDCARDNUM | 0.8910 | 0.7885 | 0.7322 |
| TAXNUM | 0.8387 | 0.6617 | 0.4301 |
| CREDITCARDNUMBER | 0.8180 | 0.8782 | 0.8166 |
| ZIPCODE | 0.8023 | 0.8974 | 0.8762 |
| TELEPHONENUM | 0.7993 | 0.7985 | 0.7093 |
| TIME | 0.7823 | 0.8313 | 0.6480 |
| BUILDINGNUM | 0.7372 | 0.2642 | 0.0625 |
| DATE | 0.7100 | 0.6634 | 0.5749 |
| STREET | 0.6934 | 0.4472 | 0.2150 |

## Usage

```python
from huggingface_hub import snapshot_download
import sys

path = snapshot_download("LocalDoc/pii-ner-azerbaijani-v4")
sys.path.append(path)
from pii_ner import PiiNer

ner = PiiNer.from_pretrained(path)          # GPU if available

ner.predict("Elçinə zəng edin, Nigarın nömrəsi dəyişib: +994 70 555 12 34.")
# [{'label': 'GIVENNAME', 'text': 'Elçin', 'start': 0, 'end': 5, 'score': ...},
#  {'label': 'GIVENNAME', 'text': 'Nigar', ...},
#  {'label': 'TELEPHONENUM', 'text': '+994 70 555 12 34', ...}]

ner.anonymize("Salam, mən Rəşad Vəliyev. Sifarişim hələ çatmayıb, ünvan: Bakı şəhəri, Nizami küçəsi 45, "
              "mənzil 12. Əlaqə nömrəm 050 123 45 67.")
# 'Salam, mən [GIVENNAME] [SURNAME]. Sifarişim hələ çatmayıb, ünvan: [CITY] şəhəri, [STREET] [BUILDINGNUM],
#  mənzil [BUILDINGNUM]. Əlaqə nömrəm [TELEPHONENUM].'

ner.predict(["text 1", "text 2"])           # batches
```

Every entity is `{"label", "text", "start", "end", "score"}`; offsets refer to the original text (the input is
lowercased internally without changing its length).

Options of `PiiNer` / `PiiNer.from_pretrained`:

| option | default | meaning |
|---|---|---|
| `luhn_filter` | `True` | drop bank-card predictions that fail the Luhn checksum |
| `card_lengths` | `(16,)` | keep bank cards only with these digit counts (`None` = any) |
| `fix_time_dot` | `True` | `10.45`, `10.00`, `saat 11.05` predicted as DATE → TIME |
| `drop_code_names` | `True` | drop "names" that contain digits or are unknown all-caps words |
| `exclude_patterns` | `()` | regexes of your own non-PII formats (e.g. order numbers) |
| `postprocess` | `True` | `False` = raw model spans |

## Entities

`GIVENNAME`, `SURNAME`, `EMAIL`, `TELEPHONENUM`, `DATE`, `TIME`, `AGE`, `IDCARDNUM`, `PASSPORTNUM`, `TAXNUM`,
`CREDITCARDNUMBER`, `DRIVERLICENSENUM`, `CITY`, `STREET`, `BUILDINGNUM`, `ZIPCODE`.

`DRIVERLICENSENUM` is not part of the benchmark.

## How it works

1. The text is lowercased without changing its length (`İ` → `i`; Python's `str.lower()` would turn it into
   two characters and shift every offset after it).
2. The model labels sub-word tokens (BIO); long texts are processed in overlapping 512-token windows.
3. Every whitespace-separated word gets one label: it is an entity if any of its sub-words is predicted as one.
4. Punctuation and hyphen/apostrophe suffixes are cut (`AZ4144-dən`, `Nəsirli'nin`), then case suffixes:
   by the dictionary of names/cities (`lexicon.json`), and for unknown words by rules learned from the
   training data (`trim_rules_all.json`).
5. Rule-based filters (see the options).

## Training

- Base: `LocalDoc/mmBERT-small-en-az`, token classification, up to 3 epochs, AdamW (lr 1e-4, cosine schedule,
  5% warmup), bf16, batches of ~16K tokens, early stopping on strict F1 of the benchmark's selection half.
- Data: [LocalDoc/pii_ner_azerbaijani_extended](https://huggingface.co/datasets/LocalDoc/pii_ner_azerbaijani_extended)
  (531K rows: templates, 3 transliteration variants, LLM-generated PII, hard negatives and mixed sentences)
  plus augmentation: a lowercase copy of every cased text; 60K copies with cities replaced from the full list
  of Azerbaijani cities and districts (case suffixes re-inflected with vowel harmony, standard / ASCII / mixed
  spelling); 30% extra texts with partial ASCII transliteration. Person names directly in front of a street
  word were merged into the STREET span.

## Limitations

- **Structured identifiers in a non-PII role** are still the main source of false positives: order numbers,
  tracking and request numbers can be tagged as tax numbers, phones or dates. If your system has fixed
  formats for such numbers, pass them as `exclude_patterns`.
- Words that are also first names (`bahadır` "expensive", `aydın` "clear", `səhər` "morning") may be tagged
  as GIVENNAME.
- Dates written with month names (`16 oktyabr 2026`) are often missed.
- Azerbaijani (Latin script) and English only; Russian/Cyrillic text is not supported.
- Trained and evaluated on synthetic data; check it on your own traffic before relying on it.

## Citation

```bibtex
@misc{pii-ner-azerbaijani-v4,
  title     = {PII NER Azerbaijani v4},
  author    = {LocalDoc},
  year      = {2026},
  publisher = {Hugging Face},
  url       = {https://huggingface.co/LocalDoc/pii-ner-azerbaijani-v4}
}
```