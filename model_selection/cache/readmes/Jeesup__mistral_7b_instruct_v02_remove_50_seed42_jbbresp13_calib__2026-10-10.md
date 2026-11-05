---
license: apache-2.0
base_model: mistralai/Mistral-7B-Instruct-v0.2
tags:
  - svd-llm
  - compression
  - low-rank
  - safety
  - calibration
---

# mistral_7b_instruct_v02_remove_50_seed42_jbbresp13_calib

`/home/jeesup0103/svd_safety/assets/models/Mistral-7B-Instruct-v0.2` compressed with the **complete SVD-LLM method**
([AIoT-MLSys-Lab/SVD-LLM](https://github.com/AIoT-MLSys-Lab/SVD-LLM), commit
`7538cca98880`), run as the authors' code rather than
reimplemented. Llama-2 is multi-head, so `component/svd_llama.py` is the authors'
file **unmodified** (`gqa_patched: True`); the only adaptation is a
compatibility shim that trims the causal mask transformers >= 4.48 builds one
column wider than the keys, which upstream's exact-shape assertion rejects.

- **Parameters removed:** 50% (keeping 50%)
- **Realised parameter fraction:** 0.49974646935096156
- **Pipeline:** data whitening -> SVD truncation -> LoRA on the U factors -> merge
  -> LoRA on the V factors -> merge -> fold to a dense checkpoint
- **Parameter update:** LoRA r=8, 2 epochs per factor,
  lr 0.0001, batch 64, on `yahma/alpaca-cleaned`

## What is different about this checkpoint

**Only the whitening calibration set.** SVD-LLM chooses which singular components
to keep by reconstruction importance on calibration data, and the published
recipe uses WikiText-2 alone -- a distribution containing no harmful requests.
This cell adds JailbreakBench's 100 harmful behaviours
([JailbreakBench/JBB-Behaviors](https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors),
harmful split) to that set, rendered **prompt-only** (the user turn plus the
assistant header, no response, so the corpus does not decide by fiat whether it
profiles refusal or compliance).

| corpus | sequences | tokens | detail |
|---|---:|---:|---|
| `wikitext2` | 255 | 522,240 | upstream get_calib_train_data |
| `jbb_harm_resp` | 13 | 26,624 | 96 unique prompts, prompt-only=False |

The WikiText half is the identical `get_calib_train_data("wikitext2", 256, seed
42)` call the published cells make, so this arm **adds** sequences rather
than replacing any. The harmful prompts are **4.85%** of the whitening token
budget: 100 behaviours are only 2,653 Llama-2 tokens, and a packed calibration
sequence must be exactly 2048 tokens long, so all 100 fit in 2 sequences
(54 appear twice as fill). Everything downstream -- truncation, both LoRA stages,
the fold -- is unchanged.

Why so small a share can matter: whitening factorises `W S = U Sigma V^T` with
`S S^T = E[x x^T]`, so importance is measured **after dividing by S**. Directions
carrying little calibration energy are amplified in the whitened basis, and
adding energy along directions WikiText never excites can move the truncation
ranking far more than the token share suggests.

## Results

| Metric | Value |
|---|---:|
| Parameter fraction retained | 0.4997 |
| WikiText-2 perplexity | 12.6185 |
| arc_easy (acc_norm) | 0.5501 |
| arc_challenge (acc_norm) | 0.3285 |
| hellaswag (acc_norm) | 0.5252 |
| winogrande (acc) | 0.5777 |
| openbookqa (acc_norm) | 0.3460 |
| piqa (acc_norm) | 0.6610 |
| mathqa (acc_norm) | 0.2543 |
| zero-shot mean | 0.4633 |
| AdvBench HarmBench ASR | 0.1885 |
| StrongREJECT HarmBench ASR | 0.3291 |
| Refusal rate, AdvBench (keyword) | 0.6692 |
| Refusal rate, benign control (keyword) | 0.0444 |
| Over-refusal rate (XSTest-safe) | 0.1626 |
| Over-refusal rate (OR-Bench-Hard-1K) | 0.2183 |
| Over-refusal macro rate | 0.1905 |

Over-refusal judging is **reliable** for this cell (XSTest-safe scored fraction 0.98; OR-Bench-Hard-1K scored fraction 1.00).

`whitening_compression.json` records the calibration set and all 224 per-matrix
ranks; `build_manifest.json` records the full build.

## Evaluation

WikiText-2 perplexity; ARC-Easy/Challenge, HellaSwag, WinoGrande, OpenBookQA,
PIQA and MathQA zero-shot; AdvBench and StrongREJECT generation judged by
`cais/HarmBench-Llama-2-13b-cls`; over-refusal on XSTest-safe and OR-Bench-Hard-1K
judged by `allenai/wildguard`. All generation uses the chat template, greedy.

## Caveats

- Compression at this ratio degrades generation quality, and safety numbers from
  a degenerate model are not evidence about alignment. Read the over-refusal and
  reliability lines alongside the ASR. On this cell, harmful-prompt generations
  are largely coherent, but output on generative benign prompts (the control set
  is mostly "write a script that ...") degrades noticeably.
- The reference point for "did the calibration change help" is the matched
  WikiText-only cell at the same removal ratio and seed, built by the same
  script. That comparison was made in a separate run of the pipeline on other
  hardware; the two evaluation stacks agree on the uncompressed model to four
  decimal places, but a same-environment control has not yet been built.
- The model is rank-deficient, not smaller on disk: factors are folded back to
  dense Llama shapes (`W = U @ V`), so it loads with stock `transformers` and
  needs no custom modelling code.
