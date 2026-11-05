---
language: pt
license: mit
library_name: transformers
pipeline_tag: text-classification
base_model: neuralmind/bert-base-portuguese-cased
tags: [onnx, sentiment, stance, portuguese, rashomon]
---

# kikori

Target-directed sentiment for [rashomon](https://github.com/walteraandrade/rashomon): given a person and a Portuguese text, how does the text treat *that person*? Trained and documented in [walteraandrade/kikori](https://github.com/walteraandrade/kikori).

## Contract

Read it from `config.json["kikori"]` rather than copying it:

- Input: the pair `(person, text)` encoded as `[CLS] person [SEP] text [SEP]`, `token_type_ids` 0 for the first segment and 1 for the second, `max_length` 256. Cut only the text so the closing `[SEP]` stays; `truncation: true` on a pair in transformers.js drops it and moves the score.
- Text: this release was trained on the window rashomon sends since [rashomon#154](https://github.com/walteraandrade/rashomon/issues/154), the largest stretch around the first mention of the person that fits the budget, cut at word boundaries. A text that fits goes through whole. The previous release read the head of the text, where on rss, nicho and juridico documents the person was outside the cut in 37%, 41% and 57% of pairs.
- Output: 3 logits in the order `neg, neu, pos`. Score = `(p_pos - p_neg) * 10`, range -10..10; class cut `neg <= -2.5`, `pos >= 2.5`. A temperature of 4.0 is already folded into the classifier weights.
- Files: `onnx/model.onnx` (fp32, 436 MB) and `onnx/model_quantized.onnx` (per-channel dynamic int8, 110 MB) for `@huggingface/transformers` (`dtype: "fp32"` / `"q8"`); `model.safetensors` for Python.
- `fixtures.json`: 24 pairs with the expected fp32 and int8 scores. fp32 should match to 1e-3 on any runtime; int8 drifts between runtimes, so test it with a tolerance. Eight of the 24 texts run 3 to 10 tokens over the budget; Python cuts their tail, a consumer that re-centres on the mention may land a few tenths away on those.

## Numbers

Holdout of 578 (person, text) pairs on the windowed text, labelled by an LLM teacher under the rules in the repo's `LABELLING.md`, teacher-human agreement ~0.73. 469 of them are the stratified set every earlier release was measured on; 109 were appended on 2026-09-24 from rss, nicho and juridico, the sources the 469 could not measure (44, 41 and 40 pairs now). `pos` recall is by the score cut, over the 47 `pos` pairs:

| | acc | MAE | pos recall |
|---|---|---|---|
| fp32 | 0.78 | 1.58 | 0.45 (21/47) |
| int8 | 0.78 | 1.67 | 0.38 (18/47) |
| constant 0 | 0.61 | 1.98 | 0.00 |
| previous release (`d03d785`), fp32, same 578 | 0.78 | 1.60 | 0.45 (21/47) |

A second frozen set, 1,467 pairs cut from the pool above `p_pos` 0.20 plus a weighted draw from below, carries 519 `pos` pairs and measures `pos` recall with some precision: 0.73 weighted in fp32, 0.71 in int8 (previous release 0.71 / not re-measured). Per source on the 578, fp32: bluesky 0.75, gnews 0.84, rss 0.80, nicho 0.83, juridico 0.82, where the off-the-shelf baseline reads 0.63, 0.73, 0.73, 0.51, 0.82.

Recipe: BERTimbau base, effective batch 32, lr 5e-5, 3 epochs with the last one kept, class-weighted cross-entropy, temperature calibration on a frozen validation split. Trained on 13,778 teacher-labelled pairs; validation is 1,353 of them, held out by document and frozen across the whole data loop (macro-F1 0.7684, `pos` recall 0.697; the five-seed mean of this training set is 0.7661 / 0.687).

What this release changes is the text, not the score: the same holdout reads the same numbers for the previous release in fp32. The point of shipping it is that rashomon now sends the window, and this model was trained on windows; 637 of its training labels were re-issued by the teacher on the window, of which 528 kept their label.

## Known bias

The person name acts as a prior learned from skewed training labels (Lula's pairs lean `pos`, Tarcísio's and the Bolsonaros' lean `neg`). Measured on the 2026-09-09 release and not re-measured here: on the same short hostile sentence with the name swapped, that model scored Lula -0.3 and everyone else -4.8 to -4.9; favourable and routine sentences showed no name effect. The training labels behind this release have the same per-person skew, so assume the prior is still here.

Compare outlets on the same person, not people against each other. See the repository README, "Known bias".

This model is a ruler, not a judge. It is biased; the requirement is that it is biased the same way for every outlet, so comparisons between outlets stay valid.
