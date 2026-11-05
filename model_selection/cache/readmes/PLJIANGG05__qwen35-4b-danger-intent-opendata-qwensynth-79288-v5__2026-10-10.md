---
language:
- en
- zh
license: cc-by-nc-4.0
base_model: Qwen/Qwen3.5-4B
base_model_relation: finetune
library_name: transformers
pipeline_tag: text-generation
tags:
- safety
- dangerous-intent-classification
- binary-classification
- lora
---
# Qwen3.5-4B Danger Intent — Open Data + Qwen Synthetic | 79,288 training-pool records | V5

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

Current repository: [PLJIANGG05/qwen35-4b-danger-intent-opendata-qwensynth-79288-v5](https://huggingface.co/PLJIANGG05/qwen35-4b-danger-intent-opendata-qwensynth-79288-v5). Historical experiment ID: **V5**. Previously named `PLJIANGG05/qwen35-4b-danger-intent-v5`.

`opendata` denotes the six existing public-source datasets listed below, `qwensynth` denotes reviewed and corrected Qwen-generated samples, and `supplement` denotes the second five-category AI-generated supplement. `sampled4000`, when present, means a sampled subset rather than the full pool. Upstream licenses are unchanged.

The name refers to the configured 79,288-record first-stage training pool. The selected checkpoint is best1750; it does not claim every pool record was visited. No second-stage supplement was used by V5.

| Training source | Records in this model's configured training data |
|---|---:|
| Aegis V2 | 25,569 |
| OR-Bench | 20,062 |
| Chinese Do-Not-Answer | 2,724 |
| AdvBench | 509 |
| HarmBench | 391 |
| JBB-Behaviors | 200 |
| Corrected Qwen3.5-4B synthetic data | 29,833 |
| **Total** | **79,288** |

SAFE: **48,003**. UNSAFE: **31,285**. Validation records are not included in these training totals. See `training_dataset_summary.json` for stage and validation provenance.

This rename changes repository naming and documentation only. Model weights, adapters, tokenizer, inference code, scoring configuration and historical results are unchanged. `release_identity.json` retains the original release ID for provenance; `rename_history.json` records the new ID. Raw training text remains excluded from this model repository.

## Training lineage

First-stage pool: 79,288 records. Selected checkpoint: best1750. Original adapter is the selected best-model export, not a new training run.

The name refers to the configured 79,288-record first-stage training pool. The selected checkpoint is best1750; it does not claim every pool record was visited. No second-stage supplement was used by V5. No new training or recalibration was performed for this rename.

## Scoring and limits

Full-candidate conditional log likelihood of SAFE and UNSAFE including the end marker; apply the frozen temperature, bias and review threshold in calibration.json.

Maximum classification context is 1,024 tokens under the fixed scorer. For longer inputs the scorer retains roughly 75 percent of the beginning and 25 percent of the end, with a visible truncation marker. This may discard safety-relevant context.

The full Qwen3.5 conditional-generation architecture is retained for adapter compatibility. Only text-input safety classification was trained and evaluated; no image/video safety claim is made.

English and Chinese are present in the task and training data. The current expanded comparison is English only and does not establish Chinese or other-language performance. `SAFE` is not a guarantee that an input or downstream response is harmless.

## Evaluation protocol

Historical results and the expanded 85 percent-trigger comparison use **NF4 upstream base plus the original unmerged adapter**, with BF16 computation. The full BF16 merged model is a deployment artifact. Requantizing the merged model is not numerically identical to quantizing the base first and adding LoRA. Deployment probe checks are separate from the benchmark.

V9 confidence below 0.85 triggers one vote each from V9, V5 and V7. Confidence equal to or above 0.85 uses V9 alone. The 85 percent threshold does not mean an 85 percent accuracy guarantee. V5/V7 use their existing calibration and decision thresholds unchanged.

XSTest was used historically for validation/calibration; ToxicChat has been inspected repeatedly. Neither is a new blind holdout. New OpenAI Moderation, SimpleSafetyTests and WildGuardTest subsets are English-filtered and normalized-exact-deduplicated against used local data. Their definitions differ from the original Qwen paper, and upstream foundation-model contamination cannot be ruled out. Evaluation results are supplied in the accompanying experiment report when complete.

## Provenance and verification

Base: [Qwen/Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B), revision `851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a`.

`merge_verification.json` records a streaming check of every exported tensor, adapter coverage, tied weights, and BF16 loader dtype conversions. `SHA256SUMS.json` lists distributed files. Adapter tensors are unchanged; its configuration has a portable pinned base identifier instead of a machine-specific path.

## Licenses and attribution

Copyright 2026 PLJIANGG05 for new fine-tuning contributions. **CC-BY-NC-4.0 applies only to the new fine-tuning contribution**, including the adapter; see `LICENSE`. It does not replace or restrict rights granted by the upstream base's Apache-2.0 license, preserved verbatim in `LICENSE.base-model`. This combined artifact contains components under different licenses. The Python inference code is Apache-2.0 under `LICENSE.code`. Upstream training sources retain their respective licenses and attribution; no claim of ownership is made over upstream data.

Please attribute PLJIANGG05 and the original Qwen authors and respect applicable upstream notices. Training text is not included in this model repository. Users should validate the classifier on their own independent data, review false positives/negatives, and retain a human review route for consequential decisions.

## Completed expanded comparison

`evaluation_comparison.json` contains completed results for all 8,498 locked records, including 2,607 new English records. It reports V9 alone, the V9-first 85 percent-trigger V9/V5/V7 ensemble, and native Qwen3Guard Strict and Loose, with confusion matrices and paired bootstrap intervals. V5 and V7 were evaluated only on triggered records in this experiment; do not interpret ensemble performance as their standalone full-suite performance.

These are original NF4 base-plus-adapter results, not benchmarks of the merged or requantized weights. `deployment_bf16.json` and `deployment_nf4.json` separately record fixed synthetic probe differences. The complete training-data publication remains pending personal-contact-information review; no raw training or benchmark text is included here.
