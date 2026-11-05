---
license: cc-by-4.0
language:
- lt
base_model: FacebookAI/xlm-roberta-large
pipeline_tag: token-classification
datasets:
- meldynamics/lt-stressed-corpus
tags:
- lithuanian
- kirciuoklis
- stress
- accentuation
- prosody
- tts
---

# Banano kirtis v2 🍌 — Lithuanian stress annotator (kirčiuoklis)

Predicts, for every word in a sentence, **which syllable carries the stress**
and **which accent type** it has (trumpinė/grave, tvirtapradė/acute,
tvirtagalė/tilde) — from sentence context, so homographs come out right:
*kasojè* … *šuõ **kãsa** duõbę*, *màno brólis **mãno***, *dù **sū́nus** … vyrèsnis
**sūnùs***, *šiõs **kalbõs** … vìsos **kal̃bos***.

v2 replaces [`kristijonas/banano-kirtis`](https://huggingface.co/kristijonas/banano-kirtis)
(v1). Same label scheme, different base (large instead of base) and — the
part that matters — different training data: written text stressed through a
morphology-aware pipeline instead of stress recovered from speech transcriptions.

Vegetable-garden lineage of open Lithuanian speech models:
svogūnas 🧅 → paprika 🌶️ → bananas 🍌.

## What it is

`XLMRobertaForTokenClassification`, 37 classes, one prediction per word
(first sub-token):

```
0                      no mark on this word
1 + syllable*3 + acc   acc: 0 = short/grave, 1 = acute, 2 = tilde
                       syllable = 0-based index of the stressed syllable nucleus
```

Fine-tuned from `FacebookAI/xlm-roberta-large` on
[`meldynamics/lt-stressed-corpus`](https://huggingface.co/datasets/meldynamics/lt-stressed-corpus):
108,324 sentences / 1.14 M labelled words from the MATAS and ALKSNIS corpora.
Those corpora carry morphology, not stress: the stress was added by the dataset's
author, who queried the VDU Kirtis service for candidate stressed forms and matched
their morphological labels against the corpus's own (manually checked) annotation.
So the marks are automatic but morphology-aware, not hand-placed. Tokens whose
stress came from either fallback path (`phonology_engine`, `lki.words`, together
~0.4% of word tokens) were excluded from the loss, as were digits and
multiple-best ties. 6 epochs, lr 2e-5, batch 32, max 256 tokens, bf16,
one A100, ~30 min.

## Evaluation — what the numbers mean

3,000 held-out corpus sentences (28,883 words), never seen in training:

| | word-exact | sentence-exact |
|---|---|---|
| model alone, words the corpus marks (label match) | 99.5 % (position 99.6 %) | – |
| model alone, full text string comparison | 97.8 % | 82 % |
| model + corpus lexicon in front (`kirtis_v2.py`, recommended) | **99.4 %** | **94.7 %** |
| v1 (`banano-kirtis`) through the same pipeline, same set | 85.4 % | 33 % |

Remaining errors in the recommended setup: 0.41 % wrong syllable, 0.09 % right
syllable / wrong accent type. Most of the model-alone gap (1.6 %) is single
letters and abbreviations that the corpus leaves bare — the lexicon layer
handles them.

**These are agreement with the corpus's stressing, not verified accuracy.**
There is still no expert-adjudicated open benchmark for Lithuanian stress.
The corpus is large and consistent, which is why the number is useful; it is
not human-verified truth. The v1 gap is partly convention: v1 learnt from
speech, where clitics are unstressed; v2 marks function words the normative
way (*ir̃, sù, priẽ, õ*). If you have, or would help build, an expert-annotated
test set, please get in touch.

## Known limitations

- **Foreign names** (`Rossi`, `Wildberries`): the model tends to leave them
  unmarked, which is the safe behaviour; check confidence.
- **Rare homograph readings** lose to the frequent one when context is thin:
  the verb *gė́lė* ("it ached") comes out as the noun *gėlė̃* (10:1 in the
  corpus).
- **Acronyms, digits, single letters** should be passed through untouched
  before calling the model (see below).
- About 3× slower than v1 (560 M parameters): ~55 ms per sentence on a
  laptop CPU, ~0.5 ms batched on an A100.

## Usage

```python
import torch
from transformers import AutoModelForTokenClassification, AutoTokenizer

MD = "kristijonas/banano-kirtis-v2"
tok = AutoTokenizer.from_pretrained(MD)
model = AutoModelForTokenClassification.from_pretrained(MD).eval()

words = "Mano brolis mano , kad rytoj lis .".split()
enc = tok([words], is_split_into_words=True, return_tensors="pt")
with torch.no_grad():
    pred = model(**enc).logits.argmax(-1)[0]

first = {}
for pos, wid in enumerate(enc.word_ids(0)):
    if wid is not None and wid not in first:
        first[wid] = pos
for i, w in enumerate(words):
    if not w[0].isalpha():
        continue                          # punctuation is context only; its label is noise
    p = int(pred[first[i]])
    if p == 0:
        print(w, "→ no mark")
    else:
        syl, acc = (p - 1) // 3, ["short", "acute", "tilde"][(p - 1) % 3]
        print(f"{w} → syllable {syl + 1}, {acc}")
```

Feed words **cased**, punctuation as its own tokens (it is context). Rendering
the combining mark onto the right letter is a separate step — see below; it
is where most of the difficulty is.

### Recommended: a lexicon in front

The model is best used behind a dictionary built from the same corpus:
forms with a single attested stress (130 k) come from the lexicon, forms with
several attested stresses (1.8 k homographs) let the model choose among the
attested variants, everything else (out-of-vocabulary words, names) goes to
the model. That is the 99.4 % row above. The reference implementation
(`kirtis_v2.py`, `rules.py`, `build_lexicon.py`) is in the training repo
and is short; the lexicon is a plain JSON `form → (syllable, accent)`.

## Placing the mark

`syllable` indexes the word's **syllable nuclei**, so you must split the word
the same way the labels were made. The rules (each learnt by shipping the wrong
output first):

1. **Only true diphthongs merge into one nucleus:** `ai au ei ui ie uo`
   (plus `oi ou eu` in loans). Every other vowel pair is hiatus — two
   syllables (*te-a-tras*).
2. **A sonorant (`l m n r`) joins the nucleus only after a SHORT vowel**
   (`a e i u`) and only when no vowel follows: *kal̃nas*, *ir̃*; after a long
   vowel it is a plain coda: *dė̃l*.
3. **`i` after a consonant and before `a ą o u ų ū` is a palatalization
   glide**, not a nucleus member: *dirbtiniù*, *vėliaũ*, *siū́lo*. Before
   `i e ė` it is a real syllable (*pri-i-ma*, *pasi-ė-mė*); `ie` is a real
   diphthong (*priẽš*, *píeva*).
4. **Within a two-element nucleus:** acute on the FIRST element (*káulas*,
   *píeva*), grave on the SECOND (*Ukraìna*), tilde on the SECOND vowel
   (*kaĩp*, *priẽš*) or on the sonorant of a mixed diphthong (*ir̃*, *kar̃tu*,
   *klieñtas*) — except native `ie`/`uo` + sonorant, where it stays on the
   vowel (*kasdiẽn*, *dviẽm*).

This implementation round-trips 99.95 % of the 1.16 M corpus tokens
(label → mark → label). Copy freely.

```python
VOW = set("aeiouyąęėįųū"); SON = set("jlmnr"); SHORT_VOW = set("aeiu")
DIPH = {"ai", "au", "ei", "ui", "ie", "uo", "oi", "ou", "eu"}
GLIDE_VOW = set("aąoųuū")
COMB = {"short": "̀", "acute": "́", "tilde": "̃"}

def nucleus_groups(word):
    w, groups, cur = word.lower(), [], []
    for i, c in enumerate(w):
        nxt = w[i + 1] if i + 1 < len(w) else ""
        if c in VOW:
            if not cur:
                cur = [i]; continue
            prev = w[cur[-1]]
            glide = (len(cur) == 1 and prev == "i" and cur[0] > 0
                     and w[cur[0] - 1] not in VOW and c in GLIDE_VOW)
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
        return word                      # cannot place: leave the word bare
    g = groups[syl]; w = word.lower()
    vowels = [i for i in g if w[i] in VOW]
    if (len(vowels) >= 2 and w[vowels[0]] == "i" and w[vowels[1]] in GLIDE_VOW
            and (vowels[0] == 0 or w[vowels[0] - 1] not in VOW)):
        vowels = vowels[1:]              # glide i: the accent belongs to the next vowel
    if acc == "tilde" and len(g) > 1:
        if w[g[-1]] in SON:
            after = w[g[-1] + 1] if g[-1] + 1 < len(w) else ""
            if (len(vowels) >= 2 and w[vowels[0]] + w[vowels[1]] in ("ie", "uo")
                    and not (w[vowels[0]] == "i" and after == "t")):
                pos = vowels[1]
            else:
                pos = g[-1]
        else:
            pos = vowels[1] if len(vowels) >= 2 else g[-1]
    elif acc == "short" and len(vowels) >= 2:
        pos = vowels[1]
    else:
        pos = vowels[0] if vowels else g[0]
    return word[:pos + 1] + COMB[acc] + word[pos + 1:]
```

Output is NFC-normalised by most toolchains (`à` becomes one code point).
For TTS training data that keeps combining marks separate, normalise the way
your corpus does.

### Things you should also do

- **Do not accent what is not Lithuanian.** Acronyms (`JAV`), digits, single
  letters (`D.`) and foreign names: pass them through untouched.
- **Do not trust confidence as knowledge.** The model returns a confident label
  for any input; leaving an unknown word unmarked is more useful than a fluent
  guess.

## Attribution

- Base: [`FacebookAI/xlm-roberta-large`](https://huggingface.co/FacebookAI/xlm-roberta-large) (MIT)
- Training data: [`meldynamics/lt-stressed-corpus`](https://huggingface.co/datasets/meldynamics/lt-stressed-corpus),
  built by [Aleksas Pielikis](https://github.com/aleksas) from the **MATAS** and
  **ALKSNIS** corpora (VDU / CLARIN-LT, CC BY 4.0), with the stress added via the VDU
  Kirtis service and his [`vdu-nlp-services`](https://github.com/aleksas/vdu-nlp-services)
  — ačiū už atvirus duomenis.
- Built by the [Kalamo](https://kalamo.ai) team.

Feedback, and especially hard Lithuanian test cases, are very welcome.
