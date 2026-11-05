---
license: apache-2.0
language: [en]
base_model: distilbert/distilbert-base-uncased
pipeline_tag: text-classification
tags:
  - safety
  - guardrail
  - dialect
  - fairness
  - group-dro
  - text-to-image
  - reproducibility
---

# Dialect-robust T2I prompt classifier (GroupDRO)

DistilBERT trained with **online GroupDRO** (group-balanced sampling over 12 (label x dialect)
groups plus a worst-group objective), on paired Standard American English / dialect
text-to-image prompts.

Reproduction artifact for Table 8 of our study on the dialect penalty in text-to-image safety
filters. The method, group definition, training hyperparameters and full analysis are in the
paper; this card covers only what you need to load and scope the checkpoint.

## ⚠️ Intended use and scope

**This is a research reproduction artifact, not a deployable NSFW filter.**

It was trained on a narrow, templated prompt distribution (240 benign + 222 unsafe base prompts,
each rendered in 6 dialects). The benign class carries a distinctive Stable-Diffusion tag style
("studio food photography, soft diffused lighting, 50mm lens, f/2.8, 8k"), and the model keys on
that surface cue:

| Input | P(NSFW) |
|---|---|
| Full held-out benign prompt (with the tag suffix) | 0.0001 |
| The same prompt with the tag suffix removed | 0.9999 |
| An ordinary sentence ("A child playing with a puppy") | 0.9999 |

Anything outside the training prompt style is classified NSFW with near-certainty. Do not use it
as a general-purpose safety filter. Use it to reproduce the paper's dialect-penalty measurements,
where all inputs share that style and the cue is dialect-invariant.

## Results

Paper Table 8 (inner-split, mean ± std over 10 seeds). This checkpoint is the **97.5% SAE, GroupDRO** cell,
seed 0.

| SAE Ratio | Algorithm | Mean Acc. (%) | Worst-Group (%) | \|ΔTPR\| (pp) | \|ΔFPR\| (pp) |
|---|---|---|---|---|---|
| 97.5% | ERM | 99.91 ± 0.14 | 99.12 ± 1.48 | 0.01 ± 0.03 | 0.19 ± 0.33 |
|  | ERM + bal. sampling | 99.99 ± 0.01 | 99.91 ± 0.17 | 0.01 ± 0.03 | 0.01 ± 0.02 |
|  | **GroupDRO** ⬅︎ **this checkpoint** | **100.00 ± 0.01** | **99.95 ± 0.14** | **0.01 ± 0.03** | **0.00 ± 0.00** |
| 98.0% | ERM | 99.97 ± 0.04 | 99.63 ± 0.51 | 0.00 ± 0.00 | 0.07 ± 0.10 |
|  | ERM + bal. sampling | 100.00 ± 0.00 | 100.00 ± 0.00 | 0.00 ± 0.00 | 0.00 ± 0.00 |
|  | GroupDRO | 99.99 ± 0.01 | 99.91 ± 0.17 | 0.01 ± 0.03 | 0.01 ± 0.02 |
| 98.5% | ERM | 99.99 ± 0.04 | 99.88 ± 0.37 | 0.00 ± 0.00 | 0.03 ± 0.10 |
|  | ERM + bal. sampling | 99.99 ± 0.03 | 99.88 ± 0.27 | 0.00 ± 0.00 | 0.03 ± 0.08 |
|  | GroupDRO | 99.99 ± 0.03 | 99.92 ± 0.25 | 0.00 ± 0.00 | 0.03 ± 0.07 |
| 99.0% | ERM | 99.95 ± 0.11 | 99.54 ± 0.99 | 0.00 ± 0.00 | 0.12 ± 0.25 |
|  | ERM + bal. sampling | 99.92 ± 0.08 | 99.65 ± 0.37 | 0.07 ± 0.11 | 0.06 ± 0.15 |
|  | GroupDRO | 99.99 ± 0.01 | 99.92 ± 0.17 | 0.00 ± 0.00 | 0.02 ± 0.03 |
| 99.5% | ERM | 97.72 ± 2.94 | 84.58 ± 19.71 | 0.02 ± 0.05 | 5.24 ± 6.80 |
|  | ERM + bal. sampling | 98.70 ± 2.41 | 90.79 ± 16.61 | 0.00 ± 0.00 | 3.00 ± 5.56 |
|  | GroupDRO | 98.73 ± 2.56 | 91.50 ± 17.23 | 0.00 ± 0.00 | 2.93 ± 5.92 |
| 100.0% | ERM | 95.04 ± 3.18 | 68.17 ± 17.30 | 0.00 ± 0.00 | 11.47 ± 7.35 |
| Balanced data | ERM | 100.00 ± 0.01 | 99.95 ± 0.14 | 0.01 ± 0.03 | 0.00 ± 0.00 |

Nine of the 10 seeds score exactly 1.0 / 1.0 (seed 3 scores 0.99964 / 0.9955), so seed 0 is the
modal outcome, not a selected best.

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tok = AutoTokenizer.from_pretrained("Minguinho-zeze/dialect-penalty-t2i-guardrail-groupdro")
model = AutoModelForSequenceClassification.from_pretrained("Minguinho-zeze/dialect-penalty-t2i-guardrail-groupdro").eval()

text = "..."  # a T2I prompt in the paper's style
with torch.no_grad():
    probs = model(**tok(text, return_tensors="pt", truncation=True, max_length=512)).logits.softmax(-1)
# id2label = {0: "SFW", 1: "NSFW"}
```

## Related

- Paper: [arXiv:2608.29589](https://arxiv.org/abs/2608.29589)
- Dataset: [`Minguinho-zeze/dialect-penalty-t2i`](https://huggingface.co/datasets/Minguinho-zeze/dialect-penalty-t2i)
- Code: [`minguinho26/dialect-penalty-t2i`](https://github.com/minguinho26/dialect-penalty-t2i) (`stage3_mitigation/`)
- Companion checkpoint: ERM + bal. sampling variant (98.0% SAE, seed 0): `Minguinho-zeze/dialect-penalty-t2i-guardrail-erm-balsampling`
