---
license: apache-2.0
language: [de, en, it, fr, es, pl]
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
# This repo stays ungated: v1.2 is the permanently open Apache 2.0 tier (ADR-0009).
---

<img src="https://huggingface.co/spaces/innovius/README/resolve/main/shinrai-logo.png" width="104" alt="ShinrAI — shield logo" align="right">

# shinrai-pii-m-v1.2

**You use the AI. The AI does not use you.**

> **Superseded by [`shinrai-pii-m-v1.3`](https://huggingface.co/innovius/shinrai-pii-m-v1.3)**
> and by ShinrAI 1.5 in the managed API at [getshinrai.com](https://getshinrai.com)
> for every language this model covers — 15 locales, 19 heads, format detection, Japanese
> back at flagship quality. v1.2 remains available as the archived western-six generation.

> 🔓 **License: v1.2 is and remains Apache 2.0 — the permanently open tier.**
> The v1.3 flagship ships under the [Innovius Open License v1.0](https://innovius.ai/shinrai/open-license.html)
> (free for government, education, research, and companies under $10M revenue;
> it converts to Apache 2.0 on 2028-09-01).

M-size ShinrAI encryption model — the detection layer of ShinrAI **semantic encryption**
(ShinrAI, 信頼, is Japanese for *trust*), and the **western-six generation**: German,
English, Italian, French, Spanish and Polish, with a 1024-token window and inventories at
Wikidata/OpenStreetMap scale.

Architecture: ModernBERT-family `mmBERT-base` encoder with a multi-head token classifier —
PERSON / CITY / STREET / ORG spans with frequency/size **tiers** and span attributes
(**origin**, **gender expression**, **name part**) for realm-preserving pseudonymization:
detected entities are swapped for natural alternatives matched to context, culture and
language (never `[MASK]` wreckage, never bias-triggering hard cuts), so downstream AI keeps
reasoning over natural text. Suited to mass de-identification (ePA / clinical,
high-security, banking) as well as realtime protection.

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

Given text in any of the six languages, the model emits entity spans with rich attributes:
entity class, a frequency/size tier (how common a name is, how large a city is), cultural
origin, gender expression and name-part structure. This is what enables **realm-preserving
replacement**: `Robert` → `Paul` — a substitute matching the original's cultural register,
frequency tier and gender expression, with no visible trace that anything was replaced and
minimal bias distortion for the consuming model.

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
knowing that *Keller* is a surname here and a basement there, that *8 avenue Victor Hugo*
is an address, how identifying each entity is, and what a culturally consistent replacement
looks like. That is what statistical models are for.

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
forms), measured for this exact checkpoint. The suites draw on Wikidata/OSM-scale entity
inventories — on these same suites the previous generation (v1.1) reads 33.6–49.3 macro.
**Register matters**: these are business/medical *register* documents; on encyclopedic
register (Wikipedia-class prose) the same checkpoint reads substantially lower
(37.7–70.4 strict, measured 2026-08) — a known register deficit, addressed in v1.3:

![Entity detection by language](assets/perf-entities.png)

| suite | PERSON | CITY | STREET | ORG | **macro** | tier acc |
|---|---|---|---|---|---|---|
| de | 91.6 | 92.6 | 92.3 | 92.4 | **92.2** | 68.5 |
| en | 97.2 | 93.8 | 95.9 | 90.5 | **94.3** | 58.7 |
| it | 95.5 | 92.0 | 94.9 | 88.4 | **92.7** | 49.7 |
| fr | 95.9 | 94.7 | 93.9 | 93.0 | **94.4** | 49.6 |
| es | 96.9 | 90.0 | 95.8 | 93.8 | **94.1** | 53.8 |
| pl | 93.8 | 81.9 | 91.4 | 89.9 | **89.2** | 56.7 |

Attribute accuracy on detected spans (these steer replacement selection):

![Replacement-steering attributes](assets/attributes.png)

| suite | origin | gender expression | name part |
|---|---|---|---|
| de | 92.4 | 88.1 | 98.7 |
| en | 87.5 | 84.6 | 95.1 |
| it | 95.0 | 85.6 | 97.2 |
| fr | 93.8 | 87.1 | 95.7 |
| es | 95.2 | 91.4 | 97.2 |
| pl | 94.8 | 84.9 | 94.6 |

### What's new vs v1.1

- **Six western languages** (was de/en/ja), each backed by real-world inventories:
  a Wikidata-scale organization inventory (CC0), real OpenStreetMap street inventories,
  and registry-backed person-name statistics for all six languages.
- **1024-token training/inference window** (was 512) — full letters fit in one window;
  sliding-window inference with overlap merge still handles documents of any length.
- **ORG generalization fixed**: 88.4–93.8 F1 (v1.1: 56.6–68.9).
- Improved recall on letter sign-offs, letterhead address blocks and full-name spans
  (one span per name, `name_part: full`).

### Known limitations

- **Polish is the weakest track** (macro 89.2; CITY 81.9 — declined city forms from the
  long tail). 
- **Tier accuracy on the new languages is 50–69** — tier band recalibration against the
  much larger v1.2 inventories is queued; span detection is unaffected.
- **Clinical narrative is not this generation's home turf**: on real doctor-letter
  corpora, PERSON recall drops noticeably below the business-document numbers above
  (see "How it compares"). For clinical de-identification at scale, our Enterprise ePA
  pipeline layers this model with additional safeguards; a dedicated clinical track is
  queued.
- **Japanese is not covered by this model.** The western pivot cost ja performance
  (60.8 macro vs v1.1's 83.8) — **route Japanese traffic to
  [`shinrai-pii-m-v1.3`](https://huggingface.co/innovius/shinrai-pii-m-v1.3)**
  (ja register F1 98.1).

## How it compares

**Against public PII models.** We benchmarked the strongest openly released PII models we
could find on this model's serving suites — the OpenMed-PII family (clinical-domain
de-identification, RoBERTa/DeBERTa-class encoders), taking the best in-language checkpoint
per suite (SuperClinical-434M / SnowflakeMed-568M class). Identical scoring pipeline,
span-level concept intersection over {PERSON, CITY, STREET, ORG}, measured 2026-08.
Macro span F1:

| suite | best in-language OpenMed-PII | shinrai v1.2 |
|---|---|---|
| de | 35.7 | **92.2** |
| en | 70.6 | **94.3** |
| it | 28.0 | **92.7** |
| fr | 24.2 | **94.4** |
| es | 46.4 | **94.1** |
| pl | — (no PII model exists) | **89.2** |

Read it fairly, in both directions:

- Our suites are multilingual business/medical documents — outside OpenMed's clinical home
  domain. On **English** their flagship stays genuinely competitive on PERSON/CITY/STREET
  (80–83 F1); outside English, in-language performance collapses, and **ORG** is a
  systematic blind spot of every PII tagger we measured (0–39 F1 in-language). For
  **Polish** no comparable PII model exists at all; the strongest cross-lingual zero-shot
  probe reads 4–30 F1 per category there.
- On **their** home turf — real German clinical narrative (GraSCCo, which is eval-only for
  us) — OpenMed's German flagship outperforms both public ShinrAI generations on PERSON
  recall and aggregate F1, and at a matched decision threshold the over-redaction rates
  are comparable (measured on CPU, 2026-07). What survives as our measured edge there is
  **calibration**: threshold-free separation AUC puts the ShinrAI v1.1 checkpoint first
  of all 18 checkpoints compared (0.8945), with every ShinrAI checkpoint above every
  OpenMed German checkpoint. If your workload is pure clinical de-identification inside
  OpenMed's domain, a clinical specialist is a strong choice there; our Enterprise ePA
  pipeline layers this model with additional safeguards for exactly that reason.
- Generic **RoBERTa/DeBERTa-class PII taggers** solve a different, smaller problem: flat
  entity labels, usually English-first. None of the models we measured emit what
  replacement needs — frequency/size tiers, cultural origin, gender expression, name-part
  structure, calibrated confidences. Detection is table stakes; ShinrAI's job is making
  the *replacement* invisible.

**Against v1.1**
([`shinrai-pii-m-v1.1`](https://huggingface.co/innovius/shinrai-pii-m-v1.1)):
this model supersedes it for German and English — 92.2 / 94.3 macro where v1.1 reads
33.6–49.3 on these harder suites — adds Italian, French, Spanish and Polish, doubles the
window to 1024 tokens and fixes ORG generalization (88.4–93.8 vs 56.6–68.9; feature
details under "What's new"). **Japanese**: 83.8 macro on v1.1 against 60.8 here — both
superseded by v1.3's dedicated ja track (98.1 register F1).

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
delta 2.8e-05 across all 7 output heads — `quant/parity-onnx.json`):

| suite | FP32 (1.23 GB) | Q8 (**309 MB**) | Δ | Q4 (spot checks¹) |
|---|---|---|---|---|
| de | 92.35 | 92.38 | +0.03 | 91.15 |
| en | 94.45 | 94.45 | ±0.00 | — |
| it | 92.75 | 92.55 | −0.20 | — |
| fr | 94.18 | 94.07 | −0.10 | — |
| es | 94.05 | 94.20 | +0.15 | — |
| pl | 89.40 | 89.10 | −0.30 | 88.65 |

**Q8 is the serving baseline for all six languages**: within ±0.33 macro-F1 of FP32 on
every suite (several improve), 4× smaller, CPU-friendly.

¹ Q4 was measured during release QA (0.75–2.1 macro points below FP32) but the artifact
does not ship in this repo — v1.1's Q4 build is available today, and a v1.x point
release carries the next ladder.

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
inputs/outputs, works with `onnxruntime` alone; ≥ 1.28 for the Q4 file), or the ShinrAI
inference SDK (sliding-window batching, IOB2 decoding, span merging, calibration — pip
package planned):

```python
import onnxruntime as ort
from transformers import AutoTokenizer

repo = "innovius/shinrai-pii-m-v1.2"  # local: path to a clone
tok = AutoTokenizer.from_pretrained(repo, subfolder="tokenizer")
sess = ort.InferenceSession("quant/model-q8.onnx")

enc = tok("Le dossier de Mme Claire Dubois, 8 avenue Victor Hugo, Lyon, est complet.",
          return_tensors="np")
out = sess.run(None, {"input_ids": enc.input_ids, "attention_mask": enc.attention_mask})
# 7 named outputs:
#   logits_person / logits_city / logits_street / logits_org   [batch, seq, 7]  (IOB2 × 3 tiers + O)
#   attr_logits_origin [.., 42] · attr_logits_gender_expression [.., 4] · attr_logits_name_part [.., 3]
# label inventories for decoding: labels-v2.0.yaml
```

Decoded output (via the ShinrAI predictor, verified against this exact checkpoint) for
`"Le dossier de Mme Claire Dubois, 8 avenue Victor Hugo, Lyon, est complet."`:

```json
{"span": [18, 31], "text": "Claire Dubois",        "type": "PERSON", "tier": "common",  "confidence": 0.941,
 "attrs": {"origin": "FR", "gender_expression": "unknown", "name_part": "family"}}
{"span": [33, 53], "text": "8 avenue Victor Hugo", "type": "STREET", "tier": "generic", "confidence": 0.852,
 "attrs": {"origin": "FR"}}
{"span": [55, 59], "text": "Lyon",                 "type": "CITY",   "tier": "medium",  "confidence": 0.848,
 "attrs": {"origin": "FR"}}
```

and for `"Bitte senden Sie den Bericht an Frau Dr. Anna Keller, Lindenweg 12, 04109 Leipzig."`:

```json
{"span": [41, 52], "text": "Anna Keller",  "type": "PERSON", "tier": "common",   "confidence": 0.959,
 "attrs": {"origin": "DE", "gender_expression": "fem", "name_part": "full"}}
{"span": [54, 66], "text": "Lindenweg 12", "type": "STREET", "tier": "specific", "confidence": 0.770,
 "attrs": {"origin": "DE"}}
{"span": [74, 81], "text": "Leipzig",      "type": "CITY",   "tier": "medium",   "confidence": 0.989,
 "attrs": {"origin": "DE"}}
```

Note what is *not* in the output: the postal code `04109`. Deterministic identifiers are
your validation layer's job (see the pipeline section) — by design, not omission.

Inference is sliding-window (window 1024, stride 128, overlap merge) — documents of any
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

![ShinrAI Connector running a ShinrAI model locally](assets/shinrai-connector.png)

*The Connector running the v1.1 sibling on a Mac — 0.12 GB in memory, CPU-only; this model
slots in the same way, with the deterministic categories (banking and cards, crypto
wallets, ID numbers, contact details) handled by the Connector's software layer, exactly
as described above.*

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

The training corpus is **synthetic**: generated, cross-checked and quality-gated by openly
released models — for this generation primarily the Mistral, Gemma (Google DeepMind) and
NVIDIA Nemotron families — and anchored in open data: GeoNames (CC-BY), Wikidata (CC0),
OpenStreetMap (ODbL), US SSA/Census name statistics (public domain) and national open-data
sources (INSEE, INE, PESEL, Italian and German municipal portals). No customer data, no
scraped personal records, no proprietary APIs anywhere in the pipeline.

Provenance note: during v1.3 preparation we found and fixed a labeling defect in the
v1.1-era generation pipeline (unlabeled person names in a subset of LLM-generated
records). The v1.2 corpus was regenerated with the fixed pipeline and re-audited to
0.00% unlabeled person names across all six languages before this checkpoint trained.

Every record carries a license-provenance field; released datasets contain only the
license-clean subset (CC0 / CC-BY / public-domain / our own generated text). Data releases:
https://huggingface.co/innovius (as they land).

## Privacy & responsible use

The model detects and helps pseudonymize personal data; it does not memorize real
individuals — training text is synthetic. Detection is probabilistic: for regulated
deployments, treat it as one layer of a defense-in-depth privacy architecture, not a sole
control (and keep deterministic identifiers in your validation layer, per above). Attribute
predictions (origin, gender expression) exist to *preserve* the statistical texture of text
under replacement — never use them to profile real people.

## Credits

EECC Research Labs · Forschungszentrum Jülich (JSC, JURECA & JUPITER) · WestAI ·
mmBERT (JHU CLSP, MIT) · the ModernBERT lineage · Mistral · Gemma · NVIDIA Nemotron ·
GeoNames · Wikidata · OpenStreetMap · the statistics offices and open-data portals of the
countries we cover.

## Citation

```bibtex
@software{shinrai_pii_2026,
  author  = {Innovius AI and EECC Research Labs},
  title   = {ShinrAI PII Models: tier- and bias-aware PII detection for realm-preserving pseudonymization},
  year    = {2026},
  version = {1.2},
  url     = {https://huggingface.co/innovius}
}
```
