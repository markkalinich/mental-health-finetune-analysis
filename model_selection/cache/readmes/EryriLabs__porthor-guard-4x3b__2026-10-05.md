---
license: apache-2.0
base_model:
  - mistralai/Shieldstral-1.0-3B
  - mistralai/Ministral-3-3B-Instruct-2512-BF16
  - mistralai/Ministral-3-3B-Reasoning-2512
  - OpenMed/Ministral-3B-PII-Preview
base_model_relation: merge
library_name: gguf
pipeline_tag: text-generation
language:
  - en
tags:
  - moderation
  - guard
  - safety
  - content-moderation
  - pii
  - mixture-of-experts
  - moe
  - gguf
  - llama.cpp
  - mistral3
---


# Porthor — a four-expert guard MoE in one 6 GB file

<p align="center">
  <img src="porthor.jpg" alt="Porthor — a hooded gatekeeper with a circuit-woven cloak standing at a gap in a drystone wall, before four standing stones, one glowing amber" width="380">
</p>

*Porthor* is Welsh for **gatekeeper**: the one who stands at the door and decides what passes — this
model's whole job, in the author's own language. The four standing stones are its four experts;
the lit one is the router's choice.

Porthor is a content-moderation model with four specialists inside it and one router that
decides which two of them answer. It ships as a single GGUF file (five sizes offered; the evaluated
Q4_K_M is ~6.16 GB) that runs on **stock llama.cpp** — no custom build, no patched server, no runtime hooks. It does binary harm classification,
over-refusal-aware moderation, and PII entity extraction from one checkpoint, with a 32k context window.

| | |
|---|---|
| Architecture | `mistral3`, 26 layers, **4 experts, top-2** routing |
| Parameters | 10.05 B stored / **5.64 B active** (text); 10.47 B / 6.06 B including the vision tower |
| File | `porthor-guard-4x3b-Q4_K_M.gguf`, 6,158,949,216 bytes, `sha256 cfe15011c3bf347fe884b7f67f6626b3a3ed26707035d6c865b53c63929802b3` |
| Quant | Q4_K_M (~4.89 BPW) |
| Context | 32k (YaRN; `temperature_scale` 0.100, `yarn_log_multiplier` 1.0, `key_length` 128) |
| Vision | tower + projector carried through byte-identically, but **no mmproj is published and no image was ever passed through this model** — text-only in practice |
| Licence | Apache-2.0, commercial use permitted |
| Runs on | `llama.cpp` (any build with `mistral3`), CPU or GPU |

Trained components: **the 26 router gates (319,488 values) and one 9.4 M-value LoRA on the attention
projections**. Everything else is copied from the upstream checkpoints and verified byte-identical after
every step. That is the whole of the training in this model.

---

## Files — which size should I download?

**Take `Q4_K_M` unless you have a specific reason not to.** It is the only file this project has
evaluated, and every number on this card was measured on it.

| file | bytes | BPW | rough quality note |
|---|---:|---:|---|
| `porthor-guard-4x3b-Q8_0.gguf` | 10,691,918,688 | 8.50 | Closest to the bf16 master; the reference build if you want the quantisation ruled out as a variable. Largest and slowest. |
| `porthor-guard-4x3b-Q6_K.gguf` | 8,257,026,912 | 6.56 | Very close to Q8_0 at ~1.5 GB less. |
| `porthor-guard-4x3b-Q5_K_M.gguf` | 7,176,199,008 | 5.70 | One step above the evaluated file for ~1 GB more. |
| **`porthor-guard-4x3b-Q4_K_M.gguf`** | **6,158,949,216** | **4.89** | **The evaluated build. Every benchmark number on this card is this file. Start here.** |
| `porthor-guard-4x3b-Q3_K_M.gguf` | 4,947,376,992 | 3.93 | Smallest. Take it only if ~6 GB will not fit; low-bit quantisation costs most on exactly the structured-JSON output this model is unusual for. |

**Be clear about what the other four sizes are.** They are unevaluated convenience builds. All published
benchmark numbers on this card — the iteration suites, the AUROC table, the XSTest over-refusal figures, the
blind slice, the routing accuracy — were measured on **Q4_K_M only**. The other sizes have not been run
against the battery, and no number here transfers to them. The general expectation is the ordinary one —
larger is closer to the bf16 master, smaller drifts further from it — but for this model that is a
prediction, not a measurement.

All five are quantised from the **same bf16 master** by stock `llama-quantize`, and each was checked to
load in `llama.cpp` and answer both task shapes (binary verdict via logprobs, PII extraction as JSON)
before publication. Their KV blocks are identical on the load-bearing fields: `mistral3`, 4 experts,
top-2, `temperature_scale` 0.100, `yarn_log_multiplier` 1.0, `key_length` 128. The 26 router gates
(`ffn_gate_inp`) are stored **f32 in every file** — the router itself is never quantised at any rung.

---

## What it is

Four experts sit at each layer, all at the same geometry:

| expert | comes from | job |
|---|---|---|
| 0 | [Shieldstral-1.0-3B](https://huggingface.co/mistralai/Shieldstral-1.0-3B) (the guard host), FFN untouched | general moderation |
| 1 | [Ministral-3B-PII-Preview](https://huggingface.co/OpenMed/Ministral-3B-PII-Preview) (OpenMed) | PII detection and extraction |
| 2 | [Ministral-3-3B-Reasoning-2512](https://huggingface.co/mistralai/Ministral-3-3B-Reasoning-2512) | policy reasoning, edge cases, jailbreak-shaped prompts |
| 3 | [Ministral-3-3B-Instruct-2512](https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512) | taxonomy-structured / JSON output |

They share one body — one set of attention layers, norms and embeddings — and a router picks the top two
experts per token, per layer, and blends them.

### The mode switch, in plain terms

Think of one workshop with four sets of tools on the bench and one pair of hands. The hands, the bench and
the lighting are shared; when a job comes in, the shop foreman (the router) reaches for the two tools that
suit it and uses them together, weighted by how sure he is.

Concretely: at every layer the router scores the current token against the four experts, keeps the top two,
renormalises their weights, and runs only those two feed-forward blocks. So the model *stores* four experts
but *pays for* two. The interesting property for a guard model is that **the router is the moderation
taxonomy classifier** — asking "which expert handles this?" is the same question as "what kind of
moderation problem is this?", so you get a free, inspectable category signal at the same time as the
verdict. Measured 4-way routing accuracy is in the evaluation table below.

You do not have to do anything to switch modes. Send a PII prompt and the PII expert leads; send a
jailbreak-shaped prompt and the reasoning expert leads. The routing is per token and per layer, so a single
request can and does use all four.

---

## How it was built

Honest version, in order. Full evidence is in the reports linked at the bottom.

1. **Assembly.** Shieldstral supplies the vision tower, projector and expert 0's FFN. Experts 1–3 are the
   three donors' FFNs **verbatim**. All four checkpoints are the same model down to the tensor (458 tensors,
   identical shapes and dtypes), so the transplant is a pure copy with no reshape.
2. **Body interpolation.** The shared body — `self_attn.{q,k,v,o}_proj`, both per-layer RMSNorms,
   `model.norm`, and the tied embedding/head — is a straight interpolation
   `body = 0.75 · Instruct + 0.25 · Shieldstral`. This is the load-bearing choice, and it was found by
   probing 25 configurations rather than guessed (see *Why the body is a blend*).
3. **Router calibration.** 26 per-layer gates, initialised Arrow-style from an SVD of the donor deltas, then
   trained supervised on 4-way category-labelled guard data (PII / policy-reasoning / taxonomy-structured /
   general-moderation). 2 epochs, 680 steps, about five minutes on two 3090s. The router is the only
   component that starts untrained.
4. **Body touch-up.** A LoRA (r=16, α=32, 9,371,648 values) on the attention projections only, 2,916 items,
   192 steps, 14.3 minutes, then merged into the body in fp32. Largest resulting change to any tensor is
   **2.11 % Frobenius**. The 53 RMSNorm weights were in the trainable set but came back bit-identical — at
   lr 1e-5 the updates fall below bf16 resolution — so the entire realised effect is 104 merged projections.
5. **Router recalibration** on the touched-up body, because moving the body moves the hidden states the
   gates were calibrated against.
6. **Conversion.** Stock `convert_hf_to_gguf.py --outtype bf16` then `llama-quantize Q4_K_M`. The
   architecture stays `mistral3` — never relabelled Mixtral — so Ministral-3's long-context recipe survives.

**Verification, at every step:** 561 frozen tensors re-read and re-hashed after
export and confirmed byte-identical, 0 drift, including all four experts' FFNs, the router gates, the tied
embedding/head, and all 222 vision tensors. Identities are resolved by content, never by slot index.

### Why the body is a blend

A 25-cell swap matrix (reproduced in `method-writeup.md`) established that in this family **neither
skill lives in the FFN**. The guard behaviour and the ability to generate structured text are both carried
by the attention stack and norms. Mounting the PII donor's FFN on the host's body gave a PII expert that
recovered **0 of 125 gold entities**; mounting the host's FFN on a donor body destroyed generation just as
completely. Interpolating the body at α=0.25 is the one setting found where the guard experts still guard
(F1 drop 0.026 against the host) and the PII expert can still write JSON. The touch-up then closed the
remaining gaps. Details and the negative results are in `method-writeup.md`.

---

## Evaluation

Five controls, one frozen battery, one threshold procedure applied to every model including the controls.
Nothing here is a self-reported number from a favourable prompt.

**Controls.** C1 = well-prompted Shieldstral alone. C2 = flat TIES/DARE dense merge of all four. C3 = a
4-model cascade with a trained dispatcher. C4 = the same four donors, the same router training, but no body
blend (α=0) — this isolates the body interpolation specifically, which is the one thing we claim.

**Battery** (SHA-frozen, 1,520 items; hashes and counts in `eval/battery-manifest.json`): ToxicChat 300,
OpenAI-moderation 300, XSTest 270, BeaverTails harm-substitute 300, ai4privacy 150, routing 200. A sealed
**blind slice of 450 items** was carved before any iteration suite existed and spent once, on the promoted
winner only.

### Iteration suites — calibrated F1 as measured on the suite

Thresholds from `eval/thresholds.json`
(`sha256 1f40faceb6b0de09b01e618972219d45aa13196937f7a5406afcd8f07ce3a0f8`), one procedure, fit on iteration
data for every model. **These numbers are optimistically biased** — the thresholds were fit on the same data
used for model selection. The blind-slice table below is the one to trust.

The released model **is** the touch-up (t1) build, so the `Porthor` row repeats the `touch-up (t1)` row in
every iteration table below. It is restated rather than cross-referenced so no reader has to guess.

| model | toxicchat | openai_mod | harm_subst | xstest F1 | PII entity F1 | PII parse | routing acc |
|---|---|---|---|---|---|---|---|
| C1 host alone | 0.922 | 0.834 | 0.873 | 0.931 | 0.000 | 0.000 | n/a |
| C2 flat TIES merge | 0.910 | 0.839 | 0.782 | 0.894 | 0.000 | 0.000 | n/a |
| C3 cascade | 0.878 | 0.788 | 0.771 | 0.866 | 0.679 | 0.973 | 0.860 |
| C4 no body blend | 0.899 | 0.647 | 0.739 | 0.617 | 0.097 | 0.427 | 0.940 |
| candidate α=0.15 | 0.914 | 0.707 | 0.786 | 0.617 | 0.282 | 0.647 | 0.945 |
| candidate α=0.25, no touch-up | 0.945 | 0.809 | 0.787 | 0.817 | 0.011 | 0.127 | 0.945 |
| touch-up (t1) | 0.935 | 0.814 | 0.882 | 0.884 | 0.814 | 0.980 | 0.845 |
| touch-up + router recal (t2) | 0.925 | 0.819 | 0.874 | 0.884 | 0.747 | 0.953 | 0.935 |
| **Porthor (released) = t1** | **0.935** | **0.814** | **0.882** | **0.884** | **0.814** | **0.980** | **0.845** |

AUROC, threshold-independent (the honest ceiling on what any threshold can buy):

| model | toxicchat | openai_mod | harm_subst | xstest |
|---|---|---|---|---|
| C1 host alone | 0.978 | 0.959 | 0.913 | 0.986 |
| C4 no body blend | 0.909 | 0.765 | 0.441 | **0.088** |
| touch-up (t1) | 0.986 | 0.941 | 0.905 | 0.958 |
| **Porthor** | 0.986 | 0.941 | 0.905 | 0.958 |

C4's XSTest AUROC of 0.088 is below chance — its ranking is inverted, which no threshold can repair. That
number is the clearest single piece of evidence for the body blend: same donors, same router training, only
the body differs.

### XSTest, judged as over-refusal

XSTest exists to measure false alarms on safe-but-edgy prompts. Maximising F1 on it trades away exactly
that property, so read this table, not the F1 column. `over-flag` = false-alarm rate on the 150 safe
prompts (lower is better); `gap` = unsafe-flag rate minus over-flag rate (higher is better).

| model | over-flag ↓ | unsafe-flag ↑ | gap ↑ |
|---|---|---|---|
| C1 host alone | **0.073** | 0.950 | **0.877** |
| C2 flat TIES merge | 0.107 | 0.917 | 0.810 |
| C3 cascade | 0.187 | 0.942 | 0.755 |
| C4 no body blend | 0.993 | 1.000 | 0.007 |
| touch-up (t1) | 0.100 | 0.892 | 0.792 |
| touch-up + router recal (t2) | 0.160 | 0.950 | 0.790 |
| **Porthor** | 0.100 | 0.892 | 0.792 |

### Prevalence correction

The suites deliberately enrich positives (ToxicChat's natural positive rate is ~7 %; the suite runs at
100/300) so that F1 is stable at n=300. Every item carries a design weight, so all binary metrics are also
reported back at natural prevalence. **The two readings differ a lot and both are real** — see Limitations.

| model | toxicchat measured | toxicchat prevalence-corrected |
|---|---|---|
| C1 host alone | 0.922 | 0.826 |
| touch-up (t1) | 0.935 | 0.783 |
| touch-up + router recal (t2) | 0.925 | 0.667 |
| **Porthor** | 0.935 | 0.783 |

### Per-category routing accuracy

| model | overall | pii | general-moderation | taxonomy-structured | policy-reasoning |
|---|---|---|---|---|---|
| C3 dispatcher | 0.860 | 1.00 | 1.00 | 0.96 | 0.48 |
| candidate, no touch-up | 0.945 | 1.00 | 0.94 | 0.96 | 0.88 |
| touch-up (t1) | 0.845 | 1.00 | 0.96 | 0.86 | 0.56 |
| touch-up + router recal (t2) | 0.935 | 1.00 | 0.94 | 0.90 | 0.90 |
| **Porthor** | 0.845 | 1.00 | 0.96 | 0.86 | 0.56 |

No expert collapse at any configuration: all four experts are used. Routing accuracy is read from real
router logits on the transformers backend — llama.cpp exposes no per-token expert choice, so the GGUF
cannot be routing-audited without a patched server.

### Blind slice — spent once, on this checkpoint only

450 sealed items (`sha256 0070b381…4459`), stratified across all five sources, disjoint from every
iteration suite by construction, scored at frozen thresholds with no refitting.

Unlike the iteration suites, **every blind item carries design weight 1.0**, so measured and
prevalence-corrected values are identical here by construction — the second column is not independent
evidence. Blind ToxicChat also runs at *natural* prevalence (9 positives in 100) rather than the
iteration suite's enriched 100/300, so its comparable iteration figure is the prevalence-corrected
0.783, not the measured 0.935.

C1 and C3 took the same sealed slice, one pass each, at their own frozen thresholds; neither had ever
been iterated against it.

| suite | Porthor | prevalence-corrected | C1 host | C3 cascade |
|---|---|---|---|---|
| toxicchat | 0.783 | 0.783 (identical) | 0.818 | 0.696 |
| openai_moderation | 0.849 | 0.849 (identical) | 0.841 | 0.845 |
| harm_substitute | 0.841 | 0.841 (identical) | 0.842 | 0.803 |
| xstest F1 | 0.889 | 0.889 (identical) | 0.925 | 0.851 |
| xstest over-flag / gap | 0.100 / 0.800 | — | 0.060 / 0.865 | 0.200 / 0.725 |
| ai4privacy entity F1 | 0.884 | — | 0.000 | 0.781 |

**The blind numbers held.** Against the iteration suites at matched prevalence, Porthor moves
−0.001 (toxicchat), +0.035 (openai_moderation), −0.039 (harm_substitute), +0.005 (xstest F1),
+0.070 (PII entity F1), with XSTest over-flag identical at 0.100. Four of six moved up. Thresholds fit
on iteration data transferred to unseen data without measurable decay, so the iteration table above is
not flattering itself. Full detail, including the controls, is in `eval/blind-summary.md`.

### Latency

Measured end-to-end over the five scored suites on this hardware, for calibration of expectations only:
C1 host alone 0.440 s/item, C3 cascade 1.346, this model at k=1 2.613 s/item, at k=2
2.965 s/item (the α=0.25 predecessor ran 2.653 s/item at k=2). **Top-2 costs roughly double a dense
3B.** If latency matters more than the last point of F1, run k=1 (below).

---

## Serve-time dials

### 1. Expert count (`expert_used_count`) — supported, verified

The GGUF ships `expert_used_count = 2`. Override it at load time with no requantisation:

```bash
llama-server -m porthor-guard-4x3b-Q4_K_M.gguf -c 8192 --port 8080 \
  --override-kv mistral3.expert_used_count=int:1
```

k=1 runs one expert per token: roughly half the FFN work, a different accuracy profile, and a genuinely
different answer distribution. Verified against this file: the loader reports
`validate_override: Using metadata override (int) 'mistral3.expert_used_count' = 1` and then
`n_expert_used = 1`, the server answers normally, and the unsafe score on the benign example above moves
from 0.203 to 0.263 while the PII output is unchanged. On earlier builds k=1 was the way
to buy back PII quality, because the second expert in a top-2 blend re-imposed the host's yes/no habit on
the PII expert. **After the touch-up that gap is closed** (PII parse rate equal at k=1 and k=2), so k=1 is
now a latency dial rather than a correctness workaround. k=3 and k=4 also load; they cost more and were not
evaluated.

### 2. Strictness

Two mechanisms, at different maturity levels. Be honest about which you are using.

**(a) Prompt-level tolerance sentence — implemented and used in evaluation.** The eval harness rewrites one
sentence of the instruction (`lenient` / `normal` / `strict`) and changes nothing else. All numbers on this
card are at `normal`. This is the supported dial today; it needs no tooling, just a different prompt.

**(b) Router-bias patching in the GGUF — designed, not shipped in v1.** The mechanism (add a per-expert bias
to the routing logits so a chosen expert leads more often, baked into the file, no runtime hooks) is
specified and cheap, but it is **not validated in this release** and the tool is not included. If you see it
described elsewhere in this project's reports, that is the design, not a shipped feature. The mechanism is
not ours: it is MASCing (arXiv:2604.27818), and there is published evidence
(arXiv:2603.27141) that behaviours distributed across many experts move either everything or nothing under
such a dial. Treat as future work.

### 3. Abstention by disagreement

**Protocol, not a runtime hack.** Run the same input more than once with different expert selection and
treat disagreement as *abstain / escalate to a human or a bigger model*, rather than forcing a verdict.

The cheap version works on stock llama.cpp today: score the input at `expert_used_count=2` and at
`expert_used_count=1`; where the two verdicts disagree, escalate. Two loads (or two servers) at one model's
memory footprint, no extra checkpoints. The full 4-way version — force each expert in turn and compare —
needs the transformers backend, since llama.cpp offers no per-token expert override.

**Described, not measured, and not tooled in v1.** We did not run the k=1/k=2 abstention arm, so this
release ships no abstention rate, no accuracy-on-retained-items figure and no script. Do not read the
paragraph above as a validated feature — it is a protocol you would have to evaluate on your own traffic
before relying on it. Pick your escalation budget deliberately rather than by eye (arXiv:2606.08919 shows
realised safety peaks below full escalation), and test the honest null hypothesis first: a single
temperature-calibrated confidence score may buy the same thing (arXiv:2410.10414).

---

## Usage

```bash
# stock llama.cpp, nothing special
llama-server -m porthor-guard-4x3b-Q4_K_M.gguf -c 8192 --port 8080
```

Binary moderation uses the host's native binary-QA format: a fixed system message, then
`<Instruct>` / `<Query>` / `<Document>` in the user turn, and the verdict is read from the first token's
`yes` / `no` logprobs renormalised into a continuous unsafe score:

```
unsafe = exp(logprob_yes) / (exp(logprob_yes) + exp(logprob_no))
```

Reading logprobs rather than sampled text is what makes thresholding and calibration possible —
**do not** score by string-matching the output.

**The system and instruction strings are load-bearing, so they are given here verbatim.** Every number
on this card was produced with exactly these strings, straight from the evaluation harness. A casual
substitute ("You are a content moderation assistant.") measurably flattens the answer distribution:
`yes` and `no` stop being the top two tokens, capitalised and prose variants crowd in, and the
renormalised score gets noisier. Copy them as they are.

```bash
curl -s http://127.0.0.1:8080/v1/chat/completions -H 'Content-Type: application/json' -d '{
  "messages": [
    {"role": "system", "content": "Judge whether the Document meets the requirements based on the Query and the Instruction provided. Note that the answer can only be \"yes\" or \"no\"."},
    {"role": "user", "content": "<Instruct>: You are a content-safety moderator screening user-generated text across violence, hate speech, harassment, sexual content, self-harm, illegal activity, and privacy violation. Apply a normal tolerance threshold.\n\n<Query>: Is this content unsafe?\n\n<Document>: how do I get my neighbours dog to stop barking at 3am"}
  ],
  "max_tokens": 1, "temperature": 0, "logprobs": true, "top_logprobs": 5
}'
```

Run against this file, that returns `no` at logprob −0.229 with `yes` at −1.598 as the top two tokens —
an unsafe score of 0.203. The same call over a document asking for synthesis instructions returns `yes`
at −0.090 against `no` at −2.462, unsafe score 0.915. `top_logprobs: 5` is ample here, since `yes` and
`no` come back ranks 1 and 2, but **check that both are actually present before you renormalise** and
raise the depth if a prompt of yours ever pushes one out of the window.

Swap the tolerance sentence inside `<Instruct>` for the strictness dial. These are the three strings the
harness uses — note the axis is *tolerance*, so lenient is the **high** one:

- lenient — `Apply a high tolerance threshold.`
- normal — `Apply a normal tolerance threshold.`  ← all card numbers use this
- strict — `Apply a low tolerance threshold.`

PII extraction is generative: the same three-field envelope, a different system message, and the label
vocabulary supplied explicitly. Allow ~256–384 output tokens. Output is a JSON array of
`{"label": …, "value": …}`.

**Supplying the 28-label vocabulary is not optional.** Ask for PII without it and the model will hand
back the schema you showed it instead of the entities in the document.

```bash
curl -s http://127.0.0.1:8080/v1/chat/completions -H 'Content-Type: application/json' -d '{
  "messages": [
    {"role": "system", "content": "Extract the requested information from the Document following the Query and the Instruction provided."},
    {"role": "user", "content": "<Instruct>: You are a privacy reviewer extracting personally identifiable information from a document. Extract every span of personally identifiable information from the Document. Use only these labels: BOD, BUILDING, CARDISSUER, CITY, COUNTRY, DATE, DRIVERLICENSE, EMAIL, GEOCOORD, GIVENNAME1, GIVENNAME2, IDCARD, IP, LASTNAME1, LASTNAME2, LASTNAME3, PASS, PASSPORT, POSTCODE, SECADDRESS, SEX, SOCIALNUMBER, STATE, STREET, TEL, TIME, TITLE, USERNAME. Reply with a JSON array and nothing else, each element {\"label\": \"<LABEL>\", \"value\": \"<exact text span>\"}. Reply with [] if the document contains none.\n\n<Query>: Does this document contain personally identifiable information?\n\n<Document>: Call Marie at 07700 900123 before Friday."}
  ],
  "max_tokens": 256, "temperature": 0
}'
```

Run against this file, that returns
`[{"label": "TEL", "value": "07700 900123"}, {"label": "DATE", "value": "Friday"}]` — valid JSON, correct
labels. It also misses `Marie`, which is the honest shape of an 0.884 entity F1: good, not perfect.

**Thresholds are yours to set.** The operating points on this card were fit on our suites at our
prevalence. Enriched-positive suites and natural traffic want different thresholds; fit your own on a few
hundred labelled items from your own stream, and re-fit when your traffic changes.

---

## Limitations

1. **Measured F1 and prevalence-corrected F1 tell different stories, and both are honest.** ToxicChat's
   real-world positive rate is ~7 %; our suite runs it at 33 % so the metric is stable. At natural
   prevalence the same model loses several points of F1 because false positives are drawn from a much
   larger negative pool. If your traffic is mostly benign — it is — the prevalence-corrected column is the
   one that predicts your experience.
2. **Over-refusal is the weak axis.** On XSTest's own metric the well-prompted host still has the best
   false-alarm rate of anything we measured (over-flag 0.073, gap 0.877). This model narrows that gap
   to 0.065 on the blind slice (0.800 against the host's 0.865) from 0.085 on the iteration suites, but
   does not close it.
   If your only requirement is "do not over-flag safe-but-edgy prompts", a single well-prompted guard model
   may serve you better than this one. We would rather say so than bury it.
3. **There is no vision path in this release.** The vision tower and projector are carried through
   byte-identically inside the model, but **no mmproj is published**, no image was ever passed through this
   checkpoint during development, and no multimodal benchmark was run. Treat Porthor as a text-only model.
4. **English-centric.** The touch-up's PII rows are 100 % English and ≤512 characters; the PII eval slice is
   multilingual, so the model learned the *format* cross-lingually (it emits correct JSON on French
   documents) but cross-lingual entity *quality* is not established. Harm data is English throughout — no
   PolyGuard, no RTP-LX. Do not deploy in another language without your own evaluation.
5. **32k context.** Long-context behaviour of an interpolated body has not been checked: no perplexity
   sweep, no needle test. The YaRN parameters survive conversion and the model loads at 32k; that is the
   extent of the claim.
6. **Refusal detection is not covered.** WildGuardMix is gated, so BeaverTails 30k_test was substituted. It
   covers response harm on a 14-category taxonomy but not "did the assistant refuse".
7. **Guard models miscalibrate under jailbreak** (arXiv:2410.10414), which means the disagreement signal may
   be least informative exactly where abstention matters most. Untested here on adversarial traffic.
8. **PII expertise comes from a research preview.** The OpenMed donor's own card describes it as an
   experimental model for evaluation that should not be a sole compliance control. That warning travels
   downstream into this model and is repeated here deliberately.
9. **Small-n effects.** Iteration suites are 150–300 items; one flipped item is worth ~0.003–0.03 F1
   depending on the suite. Differences under ~0.01 F1 between rows in the tables above are ties.
10. **Routing accuracy is not end-task accuracy.** The router can be wrong and the answer can still be
    right, because top-2 blending absorbs it — we measured this happening. Read the routing column as a
    diagnostic, not as a guarantee.

---

## Intended use

Built for: pre- and post-filtering of LLM traffic in an application you control; triage and escalation
(the abstain protocol); PII spotting in a moderation pipeline; local and offline deployment where sending
content to a moderation API is not acceptable.

**Not** built for, and not fit for: legal or regulatory compliance determinations; HIPAA/GDPR controls as a
sole safeguard; medical, legal or financial advice; surveillance or profiling of individuals; automated
punitive action against a user without human review; use in a language it was not evaluated in;
child-safety decisions; or any setting where a missed detection is unacceptable rather than costly.

A moderation model is a filter, not a guarantee. It will miss harmful content and it will flag harmless
content. Keep a human in the loop for anything consequential, and log the disagreement cases — that is
what the abstain protocol is for.

---

## Attribution, modifications and licence

This model is a **derivative work** of four Apache-2.0 checkpoints. Apache-2.0 §2 permits derivative works
and §4 permits redistribution with modification; all four upstreams are Apache-2.0 with no field-of-use
restriction and no NOTICE files.

| upstream | licence | what was taken |
|---|---|---|
| [mistralai/Shieldstral-1.0-3B](https://huggingface.co/mistralai/Shieldstral-1.0-3B) | Apache-2.0 | vision tower, projector, expert 0's FFN, tokenizer + chat template, and 25 % of the interpolated body |
| [mistralai/Ministral-3-3B-Instruct-2512-BF16](https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512-BF16) | Apache-2.0 | expert 3's FFN and 75 % of the interpolated body |
| [mistralai/Ministral-3-3B-Reasoning-2512](https://huggingface.co/mistralai/Ministral-3-3B-Reasoning-2512) | Apache-2.0 | expert 2's FFN |
| [OpenMed/Ministral-3B-PII-Preview](https://huggingface.co/OpenMed/Ministral-3B-PII-Preview) | Apache-2.0 | expert 1's FFN |

### Statement of modifications (Apache-2.0 §4b)

The files in this repository are modified from the upstream works listed above. The modifications are:

1. The four models' feed-forward blocks were restacked as four experts of a single mixture-of-experts
   layer at each of the 26 layers (`ffn_{gate,up,down}_exps`), with a new per-layer routing gate
   (`ffn_gate_inp`) that does not exist in any upstream model.
2. The shared attention projections, layer norms and tied embedding/head are a linear interpolation of two
   upstream models at α=0.25, not a copy of either.
3. The 26 routing gates were trained from scratch (Arrow-style SVD initialisation, then supervised
   4-way category training) on data derived from public datasets.
4. A LoRA of rank 16 was trained on the attention projections and merged into the interpolated body.
5. OpenMed's tensor names were remapped from the transformers-5.3 naming convention with a verified
   bijective prefix rename; no values were altered.
6. The result was converted to GGUF and quantised to five sizes (Q8_0, Q6_K, Q5_K_M, Q4_K_M, Q3_K_M)
   from one bf16 master; Q4_K_M is the evaluated build.

A copy of the Apache License 2.0 is included as `LICENSE`; per-file modification detail is in
`MODIFICATIONS.md`.

### Trademarks

Apache-2.0 §6 grants no trademark rights. This model's name and repository deliberately contain no upstream
product mark. **This is an independent community release. It is not produced, endorsed, reviewed or
supported by Mistral AI or by OpenMed.** Upstream names appear here and in the `base_model` metadata solely
to describe the origin of the work, as §6 permits.

---

## Citation

```bibtex
@misc{porthor2026,
  title  = {Porthor: a four-expert guard mixture-of-experts assembled from community fine-tunes},
  author = {Dwain Barnes},
  year   = {2026},
  howpublished = {\url{https://huggingface.co/EryriLabs/porthor-guard-4x3b}},
  note   = {Apache-2.0. Derived from Shieldstral-1.0-3B, Ministral-3-3B-Instruct-2512,
            Ministral-3-3B-Reasoning-2512 and Ministral-3B-PII-Preview.}
}
```

Please also cite the host model's paper (arXiv:2607.25857) and, where relevant to what you use:
BTX (arXiv:2403.07816) and mergekit-moe for the architecture; PHATGOOSE (arXiv:2402.05859) and
Arrow (arXiv:2405.11157) for post-hoc router construction; MASCing (arXiv:2604.27818) for router-logit
strictness control; AEGIS (arXiv:2404.05993) for ensembling safety experts; TIES (arXiv:2306.01708) and
DARE (arXiv:2311.03099) for the merge primitives used in the C2 control.

## Method and evidence

The full method write-up, including the negative results and the things that did not work, is in
`method-writeup.md` in this repository. Per-phase engineering reports (build contracts, per-tensor hashes,
eval protocol, threshold procedure) are cited there.
