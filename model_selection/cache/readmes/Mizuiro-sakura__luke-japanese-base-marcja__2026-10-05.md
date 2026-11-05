---
license: mit
language: ja
tags:
    - luke
    - pytorch
    - transformers
    - marcja
    - marc-ja
    - sentiment-analysis
    - SentimentAnalysis
    
---

# このモデルはluke-japanese-baseをファインチューニングして、MARC-ja(positive or negativeの二値分類)に用いれるようにしたものです。
このモデルはluke-japanese-baseを
yahoo japan/JGLUEのMARC-ja( https://github.com/yahoojapan/JGLUE )
を用いてファインチューニングしたものです。

positive or negativeの二値分類タスクに用いることができます。

# This model is fine-tuned model for MARC-ja which is based on luke-japanese-base

This model is fine-tuned by using yahoo japan JGLUE MARC-ja dataset.

You could use this model for binary classification (positive or negative) tasks.

# モデルの精度 accuracy of model
precision : 0.967, 
accuracy : 0.967, 
recall : 0.967, 
f1 : 0.967

既存のモデルの精度　accuracy of existing model		

Tohoku BERT large	0.955	

Waseda RoBERTa large (seq128)	0.954	

Waseda RoBERTa large (seq512)	0.961	

XLM RoBERTa large	0.964	

# How to use 使い方
sentencepieceとtransformersをインストールして (pip install sentencepiece , pip install transformers) 
以下のコードを実行することで、MARC-jaタスクを解かせることができます。
After install transformers and sentencepiec, please execute this code.
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained('Mizuiro-sakura/luke-japanese-base-marcja')
model = AutoModelForSequenceClassification.from_pretrained('Mizuiro-sakura/luke-japanese-base-marcja')

text = 'この商品は素晴らしい！とても匂いが良く、満足でした。'

token = tokenizer.encode_plus(text, truncation=True, max_length=128, padding="max_length", return_tenosr='pt')
result = model(torch.tensor(token['input_ids']).unsqueeze(0), torch.tensor(token['attention_mask']).unsqueeze(0))

if torch.argmax(result['logits'])==0:
    print('positive')
if torch.argmax(result['logits'])==1:
    print('negative')
```


# what is Luke?　Lukeとは？[1]
LUKE (Language Understanding with Knowledge-based Embeddings) is a new pre-trained contextualized representation of words and entities based on transformer. LUKE treats words and entities in a given text as independent tokens, and outputs contextualized representations of them. LUKE adopts an entity-aware self-attention mechanism that is an extension of the self-attention mechanism of the transformer, and considers the types of tokens (words or entities) when computing attention scores.

LUKE achieves state-of-the-art results on five popular NLP benchmarks including SQuAD v1.1 (extractive question answering), CoNLL-2003 (named entity recognition), ReCoRD (cloze-style question answering), TACRED (relation classification), and Open Entity (entity typing). luke-japaneseは、単語とエンティティの知識拡張型訓練済み Transformer モデルLUKEの日本語版です。LUKE は単語とエンティティを独立したトークンとして扱い、これらの文脈を考慮した表現を出力します。

# Acknowledgments　謝辞
Lukeの開発者である山田先生とStudio ousiaさんには感謝いたします。 I would like to thank Mr.Yamada @ikuyamada and Studio ousia @StudioOusia.

# Citation
[1]@inproceedings{yamada2020luke, title={LUKE: Deep Contextualized Entity Representations with Entity-aware Self-attention}, author={Ikuya Yamada and Akari Asai and Hiroyuki Shindo and Hideaki Takeda and Yuji Matsumoto}, booktitle={EMNLP}, year={2020} }





