---
license: mit
base_model: microsoft/deberta-v3-base
language:
- en
pipeline_tag: text-classification
library_name: transformers
tags:
- text-classification
- safety
- content-moderation
- image-generation
- deberta-v2
- pytorch
---

# ComfyUI Junior Prompt Safety Classifier

A compact semantic classifier for **text-to-image prompts**. It reads a prompt and
estimates, on six independent ordinal axes, what an image generated from that prompt
would depict. It was developed for a child-facing image-generation appliance
(roughly age 12+), but the model and the policy are deliberately separable: the six
dimensions and their ordinal levels are the model's output, and the shipped block
thresholds are one opinion layered on top of them.

If you want a prompt-screening signal without inheriting someone else's product
boundary, use the levels and write your own thresholds.

> **Release note — this repo changed architecture.**
> Revisions before September 2026 held a provisional v0.7 draft: a 6-layer
> `distilbert-base-uncased` with `[CLS]` pooling and raw linear outputs. This release
> replaces it with **v29db**, a 12-layer DeBERTa-v3 with mean pooling and ordinal
> heads. Pooling, activation, tokenizer and one head width all changed. **Code
> written against v0.7 will silently produce wrong numbers.** The stale `vocab.txt`
> has been removed. Pin a revision if you need the old behaviour.

## What the outputs are

Six heads, one per dimension, each **cumulative-logit ordinal** — not regression, and
not multi-class. Each head emits one logit per threshold. Apply `sigmoid`, then read
the level as *the number of leading thresholds above 0.5*, stopping at the first gap.

| Dimension | Head width | Levels | Level 1 | Level 2 | Level 3 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| `sexual` | 3 | 0–3 | suggestive / appealing | deliberate sexualisation | explicit |
| `nudity` | 2 | 0–2 | partial, incidental | substantial exposure | — |
| `violence_gore` | 2 | 0–2 | combat, action, stylised | bodies meaningfully damaged | — |
| `substances` | 2 | 0–2 | incidental (wine glass, noir cigarette) | depicted use or abuse | — |
| `disturbing` | 2 | 0–2 | dark / macabre / gothic aesthetic | depravity given real weight | — |
| `fetish` | 2 | 0–2 | gear, framing, coded presentation | explicit fetish focus | — |

`sexual` is the only width-3 head. Level 1 is designed to mean *genuinely safe* on
every axis — the classifier is forced to be sharp rather than allowed to hedge.

## Architecture

Not a stock `AutoModelForSequenceClassification`. The forward path is:

```
tokenize (max_length=256)
  -> DeBERTa-v3-base encoder, last_hidden_state
  -> MASKED MEAN pooling over the sequence      <- not [CLS]
  -> six independent nn.Linear heads (768 -> width), loaded from heads.pt
  -> sigmoid
  -> ordinal decode to a level per dimension
```

Two-view inference: the prompt is classified **twice** — raw, and canonicalised
(NFKC, zero-width strip, homoglyph folding, conservative leet folding, spaced-letter
collapse) — taking the per-dimension maximum. This closes a character-substitution
bypass where `n4k3d ...` scored below a benign prompt while the downstream T5 text
encoder still rendered it.

This two-view path is the **reference parity path** for this release: the published
weights were parity-qualified against it, and `canonicalize.py` is published so that
result can be reproduced exactly. It is not the only sound way to deploy the model.
Later serving evaluation found that a narrower input-envelope gate combined with
**single-view** inference was faster and produced equal or better measured safety
behaviour on the sets tested — see the deployment profile below. That is a serving
choice; it does not alter the frozen weights.

Three details are load-bearing and easy to get wrong: **mean pooling** (not `[CLS]`),
**sigmoid + ordinal decode** (not raw regression values), and the **second view**.

## Usage

```python
from junior_safety import SafetyClassifier

model = SafetyClassifier.from_pretrained("mitchins/comfyui-junior-safety")
r = model.classify("A cute penguin under a starry vortex sky")

print(r.levels)      # {'sexual': 0, 'nudity': 0, ... }
print(r.raw_scores)  # per-threshold sigmoid probabilities
print(r.decision)    # 'pass'
print(r.reasons)     # []
```

`junior_safety.py` and `canonicalize.py` are plain Python in this repo — no
`trust_remote_code`. Copy them in, or `hf_hub_download` them.

<details>
<summary>Equivalent plain Transformers / PyTorch</summary>

```python
import torch, torch.nn as nn
from transformers import AutoModel, AutoTokenizer
from huggingface_hub import hf_hub_download

repo = "mitchins/comfyui-junior-safety"
tok = AutoTokenizer.from_pretrained(repo)
enc = AutoModel.from_pretrained(repo).eval()

ck = torch.load(hf_hub_download(repo, "heads.pt"),
                map_location="cpu", weights_only=True)
dims, widths = ck["dims"], ck["widths"]
heads = nn.ModuleList([nn.Linear(768, w) for w in widths])
heads.load_state_dict(ck["heads"])
heads.eval()

e = tok("a soldier pointing a rifle at a civilian", truncation=True,
        max_length=256, padding=True, return_tensors="pt")
with torch.no_grad():
    h = enc(**e).last_hidden_state
    m = e["attention_mask"].unsqueeze(-1).float()
    pooled = (h * m).sum(1) / m.sum(1).clamp(min=1e-9)   # masked mean, NOT [CLS]
    for d, head in zip(dims, heads):
        p = torch.sigmoid(head(pooled))[0]
        lvl = 0
        for j in range(p.shape[0]):
            if float(p[j]) > 0.5: lvl = j + 1
            else: break
        print(f"{d:14s} level {lvl}  probs {[round(float(x),3) for x in p]}")
```

This single-view snippet omits the canonicalised second view; use it to inspect the
encoder, not as the serving path.
</details>

## The shipped policy (separable, and binary)

```
BLOCK_AT = {"sexual": 2, "nudity": 2, "violence_gore": 2,
            "substances": 2, "disturbing": 2, "fetish": 1}
block  iff  any(level >= BLOCK_AT[dim])
```

`fetish` blocks at 1 because level 1 there already means coded fetish presentation.
Everything else needs level 2.

**There is no ROUTE tier, by design.** Earlier revisions carried a soft band for
human review. With no reviewer in the product, ROUTE resolved to BLOCK — refusing
7.07% of natural traffic at a level the rubric itself defines as not unsafe. Worse,
having somewhere to park an undecided item meant items got parked: a large share of
the route-only band was content that belonged at a definite level on some axis and
was hedged instead. Removing the tier forced those to resolve. If your product has a
reviewer, a soft band is reasonable — build it from the levels, which are published
precisely so you can.

## Evaluation

The meaningful audit is a **random population sample**, not a curated benchmark.
400 prompts drawn unstratified from the corpus, judged blind on `disturbing` and
`violence_gore` by an independent LLM judge with no access to the labels, the model,
or the disagreement history:

| | rate |
| :-- | :-- |
| corpus-label block rate | 2.75% |
| blind-judge block rate | 2.75% |
| **v29db block rate** | **3.00%** |
| corpus under-label rate | 1.00% (95% CI 0.39–2.54%) |
| corpus over-label rate | 1.00% |
| high-confidence under-labels | **0 / 400** |

Under- and over-labelling are the same magnitude in opposite directions, and the
corpus and the judge block at an identical rate: no systematic boundary displacement
on those axes. The residual disagreement is low-rate boundary noise, and the model's
own errors fell on the same items where the labels and the judge disagree — it tracks
its supervision rather than adding error of its own.

**Read that as a population rate, and nothing else as one.** Enriched, adversarial and
disagreement-stratified sets are constructed to be hard and will report error rates
many times higher; that is what they are for. In this project a disagreement-stratified
sample reported 81%/75% under-labelling on the same two axes where the population rate
was 1.0%. Do not quote hard-set numbers as normal-traffic performance.

No per-dimension F1 is published. Error counts on small enriched strata moved F1
around far more than they moved the number of actual mistakes, and reporting it
invites exactly the misreading above.

## ComfyUI Junior deployment profile

These are **serving-policy controls, not learned dimensions of v29db.** The model
itself has six dimensions and a binary policy; everything in this section sits in
front of it and can be replaced without touching the weights.

```
well-formedness gate      -> prompt_format_invalid    "write it normally"
English-envelope gate     -> unsupported_language     "write it in English"
single-view v29db + policy_v6 -> content_policy_violation
else                      -> pass
```

**Language support.** The semantic model is English-only. ComfyUI Junior does not
claim multilingual moderation support. In the Junior serving profile, prompts that
appear substantially non-English are rejected *before* semantic classification with
`unsupported_language`, and clearly obfuscated or malformed prompts are rejected
with `prompt_format_invalid`. The envelope gate is fastText `lid.176`
(Meta/Facebook, distributed separately) thresholded at 0.30 on P(non-English).

The three outcomes are kept distinct on purpose. "Write it properly", "write it in
English" and "that content isn't available" are different user problems and should
never be collapsed into a single counter.

### Measured serving behaviour

| | |
| :-- | :-- |
| English false-rejection, full input gate | 0.200% (n=5,000 held-out English) |
| … English prompts containing non-ASCII | 0.60% (n=3,000) |
| non-English gated before the model | 93.1% (n=2,712) |
| red-team must-stop | 149/153 = 97.4% |
| 13-language concept stress test | 0/39 leaks |

The red-team figure excludes one prompt that was adjudicated as correctly
permissible. The four remaining misses are **semantic** — euphemism, implication,
and a payload buried in long benign prose. No input gate addresses those.

**Observed complementarity** (an observation on one corpus, not a guarantee): 186
non-English prompts got past the language gate and reached v29db. The model blocked
47 of them, and none of the remainder were labelled unsafe — so nothing unsafe and
non-English reached the generator in this corpus. The prompts the language gate
misses tend to be the ones that look most English-like, which are also the ones the
semantic model can still read. This is a measured property of one corpus, not a
guarantee about unseen input.

Two gate details matter for anyone reimplementing this. Language ID runs on the
**Latin-script portion only** — feeding CJK characters to `lid.176` makes it call
`a shrine in 東京, cherry blossoms` Japanese at p=0.58, and English tag lists with
Japanese hashtags Japanese at p=0.89; both must pass. And the zero-width-character
check requires a Latin letter on **both** sides, because a zero-width character at a
word boundary is an ordinary copy-paste artifact rather than evasion.

### Known limitations of this profile

- **Latin-script non-English input may reach v29db.** German, Dutch and Polish in
  particular are not reliably caught by the envelope gate, and Junior does not claim
  those languages are supported. Coverage by the semantic model is inconsistent
  across languages and was not designed.
- **Short prompts are the weak slice.** English prompts under 80 characters are
  wrongly gated at roughly five times the overall rate. The failure direction is a
  benign English prompt being asked to rewrite — not an unsafe prompt getting
  through. Prompts carrying non-ASCII characters are similarly elevated (0.60%).
- The block rate on any particular corpus is a property of that traffic. Do not read
  the rates above as an estimate of end-user traffic composition.

## Intended use

Semantic **pre-generation prompt screening** for image-generation systems: flagging
requests for sexual or erotic material, nudity, violence and gore, controlled-drug
imagery, disturbing content, and fetish content before an image is produced.

Designed for child-facing image-generation safety filtering.

**It is explicitly not:**

- a CSAM or CSAE classifier. Minor-age inference is not its purpose and it must not
  be deployed as that control.
- a general text-toxicity model. It judges *what an image would depict*, so it will
  pass a rude sentence that renders as nothing and flag a polite sentence that
  renders as something graphic.
- a complete safety system. A prompt-only model structurally cannot see what a
  generator actually produced. Post-generation image moderation catches failures
  this class of model cannot, and the two are complementary rather than redundant.
- a guarantee. No threshold on this model makes a generation pipeline safe on its own.

English only. Prompts in other languages are real words rather than obfuscation, and
the canonicalisation layer does not address them — that is a training-data gap, not a
normalisation one.

## Training and provenance

Trained on a large corpus of real image-generation prompts collected from public
generation platforms, with **model-assisted labelling**. Successive rounds combined
targeted hard-case analysis, dimension-specific label refinement, near-duplicate
control (character 5-gram MinHash), and frozen random-population audits.

Labels from teacher models were treated as **noisy silver supervision, never ground
truth**. No teacher output was taken as authoritative; where teacher labels and
adjudication disagreed, the disagreement was measured rather than resolved by
deferring to the teacher. Enriched and disagreement-stratified samples were kept
strictly separate from population validation — mixing them is the single most
repeated measurement error in this project's history, and it produced misleading
conclusions four separate times before the separation was enforced.

The prompt corpus is not distributed. It contains scraped third-party prompt text,
including explicit and adversarial material, and publishing it would serve no
reproduction purpose that the released weights do not already serve.

## License

MIT, matching the `microsoft/deberta-v3-base` base model from which these weights are
derived. The license covers the weights and the code in this repo. It makes no claim
about the training prompts, which are third-party text and are not distributed.

The previous v0.7 draft was Apache-2.0, correct for its DistilBERT base; the change
to MIT follows the change of base model.

## Artefact receipts

Frozen build `v29db`. SHA-256:

```
model.safetensors  5129545204d1c9ca8700369db1b055a9baac548c97dfc55140b8517cb538575e
heads.pt           d1d0b6f92c0dca4e3512739e7a26cb190fafd103b2d6056735c6ab8de5016ea9
```

Checkpoint schema: `dims = [sexual, nudity, violence_gore, substances, disturbing,
fetish]`, `widths = [3, 2, 2, 2, 2, 2]`, `backbone = microsoft/deberta-v3-base`.
`heads.pt` loads under `weights_only=True`.
