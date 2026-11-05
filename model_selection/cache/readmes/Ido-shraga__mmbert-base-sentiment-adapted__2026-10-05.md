---
license: unknown
base_model: jhu-clsp/mmbert-base
library_name: transformers
tags:
- modernbert
- mmbert
- sentiment-analysis
- twitter
- multilingual
datasets:
- cardiffnlp/tweet_eval
- cardiffnlp/super_tweeteval
- cardiffnlp/tweet_sentiment_multilingual
metrics:
- f1
- accuracy
---
# mmBERT-base — sentiment task adaptation (stage 1)

Full fine-tune of [`jhu-clsp/mmbert-base`](https://huggingface.co/jhu-clsp/mmbert-base) (multilingual ModernBERT, 22 layers, 256K-token Gemma-2 tokenizer) for **3-class tweet sentiment** (`negative` / `neutral` / `positive`), mirroring a tweet task-adapted checkpoint before per-language LoRA specialization (stage 2: [`mmbert-sentiment-lora`](https://huggingface.co/Ido-shraga/mmbert-sentiment-lora)).

## Training data (combined, ~87K train / 8.6K val)

| Dataset | Config | Train rows | Label handling |
|---|---|---:|---|
| `cardiffnlp/tweet_eval` | `sentiment` | 45,615 | 3-class as-is |
| `cardiffnlp/super_tweeteval` | `tweet_sentiment` | 26,632 | 5-point ABSA scale folded: {strongly negative, negative}→negative, {negative or neutral}→neutral, {positive, strongly positive}→positive |
| `cardiffnlp/tweet_sentiment_multilingual` | `all` | 14,712 | 3-class as-is (8 languages) |

## Hyperparameters

- 2 epochs (5,436 steps), batch 32, max length 128, bf16
- lr 3e-5, linear schedule, warmup 543 steps, weight decay 0.01
- Attention: PyTorch SDPA (flash-attention kernels) on A10G
- Best checkpoint selected by combined-validation macro-F1

## Results (best checkpoint)

| Split | macro-F1 | Accuracy |
|---|---:|---:|
| Combined validation | **0.7005** | 0.7044 |
| tweet_eval sentiment test | 0.7089 | 0.7116 |
| super_tweeteval tweet_sentiment test (folded to 3-class) | 0.6596 | 0.6682 |
| tweet_sentiment_multilingual test | 0.6908 | 0.6902 |

Note: the super_tweeteval test score is on labels folded to 3 classes and is **not** comparable to the official SuperTweetEval leaderboard metric (`1 − MAE^M` on the 5-point scale).

## Usage

```python
from transformers import pipeline

clf = pipeline("text-classification", model="Ido-shraga/mmbert-base-sentiment-adapted")
clf("Absolutely loving the new update, great work!")
```

## References

- mmBERT: arXiv 2509.06888
- TweetEval: arXiv 2010.12421 · SuperTweetEval: arXiv 2310.14757
