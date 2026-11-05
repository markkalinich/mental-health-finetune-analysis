---
license: mit
datasets:
- TimKoornstra/financial-tweets-sentiment
- TimKoornstra/synthetic-financial-tweets-sentiment
language:
- en
metrics:
- accuracy
- f1
pipeline_tag: text-classification
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
base_model: StephanAkkerman/FinTwitBERT
widget:
- text: Nice 9% pre market move for $para, pump my calls Uncle Buffett 🤑
  example_title: Bullish Crypto Tweet
- text: It is about damn time that my $ARB and $ETH bags pump FFS. 🚀
  example_title: Bullish Crypto Tweet 2
- text: $SPY $SPX closed higher 8th consecutive weeks. Last time it closed 9th straight was 20 years ago.
  example_title: Bullish Stock Tweet
- text: $TCBP Lowest float stock in the market. Float just 325k. Don’t sell for pennies, this one will be a monster. Still early
  example_title: Bullish Stock Tweet 2
- text: Italian companies braced for more political uncertainty
  example_title: Bearish News
#model-index:
#- name: FinTwitBERT-sentiment
#  results:
---

# FinTwitBERT-sentiment

FinTwitBERT-sentiment is a finetuned model for classifying the sentiment of financial tweets. It uses [FinTwitBERT](https://huggingface.co/StephanAkkerman/FinTwitBERT) as a base model, which has been pre-trained on 10 million financial tweets.
This approach ensures that the FinTwitBERT-sentiment has seen enough financial tweets, which have an informal nature, compared to other financial texts, such as news headlines.
Therefore this model performs great on informal financial texts, seen on social media.

## Intended Uses

FinTwitBERT-sentiment is intended for classifying financial tweets or other financial social media texts.

## Dataset

FinTwitBERT-sentiment has been trained on two datasets. One being a collection of several financial tweet datasets and the other a synthetic dataset created out of the first.
- [TimKoornstra/financial-tweets-sentiment](https://huggingface.co/datasets/TimKoornstra/financial-tweets-sentiment): 38,091 human-labeled tweets
- [TimKoornstra/synthetic-financial-tweets-sentiment](https://huggingface.co/datasets/TimKoornstra/synthetic-financial-tweets-sentiment): 1,428,771 synethtic tweets

## More Information

For a comprehensive overview, including the training setup and analysis of the model, visit the [FinTwitBERT GitHub repository](https://github.com/TimKoornstra/FinTwitBERT).

## Usage

Using [HuggingFace's transformers library](https://huggingface.co/docs/transformers/index) the model and tokenizers can be converted into a pipeline for text classification.

```python
from transformers import pipeline

# Create a sentiment analysis pipeline
pipe = pipeline(
    "sentiment-analysis",
    model="StephanAkkerman/FinTwitBERT-sentiment",
)

# Get the predicted sentiment
print(pipe("Nice 9% pre market move for $para, pump my calls Uncle Buffett 🤑"))
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