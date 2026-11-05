---
language: en
license: apache-2.0
base_model: ProsusAI/finbert
tags:
  - finance
  - sentiment-analysis
  - text-classification
  - finbert
datasets:
  - NOSIBLE/financial-sentiment
metrics:
  - accuracy
pipeline_tag: text-classification
---

# FinBERT — Financial Sentiment (Fine-tuned on NOSIBLE)

Full fine-tuned [ProsusAI/finbert](https://huggingface.co/ProsusAI/finbert) for financial sentiment
classification (`positive` / `neutral` / `negative`), trained on
[NOSIBLE Financial Sentiment](https://huggingface.co/datasets/NOSIBLE/financial-sentiment) (100K examples).

## Model Details
| | |
|---|---|
| Base model | ProsusAI/finbert (110M) |
| Fine-tuning | Full (all weights updated) |
| Dataset | NOSIBLE/financial-sentiment — 100K examples |
| Epochs | 1 |
| Batch size | 16 |
| Learning rate | 2e-5 |
| Warmup ratio | 0.1 |
| Max length | 512 |

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="poseidon1113/finbert-full-sft-financial-sentiment_v3"
)

classifier("Operating profit rose to EUR 13.1 mn from EUR 21.1 mn.")
# → [{'label': 'positive', 'score': 0.98}]

classifier("The company reported a loss for the third consecutive quarter.")
# → [{'label': 'negative', 'score': 0.95}]
```

## Evaluation on FiQA 2018 (all splits combined)

Evaluated on [pauri32/fiqa-2018](https://huggingface.co/datasets/pauri32/fiqa-2018)
(train + validation + test combined) after removing URLs and non-ASCII characters.

| Class | Correct | Total | Accuracy |
|---|---|---|---|
| Positive | 372 | 706 | 52.7% |
| Neutral  | 91  | 115  | 79.1%  |
| Negative | 254 | 373 | 68.1% |
| **Overall** | **717** | **1194** | **60.1%** |

## Comparison across models

| Model | Type | Overall Accuracy on FiQA |
|---|---|---|
| GPT-2 base | Causal LM | ~15% |
| GPT-2 LoRA v1 (PhraseBank) | Causal LM + LoRA | ~15% |
| GPT-2 LoRA v2 (+ NOSIBLE) | Causal LM + LoRA | ~42% |
| FinBERT base | Sequence classifier | 50.9% |
| **FinBERT + NOSIBLE (this model)** | **Sequence classifier** | **60.1%** |

## Why FinBERT outperforms GPT-2 LoRA

FinBERT's encoder-only BERT architecture reads the full sentence bidirectionally,
making it inherently better at classification tasks. GPT-2 is a generative model
adapted for classification via prompting — fundamentally less suited for this task.
For production sentiment classification, encoder models like FinBERT are the right choice.
GPT-2 LoRA is better suited for tasks requiring text generation.

## Limitations
- Trained on English financial news only
- May underperform on social media slang or non-standard financial text
- Labels reflect financial impact sentiment, not general opinion sentiment

## Citation
```bibtex
@article{araci2019finbert,
  title={FinBERT: Financial Sentiment Analysis with Pre-trained Language Models},
  author={Araci, Dogu},
  journal={arXiv preprint arXiv:1908.10063},
  year={2019}
}
```
