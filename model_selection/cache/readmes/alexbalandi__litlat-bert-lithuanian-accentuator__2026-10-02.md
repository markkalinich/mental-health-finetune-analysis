---
language: lt
license: cc-by-sa-4.0
base_model: EMBEDDIA/litlat-bert
tags:
- lithuanian
- accentuation
- stress
- morphology
- token-classification
---

# litlat-bert-lithuanian-accentuator

Single-pass Lithuanian **accentuation + morphology** model: one encoder
(litlat-bert), one forward pass per sentence, two heads — per-token
morphological labels (804 traditional-grammar labels) and per-token
stress placement (choose the letter within the word + the accent mark:
grave/acute/circumflex, or "no stress" for unadapted foreign words).
156M parameters; ~1,660 tokens/s on a laptop RTX 3080 Ti, ~46 tokens/s
CPU int8.

Built by the open kirčiuoklė project:
https://github.com/alexbalandi/kirciuokle — architecture, training
recipes, evaluation methodology and the full experiment log are
documented there (docs/).

## Quality (measured, 2026-07)

| benchmark | metric | score |
|---|---|---|
| Kirčiuotų tekstų chrestomatija (hand-stressed gold, literary; never trained on) | token exact / position / sentence | **89.9% / 92.1% / 37.6%** |
| LRT news 37.7k tokens (audited silver reference) | token exact / position | **89.8% / 91.2%** |
| ALKSNIS gold test (morphology) | combined label / UPOS | **88.8% / 96.8%** |

Reference points on the same gold benchmark and extraction: the VDU
kirčiuoklė + UDPipe pipeline scores 95.8% token exact;
phonology_engine (LIEPA) 76.7%. Published thesis baselines on their own
extraction of the same book (indicative only): transformer 0.711,
VDU Kirčiuoklis 0.702 sequence accuracy.

## Training data & provenance

- Base training: 120k MATAS v3.0 sentences (CC BY 4.0, gold
  morphology) with stress PROJECTED from this project's own open
  accentuation dictionary (built from Wiktionary/kaikki CC BY-SA +
  published accentology rules + VLKK normative data; zero
  unadjudicated disagreements against its QA reference).
- Literary fine-tune: 220k tokens of public-domain Lithuanian classics
  (lt.wikisource; authors verified dead ≥70 years), labeled by a
  CALIBRATED consensus teacher (accept a token only where the
  agreement pattern of several independent systems measures ≥98%
  accurate on gold; achieved purity ≈99.5%). Transparency note: the
  teacher's voters include the VDU+UDPipe silver pipeline, so the
  literary fine-tune distills a consensus that contains VDU-derived
  signal; the base training does not.
- The gold benchmark was firewalled out of training (exact + 8-word
  shingle dedup; 159 sentences dropped).

## Files

- `model.safetensors` — torch weights (624.5 MB). Rebuild the
  model with `joint_lib.py` (in this repo) + EMBEDDIA/litlat-bert
  tokenizer.
- `joint.onnx` / `joint.int8.onnx` — ONNX export (537.6 MB int8),
  inputs/outputs documented in `joint.meta.json`. Torch↔ONNX parity:
  fp32 ≥99.5%, int8 ≥98% token agreement.
- `labels.json` — the 804-label morphology inventory.

## Limitations

- Foreign/unadapted words should stay unaccented; the model does this
  for ~67% of such tokens (a known regression from 76% caused by the
  literary fine-tune — literary data contains no foreign words).
- Literary/poetic register trails the VDU reference by ~6pp (was ~9pp
  before the fine-tune); archaic orthography is out of scope.
- Sentences are processed independently (max 128 subwords per
  sentence; longer sentences are truncated by the reference serving
  code).
- The stress head only proposes linguistically valid (letter, mark)
  cells (audited validity mask); it cannot express marks the standard
  language forbids.

## License & attribution

CC BY-SA 4.0. Base model: EMBEDDIA/litlat-bert. Morphology training
data: MATAS v3.0 (CC BY 4.0, CLARIN-LT). Accent supervision:
this project's open dictionary (kaikki.org Wiktionary extraction
CC BY-SA; VLKK normative resources; published accentology per the
project docs) and public-domain literary texts.

## 2026-07 update (v4): interjections fixed

Earlier releases consistently mis-stressed common interjections — `prašom` came
out as *prašõm* instead of **prãšom**, `ačiū` as *ačiū̃* instead of **ãčiū**. Root
cause: a missing abbreviation (`jstk.`) in the dataset builder's morphology
parser masked ~2,450 interjection tokens out of stress supervision. The v4
weights in this repo are retrained on corrected data: interjections are fixed
and every held-out stress metric improved (LRT audited exact 92.2% → 93.0%,
stress-type exact 88.2% → 89.4%), with POS unchanged. Details:
`docs/SPEC59.md` in the project repo.

## Pruned variant (for in-browser / edge inference)

`pruned/` holds a vocabulary-pruned int8 build of this exact model,
meant for shipping to a browser (onnxruntime-web) or any size-sensitive
deployment.

**How it was pruned.** litlat-bert is trilingual (Lithuanian, Latvian,
English), so most of its ~84k SentencePiece vocabulary never fires on
Lithuanian text. We tokenized the whole open dictionary (~575k words)
plus every corpus used in the project and kept only the pieces that were
ever produced — **62,273 of 84,201 embedding rows** — plus, as a safety
floor, every special token, every ≤2-character piece, and the BPE
merge-path pieces the retained ones depend on. The ~22k dropped rows are
overwhelmingly Latvian/English-specific subwords. Removing an unused
embedding row is mathematically lossless for any input that doesn't
tokenize through it; a held-out segmentation census matched the full
tokenizer on **99.99%** of tokens.

The result is **quality-lossless**: chrestomatija-gold, audited-LRT and
ALKSNIS scores all land within ~0.02pp of the full model, and
foreign-word abstention is within ~0.4pp. Only the embedding matrix
shrank (it is ~43% of the encoder).

| file | what | size |
|---|---|---|
| `pruned/joint.int8.partial.onnx` | **recommended** int8 (parity-safe scope), 99.2% token agreement vs torch | ~470 MB |
| `pruned/joint.int8.full.onnx` | fully dynamic int8 — smaller/faster, 96.8% agreement | ~140 MB |
| `pruned/tokenizer.json` (+ configs) | the **matching pruned tokenizer** — required with the pruned weights | ~2 MB |
| `pruned/joint.meta.json` | char vocab + label metadata for decoding | — |

Use `pruned/tokenizer.json` with the pruned weights — the root-level
`tokenizer.json` is the full-vocabulary tokenizer and its ids do **not**
line up with the pruned embedding. Everything else (the I/O contract,
decoding, `label_bridge.json`) is identical to the full model.

