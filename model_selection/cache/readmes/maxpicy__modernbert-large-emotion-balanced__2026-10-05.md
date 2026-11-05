---
language: en
license: mit
library_name: transformers
pipeline_tag: text-classification
base_model: answerdotai/ModernBERT-large
tags:
- emotion
- emotion-classification
- modernbert
- text-classification
datasets:
- google-research-datasets/go_emotions
- dair-ai/emotion
- gsri-18/ISEAR-dataset-complete
- cardiffnlp/tweet_eval
metrics:
- accuracy
- f1
---

# ModernBERT-large — emotion classifier (balanced 6-dataset fine-tune)

Fine-tune of [`answerdotai/ModernBERT-large`](https://huggingface.co/answerdotai/ModernBERT-large) on a per-class **balanced** merge of 6 English emotion datasets, mirroring the methodology of [`j-hartmann/emotion-english-distilroberta-base`](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base).

**This is the production default for the EmotiSpeech NTU SC4001 project.** Smaller sister model: [`maxpicy/modernbert-base-emotion-balanced`](https://huggingface.co/maxpicy/modernbert-base-emotion-balanced).

## Labels (7-class Ekman + neutral)

`anger, disgust, fear, joy, neutral, sadness, surprise`

## Training data

6 datasets harmonised to the 7-class scheme, then **per-class downsampled to 2,045 examples** (size of the smallest class after deduping).

| Source | License | Pre-balance contribution |
|---|---|---|
| [Crowdflower 2016 (40k tweets)](https://github.com/tlkh/text-emotion-classification) | Public domain | anger, joy, neutral, sadness, surprise, fear (via `worry`) |
| [`dair-ai/emotion` (Saravia et al. 2018)](https://huggingface.co/datasets/dair-ai/emotion) | unknown | anger, fear, joy, sadness, surprise |
| [`google-research-datasets/go_emotions` (Demszky et al. 2020)](https://huggingface.co/datasets/google-research-datasets/go_emotions) | Apache 2.0 | all 7 (single-label rows only) |
| [`gsri-18/ISEAR-dataset-complete` (Vikash 2018)](https://huggingface.co/datasets/gsri-18/ISEAR-dataset-complete) | unknown | anger, disgust, fear, joy, sadness |
| [MELD (Poria et al. 2019)](https://github.com/declare-lab/MELD) | GPL-3.0 | all 7 |
| [`cardiffnlp/tweet_eval` config `emotion`](https://huggingface.co/datasets/cardiffnlp/tweet_eval) (substitute for SemEval-2018 Task 1 EI-reg) | unknown | anger, joy, sadness |

Splits after balancing: train 10,020 / val 1,432 / test 2,863.

## Training

- **Base model**: `answerdotai/ModernBERT-large` (~395M params)
- **Hyperparameters**: 2 epochs (epoch 3 overfit on the 3-epoch run; eval_loss went 0.89 → 1.54), batch 16, lr 2e-5, AdamW
- **Hardware**: 1× A100 on NSCC ASPIRE 2A (`g1` queue), ~14 minutes wall-clock
- **Tokenization**: HF auto-tokenizer, max_length 256

## Test-set evaluation

| Metric | Value |
|---|---|
| accuracy     | **0.607** |
| macro_f1     | **0.608** |
| weighted_f1  | **0.608** |

Per-class F1: anger 0.627, disgust 0.751, fear 0.522, joy 0.663, neutral 0.499, sadness 0.590, surprise 0.600. Beats the [base variant](https://huggingface.co/maxpicy/modernbert-base-emotion-balanced) by ~3 points on macro-F1.

## Usage

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

ckpt = "maxpicy/modernbert-large-emotion-balanced"
tok = AutoTokenizer.from_pretrained(ckpt)
model = AutoModelForSequenceClassification.from_pretrained(ckpt).eval()

texts = ["What is happening?", "I'm so happy today!", "I can't believe this."]
inputs = tok(texts, padding=True, truncation=True, return_tensors="pt")
with torch.inference_mode():
    probs = torch.softmax(model(**inputs).logits, dim=-1)

id2label = model.config.id2label
for text, p in zip(texts, probs):
    top = int(p.argmax())
    print(f"{text!r:40s} -> {id2label[top]} ({p[top]:.2f})")
```

## Audio benchmark behaviour

On the EmotiSpeech 63-second `kfseetoh.wav` benchmark (123 rolling-window inferences):

| Model | Distinct dominant labels | Confidence range |
|---|---|---|
| j-hartmann pretrained baseline | 6 | 0.25–0.98 |
| **`maxpicy/modernbert-large-emotion-balanced`** (this) | **6** | **0.26–0.98** |

Matches the j-hartmann reference baseline on label diversity and exceeds it on per-class diagnostic granularity (24 surprised predictions vs 13).


## Citation

If this checkpoint is useful in your work, please credit the upstream models and datasets, plus:

```
@misc{wong2026emotispeech,
  author = {Wong, Max et al.},
  title = {EmotiSpeech: word-level multimodal speech emotion},
  year = {2026},
  note = {NTU SC4001 academic project},
}
```

Methodology mirrors **j-hartmann/emotion-english-distilroberta-base** — please cite their work too.

## License

MIT for the model weights and configuration. Underlying datasets retain their own licenses (see table above).
