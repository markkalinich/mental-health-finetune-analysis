---
license: apache-2.0
language:
- multilingual
- en
- de
- fr
- es
- pt
- it
- nl
- pl
- ru
- uk
- cs
- ro
- sv
- da
- 'no'
- fi
- hu
- el
- tr
- ar
- he
- fa
- hi
- mr
- bn
- ur
- zh
- ja
- ko
- vi
- th
- id
- sw
- af
- tt
- ha
library_name: transformers
pipeline_tag: text-classification
base_model: jhu-clsp/mmBERT-base
datasets:
- google-research-datasets/go_emotions
- Horizon-Labs/go-emotions-multilingual
tags:
- emotion
- emotion-classification
- go_emotions
- multi-label-classification
- multilingual
- modernbert
- mmbert
- onnx
- transformers.js
widget:
- text: "Thank you so much, this made my day!"
  example_title: "English"
- text: "Ich kann nicht glauben, dass sie das Konzert abgesagt haben. So eine Frechheit."
  example_title: "German"
- text: "Tengo miedo de que no lleguemos a tiempo."
  example_title: "Spanish"
- text: "我真的很想念我的奶奶。"
  example_title: "Chinese"
- text: "Wow, I did not expect that at all!"
  example_title: "Surprise"
---

# Multilingual Emotions (base, 308M): the 28 GoEmotions labels in many languages

A multi-label emotion classifier with the 28 labels of Google's [GoEmotions](https://huggingface.co/datasets/google-research-datasets/go_emotions)
(admiration, amusement, anger, ... , surprise, neutral). It works on text in English and 35 other languages. It is a drop-in
multilingual alternative to English-only GoEmotions models such as
[SamLowe/roberta-base-go_emotions](https://huggingface.co/SamLowe/roberta-base-go_emotions): the labels are the same and it
uses the same sigmoid multi-label output. Built on [mmBERT-base](https://huggingface.co/jhu-clsp/mmBERT-base),
Apache-2.0. ONNX files for CPU and the browser (transformers.js) are included.
A smaller, faster version is available as
[multilingual-emotions-small](https://huggingface.co/Horizon-Labs/multilingual-emotions-small). [Try it in the browser](https://huggingface.co/spaces/Horizon-Labs/multilingual-emotions).

- Each label gets an independent probability. A text can have several emotions, or only `neutral`.
- `thresholds.json` has one threshold per label, tuned on the GoEmotions validation set. Use it instead of 0.5,
  especially for rare labels (grief, pride, relief, nervousness). See Usage.
- For the 6 Ekman emotions (anger, disgust, fear, joy, sadness, surprise), group the labels with the GoEmotions paper's
  mapping and take the maximum per group (`ekman_mapping.json`, code below).
- `onnx/model_quantized.onnx` (int8 embeddings, 641 MB) agrees with fp32 on 99.1% of 448 test texts (all 28 labels thresholded at 0.5).

## Usage

```python
import json
from huggingface_hub import hf_hub_download
from transformers import pipeline

clf = pipeline("text-classification", model="Horizon-Labs/multilingual-emotions-base", top_k=None)
thr = json.load(open(hf_hub_download("Horizon-Labs/multilingual-emotions-base", "thresholds.json")))
out = clf(["Thank you so much, this made my day!", "Tengo miedo de que no lleguemos a tiempo."])
print([[x["label"] for x in o if x["score"] >= thr[x["label"]]] for o in out])
# e.g. [['excitement', 'gratitude', 'joy'], ['fear']]

# 6 Ekman emotions: max score over each group
ekman = json.load(open(hf_hub_download("Horizon-Labs/multilingual-emotions-base", "ekman_mapping.json")))
scores = {x["label"]: x["score"] for x in out[1]}
print({e: max(scores[l] for l in ls) for e, ls in ekman.items()})
```

transformers.js:

```js
import { pipeline } from "@huggingface/transformers";
const clf = await pipeline("text-classification", "Horizon-Labs/multilingual-emotions-base", { dtype: "q8" });
console.log(await clf("Je suis tellement fier de toi !", { top_k: 5 }));
```

## Evaluation

The benchmarks were used only for evaluation, and training texts that also occur in them were removed.

- **GoEmotions test** (English Reddit comments, 5,427, 28 labels). Macro-F1 over the 28 labels, at threshold 0.5 and with
  per-label thresholds tuned on the GoEmotions validation set. Only models with the 28 GoEmotions labels are scored.
- **BRIGHTER** ([brighter-dataset/BRIGHTER-emotion-categories](https://huggingface.co/datasets/brighter-dataset/BRIGHTER-emotion-categories),
  CC-BY-4.0): human-labelled texts written in 28 languages (not translations), with 6 emotions and multiple labels
  per text; up to 1,500 test texts per language. Every model's labels are grouped into the 6 emotions (GoEmotions labels via the
  GoEmotions paper's Ekman mapping; for other label sets, by name). Each model gets one threshold per language and
  emotion, tuned on that language's BRIGHTER dev set. The score is macro-F1 over the annotated emotions, averaged over
  languages. "4 emotions" = anger, fear, joy and sadness only, the set every compared model covers.

| model | licence | GoEmotions test, macro-F1 @0.5 | GoEmotions test, macro-F1 (tuned thresholds) | BRIGHTER, 6 emotions | BRIGHTER, 4 emotions | labels |
|---|---|---|---|---|---|---|
| **this model** (308M) | Apache-2.0 | 0.473 | **0.516** | 0.420 | 0.449 | 28 GoEmotions labels, multilingual |
| [multilingual-emotions-small](https://huggingface.co/Horizon-Labs/multilingual-emotions-small) (141M) | Apache-2.0 | 0.447 | 0.494 | 0.406 | 0.432 |  |
| [SamLowe/roberta-base-go_emotions](https://huggingface.co/SamLowe/roberta-base-go_emotions) (125M) | MIT | 0.450 | 0.519 | 0.282 | 0.291 | 28 GoEmotions labels, English |
| [AnasAlokla/multilingual_go_emotions](https://huggingface.co/AnasAlokla/multilingual_go_emotions) | MIT | 0.455 | 0.538 | 0.337 | 0.355 | 28 GoEmotions labels, multilingual |
| [j-hartmann/emotion-english-distilroberta-base](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base) (82M) | none given | — | — | 0.297 | 0.315 | 7 labels, English |
| [MilaNLProc/xlm-emo-t](https://huggingface.co/MilaNLProc/xlm-emo-t) (278M) | none given | — | — | — | 0.456 | 4 labels (anger, fear, joy, sadness), multilingual tweets |
| [tabularisai/multilingual-emotion-classification](https://huggingface.co/tabularisai/multilingual-emotion-classification) (135M) | CC-BY-NC-4.0 | — | — | 0.404 | 0.428 | 11 labels, multilingual |

- The table shows the released checkpoint. Means over two training seeds: small GoEmotions tuned .499, BRIGHTER 6 emotions .405, 4 emotions .434; base GoEmotions tuned .520, BRIGHTER 6 emotions .424, 4 emotions .454.
- Models ahead of this one: GoEmotions (tuned): roberta-base-go_emotions, multilingual_go_emotions; BRIGHTER 6 emotions: none;
  BRIGHTER 4 emotions: xlm-emo-t. Most BRIGHTER languages are
  low-resource African and Asian languages that are not in our training data; GoEmotions texts are Reddit comments,
  while BRIGHTER includes tweets, news comments and other sources.

Per BRIGHTER language (macro-F1):

| language | this model (6 emotions) | this model (4) | xlm-emo-t (4) | tabularisai (6, NC) |
|---|---|---|---|---|
| Afrikaans | 0.433 | 0.477 | 0.350 | 0.339 |
| Algerian Arabic | 0.448 | 0.452 | 0.479 | 0.442 |
| Moroccan Arabic | 0.378 | 0.433 | 0.457 | 0.314 |
| Chinese | 0.448 | 0.489 | 0.564 | 0.439 |
| German | 0.432 | 0.475 | 0.510 | 0.434 |
| English | 0.565 | 0.591 | 0.618 | 0.522 |
| Spanish | 0.667 | 0.675 | 0.772 | 0.636 |
| Hausa | 0.319 | 0.321 | 0.342 | 0.354 |
| Hindi | 0.631 | 0.669 | 0.731 | 0.757 |
| Igbo | 0.269 | 0.272 | 0.294 | 0.272 |
| Indonesian | 0.516 | 0.545 | 0.587 | 0.495 |
| Javanese | 0.453 | 0.475 | 0.425 | 0.433 |
| Kinyarwanda | 0.226 | 0.282 | 0.261 | 0.194 |
| Marathi | 0.617 | 0.612 | 0.624 | 0.670 |
| Nigerian Pidgin | 0.432 | 0.379 | 0.425 | 0.451 |
| Portuguese (Brazil) | 0.388 | 0.501 | 0.564 | 0.406 |
| Portuguese (Mozambique) | 0.312 | 0.391 | 0.384 | 0.287 |
| Romanian | 0.666 | 0.719 | 0.683 | 0.570 |
| Russian | 0.657 | 0.657 | 0.755 | 0.706 |
| Sundanese | 0.361 | 0.415 | 0.458 | 0.389 |
| Swahili | 0.284 | 0.281 | 0.278 | 0.244 |
| Swedish | 0.464 | 0.492 | 0.475 | 0.367 |
| Tatar | 0.531 | 0.548 | 0.352 | 0.359 |
| Ukrainian | 0.454 | 0.515 | 0.517 | 0.462 |
| Makhuwa | 0.181 | 0.204 | 0.174 | 0.151 |
| isiXhosa | 0.309 | 0.318 | 0.294 | 0.300 |
| Yoruba | 0.165 | 0.203 | 0.196 | 0.154 |
| isiZulu | 0.165 | 0.186 | 0.189 | 0.164 |

Weakest GoEmotions labels (test F1, tuned thresholds): relief 0.26, realization 0.27, disappointment 0.30, embarrassment 0.36, annoyance 0.37, nervousness 0.37. Several of these are rare,
and GoEmotions annotators often disagree on such labels.

## Training

- **Data**: the GoEmotions training set (43,410 English Reddit comments with human labels; Apache-2.0), plus translations
  of it into 35 languages made with Qwen3.8-27B (Apache-2.0), published as
  [Horizon-Labs/go-emotions-multilingual](https://huggingface.co/datasets/Horizon-Labs/go-emotions-multilingual). Each language gets its own random sample of 12,000 comments,
  and the human labels are copied to the translation (442,991 training examples in total). The languages are
  Afrikaans, Arabic, Bengali, Chinese (Simplified), Czech, Danish, Dutch, Finnish, French, German, Greek, Hausa, Hebrew, Hindi, Hungarian, Indonesian, Italian, Japanese, Korean, Marathi, Norwegian, Persian, Polish, Portuguese (Brazilian), Romanian, Russian, Spanish, Swahili, Swedish, Tatar, Thai, Turkish, Ukrainian, Urdu, Vietnamese.
- Translations that failed to parse, looked like refusals, had an implausible length or were copied unchanged were
  dropped (about 1.2%). 3% of the source comments (in every language) were held out for validation.
- **Model**: mmBERT-base with 28 sigmoid outputs and binary cross-entropy, 1 epoch, learning rate 5e-5, max length 256
  tokens. Epochs and learning rate were chosen on the GoEmotions validation set and BRIGHTER dev sets, never the test sets.
  The checkpoint was chosen by macro-F1 on held-out training comments.
- Code: `code/` in this repository.

## Limitations

- The labels come from English Reddit comments. Translations keep the labels but can shift nuance, and the model has
  seen little native (non-translated) emotional text outside English. BRIGHTER results show it is much weaker in
  languages it was not trained on.
- The labels are subjective and inter-annotator agreement on GoEmotions is modest, so F1 around 0.5 is typical for this
  task. Rare labels are unreliable.
- It classifies the emotion expressed in the text, not the writer's actual state. Don't use it to make decisions
  about individuals.
