---
language: [id, en]
license: cc-by-sa-3.0
base_model: microsoft/Multilingual-MiniLM-L12-H384
datasets: [laskar-ks/toxic-guardrail-id-en]
pipeline_tag: text-classification
tags: [toxicity, guardrail, bilingual, indonesian, onnx]
---

# Toxic Guardrail MiniLM ID/EN — v2

A small bilingual (Indonesian + English) toxicity severity classifier for use as
an application guardrail. Fine-tuned from `microsoft/Multilingual-MiniLM-L12-H384`,
vocabulary-trimmed, and exported to ONNX INT8 for local inference on CPU.

## Output

| rating | meaning | action |
|---|---|---|
| 0 | safe | allow |
| 1 | borderline (**not available** — reserved) | soft_warn |
| 2 | toxic / abusive / obscene | warn |
| 3 | targeted harassment / hate | review |
| 4 | threat / severe toxicity | block |

`score` is expected severity — the probability-weighted mean rating divided by 4
— not max softmax. It is monotonic and safe to threshold directly.

## Results

| metric | v1 | **v2** | change |
|---|---|---|---|
| macro F1 (test, overall) | 0.632 | **0.629** | −0.003 |
| macro F1 (Indonesian, classes r0/r2) | 0.797 | **0.825** | +0.028 |
| macro F1 (English, all four classes) | 0.638 | **0.627** | −0.011 |
| MAE (Indonesian) | 0.405 | **0.351** | −0.054 |
| MAE (English) | 0.432 | **0.460** | +0.028 |
| adversarial hard-set accuracy | 62.5% | **68.75%** | +6.25 |

Overall macro-F1 is unchanged within run-to-run noise. What moved is the
distribution of that performance: Indonesian improved on every measure, English
gave back a little, and the adversarial hard set — the only evaluation drawn from
outside the training distribution — improved most.

This is the trade the v2 rebalancing bought. Training data was rebalanced from
1 : 1.46 to 1 : 1.06 (ID : EN) and rating 0 was restored to being the largest
class, which reallocated capacity toward Indonesian.

### Per-class (test)

| rating | precision | recall | f1 | support |
|---|---|---|---|---|
| r0 safe | 0.84 | 0.87 | 0.85 | 1,706 |
| r2 abusive | 0.86 | 0.71 | 0.77 | 2,125 |
| r3 hate | 0.30 | 0.65 | 0.41 | 99 |
| r4 severe | 0.35 | 0.74 | 0.48 | 183 |

Precision on the severe classes remains low. The model is deliberately biased
toward over-escalation by class weighting — recall is 0.65 and 0.74, but roughly
two-thirds of what it flags as severe is actually rating-2 content. Safe content
is rarely affected: only 10 of 1,706 rating-0 examples were escalated to 3 or 4.

### Confusion matrix

| | pred r0 | pred r2 | pred r3 | pred r4 |
|---|---|---|---|---|
| **true r0** | 1,481 | 215 | 9 | 1 |
| **true r2** | 272 | 1,502 | 119 | 232 |
| **true r3** | 3 | 13 | 64 | 19 |
| **true r4** | 3 | 24 | 20 | 136 |

Two cells deserve attention. The 351 rating-2 rows escalated to r3/r4 are the
source of the low severe-class precision. The 272 rating-2 rows dropped to r0 are
toxic content passing as safe, concentrated on the English side — English rating-2
recall is 0.64 against 0.82 for Indonesian.

## Training

Fine-tuned with an **auxiliary sentiment head**: a second linear head predicts
`sentiment_polarity` (from
[`cardiffnlp/twitter-xlm-roberta-base-sentiment`](https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment),
supplied in the dataset) as a regression task, with loss weight 0.15.

The auxiliary head is **not part of the exported graph**. It shapes the encoder
during training and is discarded at export, so deployment size, latency, and the
inference contract are identical to v1. Running a 1.1 GB sentiment model at
inference time would have destroyed the point of a 75 MB CPU-only guardrail.

Correlation between predicted and target polarity on the test set is **r = 0.736**
— high enough that the encoder genuinely learned the signal, not so high that the
auxiliary task crowded out the primary one.

Other changes from v1: class weight clamp lowered from 8.0 to 6.0, training
extended from 4 to 6 epochs, adversarial augmentation reduced from 60% to 50% of
toxic rows.


### The score has a floor

Predicted expected severity never falls below roughly 0.5, even for clearly safe
text. This is an artifact of `label_smoothing=0.05` combined with class weighting,
not a property of the data.

Practical consequence: do not display raw `score` to end users as a "toxicity
percentage" — `selamat pagi` scores around 0.30, not 0.0. Use `action` for
decisions and treat `score` as a relative ordering rather than an absolute
probability.

## Thresholds

Measured on the validation set:

```text
p(3)+p(4) > 0.95  -> block
p(3)+p(4) > 0.60  -> review
1 - p(0)  > 0.45  -> warn
otherwise         -> allow
```

**Why `block` is set so high.** Precision for the severe classes tops out at
**0.575** at τ = 0.95, and the curve is still rising at the edge of the sweep. Even
at maximum confidence, roughly 40% of what would be blocked is not actually severe
content. That is acceptable for a human review queue; it is not acceptable for
automatic blocking, so `block` is deliberately rare and `review` carries most
severe predictions.

| τ (block) | precision | recall |
|---|---|---|
| 0.60 | 0.409 | 0.855 |
| 0.80 | 0.443 | 0.784 |
| 0.90 | 0.481 | 0.723 |
| **0.95** | **0.575** | **0.596** |

The warn threshold is flat across 0.30–0.60 (F1 0.899–0.903), so 0.45 was chosen
for balance rather than optimization: precision 0.892, recall 0.912.

## Known failure: Indonesian threat detection

<!-- TODO: verifikasi dengan tabel hard eval v2. Kalau baris 13/14 sekarang
     benar, tulis ulang seluruh section ini — itu perubahan besar. -->

**The model does not reliably detect violent threats written in Indonesian.**

The Indonesian training data carries binary labels only, so it contributes to
ratings 0 and 2 exclusively. Ratings 3 and 4 were never observed in Indonesian
during training, and cross-lingual transfer from English did not close the gap in
v1:

| input | expected | predicted (v1) | score |
|---|---|---|---|
| `i will find you and kill your family` | 4 | 4 | 0.97 |
| `gw bakal cari lu terus gw bunuh` | 4 | 2 | 0.55 |
| `awas lu, gw bacok kalau ketemu` | 4 | 2 | 0.41 |

The model maps `stupid` to `goblok` correctly but does not map `kill` to `bunuh`.
In v1, `awas lu, gw bacok` scored *lower* than the ordinary insult
`dasar goblok lu` — the ordering was inverted, not merely imprecise.

Do not deploy this model for Indonesian threat detection. The aggregate macro-F1
does not measure that capability and should not be read as evidence for it.

### Other known failures

Negation and non-profane criticism are misread as toxic:

- `jangan bilang goblok ke orang lain ya` ("don't call people stupid")
- `filmnya jelek banget, buang-buang duit` (film criticism, no profanity)

Quoting and positive-filler usage are handled correctly
(`anjir keren banget bro`, `dia bilang aku anjing, sedih banget`), so the model is
not purely keyword-matching — but it is inconsistent.

### English toxic content passing as safe

272 of 2,125 rating-2 test rows were predicted rating 0, almost all English.
English rating-2 recall is 0.64 against 0.82 for Indonesian. If English is your
primary traffic, lower `TAU_WARN` below 0.45 and re-measure.

## Usage

```bash
pip install onnxruntime transformers huggingface_hub numpy   # Python
npm i @huggingface/transformers onnxruntime-node              # TypeScript
```

```python
from huggingface_hub import snapshot_download

path = snapshot_download(
    "laskar-ks/toxic-guardrail-minilm-id-en",
    allow_patterns=["*.onnx", "old2new.*", "*.json"],
)
```

> `pipeline()` and `AutoModelForSequenceClassification` will **not** work with
> this model. The embedding table was trimmed from 250,002 to 33,763 rows, so
> token ids must be remapped before they reach the model. Transformers.js and
> `transformers` are used here for tokenization only; the ONNX session is run
> directly so the remap step can sit in between. Skipping it produces
> plausible-looking garbage, not an error.

### Python

```python
import json, re, unicodedata
import numpy as np
import onnxruntime as ort
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(path)
session   = ort.InferenceSession(f"{path}/model.int8.onnx",
                                 providers=["CPUExecutionProvider"])
remap = np.load(f"{path}/old2new.npy")
meta  = json.load(open(f"{path}/guardrail_meta.json"))

RATINGS = np.array([meta["train_to_rating"][str(i)]
                    for i in range(meta["num_labels"])])

ZW  = dict.fromkeys(map(ord, "\u200b\u200c\u200d\u2060\ufeff"), None)
URL = re.compile(r"https?://\S+|www\.\S+")
MEN = re.compile(r"@\w+", re.ASCII)          # re.ASCII is required — see below
WS  = re.compile(r"\s+")

def clean_text(s: str) -> str:
    s = unicodedata.normalize("NFKC", str(s)).translate(ZW)
    s = URL.sub(" <url> ", s)
    s = MEN.sub(" <user> ", s)
    s = s.replace("\\n", " ").replace("\\t", " ").replace("USER", " <user> ")
    return WS.sub(" ", s).strip()

def check(texts):
    one = isinstance(texts, str)
    enc = tokenizer([clean_text(t) for t in ([texts] if one else texts)],
                    truncation=True, max_length=meta["max_length"],
                    padding=True, return_tensors="np")

    logits = session.run(None, {
        "input_ids": remap[enc["input_ids"].astype(np.int64)].astype(np.int64),
        "attention_mask": enc["attention_mask"].astype(np.int64),
    })[0] / meta["temperature"]

    p = np.exp(logits - logits.max(-1, keepdims=True))
    p = p / p.sum(-1, keepdims=True)

    out = []
    for row in p:
        rating   = int(RATINGS[row.argmax()])
        p_severe = float(row[2] + row[3])
        p_toxic  = float(1 - row[0])
        action = ("block"  if p_severe > meta["tau_block"]   else
                  "review" if p_severe > 0.60 or rating >= 3 else
                  "warn"   if p_toxic  > meta["tau_warn"]    else "allow")
        out.append({"rating": rating,
                    "score": round(float((row * RATINGS).sum() / 4), 4),
                    "label": meta["rating_label"][str(rating)],
                    "action": action})
    return out[0] if one else out
```

```python
check("dasar goblok lu")
# {'rating': 2, 'score': 0.58, 'label': 'abusive', 'action': 'warn'}

check(["selamat pagi", "you are stupid", "anjir keren bro"])
# [{'rating': 0, 'score': 0.30, 'label': 'safe',    'action': 'allow'},
#  {'rating': 2, 'score': 0.64, 'label': 'abusive', 'action': 'warn'},
#  {'rating': 0, 'score': 0.33, 'label': 'safe',    'action': 'allow'}]
```

### TypeScript (Transformers.js + onnxruntime-node)

```typescript
import { AutoTokenizer } from "@huggingface/transformers";
import * as ort from "onnxruntime-node";
import fs from "node:fs";

const REPO = "laskar-ks/toxic-guardrail-minilm-id-en";
const DIR  = "./toxic-guardrail-minilm-id-en";

const tokenizer = await AutoTokenizer.from_pretrained(REPO);
const session   = await ort.InferenceSession.create(`${DIR}/model.int8.onnx`);
const meta      = JSON.parse(fs.readFileSync(`${DIR}/guardrail_meta.json`, "utf8"));

// old2new.bin is a raw little-endian int32 array. old2new.npy has a NumPy
// header and cannot be read directly as a TypedArray.
const buf   = fs.readFileSync(`${DIR}/old2new.bin`);
const remap = new Int32Array(buf.buffer, buf.byteOffset, buf.byteLength / 4);

const RATINGS = Array.from({ length: meta.num_labels },
                           (_, i) => meta.train_to_rating[String(i)] as number);

const ZW  = /[\u200b\u200c\u200d\u2060\ufeff]/g;
const URL = /https?:\/\/\S+|www\.\S+/g;
const MEN = /@\w+/g;
const WS  = /\s+/g;

export function cleanText(input: string): string {
  let s = String(input).normalize("NFKC").replace(ZW, "");
  s = s.replace(URL, " <url> ").replace(MEN, " <user> ");
  s = s.replace(/\\n/g, " ").replace(/\\t/g, " ").replace(/USER/g, " <user> ");
  return s.replace(WS, " ").trim();
}

export async function check(input: string) {
  const enc = await tokenizer(cleanText(input), {
    truncation: true, max_length: meta.max_length,
  });

  // ONNX int64 inputs require BigInt64Array
  const raw  = Array.from(enc.input_ids.data as BigInt64Array, Number);
  const ids  = BigInt64Array.from(raw, (id) => BigInt(remap[id]));
  const mask = BigInt64Array.from(raw, () => 1n);
  const dims = [1, raw.length];

  const { logits } = await session.run({
    input_ids:      new ort.Tensor("int64", ids,  dims),
    attention_mask: new ort.Tensor("int64", mask, dims),
  });

  const z   = Array.from(logits.data as Float32Array, (v) => v / meta.temperature);
  const max = Math.max(...z);
  const exp = z.map((v) => Math.exp(v - max));
  const sum = exp.reduce((a, b) => a + b, 0);
  const p   = exp.map((v) => v / sum);

  const rating  = RATINGS[p.indexOf(Math.max(...p))];
  const pSevere = p[2] + p[3];
  const pToxic  = 1 - p[0];

  const action =
    pSevere > meta.tau_block        ? "block"  :
    pSevere > 0.60 || rating >= 3   ? "review" :
    pToxic  > meta.tau_warn         ? "warn"   : "allow";

  return {
    rating,
    score: +(p.reduce((a, v, i) => a + v * RATINGS[i], 0) / 4).toFixed(4),
    label: meta.rating_label[String(rating)],
    action,
  };
}
```

```typescript
await check("dasar goblok lu");
// { rating: 2, score: 0.58, label: 'abusive', action: 'warn' }

await check("anjir keren bro");
// { rating: 0, score: 0.33, label: 'safe', action: 'allow' }
```

## Normalization parity

`cleanText` must produce byte-identical output in both languages. The one trap:
`\w` is Unicode-aware in Python by default but ASCII-only in JavaScript, so the
Python side requires `re.ASCII` on the mention pattern.

`clean_parity.json` in the
[dataset repo](https://huggingface.co/datasets/laskar-ks/toxic-guardrail-id-en)
holds input/output pairs generated by the TypeScript implementation. Verify any
port against it — the `@Ünïcödé` case is the one that catches this mismatch.

## Adversarial robustness

Training data was augmented with character-level evasions — censoring (`a*jing`),
leetspeak (`4nj1ng`), letter spacing (`a n j i n g`), and elongation. These are
detected as toxic, though spacing and censoring variants tend to be over-escalated
to rating 3. Coverage is partial; novel evasion patterns will get through.

## Download size

| what you need | size |
|---|---|
| inference only (ONNX INT8 + tokenizer + remap) | ~95 MB |
| full repo, including fp32 weights for fine-tuning | ~233 MB |