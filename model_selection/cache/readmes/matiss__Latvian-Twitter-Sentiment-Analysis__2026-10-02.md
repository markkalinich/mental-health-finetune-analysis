---
license: mit
datasets:
- matiss/Latvian-Twitter-Eater-Corpus-Sentiment
language:
- lv
base_model:
- AiLab-IMCS-UL/lvbert
pipeline_tag: text-classification
tags:
- sentiment
---

# Latvian Twitter Sentiment Analysis

This is a BERT-base model trained on ~26,000 manually annotated tweets in Latvian from various sources for sentiment analysis. 


<b>Labels</b>: </br>
0 -> Neutral;</br>
1 -> Positive;</br>
2 -> Negative.

This sentiment analysis model has been integrated in [this HF Space](https://huggingface.co/spaces/matiss/Latvian-Twitter-Sentiment-Analysis).

## Example Pipeline
```python
from transformers import pipeline
model_path = "matiss/Latvian-Twitter-Sentiment-Analysis"
sentiment_task = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)
sentiment_task("Man garšo pankūkas ar kotletēm")
```
```
[{'label': 'Positive', 'score': 0.9032208919525146}]
```



## Corpora Used for Training
---------
* [Twitēdiens](https://huggingface.co/datasets/matiss/Latvian-Twitter-Eater-Corpus-Sentiment) - the Latvian Twitter Eater Corpus of ~5000 manually annotated food-related tweets.
* [Pinnis](https://github.com/pmarcis/latvian-tweet-corpus) - ~ 7000 tweets from politicians and companies
* [Peisenieks](https://github.com/FnTm/latvian-tweet-sentiment-corpus) - ~ 1000 general tweets with sentiment annotated by multiple annotators
* [Vīksna](https://github.com/RinaldsViksna/sikzinu_analize) - ~ 4000 general tweets
* [Nicemanis](https://github.com/nicemanis/LV-twitter-sentiment-corpus) - ~ 2000 general tweets
* [Špats](https://github.com/gatis/om) - ~ 6000 general tweets


Publications
---------

If you use this corpus or scripts, please cite the following paper:

Uga Sproģis and Matīss Rikters (2020). "[What Can We Learn From Almost a Decade of Food Tweets.](https://arxiv.org/abs/2007.05194)" In Proceedings of the 9th Conference Human Language Technologies - The Baltic Perspective ([Baltic HLT 2020](https://klc.vdu.lt/hlt/programme)) (2020).

```bibtex
@inproceedings{SprogisRikters2020BalticHLT,
	author = {Sproģis, Uga and Rikters, Matīss},
	booktitle={In Proceedings of the 9th Conference Human Language Technologies - The Baltic Perspective (Baltic HLT 2020)},
	title = {{What Can We Learn From Almost a Decade of Food Tweets}},
	address={Kaunas, Lithuania},
	year = {2020}
}
```