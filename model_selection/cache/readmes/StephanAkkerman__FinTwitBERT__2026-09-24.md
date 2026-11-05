---
license: mit
language:
- en
tags:
- NLP
- BERT
- FinBERT
- FinTwitBERT
- sentiment
- finance
- financial-analysis
- sentiment-analysis
- financial-sentiment-analysis
- twitter
- tweets
- tweet-analysis
- stocks
- stock-market
- crypto
- cryptocurrency
datasets:
- StephanAkkerman/stock-market-tweets-data
- StephanAkkerman/financial-tweets
- StephanAkkerman/crypto-stock-tweets
metrics:
- perplexity
widget:
- text: Paris is the [MASK] of France.
  example_title: Generic 1
- text: The goal of life is [MASK].
  example_title: Generic 2
- text: AAPL is a [MASK] sector stock.
  example_title: AAPL
- text: I predict that this stock will go [MASK].
  example_title: Stock Direction
- text: $AAPL is the ticker for the company named [MASK].
  example_title: Ticker
base_model: yiyanghkust/finbert-pretrain
model-index:
- name: FinTwitBERT
  results:
  - task:
      type: financial-tweet-prediction
      name: Financial Tweet Prediction
    dataset:
      name: Stock Market Tweets Data
      type: finance
    metrics:
    - type: Perplexity
      value: 5.022
---

# FinTwitBERT

FinTwitBERT is a language model specifically pre-trained on a large dataset of financial tweets. This specialized BERT model aims to capture the unique jargon and communication style found in the financial Twitter sphere, making it an ideal tool for sentiment analysis, trend prediction, and other financial NLP tasks.

## Sentiment Analysis
The [FinTwitBERT-sentiment](https://huggingface.co/StephanAkkerman/FinTwitBERT-sentiment) model leverages FinTwitBERT for the sentiment analysis of financial tweets, offering nuanced insights into the prevailing market sentiments.

## Dataset
FinTwitBERT is pre-trained on several financial tweets datasets, consisting of tweets mentioning stocks and cryptocurrencies:
- [StephanAkkerman/crypto-stock-tweets](https://huggingface.co/datasets/StephanAkkerman/crypto-stock-tweets): 8,024,269 tweets
- [StephanAkkerman/stock-market-tweets-data](https://huggingface.co/datasets/StephanAkkerman/stock-market-tweets-data): 923,673 tweets
- [StephanAkkerman/financial-tweets](https://huggingface.co/datasets/StephanAkkerman/financial-tweets): 263,119 tweets

## Model Details
Based on the [FinBERT](https://huggingface.co/yiyanghkust/finbert-pretrain) model and tokenizer, FinTwitBERT includes additional masks (`@USER` and `[URL]`) to handle common elements in tweets. The model underwent 10 epochs of pre-training, with early stopping to prevent overfitting.

## More Information
For a comprehensive overview, including the complete training setup details and more, visit the [FinTwitBERT GitHub repository](https://github.com/TimKoornstra/FinTwitBERT).

## Usage
Using [HuggingFace's transformers library](https://huggingface.co/docs/transformers/index) the model and tokenizers can be converted into a pipeline for masked language modeling.

```python
from transformers import pipeline

pipe = pipeline(
    "fill-mask",
    model="StephanAkkerman/FinTwitBERT",
)
print(pipe("Bitcoin is a [MASK] coin."))
```

## Citing & Authors

If you use FinTwitBERT or FinTwitBERT-sentiment in your research, please cite us as follows, noting that both authors contributed equally to this work:

```
@misc{FinTwitBERT,
  author = {Stephan Akkerman, Tim Koornstra},
  title = {FinTwitBERT: A Specialized Language Model for Financial Tweets},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/TimKoornstra/FinTwitBERT}}
}
```

Additionally, if you utilize the sentiment classifier, please cite:

```
@misc{FinTwitBERT-sentiment,
  author = {Stephan Akkerman, Tim Koornstra},
  title = {FinTwitBERT-sentiment: A Sentiment Classifier for Financial Tweets},
  year = {2023},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/StephanAkkerman/FinTwitBERT-sentiment}}
}
```

## License
This project is licensed under the MIT License. See the [LICENSE](https://choosealicense.com/licenses/mit/) file for details.