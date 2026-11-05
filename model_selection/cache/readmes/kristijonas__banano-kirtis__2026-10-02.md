---
license: cc-by-4.0
language:
- lt
base_model: FacebookAI/xlm-roberta-base
pipeline_tag: token-classification
tags:
- lithuanian
- kirciuoklis
- stress
- accentuation
- prosody
- tts
---

> **Superseded:** [`kristijonas/banano-kirtis-v2`](https://huggingface.co/kristijonas/banano-kirtis-v2) (xlm-roberta-large, trained on normative written-text stressing) scores 99.4 % word-exact on a 3,000-sentence held-out set where this model scores 85.4 % through the same pipeline. Use v2 unless you specifically want speech-style unstressed clitics.

# Banano kirtis 🍌 — Lithuanian stress annotator (kirčiuoklis)

Predicts, for every word in a sentence, **which syllable carries the stress**
and **which accent type** it has (trumpinis/grave, tvirtapradė/acute,
tvirtagalė/tilde) — using sentence context, not a lookup table.

Continuing the vegetable-garden lineage of open Lithuanian speech models
(svogūnas 🧅 → paprika 🌶️ → bananas 🍌).

## What it is

XLM-RoBERTa-base token classification, 37 classes:

```
0                      unstressed (clitics / function words)
1 + syllable*3 + acc   acc: 0 = short (grave), 1 = acute, 2 = tilde
                       syllable index 0..11, first sub-token of each word
```

Trained on ~1.08 M sentences from **LIEPA-3 `phon`** (stress recovered from
the case-encoded SAMPA transcriptions) plus **162 k lexicon forms** derived
from `svogunas/g2p-lt-lexicon`.

## Evaluation — read this before trusting any number

Internal held-out set (grouped by recording, same labelling convention as
training): 99.4 % exact, 99.4 % position, 99.5 % accent type.

**Treat that as a sanity check, not as accuracy.** It measures agreement with
our own labelling convention, so it cannot detect a systematic error in that
convention — and it did not: an earlier version scored equally well while
silently predicting "no stress" for words it had never seen. The fix was a
labelling correction (274 580 labels where the corpus simply omits a stress
mark were reclassified as *unknown* and excluded from the loss, instead of
being trained as "unstressed").

**No gold benchmark for Lithuanian stress exists**, open or otherwise. Nothing
here is validated against expert-adjudicated data. Spot-checking against other
tools on a handful of sentences is what we have, and it is too small a sample
to publish as a comparison — so we do not. If you have, or would help build,
an expert-annotated test set, please get in touch; that is the single most
useful thing anyone could contribute to Lithuanian accentuation right now.

## Known limitations

- **Foreign-origin surnames** are unreliable (e.g. `-sonas`); the model
  signals this with low confidence — use the confidence value.
- **Function words** (`ir`, `per`, `su`, `iš`) are predicted unstressed. This
  follows *spoken* Lithuanian, where they are clitics. Normative tools mark
  them. Neither is wrong; pick per use case (TTS → this model; teaching
  correct citation forms → a rule-based tool).
- ~9 % of words differ from VDU in accent *type* while agreeing on position.
- **No gold benchmark for Lithuanian stress exists.** Nothing here is
  validated against expert-adjudicated data, because no open set exists to
  validate against. Numbers are agreement, not accuracy.

## Usage

```python
import torch
from transformers import AutoModelForTokenClassification, AutoTokenizer

MD = "kristijonas/banano-kirtis"
tok = AutoTokenizer.from_pretrained(MD)
model = AutoModelForTokenClassification.from_pretrained(MD).eval()

words = "vyriausybė svarsto naują įstatymą".split()
enc = tok([words], is_split_into_words=True, return_tensors="pt")
with torch.no_grad():
    pred = model(**enc).logits.argmax(-1)[0]

first = {}
for pos, wid in enumerate(enc.word_ids(0)):
    if wid is not None and wid not in first:
        first[wid] = pos
for i, w in enumerate(words):
    p = int(pred[first[i]])
    if p == 0:
        print(w, "→ unstressed")
    else:
        syl, acc = (p - 1) // 3, ["short", "acute", "tilde"][(p - 1) % 3]
        print(f"{w} → syllable {syl + 1}, {acc}")
```

Rendering the Unicode combining mark onto the right vowel is a separate
presentation step, and it is where the real difficulty is — see
**Placing the mark** below for the four rules and a working implementation.

## Placing the mark (read this before using the output)

The model predicts *which syllable* and *which accent*. Turning that into
correctly marked text is a second problem, and it is the one that will cost
you an afternoon — these rules were each learned by shipping the wrong output
first.

### What the model returns

`XLMRobertaForTokenClassification`, 37 labels, one prediction per word
(take the FIRST subword token of each word):

```python
p = int(logits.argmax(-1)[first_subword_index])
if p == 0:
    stress = None                     # word carries no mark
else:
    syllable = (p - 1) // 3           # 0-based index into the word's nuclei
    accent   = ["short", "acute", "tilde"][(p - 1) % 3]
```

`short` = trumpinė (`◌̀`), `acute` = tvirtapradė (`◌́`), `tilde` = tvirtagalė (`◌̃`).

### Where the mark goes

`syllable` indexes the word's **syllable nuclei**, so you must split the word
the same way the labels were made. Four rules, each of which we got wrong at
first:

1. **Only true diphthongs merge into one nucleus:** `ai au ei ui ie uo`
   (plus `oi ou eu` in loans). Every other vowel pair is *hiatus* — two
   syllables. `teatras` is te‑a‑tras (3), not tea‑tras (2). Getting this wrong
   silently shifts the accent on every Latinate loan: we shipped `teatrãs`
   for `teãtras`.
2. **A sonorant (`l m n r`) joins the nucleus only after a SHORT vowel**
   (`a e i u`) and only when no vowel follows: `kal̃nas`, `ir̃`. After a long
   vowel it is a plain coda, so the mark stays on the vowel: `dė̃l`, not `dėl̃`.
3. **`i` before another vowel is a palatalization glide, not a nucleus
   member** — in `ia io iu iau iai iuo` the accent belongs to the vowel(s)
   after it: `dirbtiniù`, `vėliaũ`, `žaliaĩ`. Note `ie` is a REAL diphthong
   and is excluded (`priẽš`, `píeva`).
4. **Within a two-element nucleus:** tilde marks the SECOND element
   (`kaĩp`, `priẽš`), acute the FIRST (`káulas`, `píeva`). For a mixed
   diphthong the tilde sits on the sonorant (`ir̃`, `kar̃tu`).

### A working implementation

Copy freely.

```python
VOW = set("aeiouyąęėįųū"); SON = set("jlmnr"); SHORT_VOW = set("aeiu")
DIPH = {"ai","au","ei","ui","ie","uo","oi","ou","eu"}
COMB = {"short": "\u0300", "acute": "\u0301", "tilde": "\u0303"}

def nucleus_groups(word):
    w, groups, cur = word.lower(), [], []
    for i, c in enumerate(w):
        nxt = w[i+1] if i+1 < len(w) else ""
        if c in VOW:
            if not cur:
                cur = [i]; continue
            prev = w[cur[-1]]
            glide = (len(cur) == 1 and prev == "i" and cur[0] > 0
                     and w[cur[0]-1] not in VOW)
            if prev + c in DIPH or glide:
                cur.append(i)
            else:
                groups.append(cur); cur = [i]
        elif cur and c in SON and nxt not in VOW and w[cur[-1]] in SHORT_VOW:
            cur.append(i); groups.append(cur); cur = []
        else:
            if cur: groups.append(cur)
            cur = []
    if cur: groups.append(cur)
    return groups

def mark_word(word, syl, acc):
    groups = nucleus_groups(word)
    if not groups or syl >= len(groups):
        return None                      # cannot place: leave the word bare
    g = groups[syl]
    vs = [i for i in g if word[i].lower() in VOW]
    if len(vs) >= 3 and word[vs[0]].lower() == "i":
        vs = vs[1:]                      # iau / iai / iuo
    elif (len(vs) == 2 and word[vs[0]].lower() == "i"
          and (word[vs[0]] + word[vs[1]]).lower() in ("ia", "io", "iu")):
        vs = vs[1:]                      # ia / io / iu, but NOT ie
    if acc == "tilde" and len(g) > 1:
        pos = vs[1] if len(vs) >= 2 else g[-1]
    else:
        pos = vs[0] if vs else g[0]
    return word[:pos+1] + COMB[acc] + word[pos+1:]
```

### Things you should probably also do

- **Do not accent what is not Lithuanian.** Acronyms (`JAV`), digits, single
  letters (`D.`) and foreign names should be passed through untouched. We
  emitted `Ãxios` before adding a skip rule.
- **Abstain outside the training vocabulary.** The model returns a confident
  label for any input, including words it has never seen — it rendered
  *kirčiuoklis* as `kirčiuõklis` at 0.999 confidence. Confidence is not
  evidence of knowledge. Leaving unknown words unmarked is more useful than a
  fluent guess.
- **Put a lexicon in front of it.** A dictionary lookup beats the model on any
  word the dictionary has; use the model for what a dictionary cannot do —
  unseen words and homograph disambiguation from context.

## Attribution

- Base: [`FacebookAI/xlm-roberta-base`](https://huggingface.co/FacebookAI/xlm-roberta-base) (MIT)
- Speech data: **LIEPA-3** (CC BY 4.0, VDU / CLARIN-LT) — ačiū už atvirus duomenis
- Lexicon: [`svogunas/g2p-lt-lexicon`](https://huggingface.co/datasets/svogunas/g2p-lt-lexicon) (CC BY 4.0)
- Built by the [Kalamo](https://kalamo.ai) team.

Feedback, and especially hard Lithuanian test cases, are very welcome.
