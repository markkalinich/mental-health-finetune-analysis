---
language:
- en
license: apache-2.0
library_name: transformers
pipeline_tag: text-classification
base_model: answerdotai/ModernBERT-base
datasets:
- cardiffnlp/tweet_sentiment_multilingual
tags:
- text-classification
- sentiment-analysis
- modernbert
- twitter
metrics:
- accuracy
- f1
model-index:
- name: ModernBERT-sentiment-model
  results:
  - task:
      type: text-classification
      name: Sentiment classification
    dataset:
      name: Tweet Sentiment Multilingual (English)
      type: cardiffnlp/tweet_sentiment_multilingual
      config: english
      split: test
    metrics:
    - type: accuracy
      value: 0.6586
      name: Accuracy
    - type: f1
      value: 0.6485
      name: F1 (macro)
---

# ModernBERT-sentiment-model

A three-class English tweet sentiment classifier (`negative` / `neutral` / `positive`), fine-tuned from [`answerdotai/ModernBERT-base`](https://huggingface.co/answerdotai/ModernBERT-base) on the English subset of [`cardiffnlp/tweet_sentiment_multilingual`](https://huggingface.co/datasets/cardiffnlp/tweet_sentiment_multilingual). 149.6M parameters.

It scores **65.9% accuracy and 0.649 macro-F1** on the held-out test set (three balanced classes, so chance is 33%). That is a working baseline trained in about six minutes on 1,839 tweets, not a production model. Its main weakness is the `neutral` class; see [Limitations](#limitations).

## Labels

| id | label |
|---|---|
| 0 | negative |
| 1 | neutral |
| 2 | positive |

## Usage

Requires `transformers>=4.48` (first release with ModernBERT). The repo includes the tokenizer, so the pipeline works directly:

```python
from transformers import pipeline

clf = pipeline("text-classification", model="salmanhadli/ModernBERT-sentiment-model")
clf("I absolutely love this product! Best purchase ever!", truncation=True, max_length=128)
# label: positive
```

To get scores for all three labels, pass `top_k=None`. The model was trained on inputs truncated to 128 tokens, which is plenty for tweets; behaviour on much longer text is untested.

Unlike some decoder models, padding does not change this model's output: predictions from dynamic padding and from padding to 128 agreed on all of 300 test examples.

## Training data

[Tweet Sentiment Multilingual](https://huggingface.co/datasets/cardiffnlp/tweet_sentiment_multilingual), `english` configuration, using the dataset's own splits. All three are exactly balanced:

| split | examples | per class |
|---|---|---|
| train | 1,839 | 613 |
| validation | 324 | 108 |
| test | 870 | 290 |

The data is tweets, so it reflects Twitter language: informal, short, full of handles, hashtags and slang. The dataset card declares no license, and tweets are subject to the platform's terms. Check both before any commercial use.

## Training procedure

Full fine-tuning of all layers with the Hugging Face `Trainer`, on a GPU in bf16 (365 s reported).

| | |
|---|---|
| Base model | `answerdotai/ModernBERT-base` |
| Learning rate | 2e-5, linear decay |
| Batch size | 32 (train and eval) |
| Epochs | 3 (174 steps) |
| Weight decay | 0.01 |
| Max sequence length | 128 (padded to max length) |
| Optimizer | AdamW (fused) |
| Seed | 42 |
| Checkpoint selection | best validation weighted-F1 |

Framework versions: Transformers 5.16.1, PyTorch 2.11.0+cu128, Datasets 4.8.5.

## Results

### Test set (n = 870)

| metric | value |
|---|---|
| Accuracy | 0.6586 |
| F1 (macro) | 0.6485 |
| Loss | 0.7422 |

| class | precision | recall | F1 | support |
|---|---|---|---|---|
| negative | 0.63 | 0.82 | 0.71 | 290 |
| neutral | 0.55 | 0.41 | 0.47 | 290 |
| positive | 0.78 | 0.74 | 0.76 | 290 |

Re-evaluating the published weights independently (fp32, CPU) gives 0.6563 accuracy and 0.7420 loss, within two examples of the figures above; the small difference is numerical precision. In that run the test confusion matrix (rows are the true class) was:

| true \ predicted | negative | neutral | positive |
|---|---|---|---|
| negative | 238 | 43 | 9 |
| neutral | 118 | 118 | 54 |
| positive | 21 | 54 | 215 |

### Validation set (n = 324), per epoch

| Epoch | Train loss | Val loss | Accuracy | F1 (macro) |
|:-:|:-:|:-:|:-:|:-:|
| 1 | 0.9536 | 0.8058 | 0.6019 | 0.5980 |
| **2** | 0.6855 | **0.7537** | 0.6821 | **0.6790** |
| 3 | 0.5035 | 0.8067 | 0.6759 | 0.6778 |

The published weights are the epoch 2 checkpoint, which had the best validation F1 and the lowest validation loss. Epochs 2 and 3 differ by about a tenth of a point on F1, well within the noise of a 324-example set.

## Limitations

- **About 66% accurate.** Roughly one prediction in three is wrong. Do not use it to make decisions about people, or as the sole signal in moderation or monitoring.
- **`neutral` is mostly misread as `negative`.** In the re-evaluation, 118 of 290 neutral tweets (41%) were predicted negative, and the model over-predicts `negative` overall (precision 0.63 against recall 0.82). If your data has many neutral posts, expect a lot of them to be labelled negative.
- **Small training set** (1,839 tweets). Expect brittleness on sarcasm, negation, mixed sentiment and text unlike English tweets, such as reviews, news or other languages.
- **Confidence is informative but not calibrated.** In the re-evaluation the average top score was 0.76 on correct predictions and 0.64 on wrong ones, and 6% of wrong predictions scored above 0.9. Use scores as a ranking, not as the probability of being right.
- **English only**, despite the multilingual source dataset. It inherits biases from the training tweets and from the base model's pretraining data.
- Trained on 128-token inputs; ModernBERT supports much longer contexts, but that was not tested here.

## Citation

The dataset comes from:

```bibtex
@inproceedings{barbieri-etal-2022-xlm,
    title = "{XLM}-{T}: Multilingual Language Models in {T}witter for Sentiment Analysis and Beyond",
    author = "Barbieri, Francesco and Espinosa Anke, Luis and Camacho-Collados, Jose",
    booktitle = "Proceedings of the Thirteenth Language Resources and Evaluation Conference",
    year = "2022",
    address = "Marseille, France",
    publisher = "European Language Resources Association",
    url = "https://aclanthology.org/2022.lrec-1.27",
    pages = "258--266",
}
```

## License

Apache 2.0, following the base model. The training dataset's license is not declared; see [Training data](#training-data).
