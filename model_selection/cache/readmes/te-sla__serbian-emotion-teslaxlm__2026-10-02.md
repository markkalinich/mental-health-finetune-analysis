---
language:
  - sr
license: cc-by-sa-4.0
library_name: transformers
pipeline_tag: text-classification
base_model: te-sla/TeslaXLM
tags:
  - multi-label-classification
  - emotion-recognition
  - serbian
  - social-media
  - xlm-roberta
metrics:
  - f1
  - jaccard
---

# Serbian multi-label emotion recognition — TeslaXLM

## Model description

This is the primary publication encoder and operational default for Serbian
social-media emotion recognition. It is a full fine-tune of
[`te-sla/TeslaXLM`](https://huggingface.co/te-sla/TeslaXLM) at pinned base
revision `982ff4401029ef0b0428e3704bbc592d9cf6965e`.

The model predicts any valid subset of eight labels, in this fixed order:
`anger`, `anticipation`, `disgust`, `fear`, `joy`, `sadness`, `surprise`, and
`trust`. `neutral` is not an output label.

The release artifact is the surviving prespecified seed-42 Round 2 checkpoint.
Its `model.safetensors` SHA-256 is
`d268f017dcd632d3895054d27c9cd34e7a5257ec8b695c1589ea45425cb11421`.
It uses the same cleaned cohort, pinned base revision, full fine-tuning,
emotion-only hard labels, and unweighted BCE recipe as the final family. Its
per-label thresholds were selected on validation only. It is a runnable
representative; the separate ten-seed Round 2.1 panel remains the source of the
model-family claim.

## Intended use

Use the model for research on Serbian multi-label emotion classification and as
the primary encoder in the accompanying experimental portfolio. It is suitable
for batch analysis of Serbian Reddit/Twitter-style text after applying the same
cleaning contract used during training.

It is not intended for clinical, employment, policing, moderation enforcement,
or other high-impact decisions. It should not be used to infer a person's
stable psychological state from a short post.

## Data and preprocessing

Training used a cleaned, neutral-free Emo.SR Reddit and Twitter cohort with
29,961 rows: 23,961 train, 3,000 validation, and 3,000 test. Every retained row
has one or two positive labels. Cleaning included Unicode normalization,
Markdown-to-text conversion, whitespace control, URL/mention placeholders,
hashtag-marker removal, punctuation-run capping, and emoji preservation.

The dataset is not distributed in this model repository. The model license
metadata follows the pinned upstream base model; it does not grant rights to
the training data. Dataset redistribution and privacy require a separate
review.

## Training

- Adaptation: full fine-tuning; no LoRA.
- Objective: emotion-only unweighted binary cross-entropy with hard labels.
- Maximum sequence length: 128 tokens.
- Learning rate: `2e-5`.
- Effective batch size: 64 with physical-batch fallback.
- Precision: BF16 with TF32 and SDPA.
- Maximum epochs: 20; early-stopping patience: 3.
- Checkpoint rule: minimum validation loss within each fit.
- Release artifact: prespecified seed-42 Round 2 representative. This artifact
  was not chosen by test performance or substituted from a different objective.
- Decision thresholds: fitted per label on validation after checkpoint
  selection and stored in `thresholds.json`.

Weighted BCE, multitask objectives, GradNorm, and soft/hybrid targets were
evaluated in later rounds but did not pass the frozen promotion gates. They are
not part of this release.

## Evaluation

The compatible ten-seed unweighted encoder panel used the same 3,000-item
cleaned test cohort and validation-selected thresholds.

| Scope | Seeds | Macro F1 | Macro-F1 sample SD | Sample Jaccard |
| --- | ---: | ---: | ---: | ---: |
| TeslaXLM recipe aggregate | 10 | 0.558964 | 0.003614 | 0.560729 |
| Released seed-42 artifact | 1 | 0.558940 | — | 0.560611 |

The aggregate is the publication claim; it is not presented as the single
artifact's score. TeslaXLM ranked first within this compatible replicated
encoder panel and had the lowest Macro-F1 seed variation of the three final
encoder families.

Per-label mean F1 across ten seeds was strongest for anger (`0.7296`), joy
(`0.6995`), trust (`0.6834`), and sadness (`0.5955`). Disgust (`0.3618`) and
fear (`0.3588`) remained the hardest labels.

The separate 2,575-row neutral abstention probe is a secondary diagnostic, not
an F1 test set. The seed-42 family diagnostic activated at least one emotion on
`95.88%` of probe rows, so the model must not be described as a reliable
neutral detector.

## Inference

The published repository must include `thresholds.json`. Do not replace its
values with `0.5` or tune them on evaluation data.

```python
import json

import torch
from huggingface_hub import hf_hub_download
from transformers import AutoModelForSequenceClassification, AutoTokenizer

repo_id = "te-sla/serbian-emotion-teslaxlm"
labels = [
    "anger", "anticipation", "disgust", "fear",
    "joy", "sadness", "surprise", "trust",
]

tokenizer = AutoTokenizer.from_pretrained(repo_id)
model = AutoModelForSequenceClassification.from_pretrained(repo_id).eval()
with open(hf_hub_download(repo_id, "thresholds.json"), encoding="utf-8") as handle:
    thresholds = torch.tensor(json.load(handle)["thresholds"])

inputs = tokenizer("Ovo je primer teksta.", return_tensors="pt", truncation=True, max_length=128)
with torch.inference_mode():
    probabilities = torch.sigmoid(model(**inputs).logits[0]).cpu()
prediction = [label for label, score, cutoff in zip(labels, probabilities, thresholds) if score >= cutoff]
print(prediction)
```

## Limitations

- The evidence is Serbian social-media text; generalization to news, speech,
  other languages, or formal prose is not established.
- Rare labels, especially disgust and fear, have substantially lower F1.
- The neutral probe shows high false activation under the selected threshold
  policy.
- Social-media models can reproduce demographic, topical, and annotation
  biases from their training data.
- Test evidence is internal and was reused adaptively across later rounds.
- Scores must not be pooled with incompatible nine-label, fixed-threshold, or
  generative panels.

## Reproducibility and evidence

The technical report, exact configuration, ten-seed tables, threshold files,
artifact hash, and code paths are indexed in the accompanying source
repository. `artifact_evaluation.json` records this checkpoint's validation and
test metrics, prediction-cache hashes, thresholds, and the separate family
aggregate. The source repository is currently private; a public code and evidence
archive is not yet linked from this card.

## Citation

The final paper identifier and citation have not yet been assigned. The verified
paper link and BibTeX citation will be added when available.
