---
library_name: transformers
tags:
- sentiment-analysis
- roberta
- twitter
- political-communication
- uk-election
license: mit
language:
- en
base_model:
- cardiffnlp/twitter-roberta-base-sentiment
---

# UK Campaign Sentiment RoBERTa

This model is a fine-tuned version of [`cardiffnlp/twitter-roberta-base-sentiment`](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment) for sentiment classification of tweets posted by UK general election candidates in the 2024 campaign period. It is part of a broader project introducing a multimodal dataset of campaign content, including text, images, and video.

## Model Details

- **Developed by:** [anonymised]
- **Model type:** RoBERTa-base (fine-tuned)
- **Language:** English
- **Fine-tuned from:** `cardiffnlp/twitter-roberta-base-sentiment`
- **License:** MIT 

## Training Details

- **Training data:** Manually annotated tweets from 2024 UK election candidates.
- **Classes:** Negative (−1), Neutral (0), Positive (1)
- **Training period:** 4 epochs with learning rate 2e−5 and batch size 8

## Uses

This model is intended for sentiment analysis of political tweets, especially campaign-related content during UK elections. It can be applied to study negativity, campaign tone, or partisan differences in emotional framing.

## Limitations

- The original model achieved approximately 72% accuracy on a manually annotated validation set, with strongest performance on neutral tweets. 
- While this version has been fine-tuned on UK election campaign tweets, it may not generalize well to other domains or more informal, non-political language.

