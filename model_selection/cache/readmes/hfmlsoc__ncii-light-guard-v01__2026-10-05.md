---
library_name: transformers
license: mit
language:
- en
base_model:
- microsoft/harrier-oss-v1-270m
pipeline_tag: text-classification
---

# Model Card for NCII-Light-Guard v0.1

The following is a light-weight classification model designed to score the NCII risk of image editing prompts. 

### How to use

Minimal use code with `pipeline`:

```python
from transformers import pipeline

clf = pipeline("text-classification", model="hfmlsoc/ncii-light-guard-v01")
clf("skirt riding up the thigh")
```

Returns:
```
[{'label': 'ncii', 'score': 0.672331690788269}]
```

## Why this exists

General-purpose image-editing models have recently become more performant, particularly in their ability to preserve the identity of individual people while making photo-realistic changes to a picture.
This has led to increased concerns about abuse of models to create **non-consensual intimate imagery (NCII)** from ordinary photos. As a result, some jurisdictions, including the EU, are introducing regulation mandating deployers to add targeted guardrails to prevent users from easily nudifying subjects of photographs or editing images to sexualize them without their consent.

This model acts as a small **prompt guard**: it scores whether an instruction looks like an edit request that has a high risk of enabling NCII creation.

The proposed model was designed to prioritize computational efficiency, it is meant as an extremely easy to deploy minimal step regardless of compute resources and to avoid using compute or time overhead to a demo, and as a way to add significant limitations on the abuse landscape rather than to catch every possible "jailbreak". The coverage and accuracy were maximized under these constraints, but it should be deployed with limitations in mind.

## What the model is

- **Model:** [`hfmlsoc/ncii-light-guard-v01`](https://huggingface.co/hfmlsoc/ncii-light-guard-v01)
- **Base model:** [`microsoft/harrier-oss-v1-270m`](https://huggingface.co/microsoft/harrier-oss-v1-270m) (~270M-parameter encoder)
- **Task:** binary text classification — `safe` for **Likely safe** vs `ncii` for **NCII risk**
- **Input:** an image-edit (or similar) prompt  
- **Output:** label, probability of `ncii` (**NCII risk**)

**`ncii` (positive)** means: if applied to a real person’s photo, the edit carries a risk of significantly nudifying or adding a clear sexual dimension to the subject's direct situation. Since consent cannot be identified at the prompt level, the model returns a NCII-risk signal — not a determination of user intent or non-consent.
**`safe`** means: clothes, style, scene, objects, or other edits that would not typically count as NCII on a user’s photo. Edge cases considered included removing or replacing clothing without meaningfully changing nudity, general romance scenes, and background edits not directly related to the user. The name stresses that this is a heuristic “looks low-risk from text alone,” not a guarantee of safety.

## Limitations

- **Text only** — does not see the image; identity or context in the photo is unknown
- **English-language** — while the model's pre-training and regularization during fine-tuning give it some multilingual performance, it was trained primarily on English-language data
- **Inherent biases** — Despite efforts to balance gender in the training set, the model still shows significant gender-dependent discrepancies on test examples; the model has not been systematically evaluated to date for disparate performance based on gender or sexual identity, size or other relevant social factors
- **Not a legal or safety guarantee** — `likely-safe` / `ncii-risk` are heuristics, not proof of intent, consent, or harm
- **Domain shift:** T2I tag soup, other languages, and adversarial phrasing are harder
- **Eval contamination note:** some public edit *benchmark* prompts appear in training as presumed-safe negatives; treat reported F1 as in-distribution for this constructed mix, not as a pure unseen-benchmark score

## Feedback

You can test the model and provide feedback on its preditions using its [testing Space](https://huggingface.co/spaces/yjernite/test-ncii-promptguard)

## Training overview

The model was trained on "presumed safe" image generation prompts from diverse image editing prompts datasets **including evaluation datasets.**

Synthetic positive examples were obtained by asking Cursor Grok 4.5 to generate 1000 examples across styles and types of NCII. The same model was then ask to rephrase these into minimal "safe alternatives" to create contrastive training examples. Additionally, selected image generation prompts from a public dataset of prompts submitted to CivitAI models were rephrased into editing instructions and annotated by the same model. This version of Cursor/Grok was selected after large open-weight models declined to engage with the topic or to provide synthetic examples given their safety-finetuning.

After training a first model on the dataset described above, all examples were scored, and ~1,400 examples combining "presumed safe" and examples from general-purpose datasets with high score as well as examples annotated by Cursor/Grok as ncii-risk with low predicted scores were manually re-annotated.

Splits are **cluster-aware** (similar prompts kept together) with all `ncii-risk` clusters represented in train. `likely-safe` examples are sampled **per source**, with large sources capped at **2,000** via farthest-point sampling before split assignment. Raw CivitAI ImageGem T2I prompts (`civitai_imagegem`) were excluded from these splits.

| Split | Total | `ncii-risk` | `likely-safe` |
|-------|------:|------------:|--------------:|
| train | 16,817 | 1,200 | 15,617 |
| val | 781 | 56 | 725 |
| test | 971 | 70 | 901 |

The model here was trained on this final dataset as a **rank-8 LoRA** on [`microsoft/harrier-oss-v1-270m`](https://huggingface.co/microsoft/harrier-oss-v1-270m), then merged for deployment. Held-out in-distribution metrics for the shipped run were about **val F1 ≈ 0.94** and **test F1 ≈ 0.92** (accuracy ~99% under heavy class imbalance). Real-world prompts will differ.

### Sources of training examples

| Source | Upstream / notes | Train |
|--------|------------------|------:|
| [`real_edit`](https://huggingface.co/datasets/peter-sushko/RealEdit) | Reddit PhotoshopRequest-style edit requests | 1,810 |
| [`real_edit_plus`](https://huggingface.co/datasets/ben-caffee/RealEdit-Jul2021-Dec2024) | Later RealEdit-style crawl (separate source) | 1,810 |
| [`editscore`](https://huggingface.co/datasets/EditScore/EditScore-RL-Data) | Edit instructions (`likely-safe`-heavy) | 1,810 |
| [`human_edit`](https://huggingface.co/datasets/BryanW/HumanEdit) | Human edit instructions | 1,810 |
| `civitai_midband_edits` | From [`ImageGem`](https://huggingface.co/datasets/MAPS-research/ImageGem-images) CivitAI prompts, rephrased as edits + mid-band scores | 1,810 |
| `training_examples_safe` | Synthetic contrastive `likely-safe` rephrases of NCII-risk prompts | 1,789 |
| [`editjudge_bench`](https://huggingface.co/datasets/EDAnonSubmission/benchmark) | EditJudge-Bench | 1,354 |
| [`geditbench_v2`](https://huggingface.co/datasets/GEditBench-v2/GEditBench-v2) | GEditBench-v2 | 1,040 |
| `training_examples` | Synthetic `ncii-risk` positives (bundled into the 1,200 train positives) | (in `ncii-risk` pool) |
| [`kontext_bench`](https://huggingface.co/datasets/black-forest-labs/kontext-bench) | Kontext-Bench | 856 |
| [`psr_328`](https://huggingface.co/datasets/PSRDataset/PSR-328) | PhotoshopRequest subset | 571 |
| [`sredit_bench`](https://huggingface.co/datasets/zjYinnnn/SREdit-Bench) | SREdit-Bench | 513 |
| [`geditbench`](https://huggingface.co/datasets/stepfun-ai/GEdit-Bench) | GEdit-Bench (English) | 262 |
| [`omniedit`](https://huggingface.co/datasets/TIGER-Lab/OmniEdit-Filtered-1.2M) | OmniEdit (small kept slice) | 182 |

`ncii-risk` labels are concentrated in synthetic `training_examples` plus mid-band / re-annotated rows; most public edit corpora contribute hard **`likely-safe`** negatives.