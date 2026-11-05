---
license: mit
language:
  - en
base_model: cardiffnlp/twitter-roberta-base-sentiment-latest
library_name: peft
pipeline_tag: text-classification
datasets:
  - mteb/tweet_sentiment_extraction
tags:
  - sentiment-analysis
  - singlish
  - singapore
  - text-classification
  - roberta
  - lora
  - qlora
  - peft
metrics:
  - accuracy
  - f1
model-index:
  - name: sg-sentiment-roberta
    results:
      - task:
          type: text-classification
          name: Sentiment Classification
        dataset:
          name: SG Sentiment (public tweets + HardwareZone forum posts)
          type: custom
        metrics:
          - type: accuracy
            value: 0.782
            name: Accuracy
          - type: f1
            value: 0.784
            name: F1 Macro
---

# SG Sentiment RoBERTa

A 3-class sentiment classifier for Singapore English and Singlish, fine-tuned with QLoRA.

Most off-the-shelf sentiment models are trained on American English Twitter data and degrade on local phrasing, particle usage (`lah`, `sia`, `meh`), and code-mixing. This model adapts a strong English sentiment base to Singaporean text using a small, cheap adapter rather than a full fine-tune.

- **Live demo:** [HuggingFace Space](https://huggingface.co/spaces/Yi-Siang/sg-sentiment-roberta)
- **Code and training pipeline:** [GitHub](https://github.com/ChewYiSiang/sg-sentiment-roberta)

## Usage

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="Yi-Siang/sg-sentiment-roberta")
classifier("wah shiok sia this chicken rice confirm best")
# [{'label': 'positive', 'score': ...}]
```

To load the adapter directly onto the base model instead of the merged weights:

```python
from peft import AutoPeftModelForSequenceClassification
from transformers import AutoTokenizer

model = AutoPeftModelForSequenceClassification.from_pretrained("Yi-Siang/sg-sentiment-roberta")
tokenizer = AutoTokenizer.from_pretrained("Yi-Siang/sg-sentiment-roberta")
```

## Model details

| | |
|---|---|
| Base model | `cardiffnlp/twitter-roberta-base-sentiment-latest` |
| Method | QLoRA: 4-bit NF4 quantised base + LoRA adapters |
| LoRA config | r=8, alpha=16, dropout=0.1, target modules `query` and `value` |
| Also trained | `classifier` and `score` heads (`modules_to_save`) |
| Trainable params | 1.48M |
| Task | 3-class sentiment (positive / negative / neutral) |
| Epochs | 3 |
| Learning rate | 5e-4 |

Only the query and value projections carry adapters, which is the standard LoRA placement from the original paper. The classification head is trained in full because the base model's head does not transfer cleanly to a relabelled dataset.

## Training data

| Source | Examples | Labelling |
|---|---|---|
| [`mteb/tweet_sentiment_extraction`](https://huggingface.co/datasets/mteb/tweet_sentiment_extraction) | 25,342 | Original human labels |
| HardwareZone forum posts | 1,998 | Auto-labelled with Gemma2:2b, run locally via Ollama |
| **Total** | **27,340** | Stratified train / validation / test split |

Class imbalance was handled with computed class weights (roughly 1.06 / 0.88 / 1.08), so the classes are close to balanced and weighting is a minor correction rather than a load-bearing fix.

The Singaporean portion is deliberately small relative to the tweet corpus. The design assumption is that the base model already handles English sentiment well, and the local data is there to shift the decision boundary on Singlish rather than to teach sentiment from scratch.

## Results

Best configuration, held-out evaluation set:

| Metric | Score |
|---|---|
| Accuracy | 0.782 |
| F1 Macro | 0.784 |

### Ablation

Four configurations were trained and compared, tracked in Weights & Biases:

| Run | LoRA rank | Learning rate | Trainable params | Accuracy | F1 Macro |
|---|---|---|---|---|---|
| 1 | 16 | 2e-4 | 2.96M | 0.768 | 0.770 |
| 2 | 8 | 2e-4 | 1.48M | 0.766 | 0.768 |
| 3 | 8 | 5e-4 | 1.48M | 0.774 | 0.776 |
| **4** | **8** | **5e-4** | **1.48M** | **0.782** | **0.784** |

Run 4 shares its hyperparameters with Run 3 and differs in the classification head setup, which produced the single largest gain in the sweep.

Two further things the sweep shows. Doubling the rank from 8 to 16 doubled trainable parameters and improved neither metric, so the adaptation required here is genuinely low-rank and rank 8 is already sufficient capacity. Learning rate mattered more than capacity, which is the usual pattern for LoRA on a dataset this size. F1 macro tracks accuracy closely across all four runs, which is expected given the classes are near-balanced.

## Intended use

Sentiment analysis of informal Singaporean English text: forum posts, social media, reviews, chat.

## Limitations

- **Label noise.** The HardwareZone portion was labelled by a 2B parameter local LLM, not by humans. Those labels are not audited and will contain errors.
- **Narrow Singlish coverage.** 1,998 local examples from a single forum, skewed toward the demographics and topics of that forum. Singlish from other contexts is underrepresented.
- **Informal register only.** Not appropriate for formal documents, legal text, or long-form content.
- **Three coarse classes.** No intensity, no aspect-level sentiment, no sarcasm handling. Sarcasm is common in forum text and is a known failure mode here.
- **Not evaluated for fairness.** No testing across demographic, dialect, or topic subgroups.

## Reproduction

Full data pipeline, training script, and serving code are in the [GitHub repo](https://github.com/ChewYiSiang/sg-sentiment-roberta), including the W&B run configuration and the Docker setup for the inference API.

## Citation

```bibtex
@misc{chew2026sgsentimentroberta,
  author = {Chew, Yi Siang},
  title  = {SG Sentiment RoBERTa: QLoRA-adapted Sentiment Classification for Singapore English},
  year   = {2026},
  url    = {https://huggingface.co/Yi-Siang/sg-sentiment-roberta}
}
```
