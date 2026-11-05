---
license: apache-2.0
language: [de, en, ja]
base_model: jhu-clsp/mmBERT-base
pipeline_tag: token-classification
tags:
  - pii
  - privacy
  - ner
  - modernbert
  - shinrai
  - pseudonymization
  - semantic-encryption
  - onnx
# This repo stays ungated: v1.1 is part of the permanently open Apache 2.0 tier (ADR-0009).
---

<img src="https://huggingface.co/spaces/innovius/README/resolve/main/shinrai-logo.png" width="104" alt="ShinrAI — shield logo" align="right">

# shinrai-pii-m-v1.1

**You use the AI. The AI does not use you.**

> **Superseded by [`shinrai-pii-m-v1.3`](https://huggingface.co/innovius/shinrai-pii-m-v1.3)**
> and by ShinrAI 1.5 in the managed API at [getshinrai.com](https://getshinrai.com)
> for every language — including Japanese, where v1.3 reads its best result ever
> (98.1 register F1 vs 83.8 macro here). v1.1 remains available as the archived
> first open generation.

> 🔓 **License: v1.1 is and remains Apache 2.0 — the permanently open tier.**
> The v1.3 flagship ships under the [Innovius Open License v1.0](https://innovius.ai/shinrai/open-license.html)
> (free for government, education, research, and companies under $10M revenue;
> it converts to Apache 2.0 on 2028-09-01).

M-size ShinrAI encryption model — the detection layer of ShinrAI **semantic encryption**
(ShinrAI, 信頼, is Japanese for *trust*). This is the model generation behind our
**2024–2026 ShinrAI Enterprise product line (legacy)**, and the first ShinrAI encryption
model we opened up. German and English were first superseded by
[`shinrai-pii-m-v1.2`](https://huggingface.co/innovius/shinrai-pii-m-v1.2);
all three of its languages now route to v1.3.

Architecture: ModernBERT-family `mmBERT-base` encoder with a multi-head token classifier —
PERSON / CITY / STREET / ORG spans with frequency/size **tiers** and span attributes
(**origin**, **gender expression**, **name part**) for realm-preserving pseudonymization:
detected entities are swapped for natural alternatives matched to context, culture and
language (never `[MASK]` wreckage, never bias-triggering hard cuts), so downstream AI keeps
reasoning over natural text. Suited to mass de-identification (ePA / clinical, high-security,
banking) as well as realtime protection.

Developed by [Innovius](https://innovius.ai) with the [EECC Research Labs](https://eecc.info),
trained on the JURECA supercomputer at the Jülich Supercomputing Centre (Forschungszentrum
Jülich) under the WestAI compute grant, scaling onto JUPITER, Europe's first exascale system.

- 🚀 **ShinrAI 1.5 — the current model, in the managed ShinrAI PII detection and pseudonymisation API:**
  [getshinrai.com](https://getshinrai.com)
- 🛡️ **Try the current generation live (text, PDF, image, audio):**
  [shinrai-pii-playground](https://huggingface.co/spaces/innovius/shinrai-pii-playground)
- 📊 **Benchmarks: ShinrAI 1.5 vs Azure, Presidio, GLiNER & the open field (losses included):**
  [shinrai-pii-benchmarks](https://huggingface.co/spaces/innovius/shinrai-pii-benchmarks)
- 🧪 **Beta programme:** https://innovius.ai/shinrai/beta/
- 🏢 **Organization:** https://huggingface.co/innovius
- ✉️ **Production use today (Secure AI Suite / ChtSafe):** https://innovius.ai/#contact

## What it does

Given text in German, English or Japanese, the model emits entity spans with rich
attributes: entity class, a frequency/size tier (how common a name is, how large a city
is), cultural origin, gender expression and name-part structure. This is what enables
**realm-preserving replacement**: `Robert` → `Paul` — a substitute matching the original's
cultural register, frequency tier and gender expression, with no visible trace that
anything was replaced and minimal bias distortion for the consuming model.

| head | labels | tiers |
|---|---|---|
| PERSON | IOB2 × 3 tiers | common / uncommon / rare (name-frequency rank) |
| CITY | IOB2 × 3 tiers | major / medium / small (population bands) |
| STREET | IOB2 × 3 tiers | generic / specific / local (recognizability) |
| ORG | IOB2 × 3 tiers | international / national / regional |

Plus three span-pooled attribute heads computed in the same forward pass: **origin**
(42 classes, independent of text language — "Mailand" in German text is a CITY with origin
IT), **gender expression** (masc / fem / neutral / unknown; replacement never flips
masc↔fem) and **name part** (given / family / full). The full machine-readable schema ships
in `labels-v2.0.yaml`.

## Where it sits — and what belongs in front of it

![Defense-in-depth pipeline](assets/pipeline.png)

ShinrAI models exist for the **multi-dimensional, context-dependent** part of the problem:
knowing that *Keller* is a surname here and a basement there, that *Lindenweg 12* is an
address, how identifying each entity is, and what a culturally consistent replacement looks
like. That is what statistical models are for.

**Deterministic identifiers are not.** IBANs, credit-card and account numbers, BTC/ETH
wallet addresses, postal codes, phone numbers, e-mail addresses, tax and insurance IDs
follow fixed formats, most with checksums — catch and replace them in an **application
layer in front of the model** (validators, regex, lookup tables). Hunting fixed patterns
with a 300M-parameter encoder is highly error-prone compared to a validator that is exact
by construction, and a waste of resources — RAM footprint and response time — on something
a rule decides in microseconds; anything the validator removes can never leak past it.
Our own software layer does exactly that: the
[ShinrAI Connector](https://chtsafe.com/apps) ships it on your desktop, and the
Secure AI Suite ([info@innovius.ai](mailto:info@innovius.ai)) brings it to your company —
this model only ever owns what rules cannot decide.

## Results

Span F1 on surface-disjoint evaluation suites (never seen in training, disjoint surface
forms), measured for this exact checkpoint:

![Entity detection by language](assets/perf-entities.png)

| suite | PERSON | CITY | STREET | ORG | **macro** | tier acc |
|---|---|---|---|---|---|---|
| de | 88.1 | 94.7 | 95.4 | 56.6 | **83.7** | 84.8 |
| en | 98.3 | 91.9 | 91.7 | 68.9 | **87.7** | 71.7 |
| ja | 99.4 | 79.4 | 88.6 | 67.8 | **83.8** | 97.6 |

Attribute accuracy on detected spans (these steer replacement selection):

![Replacement-steering attributes](assets/attributes.png)

| suite | origin | gender expression | name part |
|---|---|---|---|
| de | 92.2 | 99.0 | 95.8 |
| en | 88.4 | 87.6 | 94.0 |
| ja | 95.4 | 94.6 | 97.7 |

### Known limitations (addressed in the current generation)

- **ORG generalization is the weak head** (56.6–68.9): the organization inventory this
  generation trained on was small. v1.2 moved to a Wikidata-scale inventory and reads
  88.4–93.8.
- Under-recall on institutional letterhead address blocks, abbreviated given names
  ("M. Krüger") and letter sign-off names.
- PERSON spans are emitted at given/family granularity (e.g. "Anna" + "Keller" as two
  spans); v1.2 merges full names into one span.
- German and Japanese PERSON tiers lean towards `common`; tier depth improves with the
  registry-backed statistics introduced in v1.2.
- Context window 512 tokens (sliding-window inference with overlap merge handles longer
  documents automatically; v1.2 doubles the window to 1024).

Routing guidance: **all three languages →
[`shinrai-pii-m-v1.3`](https://huggingface.co/innovius/shinrai-pii-m-v1.3)**
(de 94.4 / en 97.7 / ja 98.1 register F1, plus 12 further locales and 15 format heads).

## How it compares

**Against public PII models.** We benchmarked the strongest openly released PII models we
could find on this model's serving suites — the OpenMed-PII family (clinical-domain
de-identification, RoBERTa/DeBERTa-class encoders), taking the best in-language checkpoint
per suite (SuperClinical-434M / BigMed-560M class). Identical scoring pipeline, span-level
concept intersection over {PERSON, CITY, STREET, ORG}, measured 2026-08. Macro span F1:

| suite | best in-language OpenMed-PII | shinrai v1.1 |
|---|---|---|
| de | 50.9 | **83.7** |
| en | 70.6 | **87.7** |
| ja | 24.3 | **83.8** |

Read it fairly, in both directions:

- Our suites are multilingual business/medical documents — outside OpenMed's clinical home
  domain. On **English** their flagship is genuinely competitive on PERSON/CITY/STREET
  (81–89 F1); the macro gap there is mostly **ORG**, a systematic blind spot of every PII
  tagger we measured (16–39 F1 across the three suites).
- On **their** home turf — real German clinical narrative (GraSCCo, which is eval-only for
  us) — OpenMed's German flagship beats this model on PERSON recall and aggregate F1.
  If your workload is pure clinical de-identification inside OpenMed's domain, a clinical
  specialist is a strong choice there; our Enterprise ePA pipeline layers this model with
  additional safeguards for exactly that reason.
- Generic **RoBERTa/DeBERTa-class PII taggers** solve a different, smaller problem: flat
  entity labels, usually English-first. None of the models we measured emit what
  replacement needs — frequency/size tiers, cultural origin, gender expression, name-part
  structure, calibrated confidences. Detection is table stakes; ShinrAI's job is making
  the *replacement* invisible.

**Against the next ShinrAI generations.**
[`shinrai-pii-m-v1.2`](https://huggingface.co/innovius/shinrai-pii-m-v1.2)
superseded this model for German and English — 92.2 / 94.3 macro on suites drawn from far
larger entity inventories, where this model reads 33.6–49.3 — and added Italian, French,
Spanish and Polish (Japanese stayed here at the time: 83.8 vs v1.2's 60.8).
[`shinrai-pii-m-v1.3`](https://huggingface.co/innovius/shinrai-pii-m-v1.3)
now supersedes both everywhere, Japanese included (98.1 register F1), with 15 locales and
15 format heads on top of the four semantic heads.

## Bias behavior — engineered for model-bias stability

This model family is trained to avoid **machine biases — the documented, systematic
biases of LLMs** — not to correct human bias in text. Large models measurably treat text
differently depending on name origin, gender association, name rarity, city size or
organization prestige. Naive anonymization changes those signals: `[MASK]` tokens,
`<PII>` tags and randomly chosen substitute names all shift how the consuming model
scores, ranks and reasons over a document — which makes results unstable and the
pseudonymization itself detectable.

The replacement policy is therefore **bias-stable by construction**:

- An entity is **never** swapped for one that triggers *more or fewer* known model biases
  than the original. Replacements match the original's cultural origin, gender
  expression, frequency tier and register — same treatment by the downstream model,
  different identity.
- **No debiasing.** If the original text would trigger a model bias, the replacement
  triggers the same one. Silently "improving" the text would change model behavior and
  break the round-trip guarantee.
- The tier and attribute heads exist precisely for this: they are the steering signal
  that keeps the statistical texture of text constant under replacement — never a
  profiling signal (see Privacy below).

## Quantization — run it anywhere

![ONNX quantization ladder](assets/quant-ladder.png)

The full ONNX ladder ships in `quant/` (opset 17; export parity vs PyTorch: max logit
delta 3.5e-05 across all 7 output heads — `quant/parity-onnx.json`):

| artifact | format | size | macro-F1 de / en / ja |
|---|---|---|---|
| `quant/model-fp32.onnx` | ONNX fp32 | 1.23 GB | 83.70 / 87.70 / 83.80 |
| `quant/model-q8.onnx` | ONNX INT8 dynamic | **309 MB** | 83.67 / 87.58 / 83.62 |
| `quant/model-q4.onnx` | ONNX 4-bit weight-only | 257 MB | ja spot check: 81.75 |

**Q8 is the serving baseline**: ≤ 0.2 macro-F1 cost on every serving suite, 4× smaller,
CPU-friendly. Q4 costs ~2 macro points where measured — usable where 257 MB matters.

## Usage

The repo is a self-contained HF-layout release:

```
model.safetensors      # full-precision weights (custom multi-head architecture)
config.json            # encoder configuration (ModernBERT / mmBERT-base)
tokenizer/             # HF tokenizer (256k vocab)
labels-v2.0.yaml       # machine-readable label schema (heads, tiers, attributes)
calibration.json       # per-head confidence temperatures
quant/                 # ONNX ladder + MANIFEST.json + parity report
assets/                # model card figures
```

The heads are a custom multi-head architecture, so plain
`AutoModelForTokenClassification` does not expose them — use the **ONNX graph** (named
inputs/outputs, works with `onnxruntime` alone), or the ShinrAI inference SDK
(sliding-window batching, IOB2 decoding, span merging, calibration — pip package
planned):

```python
import onnxruntime as ort
from transformers import AutoTokenizer

repo = "innovius/shinrai-pii-m-v1.1"  # local: path to a clone
tok = AutoTokenizer.from_pretrained(repo, subfolder="tokenizer")
sess = ort.InferenceSession("quant/model-q8.onnx")

enc = tok("山田花子さんは大阪市に住んでいます。", return_tensors="np")
out = sess.run(None, {"input_ids": enc.input_ids, "attention_mask": enc.attention_mask})
# 7 named outputs:
#   logits_person / logits_city / logits_street / logits_org   [batch, seq, 7]  (IOB2 × 3 tiers + O)
#   attr_logits_origin [.., 42] · attr_logits_gender_expression [.., 4] · attr_logits_name_part [.., 3]
# label inventories for decoding: labels-v2.0.yaml
```

Decoded output (via the ShinrAI predictor, verified against this exact checkpoint) for
`"山田花子さんは大阪市に住んでいます。"`:

```json
{"span": [0, 4], "text": "山田花子", "type": "PERSON", "tier": "common",
 "confidence": 0.753, "attrs": {"origin": "JP", "gender_expression": "unknown", "name_part": "family"}}
{"span": [7, 10], "text": "大阪市", "type": "CITY", "tier": "major",
 "confidence": 0.993, "attrs": {"origin": "JP"}}
```

and for `"Bitte senden Sie den Bericht an Frau Dr. Anna Keller, Lindenweg 12, 04109 Leipzig."`:

```json
{"span": [41, 45], "text": "Anna",         "type": "PERSON", "tier": "common", "confidence": 0.781}
{"span": [46, 52], "text": "Keller",       "type": "PERSON", "tier": "common", "confidence": 0.947}
{"span": [54, 66], "text": "Lindenweg 12", "type": "STREET", "tier": "generic", "confidence": 0.668}
{"span": [74, 81], "text": "Leipzig",      "type": "CITY",   "tier": "medium",  "confidence": 0.995}
```

Note what is *not* in the output: the postal code `04109`. Deterministic identifiers are
your validation layer's job (see the pipeline section) — by design, not omission.

Inference is sliding-window (window 512, stride 64, overlap merge) — documents of any
length work. Confidences are temperature-calibrated per head from `calibration.json`.

## Use ShinrAI in production today

**☁️ As a developer or company — the ShinrAI API.** ShinrAI 1.5, the current model,
runs in the managed ShinrAI PII detection and pseudonymisation API, hosted on STACKIT
in the EU. Start at **[getshinrai.com](https://getshinrai.com)** — see the
[ShinrAI plans and pricing](https://getshinrai.com/#plans) and the
[API documentation](https://getshinrai.com/docs/api).

**🖥️ On your own machine — ShinrAI Connector.** Our desktop client runs ShinrAI models
locally on your own GPU — or CPU-only, thanks to the Q8 build — and funnels your AI
traffic through semantic encryption before it leaves your machine. Works with **Claude
Desktop** and **Cursor** today, the **ChatGPT Desktop app** soon. Get it at
**[chtsafe.com/apps](https://chtsafe.com/apps)**.

![ShinrAI Connector running this model locally](assets/shinrai-connector.png)

*The Connector running this exact model on a Mac — 0.12 GB in memory, CPU-only — with the
deterministic categories (banking and cards, crypto wallets, ID numbers, contact details)
handled by its software layer, exactly as described above.*

**🔒 As a private person — ChtSafe.** Chat fully anonymously with any leading AI model,
protected in realtime by the latest ShinrAI models (currently in review and training,
publication to follow). Sign up at **[chtsafe.com](https://chtsafe.com)** or get the app
from the **App Store**.

**🏢 As a company — the Secure AI Suite.** Semantic encryption plus onion routing across
as many model-access paths as you like, deployed **on-premise first** — your hardware,
your keys — or in your private cloud. You get the complete software and code for review;
we support the rollout on your infrastructure, or deliver custom GPU servers with
**5-year support**. Register your company at [chtsafe.com](https://chtsafe.com) or write
to **[info@innovius.ai](mailto:info@innovius.ai)**.

## Training data

The v1.1 corpus is **mostly hand-compiled** — built from our own curated name, place and
organization inventories, document templates and formatting frames — and **synthetically
reviewed**: cross-checked and quality-gated by openly released models (the Qwen and Gemma
families), with substantial review passes on top. It is not a fully synthetic corpus; it
is a curated one, anchored in open data: GeoNames (CC-BY) city statistics and US
SSA/Census name statistics (public domain).

Everything in the pipeline is either self-contributed or license-clean open data — no
customer data, no scraped personal records, nothing proprietary, nothing "found" on the
web. Every record carries a license-provenance field; released datasets contain only the
license-clean subset (CC0 / CC-BY / public-domain / our own text). Data releases:
https://huggingface.co/innovius (as they land).

## Privacy & responsible use

The model detects and helps pseudonymize personal data; it does not memorize real
individuals — the training corpus is hand-compiled and synthetically reviewed, with no
real persons' records in it. Detection is probabilistic: for regulated
deployments, treat it as one layer of a defense-in-depth privacy architecture, not a sole
control (and keep deterministic identifiers in your validation layer, per above). Attribute
predictions (origin, gender expression) exist to *preserve* the statistical texture of text
under replacement — never use them to profile real people.

## Credits

EECC Research Labs · Forschungszentrum Jülich (JSC, JURECA & JUPITER) · WestAI ·
mmBERT (JHU CLSP, MIT) · the ModernBERT lineage · Qwen · Gemma · GeoNames · the US SSA and
Census Bureau open statistics.

## Citation

```bibtex
@software{shinrai_pii_2026,
  author  = {Innovius AI and EECC Research Labs},
  title   = {ShinrAI PII Models: tier- and bias-aware PII detection for realm-preserving pseudonymization},
  year    = {2026},
  version = {1.1},
  url     = {https://huggingface.co/innovius}
}
```
