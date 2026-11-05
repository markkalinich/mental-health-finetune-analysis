---
language:
- en
- zh
license: cc-by-nc-4.0
base_model: Qwen/Qwen3Guard-Gen-4B
base_model_relation: finetune
library_name: transformers
pipeline_tag: text-generation
tags:
- safety
- dangerous-intent-classification
- binary-classification
- lora
---
# Qwen3Guard-Gen-4B Danger Intent — Open Data + Qwen Synthetic + Supplement | 4,000 sampled training records | V9

Merged BF16 full model for classifying a **user input** as `SAFE` or `UNSAFE`. This repository also preserves the original LoRA tensors in `adapter/`. It is a research classifier, not a general-purpose assistant and not an independently certified safety system.

## Quick start

Download this repository, install `requirements.txt` with an appropriate PyTorch CUDA build, then run:

```bash
python predict.py --model . --text "How do I protect my email account?" --load-in-4bit
```

To reproduce the historical loading strategy rather than quantizing the merged weights:

```bash
python predict.py --model . --reference --load-in-4bit --text "How do I protect my email account?"
```

`--reference` downloads the pinned upstream base if absent and loads `adapter/`. Full BF16 CPU inference is available with `--device cpu` and without `--load-in-4bit`. Memory demand is materially higher than 4-bit CUDA inference. The portable script selects the correct full architecture automatically. **Do not apply the adapter on top of this repository's already merged weights.**

The saved native upstream chat template is preserved for provenance. Binary classification uses the explicit fixed template in `predict.py` and `danger_intent_config.json`, not an unmodified generic chat pipeline. Output includes the binary prediction, raw margin, risk score, threshold and truncation indicator.

## Training data behind the repository name

Current repository: [PLJIANGG05/qwen3guard-gen-4b-danger-intent-opendata-qwensynth-supplement-sampled4000-v9](https://huggingface.co/PLJIANGG05/qwen3guard-gen-4b-danger-intent-opendata-qwensynth-supplement-sampled4000-v9). Historical experiment ID: **V9**. Previously named `PLJIANGG05/qwen3guard-gen-4b-danger-intent-v9`.

`opendata` denotes the six existing public-source datasets listed below, `qwensynth` denotes reviewed and corrected Qwen-generated samples, and `supplement` denotes the second five-category AI-generated supplement. `sampled4000`, when present, means a sampled subset rather than the full pool. Upstream licenses are unchanged.

Only 4,000 sampled records were used for training, not the entire candidate pool. The 84,287-record candidate pool included V5 first-stage data, V7 supplemental training data and the 500-record V7 supplemental validation pool. V9 has its own disjoint 400-record validation set. XSTest and ToxicChat were excluded from sampling.

| Training source | Records in this model's configured training data |
|---|---:|
| AdvBench | 26 |
| Aegis V2 | 1,193 |
| Five-category AI synthetic supplement 01-05 | 252 |
| Chinese Do-Not-Answer | 123 |
| HarmBench | 13 |
| JBB-Behaviors | 12 |
| OR-Bench | 939 |
| Corrected Qwen3.5-4B synthetic data | 1,442 |
| **Total** | **4,000** |

SAFE: **2,373**. UNSAFE: **1,627**. Validation records are not included in these training totals. See `training_dataset_summary.json` for stage and validation provenance.

This rename changes repository naming and documentation only. Model weights, adapters, tokenizer, inference code, scoring configuration and historical results are unchanged. `release_identity.json` retains the original release ID for provenance; `rename_history.json` records the new ID. Raw training text remains excluded from this model repository.

## Training lineage

4,000 randomly selected training records, plus 400 disjoint validation records, from the existing local pools. The candidate pool included the V7 supplementary validation pool. XSTest and ToxicChat were excluded from this random sampling.

Only 4,000 sampled records were used for training, not the entire candidate pool. The 84,287-record candidate pool included V5 first-stage data, V7 supplemental training data and the 500-record V7 supplemental validation pool. V9 has its own disjoint 400-record validation set. XSTest and ToxicChat were excluded from sampling. No new training or recalibration was performed for this rename.

## Scoring and limits

Two first-label-token logits, normalized only against SAFE and UNSAFE. Predict UNSAFE at P_UNSAFE >= 0.5. This is a relative candidate score, not a calibrated probability of correctness.

Maximum classification context is 1,024 tokens under the fixed scorer. For longer inputs the scorer retains roughly 75 percent of the beginning and 25 percent of the end, with a visible truncation marker. This may discard safety-relevant context.

This model is no longer the original three-class Qwen3Guard. Do not use the native Guard template, response safety labels, or Controversial policy for this binary fine-tuned checkpoint.

English and Chinese are present in the task and training data. The current expanded comparison is English only and does not establish Chinese or other-language performance. `SAFE` is not a guarantee that an input or downstream response is harmless.

## Evaluation protocol

Historical results and the expanded 85 percent-trigger comparison use **NF4 upstream base plus the original unmerged adapter**, with BF16 computation. The full BF16 merged model is a deployment artifact. Requantizing the merged model is not numerically identical to quantizing the base first and adding LoRA. Deployment probe checks are separate from the benchmark.

V9 confidence below 0.85 triggers one vote each from V9, V5 and V7. Confidence equal to or above 0.85 uses V9 alone. The 85 percent threshold does not mean an 85 percent accuracy guarantee. V5/V7 use their existing calibration and decision thresholds unchanged.

XSTest was used historically for validation/calibration; ToxicChat has been inspected repeatedly. Neither is a new blind holdout. New OpenAI Moderation, SimpleSafetyTests and WildGuardTest subsets are English-filtered and normalized-exact-deduplicated against used local data. Their definitions differ from the original Qwen paper, and upstream foundation-model contamination cannot be ruled out. Evaluation results are supplied in the accompanying experiment report when complete.

## Provenance and verification

Base: [Qwen/Qwen3Guard-Gen-4B](https://huggingface.co/Qwen/Qwen3Guard-Gen-4B), revision `6ec42827da0c1ff11e7a49dc269d2e810d27e108`.

`merge_verification.json` records a streaming check of every exported tensor, adapter coverage, tied weights, and BF16 loader dtype conversions. `SHA256SUMS.json` lists distributed files. Adapter tensors are unchanged; its configuration has a portable pinned base identifier instead of a machine-specific path.

## Licenses and attribution

Copyright 2026 PLJIANGG05 for new fine-tuning contributions. **CC-BY-NC-4.0 applies only to the new fine-tuning contribution**, including the adapter; see `LICENSE`. It does not replace or restrict rights granted by the upstream base's Apache-2.0 license, preserved verbatim in `LICENSE.base-model`. This combined artifact contains components under different licenses. The Python inference code is Apache-2.0 under `LICENSE.code`. Upstream training sources retain their respective licenses and attribution; no claim of ownership is made over upstream data.

Please attribute PLJIANGG05 and the original Qwen authors and respect applicable upstream notices. Training text is not included in this model repository. Users should validate the classifier on their own independent data, review false positives/negatives, and retain a human review route for consequential decisions.

## Completed expanded comparison

`evaluation_comparison.json` contains completed results for all 8,498 locked records, including 2,607 new English records. It reports V9 alone, the V9-first 85 percent-trigger V9/V5/V7 ensemble, and native Qwen3Guard Strict and Loose, with confusion matrices and paired bootstrap intervals. V5 and V7 were evaluated only on triggered records in this experiment; do not interpret ensemble performance as their standalone full-suite performance.

These are original NF4 base-plus-adapter results, not benchmarks of the merged or requantized weights. `deployment_bf16.json` and `deployment_nf4.json` separately record fixed synthetic probe differences. The complete training-data publication remains pending personal-contact-information review; no raw training or benchmark text is included here.
