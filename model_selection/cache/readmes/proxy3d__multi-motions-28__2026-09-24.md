---
language:
  - en
  - ru
license: mit
library_name: transformers
pipeline_tag: text-classification
base_model: FacebookAI/xlm-roberta-base
tags:
  - emotion-classification
  - multi-label-classification
  - goemotions
  - xlm-roberta
  - english
  - russian
  - affective-computing
widget:
  - text: "Я наконец закончил — какое облегчение!"
  - text: "Thank you, this really helped me."
---

# Multi-Motions 28 — EN/RU


> ## 📖 Detailed article and benchmarks
>
> A full description of the model, data preparation, EN/RU training approach,
> benchmark results and native-Russian validation is available here:
>
> **[Multi-Motions 28 — Article & Benchmarks](https://huggingface.co/spaces/proxy3d/multi-motions-28-article)**
>
**One bilingual XLM-RoBERTa checkpoint · English + Russian · 28 GoEmotions-compatible outputs · multi-label classification.**

**Author:** Ilya Zelenskiy (proxy3d)  
**Telegram channel:** https://t.me/greenruff  
**Model repository:** https://huggingface.co/proxy3d/multi-motions-28

**Related work:**
- Communication Styles LLM — article / live documentation: https://iproxy3d.github.io/communication-styles-llm/
- Communication Styles LLM — GitHub: https://github.com/iproxy3d/communication-styles-llm
- **Multi-Motions 28 — detailed article and benchmarks:** https://huggingface.co/spaces/proxy3d/multi-motions-28-article

The model returns a complete **28-dimensional sigmoid score vector**: 27 fine-grained emotions plus `neutral`. It was built as a single EN/RU model rather than separate English and Russian classifiers, and it was additionally validated on independent **native-Russian** corpora that were not used for training or checkpoint selection.

> **Detailed article:** [https://huggingface.co/spaces/proxy3d/multi-motions-28-article](https://huggingface.co/spaces/proxy3d/multi-motions-28-article)  
> **Russian quick overview:** [`README_RU.md`](./README_RU.md)  
> **Machine-readable benchmarks:** [`benchmarks.json`](./benchmarks.json)


## Why use this model?

- One checkpoint for **English and Russian**.
- Fine-grained **28-label** GoEmotions-compatible representation rather than only a small set of basic emotions.
- Full continuous score vector is available for agents, analytics, routing, state models, and downstream calibration.
- The selected training configuration was checked across **3 independent random seeds**.
- Russian transfer was tested on **CEDR** and **SemEval-2025 RU** without training on either benchmark.

## Application context — Communication Styles LLM

A practical application context for this classifier is the **Communication Styles LLM** project, which explores emotion-aware conversational agents, persistent emotional state, communication styles, motivation, and microdialogue-based behavior control.

The 28-dimensional output of this model can be used as the semantic emotion signal for such a system: instead of reducing a message to a single emotion label, downstream logic can consume the full emotion vector and combine it with state, style, and dialogue context.

- **Article / live documentation:** https://iproxy3d.github.io/communication-styles-llm/
- **GitHub repository:** https://github.com/iproxy3d/communication-styles-llm

The companion repository is also the natural place for end-to-end integration examples that connect this classifier to the agent pipeline.

## Labels

`admiration, amusement, anger, annoyance, approval, caring, confusion, curiosity, desire, disappointment, disapproval, disgust, embarrassment, excitement, fear, gratitude, grief, joy, love, nervousness, optimism, pride, realization, relief, remorse, sadness, surprise, neutral`

## Quick start — Transformers

```python
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

MODEL_ID = "proxy3d/multi-motions-28"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, use_fast=True)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_ID).eval()

text = "Я наконец закончил — какое облегчение!"
inputs = tokenizer(
    text,
    return_tensors="pt",
    truncation=True,
    max_length=64,
)

with torch.inference_mode():
    scores = torch.sigmoid(model(**inputs).logits[0])

result = sorted(
    [(model.config.id2label[i], float(scores[i])) for i in range(len(scores))],
    key=lambda x: x[1],
    reverse=True,
)

print(result[:5])
```

The model was trained/evaluated with `max_length=64`; using the same value is recommended for reproducible inference behavior.

## Hugging Face pipeline

Because `config.json` declares `problem_type = "multi_label_classification"`, the Transformers text-classification pipeline uses sigmoid outputs for this model.

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="proxy3d/multi-motions-28",
    tokenizer="proxy3d/multi-motions-28",
)

scores = classifier(
    "I am nervous, but also excited about tomorrow.",
    top_k=None,
    truncation=True,
    max_length=64,
)
print(scores)
```

## Convenience wrapper

If you clone the repository, it also contains a small inference wrapper that returns all 28 scores plus optional thresholded labels:

```bash
pip install -e .
```

```python
from goemotions_en_ru import EmotionClassifier

clf = EmotionClassifier("proxy3d/multi-motions-28")
result = clf.predict("Спасибо, это действительно помогло.", top_k=5)

print(result["top"])
print(result["scores"])   # all 28 dimensions
print(result["labels"])   # convenience thresholds
```

## Benchmarks

Values are mean ± population standard deviation over 3 independently trained seeds.

| Evaluation | Micro-F1 | Macro-F1 | Micro-AP | Macro-AP |
|---|---:|---:|---:|---:|
| GoEmotions EN test | **0.5953 ± 0.0017** | **0.5196 ± 0.0035** | **0.6366 ± 0.0041** | **0.5065 ± 0.0028** |
| GoEmotions RU translated test | **0.5654 ± 0.0014** | **0.4826 ± 0.0050** | **0.5950 ± 0.0023** | **0.4609 ± 0.0057** |
| CEDR native RU, 5 shared labels | **0.5180 ± 0.0135** | **0.5295 ± 0.0181** | **0.6388 ± 0.0003** | **0.6762 ± 0.0079** |
| SemEval-2025 native RU, 6 shared labels | **0.6355 ± 0.0142** | **0.6332 ± 0.0180** | **0.8407 ± 0.0013** | **0.8448 ± 0.0047** |

### How to interpret the native-Russian results

CEDR and SemEval-2025 RU are **external transfer tests**, not datasets on which this checkpoint was trained or tuned. The model saw **zero CEDR and zero SemEval/BRIGHTER train/dev examples** during training and checkpoint selection. Only emotions actually annotated by each benchmark were scored; the other GoEmotions dimensions were ignored rather than treated as negatives.

This is deliberately different from a benchmark leaderboard where systems are trained directly on the target benchmark. The native-RU tests answer a different engineering question: **does the bilingual 28-emotion representation transfer to original Russian text from unseen corpora?**

See `benchmarks.json` for machine-readable aggregate metrics. The full article is published as a free [Hugging Face Static Space](https://huggingface.co/spaces/proxy3d/multi-motions-28-article); its source is also kept in `docs/index.html`.

## Scores and thresholds

The raw model output should be passed through sigmoid. The resulting 28 values are best interpreted as **model confidence scores**, not universally calibrated probabilities.

`thresholds.json` contains per-label thresholds selected on the bilingual GoEmotions validation distribution. They are useful defaults, but fixed thresholds are domain-sensitive. On a new production domain, continuous scores are usually the safest interface; recalibrate thresholds on a separate development set if hard labels are required.

## Intended use

Suitable for:

- emotion-aware conversational agents;
- affect/state representations;
- analytics and monitoring;
- routing and downstream decision systems;
- EN/RU research requiring a shared fine-grained emotion space.

Do not use expressed-text emotion as a clinical diagnosis or as the sole basis for high-stakes decisions about a person.

## Architecture

- Backbone: `FacebookAI/xlm-roberta-base`
- Task: multi-label sequence classification
- Outputs: 28 independent logits → sigmoid scores
- Languages validated in this release: English and Russian
- Recommended inference max length: 64 tokens

The public model repository intentionally contains **no training datasets, dataset-construction scripts, translation pipeline, synthetic-data generator, annotation pipeline, trainer states, or training code**.

## Author and project links

- **Author:** Ilya Zelenskiy (proxy3d)
- **Telegram channel:** https://t.me/greenruff  
**Model repository:** https://huggingface.co/proxy3d/multi-motions-28
- **Communication Styles LLM article:** https://iproxy3d.github.io/communication-styles-llm/
- **Communication Styles LLM GitHub:** https://github.com/iproxy3d/communication-styles-llm
- **Multi-Motions 28 detailed article:** https://huggingface.co/spaces/proxy3d/multi-motions-28-article
- **Citation metadata:** `CITATION.cff`

## License

Released under the MIT License. See `THIRD_PARTY_NOTICES.md` for third-party notices and the training-data licensing reminder.

