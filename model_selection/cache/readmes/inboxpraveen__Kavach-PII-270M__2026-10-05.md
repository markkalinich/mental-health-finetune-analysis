---
license: gemma
base_model: google/gemma-3-270m-it
library_name: transformers
pipeline_tag: text-generation
tags:
  - pii
  - pii-detection
  - privacy
  - redaction
  - anonymization
  - ner
  - token-classification
  - gdpr
  - hipaa
  - multilingual
  - gemma3
language:
  - en
  - hi
  - ta
  - te
  - bn
  - mr
  - gu
  - kn
  - ml
  - pa
  - ur
  - ar
  - zh
  - ja
  - ko
  - ru
  - tr
  - vi
  - id
  - es
  - fr
  - de
  - it
  - pt
  - nl
  - pl
---

# Kavach PII 270M

A 270M parameter model that finds personal data in 29 languages. This is version 3. On a held-out test set of 4,577 documents it scores 92.0 value-F1, where GLiNER-PII scores 59.3 and Microsoft Presidio scores 29.5, measured with the same script against the same gold annotations. On 480 documents built entirely by code in eight real-world formats, which share nothing with the training data generator, it scores 90.4.

*Kavach* (कवच) is Sanskrit for "armour". The model reads a document and returns the personal data it contains as a JSON list. It runs on a laptop GPU or on CPU, and it was built for the inputs real pipelines actually receive: call-centre ASR transcripts, scanned OCR output, bank statements and CSV exports, forms, chat, code, logs, and deliberately obfuscated text.

![Comparison against v2, GLiNER, Presidio and regex baselines](assets/01-headline-comparison.png)

| | Kavach v3 | Kavach v2 | GLiNER-PII multi-v1 | Presidio | Regex + checksum |
|---|---|---|---|---|---|
| **Value F1** | **92.0** | 79.0 | 59.3 | 29.5 | 30.3 |
| Precision | **92.0** | 86.8 | 67.1 | 30.3 | 66.0 |
| Recall | **92.1** | 72.5 | 53.1 | 28.7 | 19.6 |
| Exact span F1 | **92.5** | 80.1 | 57.8 | 29.5 | 29.1 |
| Redaction recall | **96.0** | 82.2 | 61.1 | 48.9 | 23.9 |
| **False positives on PII-free documents** | 12.5% | **2.0%** | 77.7% | 83.4% | 23.9% |

Test set: 4,577 held-out documents with 28,672 labelled values, 440 of them free of personal data. It is 3,347 documents from the v2 test set with repaired labels, plus 1,230 new held-out documents. The v2 column is v2's own predictions, re-scored on this gold, not a number copied from the old card. Label sets of the other systems were mapped to ours on a best-effort basis; see [Fair comparison notes](#fair-comparison-notes).

The last row is the one place where v3 is worse than v2, and it matters for redaction pipelines. Presidio flags something in 83% of documents that contain no personal data and GLiNER in 78%. v2 did so in 2.0%, and v3 does so in 12.5%. Most of v3's cases (35 of the 55 documents) are nothing but a date or a reference number in a document about nobody: an expiry date on a product notice, an order reference in a shipping log. A date or a case number is personal data only when it belongs to someone's record, and v3 learnt to tag them eagerly from dense bank statements and forms. If over-masking such documents is a problem for you, drop the result when the only labels found are dates and case numbers:

```python
if {s["label"] for s in result["spans"]} <= {"DATE_TIME", "CASE_ID"}:
    result["spans"] = []
```

On the test set that brings the rate from 12.5% to 4.5%, at a cost of 0.5 F1, because some real records contain nothing else (an appointment reminder with a booking reference, for example).

## What's new in v3

v3 is the same model size, the same base model and the same training recipe as v2; only the augmentation rate changed. What changed is the data: every label in the old corpus was re-checked, 23,434 new training documents were added, and the label set was simplified from 52 labels to 43. The table below scores both models on the same documents against the same gold at every step, so each step isolates one change.

![v3 against v2 on every evaluation set](assets/02-v2-vs-v3.png)

| Evaluation set | Documents | Kavach v2 | Kavach v3 | Change |
|---|---|---|---|---|
| v2 test documents, original v2 gold | 3,347 | **89.1** | 84.7 | -4.4 |
| same documents, repaired gold, only values the old gold also had | 3,347 | 90.6 | **92.2** | +1.6 |
| same documents, repaired v3 gold | 3,347 | 84.3 | **91.4** | +7.1 |
| new v3 test documents only | 1,230 | 72.7 | **92.8** | +20.1 |
| full v3 test | 4,577 | 79.1 | **92.1** | +13.0 |
| hard cases, second-reader checked gold | 435 | 50.4 | **83.7** | +33.3 |
| production probe, built by code | 480 | 72.3 | **90.4** | +18.1 |
| simulated ASR rewrites | 289 | 87.0 | **89.5** | +2.5 |
| real render-to-Tesseract OCR | 250 | 80.4 | **84.5** | +4.1 |
| PII embedded in real Wikipedia text | 300 | 79.4 | **83.9** | +4.5 |

Reading it from the top:

* **v2's card reported 88.4 on its own test set, and that gold was missing roughly one value in ten.** Re-annotating the 65,000 v2 documents found the gaps, mostly names in form fields and signature lines, repeated and partial mentions, and organisation names. Against the repaired gold, v2 scores 84.3 on its own test documents and v3 scores 91.4.
* **The first row is the one to read carefully.** On the original v2 gold, v3 scores lower than v2. Its recall there is higher than v2's (90.8 against 88.7), but its precision is 79.4, because it finds 3,181 values the old gold does not contain. 1,982 of them (62%) are in the repaired gold with the same label, and most of the rest are values whose rules changed in v3 (see [Migrating from v2](#migrating-from-v2)).
* **The second row is the like-for-like number.** It keeps only the values the old gold also had, so neither model is rewarded or penalised for the new rules. v3 is 1.6 points ahead there.
* **The new test documents** come from the same generator as 17,942 of v3's training documents, a style v2 never saw, so part of the 20-point gap there is familiarity. The production probe is the check against that: it was built by code, not by a language model, and v3 leads by 18 points on it.
* **The hard cases** are the error types v2 was worst at, written deliberately (see [Hard cases](#hard-cases)).

What went into the new training data:

| | Documents |
|---|---|
| Dense records with 15 to 40 values: bank statements, CSV exports, logs, KYC forms, claims | 5,795 |
| Long documents of 200 to 500 words: email threads, transcripts, reports | 3,104 |
| Rare labels in natural context | 2,223 |
| Weak languages: Indic scripts, romanised and code-mixed text | 3,028 |
| Hard negatives: few or no values among non-personal look-alikes | 2,354 |
| Noisy values: typos, OCR confusions, look-alike letters, zero-width characters | 1,438 |
| Hard cases, one per error type v2 made most often (see below) | 5,492 |

See [Dataset](#dataset) for how the labels were checked.

## Migrating from v2

v3 is a drop-in replacement with one breaking change: **the label list is shorter**. v3 was trained with 43 labels, and the label list is part of the prompt, so code that still sends the v2 list of 52 is sending a prompt the model never saw. Replace `LABELS` with the list in the Quick start below. Nothing else in the prompt changed.

Eleven v2 labels were folded into broader ones, and two new ones (`BANK_CODE`, `PAYMENT_ID`) take their place. Most of the folded labels were identifier types that cannot be told apart without a cue word: a bare 12-digit number can be an Aadhaar, a tax ID or an account number, v2 lost points guessing between them, and a redaction pipeline treats them all the same way. `SIGNATURE` was usually the same string as the person's name, which value-only output cannot separate, and `POSTAL_CODE` was v2's weakest label at 33.8 F1.

| v2 label | v3 label |
|---|---|
| `SSN_US`, `AADHAAR_IN`, `PAN_IN`, `TAX_ID` | `NATIONAL_ID` |
| `IBAN` | `BANK_ACCOUNT` |
| `SWIFT_BIC`, `ROUTING_CODE` | `BANK_CODE` |
| `UPI_VPA`, `WALLET_ID` | `PAYMENT_ID` |
| `POSTAL_CODE` | `ADDRESS` (a standalone postcode is still tagged) |
| `SIGNATURE` | `PERSON` |

What gets tagged also changed in a few places, so a v3 output is not always a relabelled v2 output:

* **Specific dates only.** `DATE_TIME` needs a day of the month, a year or a clock time. "Yesterday", "last Tuesday" and "March" on their own are no longer tagged, and neither are log timestamps, build dates, public-event dates or business hours.
* **Places are not addresses.** A city, state or country on its own is not an `ADDRESS`, and neither is an organisation's public address in a letterhead or footer.
* **Public contacts are not personal data.** Toll-free helplines and generic mailboxes (`support@`, `info@`, `noreply@`) are not tagged. A named person's direct line and email still are.
* **Realistic values inside code, logs and JSON are tagged**, because customer data pasted into a stack trace is still customer data. Obvious placeholders (`test@example.com`, `555-0100`, `John Doe`, `123-45-6789`) are not.
* **Honorifics and cue words stay outside the value**, in every script: `Mr Rao`, `Rao sir`, `Yamada-san` and `गवळी सर` all tag the name alone, and `MRN 77123` tags `77123`.

If you ran v2 with `max_new_tokens=768`, raise it to 1024. v3 was trained on dense records (bank statements, CSV exports, KYC forms) whose answer can run past 768 tokens.

## Quick start

```python
import json
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL = "inboxpraveen/Kavach-PII-270M"
tok = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForCausalLM.from_pretrained(MODEL, dtype="bfloat16").to("cuda").eval()

LABELS = ["ADDRESS","AGE","API_KEY_TOKEN","BANK_ACCOUNT","BANK_CODE","BIOMETRIC_DESCRIPTOR","CARD_CVV","CARD_EXPIRY",
"CASE_ID","CREDIT_DEBIT_CARD","DATE_TIME","DEVICE_ID","DISABILITY","DOB","DRIVING_LICENSE","EMAIL","EMPLOYEE_ID",
"ETHNICITY","GENDER_SEX","GEO_LOCATION","HEALTH_ID","INSURANCE_ID","IP_ADDRESS","LAB_ORDER_ID","LICENSE_PLATE",
"MAC_ADDRESS","MEDICAL_RECORD_ID","NATIONAL_ID","ORGANIZATION","PASSPORT","PASSWORD_SECRET","PAYMENT_ID","PERSON",
"PHONE","POLITICAL_BELIEF","PRESCRIPTION_ID","RELIGION","STUDENT_ID","TRANSACTION_ID","URL_PERSONAL","USERNAME","VIN",
"VOTER_ID"]

INSTRUCTION = (
    "Extract all personal data (PII/PHI/PCI) from the text.\n"
    "Labels: " + ", ".join(LABELS) + "\n"
    'Return ONLY a JSON array of objects {"label": ..., "text": ...}. Copy each value EXACTLY as it appears in the '
    "text (same characters, spacing and spelling; for spoken values copy from the first to the last spoken token). "
    "List each distinct (label, value) pair once, in order of first appearance. "
    "If the text contains no personal data, return []."
)

def extract(text):
    msgs = [{"role": "user", "content": f"{INSTRUCTION}\n\nText:\n<<<\n{text}\n>>>"}]
    prompt = tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
    ids = tok(prompt, return_tensors="pt", add_special_tokens=False).to(model.device)
    out = model.generate(**ids, max_new_tokens=1024, do_sample=False)
    raw = tok.decode(out[0][ids["input_ids"].shape[1]:], skip_special_tokens=True)
    return json.loads(raw[raw.find("["): raw.rfind("]") + 1])

print(extract("Hi, this is Derek Okafor from Meridian Bank, my number is +1-617-555-0142."))
# [{"label": "PERSON", "text": "Derek Okafor"},
#  {"label": "ORGANIZATION", "text": "Meridian Bank"},
#  {"label": "PHONE", "text": "+1-617-555-0142"}]

print(extract("Please call our helpline 1800-266-1234 or write to support@meridianbank.com. "
              "Your case CK-80691 is with Priya Nair, priya.nair@gmail.com."))
# [{"label": "CASE_ID", "text": "CK-80691"},
#  {"label": "PERSON", "text": "Priya Nair"},
#  {"label": "EMAIL", "text": "priya.nair@gmail.com"}]
# The helpline and the support mailbox are public contacts, not personal data.
```

## Serving

All three servers below expose an OpenAI-compatible `/v1/chat/completions` endpoint, so the same client code works against any of them. Send the instruction as a single user turn, exactly as in the Quick start above. Use `temperature: 0`.

### vLLM

```bash
pip install vllm

vllm serve inboxpraveen/Kavach-PII-270M \
    --dtype bfloat16 \
    --max-model-len 4096 \
    --port 8000
```

To serve the LoRA adapter on top of the stock base model instead of the merged weights:

```bash
vllm serve google/gemma-3-270m-it \
    --enable-lora \
    --lora-modules kavach=inboxpraveen/Kavach-PII-270M/adapter \
    --dtype bfloat16 --max-model-len 4096 --port 8000
```

### SGLang

```bash
pip install "sglang[all]"

python -m sglang.launch_server \
    --model-path inboxpraveen/Kavach-PII-270M \
    --dtype bfloat16 \
    --context-length 4096 \
    --port 30000
```

### Client for either server

```python
import json
from openai import OpenAI

client = OpenAI(base_url="http://127.0.0.1:8000/v1", api_key="EMPTY")   # 30000 for SGLang

def extract(text):
    r = client.chat.completions.create(
        model="inboxpraveen/Kavach-PII-270M",
        messages=[{"role": "user", "content": f"{INSTRUCTION}\n\nText:\n<<<\n{text}\n>>>"}],
        temperature=0, max_tokens=1024,
    )
    raw = r.choices[0].message.content
    return json.loads(raw[raw.find("["): raw.rfind("]") + 1])
```

Batching is worth setting up. Documents are independent, most answers are short (the median test answer is 88 tokens), and both servers handle concurrent requests well. The accuracy figures in this card were produced with the `transformers` path and with llama.cpp; vLLM and SGLang use the same weights and the same greedy decoding, so results should match, but they were not separately benchmarked.

### llama.cpp, Ollama, LM Studio

See [Kavach-PII-270M-GGUF](https://huggingface.co/inboxpraveen/Kavach-PII-270M-GGUF) for quantised builds down to 169 MB.

## Long inputs, transcripts and character offsets

The model does not predict character positions. It returns values, and you find them in the source text afterwards. That removes the one thing a generative model reliably gets wrong: asked to emit indices, it produces plausible looking numbers that are simply incorrect. Asked to copy a value, it copies it, and a value it invents cannot be found, so hallucinations become detectable instead of silent.

[`kavach_extract.py`](kavach_extract.py) in this repository does the whole job in one function: it splits long text into overlapping windows, calls the model on each, locates every returned value in the original string, merges the windows and hands back character offsets. It has no dependencies beyond the standard library, and you supply the model call.

```python
from kavach_extract import extract_pii, redact, transformers_generate

gen = transformers_generate(model, tok)          # or openai_generate(...) for vLLM, SGLang, llama-server

result = extract_pii(transcript, gen)
for s in result["spans"]:
    print(s["start"], s["end"], s["label"], repr(s["text"]))

print(redact(transcript, result["spans"]))       # 'Hi, this is [PERSON] from [ORGANIZATION]...'
print(result["unlocatable"])                     # values the model invented; should be near empty
print(result["warnings"])                        # empty list means a clean run
```

It is written to survive real input: `None`, bytes, a number, an empty string, a model call that raises, and output that is not valid JSON are all handled and reported in `result["warnings"]` rather than raised. Running the file directly (`python kavach_extract.py`) runs its self-test, which needs no GPU and no model. Both back-ends are tested end to end on v3: `transformers` locally and `openai_generate` against a live `llama-server`.

### Window size

The defaults below are measured, not reasoned about. v3 saw longer documents in training than v2 did (a median of 49 words against 39, and 3,265 training documents over 200 words), and it shows: window size matters less than it did for v2, but past a certain length it still matters.

**On a coherent document, window size barely matters.** These are 92 real test documents of 180 to 385 words, scored against their own gold:

| | Precision | Recall | Value F1 |
| --- | --- | --- | --- |
| Whole document, one call | 0.893 | 0.895 | 0.894 |
| Windowed 250 / 40 | 0.875 | 0.911 | 0.893 |
| Windowed 180 / 35 | 0.873 | 0.923 | **0.897** |
| Windowed 150 / 30 | 0.874 | 0.920 | 0.896 |
| Windowed 120 / 25 | 0.869 | 0.926 | 0.896 |
| Windowed 100 / 20 | 0.866 | 0.920 | 0.892 |
| Windowed 50 / 12 | 0.858 | 0.926 | 0.891 |

Every setting lands between 0.891 and 0.897. Smaller windows trade a little precision for recall, because the model needs the surrounding sentence to tell a date of birth from an appointment date, or a patient from a clinician, and a small window takes some of that away. At 50 words v2 lost 13 points of precision; v3 loses 3.5.

**On text that runs past a few hundred words, recall falls away.** These are eight documents of 670 to 760 words, each built by stitching unrelated test documents together, which is the harder case:

| Window / overlap | Precision | Recall | Value F1 | Model calls |
| --- | --- | --- | --- | --- |
| 30 / 8 | 0.866 | 0.886 | 0.876 | 261 |
| 50 / 12 | 0.893 | 0.896 | 0.894 | 150 |
| 100 / 20 | 0.906 | 0.915 | **0.911** | 73 |
| 120 / 25 | 0.902 | 0.906 | 0.904 | 61 |
| 150 / 30 | 0.895 | 0.904 | 0.899 | 49 |
| 180 / 35 | 0.897 | 0.869 | 0.883 | 42 |
| 200 / 40 | 0.883 | 0.842 | 0.862 | 38 |
| 250 / 40 | 0.877 | 0.773 | 0.822 | 32 |
| 400 / 80 | 0.879 | 0.642 | 0.742 | 19 |

Precision holds up to 400 words; recall does not. A single answer stops short of listing everything in a long, dense input, so one 400-word window finds only 64% of the values. Sending each source document on its own scores 0.901, which is the ceiling any windowing scheme is working towards; the rows from 100 to 150 words reach it or come within 0.002 (the small excess above it is noise on eight documents). v3 degrades more gently than v2 (0.742 against 0.635 at 400 words), but the shape is the same.

**The default is 120 words with 25 of overlap**, near the top of both tables; 100 to 150 behaves about the same. Do not go past about 180 words, where recall starts to fall. Keep the overlap at 20 or more, or a long address can straddle an edge and be seen whole by neither window. If your input is always coherent prose rather than concatenated records, the choice barely matters.

These runs used the F16 GGUF build through `llama-server`. On the coherent set, the `transformers` path gave the same scores to within 0.002.

A document shorter than the window is sent in one call untouched, so ordinary short inputs never pay the windowing cost at all.

One note on throughput: `extract_pii` batches the windows of a single document together. If you are processing many documents, run several `extract_pii` calls concurrently rather than relying on that internal batching, or the GPU will sit mostly idle.

### Speech-to-text input

Transcripts work as they come out of the recogniser. Bracketed timestamps (`[00:01:02]`), SRT ranges (`00:00:03,500 --> 00:00:07,120`), WebVTT cues and plain `Speaker 1:` turns pass through untouched, and the timestamps survive redaction. This is not special-case code: 1,068 training documents contain bracketed timestamps and only one of them tags any, so the model learned to ignore them. Measured on v3 with the 30 longest timestamped test documents: none of their 419 timestamps was tagged as personal data, all 419 survived redaction intact, and every returned offset indexed the original string exactly. Where the transcript has line breaks, window edges prefer to land on one, so a speaker turn stays whole; a transcript that arrives as one unbroken line is cut on word boundaries instead.

```
[00:00:03] Speaker 1: Hello, this is [PERSON] from [ORGANIZATION].
[00:00:09] Speaker 2: Hi [PERSON]. My parcel is [CASE_ID] and my mobile is [PHONE].
```

### Locating values correctly

Matching is stricter than a plain substring search, which matters more than it sounds. A naive `re.escape` locator places values inside longer words: `Raj` lands in the middle of `Rajesh`, `2024` inside `20245`, and redaction then emits `[PERSON]esh`. `extract_pii` requires a whole-word match, with the boundary rule switched off for Chinese, Japanese, Thai, Khmer, Burmese and Korean, where words are not space-separated or particles attach directly to the noun. Indic and Arabic combining marks count as part of the word, which is the bug that a plain `\b` has against Devanagari.

Where a value occurs nowhere as a whole word, usually because the recogniser ran two words together, the span is still produced and flagged `"partial": True`, on the grounds that a mask starting mid-word beats leaving a real address in the clear. Drop those spans if you would rather under-mask.

On the 4,577-document test set:

| Outcome | Share of 28,712 predicted values |
| --- | --- |
| Located as a whole word | 98.79% |
| Located only inside a longer run, flagged `partial` | 0.41% |
| Not present in the text at all (hallucination) | 0.79% |

On the same test set, 1.8% of v2's predicted values could not be found in the text.

<details>
<summary>Full source of <code>kavach_extract.py</code></summary>

```python
"""
Kavach PII 270M: one self-contained extraction function.

Copy this file, or just the two public functions, into your project. It has no dependencies beyond the standard
library; you supply the model call.

    from kavach_extract import extract_pii, redact

    result = extract_pii(text, generate)     # `generate` defined below for your runtime
    print(result["spans"])                   # [{'start': 12, 'end': 24, 'label': 'PERSON', 'text': 'Derek Okafor'}, ...]
    print(redact(text, result["spans"]))     # 'Hi, this is [PERSON] from [ORGANIZATION]...'

What it handles
    * Input of any length. Text longer than one window is split into overlapping word windows, each sent
      separately, and the results merged back onto the original string with correct offsets.
    * Speech-to-text output with timestamps: '[00:01:02] Speaker 1: ...', '00:00:03,500 --> 00:00:07,120',
      WebVTT cues and plain 'Speaker 1:' turns. Where the transcript has line breaks, windows prefer to cut on
      one, so a speaker turn or a subtitle cue stays whole; a transcript that arrives as a single unbroken line
      is simply cut on word boundaries. Timestamps are never treated as personal data, because the model was
      trained that way: 1,068 training documents contain bracketed timestamps and only one tags them.
    * Values repeated across the document. A name found once is masked at every occurrence.
    * Bad input: None, bytes, numbers, empty or whitespace-only strings, and model calls that fail or return
      something that is not JSON. Nothing raises; problems are reported in result["warnings"].

Window defaults are measured, not guessed, and they are a compromise between two opposite failures.

Too small and precision goes: on 92 real test documents of 180-385 words, a 50-word window scores 0.858
precision against 0.893 for the same documents sent whole, because the model needs the surrounding sentence to
tell a date of birth from an appointment date. Too large and recall goes: on 660-word inputs, recall falls from
0.92 at a 100-word window to 0.64 at 400, because a single answer stops short of listing everything in a long,
dense input.

120 words with 25 of overlap is near the top of both curves; 100 to 150 behaves about the same. Do not drop
below about 60, and do not go past about 180. Keep the overlap at 20 or more, or a long address can straddle an
edge and be seen whole by neither window. A document shorter than the window is sent in one call untouched.
"""

from __future__ import annotations

import json
import re
import unicodedata

__all__ = ["extract_pii", "redact", "LABELS", "INSTRUCTION", "build_prompt"]

LABELS = [
    "ADDRESS", "AGE", "API_KEY_TOKEN", "BANK_ACCOUNT", "BANK_CODE", "BIOMETRIC_DESCRIPTOR", "CARD_CVV",
    "CARD_EXPIRY", "CASE_ID", "CREDIT_DEBIT_CARD", "DATE_TIME", "DEVICE_ID", "DISABILITY", "DOB", "DRIVING_LICENSE",
    "EMAIL", "EMPLOYEE_ID", "ETHNICITY", "GENDER_SEX", "GEO_LOCATION", "HEALTH_ID", "INSURANCE_ID", "IP_ADDRESS",
    "LAB_ORDER_ID", "LICENSE_PLATE", "MAC_ADDRESS", "MEDICAL_RECORD_ID", "NATIONAL_ID", "ORGANIZATION", "PASSPORT",
    "PASSWORD_SECRET", "PAYMENT_ID", "PERSON", "PHONE", "POLITICAL_BELIEF", "PRESCRIPTION_ID", "RELIGION",
    "STUDENT_ID", "TRANSACTION_ID", "URL_PERSONAL", "USERNAME", "VIN", "VOTER_ID",
]

INSTRUCTION = (
    "Extract all personal data (PII/PHI/PCI) from the text.\n"
    "Labels: " + ", ".join(LABELS) + "\n"
    'Return ONLY a JSON array of objects {"label": ..., "text": ...}. Copy each value EXACTLY as it appears in '
    "the text (same characters, spacing and spelling; for spoken values copy from the first to the last spoken "
    "token). List each distinct (label, value) pair once, in order of first appearance. "
    "If the text contains no personal data, return []."
)


def build_prompt(chunk: str) -> str:
    """The user turn the model expects. Pass this through your tokenizer's chat template."""
    return f"{INSTRUCTION}\n\nText:\n<<<\n{chunk}\n>>>"


# --------------------------------------------------------------------------------------------------
# input hygiene

_CONTROL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")


def _as_text(value) -> tuple[str, list[str]]:
    """Coerce anything reasonable to a string without raising. Returns (text, warnings)."""
    warnings: list[str] = []
    if value is None:
        return "", ["input was None"]
    if isinstance(value, bytes):
        value = value.decode("utf-8", errors="replace")
        warnings.append("input was bytes, decoded as utf-8 with replacement")
    elif not isinstance(value, str):
        warnings.append(f"input was {type(value).__name__}, coerced with str()")
        value = str(value)
    if "�" in value:
        warnings.append("input contains U+FFFD replacement characters, upstream decoding may be wrong")
    cleaned = _CONTROL.sub(" ", value)
    if cleaned != value:
        warnings.append("control characters replaced with spaces")
    return cleaned, warnings


# --------------------------------------------------------------------------------------------------
# chunking

_WORD = re.compile(r"\S+")
# Places a transcript can be cut without splitting a turn: a newline, or the end of a subtitle cue.
_LINE_BREAK = re.compile(r"\n")


def _windows(text: str, window_words: int, overlap_words: int, snap: float = 0.25):
    """Yield (char_start, char_end) windows over `text`.

    Windows are built on word boundaries so a timestamp token such as '[00:01:02]' is never split. Where a
    newline sits near the computed edge, the edge snaps to it, which keeps one speaker turn or one subtitle
    cue inside a single window.
    """
    words = [(m.start(), m.end()) for m in _WORD.finditer(text)]
    n = len(words)
    if n == 0:
        return
    if n <= window_words:
        yield words[0][0], words[-1][1]
        return

    slack = max(1, int(window_words * snap))
    i = 0
    while i < n:
        j = min(i + window_words, n)
        start, end = words[i][0], words[j - 1][1]

        # Snap the trailing edge to the nearest newline within `slack` words, so a speaker turn or a
        # subtitle cue stays whole.
        if j < n:
            lo = words[max(i + 1, j - slack) - 1][1]
            hi = words[min(n, j + slack) - 1][1]
            nl = [m.end() for m in _LINE_BREAK.finditer(text, lo, hi)]
            if nl:
                end = min(nl, key=lambda p: abs(p - end))

        yield start, end
        if end >= words[-1][1]:
            return

        # First word not yet covered, then step back `overlap_words` so the next window re-reads context.
        # Scan from i, not j: a backward snap leaves words before j still uncovered, and starting at j
        # would step the next window past them.
        k = i
        while k < n and words[k][0] < end:
            k += 1
        i = max(i + 1, k - overlap_words)


# --------------------------------------------------------------------------------------------------
# output parsing

_OBJ = re.compile(r'\{\s*"label"\s*:\s*"((?:[^"\\]|\\.)*)"\s*,\s*"text"\s*:\s*"((?:[^"\\]|\\.)*)"\s*\}', re.S)


def _unescape(v: str) -> str:
    try:
        return json.loads('"' + v + '"')
    except json.JSONDecodeError:
        return re.sub(r'\\(["\\/])', r"\1", v).replace("\\n", "\n").replace("\\t", "\t")


def _parse(raw, labels: set[str]) -> tuple[list[dict], bool]:
    """Model text to entities. Tolerates code fences, prose around the array and trailing commas."""
    if not isinstance(raw, str) or not raw.strip():
        return [], False
    s = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw.strip(), flags=re.S).strip()
    if s == "[]":
        return [], True
    a, b = s.find("["), s.rfind("]")
    cand = s[a:b + 1] if a != -1 and b > a else s
    ok = True
    try:
        items = json.loads(cand)
    except json.JSONDecodeError:
        try:
            items = json.loads(re.sub(r",\s*([\]}])", r"\1", cand))
        except json.JSONDecodeError:
            ok = False
            items = [{"label": m.group(1), "text": _unescape(m.group(2))} for m in _OBJ.finditer(s)]
    if not isinstance(items, list):
        return [], False
    out, seen = [], set()
    for e in items:
        if not isinstance(e, dict):
            ok = False
            continue
        lab, val = e.get("label"), e.get("text")
        if not isinstance(lab, str) or not isinstance(val, str):
            ok = False
            continue
        lab, val = lab.strip().upper(), val.strip()
        if lab in labels and val and (lab, val) not in seen:
            seen.add((lab, val))
            out.append({"label": lab, "text": val})
    return out, ok


# --------------------------------------------------------------------------------------------------
# locating values back in the source text

_ZW = "​‌‍⁠﻿"
_GAP = r"[\s" + _ZW + r"]*"


def _flex(value: str):
    """The value's non-blank characters in order, tolerating any whitespace or zero-width run between them.
    Finds values that the source spreads over a line break or salts with invisible characters."""
    chars = [c for c in value if not c.isspace() and c not in _ZW]
    if len(chars) < 3:
        return None
    return _GAP.join(re.escape(c) for c in chars)


# Scripts where a boundary test cannot work, so it is not applied: Chinese, Japanese, Thai, Lao, Khmer and
# Burmese put no space between words, and Korean attaches its particles straight onto the noun, so the
# character after a name is almost always another letter of the same sentence.
def _unspaced(ch: str) -> bool:
    o = ord(ch)
    return (0x1100 <= o <= 0x11FF or 0x3040 <= o <= 0x30FF or 0x3130 <= o <= 0x318F
            or 0x3400 <= o <= 0x4DBF or 0x4E00 <= o <= 0x9FFF or 0xAC00 <= o <= 0xD7AF
            or 0xF900 <= o <= 0xFAFF or 0x0E00 <= o <= 0x0EFF or 0x1780 <= o <= 0x17FF
            or 0x1000 <= o <= 0x109F)


def _wordish(ch: str) -> bool:
    # Combining marks count: the vowel sign in "राजेश" after "राज" means the word continues, even though the
    # mark is not alphanumeric. Without this, Indic and Arabic values match inside longer words. Variation
    # selectors and zero-width joiners are marks too but belong to emoji, so they are not part of a word.
    o = ord(ch)
    if 0xFE00 <= o <= 0xFE0F or 0x200B <= o <= 0x200F or 0xE0100 <= o <= 0xE01EF:
        return False
    return (ch.isalnum() or ch == "_" or unicodedata.category(ch).startswith("M")) and not _unspaced(ch)


def _bounded(text: str, a: int, b: int) -> bool:
    """False when the match sits inside a longer word or number: 'Raj' inside 'Rajesh', '2024' inside '20245'.
    Without this a three-letter name redacts the first syllable of every longer word that starts the same way."""
    if a > 0 and _wordish(text[a]) and _wordish(text[a - 1]):
        return False
    if b < len(text) and _wordish(text[b - 1]) and _wordish(text[b]):
        return False
    return True


def _find(text: str, value: str, lenient: bool):
    """Occurrences of `value` in `text` as (hits, partial), most literal match tier first.

    A whole-word match always wins. Only when the value occurs nowhere as a whole word does this fall back to
    matching inside a longer run, and it says so by returning partial=True. That fallback matters for redaction:
    when speech-to-text glues two words together ("sixfourteen park street"), refusing the match would leave a
    real address in the clear, which is worse than a mask that starts mid-word.
    """
    tiers = [(re.escape(value), 0), (_flex(value), 0)]
    if lenient:
        tiers.append((_flex(value), re.I))
    raw = []
    for pattern, flags in tiers:
        if not pattern:
            continue
        try:
            found = [(m.start(), m.end()) for m in re.finditer(pattern, text, flags) if m.end() > m.start()]
        except re.error:
            continue
        if not found:
            continue
        clean = [h for h in found if _bounded(text, *h)]
        if clean:
            return clean, False
        raw = raw or found
    return raw, True


# --------------------------------------------------------------------------------------------------
# the public function


def extract_pii(
    text,
    generate,
    *,
    window_words: int = 120,
    overlap_words: int = 25,
    labels=None,
    lenient: bool = True,
    propagate: bool = True,
    min_propagate_len: int = 4,
    max_chars: int = 2_000_000,
):
    """Find personal data in `text` of any length and return it with character offsets.

    Parameters
    ----------
    text
        The document. Anything str-able; None, bytes and other types are handled rather than raising.
    generate
        Callable taking a list of prompt strings and returning a list of model output strings, same length
        and order. See the adapters at the bottom of this file for transformers, an OpenAI-compatible server
        and llama.cpp. Batching is up to you; this function hands it every window at once.
    window_words, overlap_words
        Sliding window over the text, in words. The defaults are measured (see the module docstring); 100 to 150
        with 20-30 of overlap all behave about the same, and both smaller and larger settings are worse, for
        different reasons. Text shorter than one window is sent in a single call.
    labels
        Restrict to a subset of the 43 labels, for example {"PERSON", "PHONE"}. Default: all.
    lenient
        Also match values case-insensitively when locating them. Slightly higher recall, slightly higher risk
        of matching the wrong occurrence.
    propagate
        After merging, search the whole document for every value found anywhere, so a name the model reported
        in one window is also masked where a later window missed it. Values shorter than `min_propagate_len`
        are excluded, since short strings match coincidentally.
    max_chars
        Refuse to process beyond this, to avoid a runaway call. Reported as a warning, not an exception.

    Returns
    -------
    dict with keys
        spans        list of {"start", "end", "label", "text"}, sorted, non-overlapping, offsets into the
                     original string you passed in. A span also carries "partial": True when the value only
                     occurred inside a longer run of text, which is rare (0.4% of predictions on the test set)
                     and usually means speech-to-text ran two words together. Drop those if you would rather
                     under-mask than mask across a word edge.
        entities     list of unique {"label", "text"} in order of first appearance
        unlocatable  values the model returned that do not occur in the text. These are hallucinations and
                     the count is a useful health metric; they are not included in `spans`
        chunks       how many windows were used
        warnings     anything that went wrong, as plain strings. Empty list means a clean run
    """
    labels = set(labels) if labels else set(LABELS)
    body, warnings = _as_text(text)
    empty = {"spans": [], "entities": [], "unlocatable": [], "chunks": 0, "warnings": warnings}

    if not body.strip():
        return empty
    if len(body) > max_chars:
        warnings.append(f"input of {len(body):,} characters truncated to {max_chars:,}")
        body = body[:max_chars]
    if window_words < 60:
        warnings.append(f"window_words={window_words} is below the measured useful range; expect false "
                        f"positives, since the model loses the context that disambiguates a label")
    if overlap_words >= window_words:
        overlap_words = max(1, window_words // 4)
        warnings.append(f"overlap_words was >= window_words, reduced to {overlap_words}")

    spans_of = list(_windows(body, window_words, overlap_words))
    if not spans_of:
        return empty
    prompts = [build_prompt(body[a:b]) for a, b in spans_of]

    try:
        raws = generate(prompts)
    except Exception as exc:                                    # the model call is the caller's code
        warnings.append(f"generate() raised {type(exc).__name__}: {exc}")
        return {**empty, "chunks": len(prompts)}
    if not isinstance(raws, (list, tuple)) or len(raws) != len(prompts):
        warnings.append(f"generate() returned {type(raws).__name__} of unexpected length, expected {len(prompts)}")
        return {**empty, "chunks": len(prompts)}

    # Locate each window's values inside that window, then shift into document coordinates.
    found: list[dict] = []
    order: list[tuple[str, str]] = []
    unlocatable: list[dict] = []
    for idx, ((a, b), raw) in enumerate(zip(spans_of, raws)):
        chunk = body[a:b]
        ents, ok = _parse(raw, labels)
        if not ok:
            warnings.append(f"window {idx + 1} output was not valid JSON, recovered what was parseable")
        for e in sorted(ents, key=lambda e: -len(e["text"])):
            hits, partial = _find(chunk, e["text"], lenient)
            if not hits:
                unlocatable.append({**e, "window": idx + 1})
                continue
            if (e["label"], e["text"]) not in order:
                order.append((e["label"], e["text"]))
            for s, t in hits:
                while s < t and chunk[s].isspace():
                    s += 1
                while t > s and chunk[t - 1].isspace():
                    t -= 1
                if s < t:
                    sp = {"start": a + s, "end": a + t, "label": e["label"], "text": body[a + s:a + t]}
                    if partial:
                        sp["partial"] = True
                    found.append(sp)

    # A value seen in one window may be missed in another; look for every value across the whole document.
    if propagate:
        for lab, val in order:
            if len(val) < min_propagate_len:
                continue
            hits, partial = _find(body, val, lenient)
            for s, t in hits:
                sp = {"start": s, "end": t, "label": lab, "text": body[s:t]}
                if partial:
                    sp["partial"] = True
                found.append(sp)

    # Resolve overlaps: longest span wins, then the earliest. This is the same policy the training data uses.
    found.sort(key=lambda s: (-(s["end"] - s["start"]), s["start"]))
    kept: list[dict] = []
    for sp in found:
        if any(not (sp["end"] <= k["start"] or sp["start"] >= k["end"]) for k in kept):
            continue
        kept.append(sp)
    kept.sort(key=lambda s: s["start"])

    return {
        "spans": kept,
        "entities": [{"label": l, "text": v} for l, v in order],
        "unlocatable": unlocatable,
        "chunks": len(prompts),
        "warnings": warnings,
    }


def redact(text, spans, mask="[{label}]") -> str:
    """Replace each span in `text`. `mask` may use {label} and {text}, or be a plain string.

    >>> redact("Call Derek on 555-0142", spans)
    'Call [PERSON] on [PHONE]'
    """
    body, _ = _as_text(text)
    out = body
    for s in sorted(spans, key=lambda s: -s["start"]):
        try:
            rep = mask.format(label=s["label"], text=s.get("text", ""))
        except (KeyError, IndexError):
            rep = mask
        out = out[:s["start"]] + rep + out[s["end"]:]
    return out


# --------------------------------------------------------------------------------------------------
# generate() adapters. Pick one.

def transformers_generate(model, tokenizer, max_new_tokens=1024, batch_size=8):
    """generate() backed by a local transformers model."""
    import torch

    tokenizer.padding_side = "left"
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token = tokenizer.eos_token

    def run(prompts):
        outs = []
        for i in range(0, len(prompts), batch_size):
            batch = prompts[i:i + batch_size]
            rendered = [tokenizer.apply_chat_template([{"role": "user", "content": p}],
                                                      tokenize=False, add_generation_prompt=True) for p in batch]
            enc = tokenizer(rendered, return_tensors="pt", padding=True, add_special_tokens=False).to(model.device)
            with torch.no_grad():
                gen = model.generate(**enc, max_new_tokens=max_new_tokens, do_sample=False,
                                     pad_token_id=tokenizer.pad_token_id)
            for row in range(len(batch)):
                outs.append(tokenizer.decode(gen[row][enc["input_ids"].shape[1]:], skip_special_tokens=True))
        return outs
    return run


def openai_generate(base_url="http://127.0.0.1:8000/v1", model="inboxpraveen/Kavach-PII-270M",
                    api_key="EMPTY", max_tokens=1024, workers=4):
    """generate() backed by any OpenAI-compatible server: vLLM, SGLang or llama-server."""
    from concurrent.futures import ThreadPoolExecutor
    from openai import OpenAI

    client = OpenAI(base_url=base_url, api_key=api_key)

    def one(prompt):
        r = client.chat.completions.create(model=model, messages=[{"role": "user", "content": prompt}],
                                           temperature=0, max_tokens=max_tokens)
        return r.choices[0].message.content or ""

    def run(prompts):
        with ThreadPoolExecutor(max_workers=workers) as ex:
            return list(ex.map(one, prompts))
    return run


if __name__ == "__main__":
    # Offline self-test of everything except the model call: window coverage, value boundaries, offsets,
    # merging, redaction and bad input. Needs no GPU and no model.
    import random

    failures = []

    def check(name, cond, detail=""):
        print(f"  {'PASS' if cond else 'FAIL'}  {name}{'' if cond else '  <- ' + detail}")
        if not cond:
            failures.append(name)

    # 1. Every word lands in at least one window, at every setting, on irregular line lengths.
    #    A window edge that snaps backwards used to leave a few words in no window at all.
    print("windowing")
    random.seed(3)
    lost = 0
    for win, ov in ((30, 8), (40, 10), (50, 12), (60, 12), (80, 16), (140, 28)):
        for _ in range(300):
            txt = "\n".join(" ".join(f"L{i}w{j}" for j in range(random.randint(2, 30))) for i in range(14))
            ws = [(m.start(), m.end()) for m in _WORD.finditer(txt)]
            wins = list(_windows(txt, win, ov))
            lost += sum(1 for a, b in ws if not any(p <= a and b <= q for p, q in wins))
    check("every word appears in some window", lost == 0, f"{lost} words fell between windows")

    # 2. A value must not match inside a longer word or number, while scripts without word spaces still match.
    print("value matching")
    boundary_cases = (
        ("Raj", "Raj works with Rajesh in Rajasthan.", 1, "must not hit Rajesh or Rajasthan"),
        ("2024", "Order 20245 was placed in 2024.", 1, "must not hit 20245"),
        ("ana@x.com", "mail ana@x.com or bana@x.com", 1, "must not hit bana@x.com"),
        ("राज", "राज और राजेश", 1,
         "Devanagari: the vowel sign continues the word"),
        ("홍길동", "홍길동은 서울에 삽니다.", 1,
         "Korean: an attached particle must not block the match"),
        ("田中", "田中さんは田中建設へ", 2,
         "Japanese has no spaces between words"),
        ("555-0142", "Call 555-0142 now.", 1, "punctuated values are still found"),
    )
    for val, txt, want, why in boundary_cases:
        got, partial = _find(txt, val, True)
        check(f"{val!r} matched {want}x whole-word", len(got) == want and not partial,
              f"{why}; got {len(got)}, partial={partial}")

    # 3. End to end over a transcript, with a stub model in place of the real one.
    print("end to end")
    transcript = (
        "[00:00:03] Speaker 1: Good morning, thank you for calling. This is Raj from J&T Express "
        "Singapore, how can I help you today?\n"
        "[00:00:09] Speaker 2: Hi Raj. I am calling about a parcel that has not arrived. My parcel is "
        "CK-80691 and my mobile is 555-0142 if you need to reach me about it later on.\n"
        "[00:00:15] Speaker 1: Thank you, let me pull that up on the system now. I can see it left the "
        "depot on Tuesday afternoon and has been showing as out for delivery since, which is unusual.\n"
        "[00:00:24] Speaker 2: That is what the tracking page told me too, which is why I wanted to ask "
        "somebody directly rather than keep refreshing the page all morning.\n"
        "[00:00:31] Speaker 1: Completely understood. I will text Rajesh at 555-0199 to chase the driver "
        "and we will come back to you before the end of the day.\n"
    )
    KNOWN = (("PERSON", "Raj"), ("ORGANIZATION", "J&T Express Singapore"), ("CASE_ID", "CK-80691"),
             ("PHONE", "555-0142"), ("PERSON", "Rajesh"), ("PHONE", "555-0199"))

    def stub(prompts):
        # whole-token match, the way the real model copies values
        return [json.dumps([{"label": l, "text": v} for l, v in KNOWN
                            if re.search(r"(?<![\w-])" + re.escape(v) + r"(?![\w-])", p)]) for p in prompts]

    r = extract_pii(transcript, stub, window_words=60, overlap_words=15)
    check("the transcript needed more than one window", r["chunks"] > 1, f"chunks={r['chunks']}")
    check("no warnings on clean input", r["warnings"] == [], str(r["warnings"]))
    check("offsets index the original string",
          all(transcript[s["start"]:s["end"]] == s["text"] for s in r["spans"]))
    check("spans do not overlap",
          all(a["end"] <= b["start"] for a, b in zip(r["spans"], r["spans"][1:])))
    red = redact(transcript, r["spans"])
    check("timestamps survive redaction", red.count("[00:0") == 5, red[:70])
    check("'Raj' did not eat the start of 'Rajesh'", "[PERSON]esh" not in red, red[:200])
    check("both phone numbers masked", red.count("[PHONE]") == 2, red[:200])
    check("nothing unlocatable", r["unlocatable"] == [], str(r["unlocatable"]))
    check("both names masked separately",
          red.count("[PERSON]") == 3, red[:200])

    # A value that occurs only inside a longer run is still masked, but flagged, so a caller can drop it.
    inside = extract_pii("Speaker 2: tomazh adams called.",
                         lambda p: ['[{"label":"PERSON","text":"mazh adams"}]'])
    check("value only inside a longer word is masked and flagged partial",
          len(inside["spans"]) == 1 and inside["spans"][0].get("partial") is True, str(inside["spans"]))
    check("a whole-word match is never flagged partial",
          all("partial" not in sp for sp in r["spans"]), str(r["spans"]))

    # An emoji's variation selector must not look like part of a word.
    emoji = extract_pii("ref ✉️TZ-59654 today",
                        lambda p: ['[{"label":"TRANSACTION_ID","text":"TZ-59654"}]'])
    check("emoji variation selector is not a word character",
          len(emoji["spans"]) == 1 and "partial" not in emoji["spans"][0], str(emoji["spans"]))

    # 4. Nothing raises, whatever it is handed.
    print("bad input")
    for bad in (None, b"bytes in", 12345, "", "   \n  ", ["a", "list"], {"k": "v"}, 3.14):
        try:
            res = extract_pii(bad, stub)
            check(f"{type(bad).__name__} handled", isinstance(res["spans"], list))
        except Exception as exc:
            check(f"{type(bad).__name__} handled", False, f"raised {type(exc).__name__}: {exc}")

    def boom(prompts):
        raise RuntimeError("model is down")

    check("generate() failure reported, not raised",
          extract_pii("Call Raj on 555-0142.", boom)["warnings"][0].startswith("generate() raised"))
    check("short generate() output caught",
          "unexpected length" in extract_pii("Call Raj on 555-0142.", lambda p: [])["warnings"][0])
    check("unparseable model output reported",
          any("not valid JSON" in w for w in extract_pii("Call Raj.", lambda p: ["sorry, I cannot"])["warnings"]))

    print()
    if failures:
        print(f"self-test: {len(failures)} FAILURE(S): {failures}")
        raise SystemExit(1)
    print("self-test: PASS")
```

</details>

## Prompt guidance

* Use the instruction above verbatim, with the 43-label list. The model was trained on exactly this text, and paraphrasing it costs accuracy.
* Use greedy decoding (`do_sample=False`, or `temperature: 0`). Sampling adds nothing on an extraction task and breaks JSON validity.
* Allow 1024 new tokens, or `48 + 1.6 * input_tokens` capped at 1024. Most answers are short (the median test answer is 88 tokens), but a dense bank statement or CSV export can need more than 800: 19 of the 480 production-probe answers are longer than 768 tokens.
* Retry unparseable outputs once with `repetition_penalty=1.1`. Small models occasionally fall into a repetition loop. On v3's evaluation sets, re-decoding only the failures recovered 102 of 108. Do not apply the penalty to every request: on v2 that lowered F1 by 1.4 points.
* Normalise case first if your input may contain random mixed capitalisation (`jOhN sMiTh`). It still costs 8.5 F1 and makes the model flag far more documents that contain no personal data. See [Limitations](#limitations).
* Send one document per call, and window anything long. `kavach_extract.py` above does the windowing for you.

## Results

### Hard cases

v2's errors fell into nine recurring types. For each, v3's training set has hundreds of documents built around it, and a separate gold set of 435 documents (15 per language, about 16 values each) measures it. The gold documents were written by different writers from the training documents, drew their values from separate pools, and were each re-read by a second LLM reader, grouped differently from the writers, who confirmed 99.8% of the 6,837 labels. Each document also carries planted non-personal look-alikes: helplines, head-office addresses, SKUs, version strings and public dates.

![Hard cases by failure type](assets/06-hard-cases.png)

| Failure type | Docs | Gold values | Kavach v3 | Kavach v2 | GLiNER | Presidio |
|---|---|---|---|---|---|---|
| Which identifier is which (several IDs, told apart by cue words) | 45 | 771 | **90.0** | 48.7 | 43.0 | 15.8 |
| Partial and masked values (`card ending 4532`, `XXXX-XX-1234`) | 46 | 591 | **89.0** | 59.4 | 40.9 | 13.8 |
| Organisations and public contacts (tag the firm, not its helpline) | 43 | 565 | **87.2** | 54.5 | 44.2 | 25.3 |
| Technical text (logs, stack traces, JSON, SQL, configs) | 44 | 600 | **86.9** | 65.2 | 48.4 | 27.4 |
| Dense structured records (6 to 12 transaction lines) | 43 | 1,533 | **85.9** | 34.1 | 36.6 | 30.4 |
| Sensitive attributes and dates | 45 | 716 | **82.7** | 51.5 | 50.5 | 14.2 |
| Words glued to values (case endings, particles, postpositions) | 46 | 631 | **78.5** | 51.6 | 34.9 | 16.4 |
| Spoken values in transcripts (numbers read aloud, with corrections) | 47 | 704 | **75.9** | 49.3 | 38.1 | 10.9 |
| Name variants (a full name, then a nickname or surname alone) | 47 | 737 | **75.3** | 58.5 | 45.3 | 21.3 |

| | Kavach v3 | Kavach v2 | GLiNER | Presidio | Regex + checksum |
|---|---|---|---|---|---|
| **Value F1, all 435 documents** | **83.5** | 50.2 | 41.5 | 20.0 | 18.6 |
| Redaction recall | **91.0** | 59.8 | 42.1 | 36.8 | 21.0 |
| **Planted look-alikes tagged (of 2,213)** | **164** | 290 | 477 | 681 | 344 |
| Predicted values not in the text | **2.7%** | 7.1% | n/a | n/a | n/a |

Dense records went from v2's worst case (34.1) to 85.9. Name variants and spoken values are now the weakest, both in the mid-70s. One caveat belongs next to these numbers: the gold was written by the same kind of process that wrote the hard-case training documents, with different writers and value pools. The production probe below is the independent check.

### Production probe

480 documents in eight real-world formats, 60 per format, in English, Hindi, Tamil, Arabic, Spanish and German. No language model wrote any of it. A script builds each document and records every personal value it inserts, so the gold is complete by construction, and each document also carries planted look-alikes that must not be tagged: helplines, head-office addresses, app versions, opening hours.

| Format | Gold values | Kavach v3 | Kavach v2 | GLiNER | Presidio |
|---|---|---|---|---|---|
| Insurance claim form | 797 | **99.1** | 84.6 | 74.5 | 42.1 |
| KYC form | 660 | **98.6** | 84.2 | 94.4 | 27.6 |
| Email thread | 660 | **97.6** | 92.4 | 71.5 | 42.1 |
| Discharge summary | 660 | **95.8** | 69.0 | 58.2 | 42.5 |
| Call transcript | 420 | 93.1 | **98.1** | 61.0 | 38.3 |
| Access log | 1,248 | **88.0** | 66.4 | 79.3 | 27.3 |
| CSV export | 2,465 | **86.7** | 63.2 | 57.2 | 39.3 |
| Bank statement | 1,014 | **82.6** | 58.2 | 15.5 | 29.7 |
| **All formats** | 7,924 | **90.4** | 72.2 | 62.7 | 35.6 |

v3 tagged none of the 180 planted look-alikes; v2 tagged 48, GLiNER 178 and Presidio all 180. Redaction recall is 96.3.

Two things in this table need explaining. The bank statement and CSV scores are held down by the probe's own gold: the script that built it predates v3's labelling rules and does not record transaction dates on a statement or customer IDs in a CSV export, both of which v3 tags as personal (a transaction date on someone's statement is part of their record). Those two account for 912 of v3's 1,081 unmatched predictions. The gold was fixed before v3 was trained and has not been changed. The call transcript row is a real regression: when a customer reads out an 8-digit account number straight after their phone number, v3 labels it `PHONE` in 13 of the 60 transcripts. The value is still found and masked; only its type is wrong.

### By input condition

![Value-F1 by input condition: v3 against v2, GLiNER and Presidio](assets/03-conditions-radar.png)

| Condition | Test docs | Kavach v3 | Kavach v2 | GLiNER | Presidio |
|---|---|---|---|---|---|
| Masked or partial values | 161 | **95.6** | 86.9 | 55.7 | 16.3 |
| Structured forms | 238 | **94.0** | 85.0 | 70.4 | 30.2 |
| Dialogue transcripts | 265 | **93.8** | 90.1 | 60.1 | 22.2 |
| Clean text | 1,374 | **93.2** | 85.8 | 61.9 | 26.6 |
| OCR output | 74 | **93.0** | 83.5 | 71.9 | 31.9 |
| Code and logs | 115 | **91.5** | 81.1 | 51.4 | 24.7 |
| ASR transcripts | 688 | **86.9** | 79.8 | 49.6 | 17.3 |
| Adversarial formatting | 245 | **85.4** | 79.5 | 55.6 | 16.7 |

These are the 3,347 test documents that carry a condition tag (the documents inherited from v2's test set); the 1,230 new test documents are not tagged by condition. v3 is ahead of v2 in all eight conditions. The largest gains are on code and logs (+10.4), OCR output (+9.5), structured forms (+9.0) and masked values (+8.7); the smallest is on dialogue transcripts (+3.7), where v2 was already strong. The weakest condition for v3 (adversarial formatting, 85.4) is above the strongest condition for GLiNER (OCR, 71.9).

### By language

Every language group has at least 85 held-out test documents, so each figure carries a 95% confidence interval between 2 and 8 points wide. v3 is ahead of v2 in all 29, and ahead of GLiNER in all 29.

![Per-language comparison](assets/04-languages.png)

| Language | Test docs | Kavach v3 F1 | 95% CI | Kavach v2 | GLiNER |
|---|---|---|---|---|---|
| Dutch | 90 | **96.4** | 94.3 to 98.3 | 84.7 | 76.6 |
| Multilingual mix (3 or more) | 120 | **96.0** | 94.8 to 97.1 | 86.3 | 72.9 |
| Romanized Indian language | 118 | **94.9** | 93.1 to 96.6 | 87.3 | 72.3 |
| Simplified Chinese | 100 | **94.6** | 92.7 to 96.2 | 84.0 | 57.3 |
| Indonesian | 96 | **93.8** | 91.7 to 95.7 | 82.2 | 73.8 |
| Japanese | 91 | **93.6** | 91.4 to 95.7 | 86.5 | 47.2 |
| Turkish | 96 | **93.1** | 91.2 to 94.9 | 83.4 | 66.3 |
| Hindi | 141 | **92.9** | 90.8 to 94.8 | 81.0 | 38.1 |
| English | 1,238 | **92.8** | 91.9 to 93.6 | 81.4 | 64.9 |
| Russian | 96 | **92.3** | 89.9 to 94.8 | 80.8 | 63.8 |
| Telugu | 174 | **92.3** | 90.7 to 93.8 | 70.9 | 38.1 |
| Korean | 106 | **92.2** | 90.1 to 94.3 | 81.1 | 57.7 |
| Arabic | 173 | **91.7** | 89.7 to 93.6 | 75.5 | 71.4 |
| Vietnamese | 97 | **91.7** | 89.1 to 93.9 | 80.1 | 68.0 |
| Punjabi | 118 | **91.6** | 89.4 to 93.7 | 78.5 | 42.5 |
| Portuguese | 95 | **91.5** | 88.8 to 93.6 | 80.7 | 67.8 |
| Spanish | 125 | **91.4** | 89.3 to 93.3 | 81.6 | 71.8 |
| Polish | 98 | **91.3** | 88.8 to 93.8 | 82.1 | 73.3 |
| Kannada | 156 | **91.2** | 89.1 to 93.1 | 72.7 | 43.8 |
| German | 107 | **91.1** | 88.5 to 93.4 | 82.8 | 67.6 |
| Urdu | 107 | **90.7** | 88.3 to 93.1 | 77.2 | 70.4 |
| Marathi | 118 | **90.6** | 88.2 to 92.9 | 77.9 | 38.8 |
| Malayalam | 156 | **90.6** | 88.5 to 92.4 | 70.3 | 41.1 |
| French | 98 | **90.5** | 87.6 to 93.1 | 77.9 | 61.1 |
| Chinese | 85 | **90.2** | 85.5 to 93.8 | 81.8 | 37.6 |
| Bengali | 169 | **90.1** | 88.0 to 92.1 | 72.3 | 42.9 |
| Tamil | 194 | **89.9** | 87.6 to 91.7 | 71.7 | 35.8 |
| Gujarati | 112 | **89.9** | 87.3 to 92.5 | 76.8 | 42.3 |
| Italian | 103 | **87.4** | 84.1 to 90.6 | 77.5 | 67.9 |

Languages are covered in native script, romanised form, and code-switched with English. The largest gains are in the Dravidian and Indo-Aryan languages that were v2's weakest: Kannada went from 72.7 to 91.2, Malayalam from 70.3 to 90.6, Telugu from 70.9 to 92.3. The spread across all 29 languages is now under 10 points, against 17 for v2.

### By label

43 labels are supported. The table lists those with at least 50 test instances.

![Per-label comparison](assets/05-labels.png)

| Label | Test instances | Kavach v3 F1 | Kavach v2 F1 | GLiNER F1 |
|---|---|---|---|---|
| `PERSON` | 5,371 | **94.3** | 88.1 | 40.4 |
| `PHONE` | 3,678 | **95.4** | 91.7 | 75.3 |
| `ORGANIZATION` | 2,732 | **87.5** | 78.6 | 66.0 |
| `EMAIL` | 2,652 | **96.6** | 92.2 | 87.0 |
| `DOB` | 2,616 | **97.2** | 92.0 | 87.6 |
| `CASE_ID` | 2,031 | **88.3** | 52.4 | 23.9 |
| `DATE_TIME` | 2,014 | **84.6** | 15.6 | 54.7 |
| `ADDRESS` | 1,587 | **87.2** | 76.7 | 44.4 |
| `NATIONAL_ID` | 995 | **93.0** | 77.0 | 50.8 |
| `CREDIT_DEBIT_CARD` | 494 | **93.7** | 76.1 | 57.7 |
| `BANK_ACCOUNT` | 406 | **94.1** | 77.8 | 59.6 |
| `EMPLOYEE_ID` | 374 | **89.0** | 72.5 | 33.0 |
| `INSURANCE_ID` | 329 | **91.4** | 75.4 | 56.1 |
| `BANK_CODE` | 317 | **94.5** | 58.4 | 29.2 |
| `TRANSACTION_ID` | 310 | **86.0** | 47.3 | 42.8 |
| `CARD_EXPIRY` | 245 | **99.6** | 77.9 | 63.1 |
| `CARD_CVV` | 232 | **96.1** | 79.5 | 62.6 |
| `MEDICAL_RECORD_ID` | 204 | **85.9** | 71.3 | 45.0 |
| `AGE` | 200 | **95.2** | 44.0 | 71.2 |
| `USERNAME` | 179 | **88.0** | 75.2 | 53.1 |
| `LAB_ORDER_ID` | 173 | **92.1** | 71.7 | 65.8 |
| `PRESCRIPTION_ID` | 166 | **92.6** | 79.0 | 55.5 |
| `LICENSE_PLATE` | 158 | **89.4** | 63.0 | 40.3 |
| `PASSPORT` | 147 | **92.6** | 86.6 | 60.4 |
| `STUDENT_ID` | 132 | **89.8** | 79.1 | 62.5 |
| `DRIVING_LICENSE` | 116 | **83.6** | 71.9 | 34.9 |
| `GENDER_SEX` | 99 | **92.2** | 7.5 | 47.6 |
| `DEVICE_ID` | 80 | **84.8** | 69.0 | 37.6 |
| `HEALTH_ID` | 75 | **87.8** | 61.7 | 27.7 |
| `PASSWORD_SECRET` | 63 | **69.4** | 40.0 | 25.3 |
| `API_KEY_TOKEN` | 54 | **76.6** | 43.0 | 29.5 |
| `PAYMENT_ID` | 54 | **75.8** | 67.4 | 31.8 |

Every label improved. The very low v2 figures for `DATE_TIME` and `GENDER_SEX` are mostly rule changes rather than v2 getting worse: v2 tagged vague dates such as "yesterday" and "Friday", which v3's gold does not count, and v2's training data rarely tagged gender at all.

Labels with fewer than 50 test instances, whose figures are indicative only: `IP_ADDRESS` 92.2 (47), `VIN` 89.4 (47), `URL_PERSONAL` 86.0 (46), `RELIGION` 87.1 (42), `VOTER_ID` 88.2 (37), `DISABILITY` 62.2 (36), `BIOMETRIC_DESCRIPTOR` 79.3 (32), `ETHNICITY` 74.1 (29), `POLITICAL_BELIEF` 81.4 (29), `MAC_ADDRESS` 89.4 (23), `GEO_LOCATION` 92.3 (19).

Full label set, 43 in total:

`ADDRESS` `AGE` `API_KEY_TOKEN` `BANK_ACCOUNT` `BANK_CODE` `BIOMETRIC_DESCRIPTOR` `CARD_CVV` `CARD_EXPIRY` `CASE_ID` `CREDIT_DEBIT_CARD` `DATE_TIME` `DEVICE_ID` `DISABILITY` `DOB` `DRIVING_LICENSE` `EMAIL` `EMPLOYEE_ID` `ETHNICITY` `GENDER_SEX` `GEO_LOCATION` `HEALTH_ID` `INSURANCE_ID` `IP_ADDRESS` `LAB_ORDER_ID` `LICENSE_PLATE` `MAC_ADDRESS` `MEDICAL_RECORD_ID` `NATIONAL_ID` `ORGANIZATION` `PASSPORT` `PASSWORD_SECRET` `PAYMENT_ID` `PERSON` `PHONE` `POLITICAL_BELIEF` `PRESCRIPTION_ID` `RELIGION` `STUDENT_ID` `TRANSACTION_ID` `URL_PERSONAL` `USERNAME` `VIN` `VOTER_ID`

### Robustness

Eighteen offset-safe corruptions applied to 300 held-out dev documents, each measured against the model's own clean baseline of 92.8.

![Robustness under corruption](assets/07-robustness.png)

| Corruption | v3 change | v2 change |
|---|---|---|
| Random mixed capitalisation | -8.5 | -15.6 |
| All uppercase | -3.8 | -4.7 |
| Keyboard typos | -3.1 | -8.5 |
| Punctuation stripped | -1.8 | -3.2 |
| All lowercase | -1.4 | -3.3 |
| Whitespace noise | -1.3 | -0.6 |
| Zero-width characters injected | -1.0 | -1.0 |
| Homoglyph substitution | -0.9 | -1.1 |
| Words dropped | -0.8 | -1.2 |
| Values spaced out (`9 8 7 6`) | -0.6 | -1.3 |
| Full-width characters | -0.6 | -1.9 |
| JSON escaping | -0.5 | -0.4 |
| Prefix and suffix noise | -0.5 | -0.5 |
| Digits written as words | -0.4 | -1.1 |
| Mojibake | 0.0 | 0.0 |
| Separator changes | 0.0 | -0.3 |
| Markdown wrapping | +0.6 | -2.3 |
| HTML wrapping | +0.9 | +1.3 |

Fourteen of the eighteen cost under 1.5 F1. Random capitalisation is still the worst case, but v3 loses about half what v2 did, and keyboard typos went from -8.5 to -3.1. The v2 column is from the v2 card, measured the same way on 300 of v2's own dev documents, so compare the size of each drop rather than the absolute scores.

## Compliance coverage

Mapped against the 18 HIPAA Safe Harbor identifiers, 16 of 18 have trained support. Identifier 17 is photographs, which is out of scope for a text model.

| HIPAA identifier | Label |
|---|---|
| Names | `PERSON` |
| Geography smaller than a state | `ADDRESS` (including standalone postcodes) |
| Dates, ages over 89 | `DOB`, `DATE_TIME`, `AGE` |
| Telephone and fax | `PHONE` |
| Email | `EMAIL` |
| Social Security numbers | `NATIONAL_ID` |
| Medical record numbers | `MEDICAL_RECORD_ID` |
| Health plan beneficiary numbers | `INSURANCE_ID`, `HEALTH_ID` |
| Account numbers | `BANK_ACCOUNT`, `CREDIT_DEBIT_CARD`, `PAYMENT_ID` |
| Certificate and licence numbers | `DRIVING_LICENSE`, `EMPLOYEE_ID` (NPI, DEA, professional registrations) |
| Vehicle identifiers | `VIN`, `LICENSE_PLATE` |
| Device identifiers | `DEVICE_ID`, `MAC_ADDRESS` |
| Web URLs | `URL_PERSONAL` |
| IP addresses | `IP_ADDRESS` |
| Biometric identifiers | `BIOMETRIC_DESCRIPTOR` |
| Any other unique identifying number | `CASE_ID`, `STUDENT_ID`, `TRANSACTION_ID`, and the rest of the ID family |

Also covered: PCI (`CREDIT_DEBIT_CARD`, `CARD_EXPIRY`, `CARD_CVV`, `BANK_ACCOUNT` including IBAN, `BANK_CODE` for SWIFT/BIC, IFSC, ABA routing and sort codes), national identifiers of any country under `NATIONAL_ID` (SSN, Aadhaar, PAN, NIN, NRIC, CPF, DNI, Emirates ID, codice fiscale, Steuer-ID and others), UPI IDs and wallets under `PAYMENT_ID`, and US healthcare administration (NPI and DEA under `EMPLOYEE_ID`, Medicare MBI and Medicaid IDs under `HEALTH_ID`). GDPR special categories are covered by `RELIGION`, `ETHNICITY`, `POLITICAL_BELIEF`, `DISABILITY`, `GENDER_SEX` and `BIOMETRIC_DESCRIPTOR`, though test support for them is thin (see [Limitations](#limitations)).

## Training

| | |
|---|---|
| Base model | `google/gemma-3-270m-it`, 268M parameters |
| Method | LoRA, r=64, alpha=128, dropout 0.05, on all attention and MLP projections (15.2M trainable, 5.4%), unchanged from v2 |
| Precision | base weights bf16 throughout, only the adapter was trained |
| Data | 81,337 training documents, 46.4M tokens (6 documents longer than 3,072 tokens left out) |
| Schedule | 3 epochs, 15,819 steps, lr 2e-4 with linear decay and 3% warmup, effective batch 16 |
| Augmentation | 18 offset-safe corruption operations applied on the fly at p=0.5 (v2: 0.35) |
| Hardware | one NVIDIA RTX 5060 Laptop GPU (8 GB), 6.2 hours, 2.61 GB peak |
| Loss | cross-entropy on the assistant JSON only, prompt tokens masked out |

Best dev loss 0.0281, measured on 1,000 documents of the v3 dev set. It is not comparable with v2's 0.0397, which was measured on a different dev set with a different label list.

### Dataset

About 91,700 documents and 593,000 labelled values across all splits, entirely synthetic. No real personal data was used.

| Split | Documents | Values | PII-free |
|---|---|---|---|
| train | 81,343 | 523,028 | 7,506 |
| dev | 3,964 | 21,520 | 393 |
| test | 4,577 | 28,672 | 440 |
| hard cases (gold) | 435 | 6,862 | 29 |
| production probe (built by code) | 480 | 7,924 | 0 |
| simulated ASR / real OCR / real-text injection | 289 / 250 / 300 | 1,409 / 1,349 / 2,030 | 0 / 0 / 68 |

The training set is the 57,909 v2 training documents, relabelled, plus 23,434 new ones. It spans 29 languages, 23 domains (contact centre, healthcare, pharmacy and labs, insurance, banking, government, telecom, e-commerce, education and HR, legal, IT helpdesk, logistics, real estate, automotive, travel and others), hard negatives and prompt-injection wrappers, and 12 input conditions. It keeps v2's real noise round trips (browser render into Tesseract OCR, an ASR simulator few-shot prompted on real Whisper output), PII embedded in real Wikipedia passages, and 600 hand-built negatives covering already-redacted text, blank forms, placeholder rows and medical billing code lists.

**How the labels were checked.** The weakness v3 set out to fix was label quality as much as coverage, so most of the work went here:

* **Re-annotation.** Every existing document, 65,000 of them, went back through LLM annotators that proposed additions, removals, relabels and boundary fixes against the existing gold. A stronger model, reasoning before it answered, verified every removal and relabel, and every boundary change that lengthened a value. Evaluation sets were audited twice more by independent models. A document-by-document review of a 500-document sample found the old gold had been missing roughly one value in ten.
* **Written rules, applied by code.** Honorifics and cue words outside the value in every script, sentence punctuation, time particles in Korean, Kannada and Tamil, place names that are not addresses, vague dates, fully masked values and placeholder values. Each rule logs every change it makes, and each was checked on a sample before it was applied to every split.
* **Measured per language.** 4,400 training documents (150 per language, 200 for English) were audited by a model that had not audited the training set before, with every correction verified: precision 98.9, recall 98.4, and no language below 97.9 precision or 97.1 recall. 870 training documents (30 per language, 7,665 labels) were then read one at a time by LLM reviewers working from the written annotation rules (not by people): precision 97.8, recall 97.1. The error types found there (missed name variants, boundaries, values that are not personal) were then fixed across the whole corpus by rule.
* **Hard-case documents were filtered, not trusted.** The 4,022 hard-case documents from a local generator passed a gate that removes placeholders, sequential and repeated-digit identifiers, copied example values, near duplicates and anything sharing an identifier with an evaluation split. Documents an automated auditor flagged as possibly missing values were set aside rather than trained on, because no automated judge could tell a real omission from a false alarm reliably. The same kind of document-by-document review, 20 documents per language, then excluded 10 languages that fell below 97 precision or 95 recall from that batch.
* **No leakage.** Splits are grouped by synthetic identity, so no generated person appears on both sides of a split. 564 test and 288 dev documents that shared an identifier with a training document were moved into training, exact duplicates were removed, and no training text appears in any evaluation split. Documents derived from a training document move with their source, so a rewrite of a training document can never appear in test.

## Fair comparison notes

* The cross-system tables were scored by the same script (`pii_eval.py`), on the same documents, against the same gold. Values are compared after whitespace normalisation; case matters.
* The v2-versus-v3 table was scored with `eval_v3.py`, the script that produced the v2 baselines before v3 was trained. It also normalises case. On the same data the two scripts agree to within 0.2 points.
* v2, GLiNER, Presidio and the regex baseline emit v2 label names. Their predictions were mapped to the v3 labels with the table in [Migrating from v2](#migrating-from-v2), so none of them is penalised for naming.
* GLiNER-PII (`urchade/gliner_multi_pii-v1`) was queried with natural-language label names mapped to our labels, threshold 0.4, 1,500-character chunks.
* Presidio used the default `AnalyzerEngine` with spaCy `en_core_web_lg`, threshold 0.35. Its recognisers are English-first, which is part of why it scores poorly on the multilingual portion. It is included because it is the most widely deployed open-source baseline, not because the comparison is favourable.
* GLiNER and Presidio can only lose recall on label types they do not model. Unmappable types were dropped from their predictions rather than counted as errors.
* The test gold came from the same pipeline that produced the training data. That is the honest caveat on every number here: it is our own test set. The hard-case gold shares its generation process with the hard-case training documents, although the writers and value pools differ. The production probe is the one set that shares nothing with the training pipeline: code built it, no language model touched it, and its gold is complete by construction. The real-text injection slice reuses passages whose base text also appears in training, so treat it as a robustness check rather than an independent test.
* Independent evaluation on third-party corpora remains the obvious next step.

## Limitations

* **False positives on documents with no personal data** rose from 2.0% in v2 to 12.5%, mostly dates and reference numbers in documents about nobody. The two-line filter under the headline table brings it to 4.5% for 0.5 F1.
* **Name variants and spoken values are the weakest cases.** A person named in full and later by nickname or surname alone scores 75.3 on the hard-case gold, and numbers read aloud with corrections score 75.9. Words glued to values (case endings, particles) are next at 78.5.
* **Indic scripts trail on the hard cases.** On the hard-case gold, Urdu (74.6), Kannada (75.1), Punjabi (76.1) and Marathi (76.2) are the lowest languages, against 90 and above for English, Dutch and Chinese. Each language has only 15 hard-case documents, so treat these as directional.
* **Identifier typing still has a ceiling.** A bare number without a cue word cannot always be typed. In call transcripts, an 8-digit account number read out right after a phone number is labelled `PHONE` in 13 of the 60 production-probe transcripts. For redaction what matters is that the value is found, and redaction recall is 96.0 on the test set.
* **Random capitalisation is still the worst corruption.** Mixed random caps cost 8.5 F1 (v2: 15.6), and among the 23 PII-free documents in the robustness sample, the number flagged rose from 2 to 10. All-uppercase text costs 3.8 and keyboard typos 3.1. Normalise case before calling the model if your inputs may contain it.
* **Weak labels.** `DISABILITY` (62.2), `PASSWORD_SECRET` (69.4), `ETHNICITY` (74.1), `PAYMENT_ID` (75.8) and `API_KEY_TOKEN` (76.6) are the soft spots, and most special-category labels have fewer than 50 test instances each.
* **`SIGNATURE` no longer exists.** A signature line is tagged `PERSON`, like any other name.
* **Do not add a regex union.** Tested on v2: combining the model with checksum and regex recognisers lowered F1 from 88.4 to 86.6 and raised the false-positive rate from 0.4% to 9.0%.
* **Synthetic training data.** Style is bounded by the generators that produced it. Real noise round trips, augmentation, real-text injection and the code-built probe reduce that fingerprint but do not remove it.
* **Not a compliance guarantee.** This is a detection aid. Regulated workflows still need human review.

## Other formats

* Quantised GGUF builds for llama.cpp, Ollama and LM Studio: [Kavach-PII-270M-GGUF](https://huggingface.co/inboxpraveen/Kavach-PII-270M-GGUF)
* LoRA adapter only, 61 MB, applies to `google/gemma-3-270m-it`: the `adapter/` folder in this repository.
* v2 (52 labels) remains available in this repository's commit history.

## Licence

Built with Gemma. This model is a fine-tune of `google/gemma-3-270m-it` and is governed by the [Gemma Terms of Use](https://ai.google.dev/gemma/terms) and the [Gemma Prohibited Use Policy](https://ai.google.dev/gemma/prohibited_use_policy), both of which pass through to you and to anyone you redistribute it to. The evaluation code is Apache-2.0 and the synthetic dataset is CC-BY-4.0.

## Citation

```bibtex
@software{kavach_pii_270m,
  title   = {Kavach PII 270M: multilingual personal data extraction with post-hoc span recovery},
  author  = {Praveen Kumar},
  year    = {2026},
  version = {3},
  url     = {https://huggingface.co/inboxpraveen/Kavach-PII-270M},
  note    = {Fine-tune of google/gemma-3-270m-it}
}
```
