---
language: en
license: mit
base_model: FacebookAI/roberta-base
datasets:
  - google-research-datasets/go_emotions
pipeline_tag: text-classification
tags:
  - roberta
  - emotion
  - multi-label-classification
---

# Open Emotions

An English RoBERTa text classifier fine-tuned on GoEmotions for 27 emotions plus neutral. It predicts multiple labels independently. It detects emotions expressed in language; its scores do not establish a person's internal emotional state.

Repository: `mts-the-architect/open-emotions`. These are the original Open Emotions GoEmotions fine-tuned weights, published with openly downloadable weights. The later synthetic continuation is not included.

## Evaluation

Evaluated on the official GoEmotions `simplified` test split after selecting the checkpoint and threshold using validation data.

| Metric | Test result |
| --- | --- |
| Micro-F1 | 0.6047 |
| Macro-F1 | 0.4353 |

Global score threshold: **0.30**. This threshold was selected on validation micro-F1 from a grid of 0.10 through 0.80 in increments of 0.05. It was not selected on test results. Checkpoints were selected by validation micro-F1 at threshold 0.5. Scores use sigmoid and do not sum to one.

| Emotion | Precision | Recall | F1 | Test support |
| --- | --- | --- | --- | --- |
| admiration | 0.649 | 0.778 | 0.708 | 504 |
| amusement | 0.745 | 0.909 | 0.819 | 264 |
| anger | 0.440 | 0.515 | 0.474 | 198 |
| annoyance | 0.393 | 0.309 | 0.346 | 320 |
| approval | 0.450 | 0.396 | 0.421 | 351 |
| caring | 0.418 | 0.437 | 0.428 | 135 |
| confusion | 0.457 | 0.418 | 0.437 | 153 |
| curiosity | 0.491 | 0.704 | 0.579 | 284 |
| desire | 0.642 | 0.410 | 0.500 | 83 |
| disappointment | 0.484 | 0.099 | 0.165 | 151 |
| disapproval | 0.399 | 0.419 | 0.409 | 267 |
| disgust | 0.609 | 0.317 | 0.417 | 123 |
| embarrassment | 0.000 | 0.000 | 0.000 | 37 |
| excitement | 0.485 | 0.311 | 0.379 | 103 |
| fear | 0.662 | 0.679 | 0.671 | 78 |
| gratitude | 0.929 | 0.923 | 0.926 | 352 |
| grief | 0.000 | 0.000 | 0.000 | 6 |
| joy | 0.600 | 0.634 | 0.616 | 161 |
| love | 0.734 | 0.882 | 0.802 | 238 |
| nervousness | 0.000 | 0.000 | 0.000 | 23 |
| optimism | 0.620 | 0.527 | 0.570 | 186 |
| pride | 0.000 | 0.000 | 0.000 | 16 |
| realization | 0.800 | 0.028 | 0.053 | 145 |
| relief | 0.000 | 0.000 | 0.000 | 11 |
| remorse | 0.622 | 0.911 | 0.739 | 56 |
| sadness | 0.503 | 0.513 | 0.508 | 156 |
| surprise | 0.528 | 0.539 | 0.533 | 141 |
| neutral | 0.655 | 0.726 | 0.689 | 1787 |

## Training

- Base checkpoint: `FacebookAI/roberta-base` at `e2da8e2f811d1448a5b465c236feacd80ffbac7b`.
- Dataset: `google-research-datasets/go_emotions`, configuration `simplified`, revision `add492243ff905527e67aeb8b80c082af02207c3`.
- Official splits: 43,410 train, 5,426 validation, 5,427 test examples.
- Full encoder and classifier fine-tuning, with binary cross-entropy on logits and multi-hot targets.
- 3 epochs, batch size 32, maximum length 128, learning rate 2e-05, seed 42.
- AdamW, weight decay 0.01, linear decay with 6% warmup, gradient norm clipping at 1.0.
- Full precision and eager attention. Hardware: AMD Radeon(TM) 8060S Graphics using AMD ROCm PyTorch inside WSL on an ASUS ROG Flow Z13.
- Recorded training runtime: 30.5 minutes, including initialization and evaluation.
- Package versions and settings: `training_run.json`; epoch results: `history.json`; detailed test results: `test_metrics.json`.
- Training source: `training_script.py`, with its digest in `training_source.sha256`; Linux package lock: `training_environment.lock.txt`.

## Training hardware and environment

- Laptop: ASUS ROG Flow Z13 (2025), GZ302EA.
- Processor: AMD Ryzen AI Max+ 395.
- Training GPU: integrated AMD Radeon 8060S Graphics.
- System memory: 128 GB unified RAM (approximately 123.6 GiB reported by Windows).
- Host: Windows 11 Pro; training ran in Ubuntu 24.04 under WSL 2.
- Full-precision training; no quantization or mixed precision was used.
- One local machine and one GPU; no cloud training service.

The unified RAM figure is system capacity, not measured peak training memory. Peak GPU memory and power consumption were not recorded.

| Package | Recorded version |
| --- | --- |
| torch | 2.13.0+rocm10.0.0 |
| transformers | 4.57.6 |
| datasets | 3.6.0 |
| numpy | 2.5.3 |
| pyarrow | 20.0.0 |

## Training progression

There were 1,357 optimizer steps per epoch, 4,071 steps across three epochs, and 130,230 training-example presentations. The reported losses are mean batch training losses; they are not classification accuracy. Validation figures below use threshold 0.50 for checkpoint selection. Final test figures use the separately selected validation threshold of 0.30, so the tables use different thresholds.

| Epoch | Mean training loss | Validation micro F1 | Validation macro F1 |
| --- | ---: | ---: | ---: |
| 1 | 0.16473 | 0.4037 | 0.1681 |
| 2 | 0.09309 | 0.5408 | 0.3447 |
| 3 | 0.08309 | 0.5590 | 0.3687 |

The selected checkpoint was epoch 3. The total recorded run took 1,829.27 seconds (30.49 minutes), including initialization and evaluation. Full settings and exact raw values are included in `training_run.json` and `history.json`. The training inputs were real GoEmotions examples; synthetic examples were not used for this published checkpoint.

## Local use

From the project directory:

```powershell
.\.venv\Scripts\python.exe predict_emotions.py "Thank you so much for helping me."
```

Or load the model using Transformers:

```python
import json
from pathlib import Path
from transformers import pipeline

from huggingface_hub import snapshot_download
folder = Path(snapshot_download("mts-the-architect/open-emotions-125m-fp32"))
options = json.loads((folder / "thresholds.json").read_text())
classifier = pipeline("text-classification", model=str(folder), tokenizer=str(folder), device=-1)
scores = classifier("Thank you so much for helping me.", top_k=None,
                    function_to_apply="sigmoid", truncation=True,
                    max_length=options["max_length"])
labels = [item for item in scores if item["score"] >= options["global_threshold"]]
print(labels)
```

## Limits and interpretation

GoEmotions contains English Reddit comments with human annotations. Performance on other domains, languages, long documents, irony, or ambiguous text has not been established here. Rare emotions have much less training data; consult the per-label results. Inputs longer than the configured maximum are truncated. A single global threshold trades precision against recall and does not calibrate scores as probabilities. This is an initial baseline; no superiority over existing emotion models is claimed.

## Sources and attribution

- [RoBERTa base model card](https://huggingface.co/FacebookAI/roberta-base), which lists MIT licensing.
- [GoEmotions dataset card](https://huggingface.co/datasets/google-research-datasets/go_emotions), which lists Apache-2.0 licensing. Original comments are not included in this model artifact.
- [GoEmotions paper](https://research.google/pubs/goemotions-a-dataset-of-fine-grained-emotions/): Demszky et al., 2020.
- [RoBERTa paper](https://arxiv.org/abs/1907.11692): Liu et al., 2019.

The model includes the original MIT license notice in `LICENSE`. Refer to the dataset source for its own license and terms.

## Long-text chunks and sliding windows

[Windowing guide](WINDOWING_GUIDE.md) includes starting ranges, local usage and a labeled evaluation plan. Start with **128 total tokens / 32 context tokens overlap**; compare no overlap, 25% and 50% overlap. Total window tokens include special tokens and, for sensations, the repeated target/context prefix.

Download `predict_windows.py` for per-window evidence and exploratory max/mean summaries. Sensations evaluates only windows containing a complete target mention. Windowing does not increase the model's native context capacity, change the trained weights, or establish higher accuracy. Existing thresholds were calibrated on short inputs; document-level aggregation is not calibrated.

[Diagnostic report](WINDOW_EXPERIMENT_RESULTS.md) compares 18 configurations on an assistant-authored sample without reference labels. `window-experiment-results.zip` contains the sample, all results and comparison records; `experiment_windows.py` and `test_windows.py` preserve the reproducible diagnostic and boundary checks.

## HTTP inference and API access approval

See [API_USAGE.md](API_USAGE.md) for running the local service, requesting an API key, owner approval/revocation commands, and using the inference endpoints. Download `serve_models.py`, `api_access.py`, `api_demo.html` and `predict_windows.py`; `--model-dir TASK=PATH` accepts downloaded model directories.

Default access requires approved keys, with **10 requests/minute and 500/day per key**. Applications remain pending until owner approval. Rate exhaustion returns HTTP 429 with Retry-After; input size and inference concurrency are also bounded. `test_api_access.py` exercises approvals, revocation and quotas. The server is local only; these Hub files do not deploy a public HTTP endpoint. Never upload the private approval/usage database.
