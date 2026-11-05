---
language: en        # <-- my language
widget:
 - text: " Chinese stocks’ plunge on Monday over fears about China’s new leadership team “may be misguided,” consulting firm Teneo said. Chinese stocks in Hong Kong and New York, especially internet tech giants such as [TGT], dropped on the first trading day after Chinese President Xi Jinping cemented his firm grip on power with a new core leadership team filled with his loyalists. Over the last several years, Xi has shown a preference for greater state involvement in the economy. “Close relationships with Xi notwithstanding, Li Qiang, Li Xi, and Cai Qi all enter the [Politburo standing committee] after heading up rich provinces where economic growth is still the top priority,” Teneo Managing Director Gabriel Wildau and a team said in a note."
tags:
- t5
- finbert
- financial-sentiment-analysis
- sentiment-analysis
license:
- apache-2.0
---
## Model Description
FinABSA-Longer is a T5-Large model trained for Aspect-Based Sentiment Analysis(ABSA) tasks using [SEntFiN 1.0](https://asistdl.onlinelibrary.wiley.com/doi/10.1002/asi.24634?af=R) and additional augmentation techniques. It shows robust behavior to even longer sequences compared to the previous [FinABSA model](https://huggingface.co/amphora/FinABSA). By replacing the target aspect with a [TGT] token the model predicts the sentiment concentrating to the aspect.[GitHub Repo](https://github.com/guijinSON/FinABSA)
## How to use
You can use this model directly using the AutoModelForSeq2SeqLM class.
```python
>>> from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

>>> tokenizer = AutoTokenizer.from_pretrained("amphora/FinABSA")
>>> model = AutoModelForSeq2SeqLM.from_pretrained("amphora/FinABSA")

>>> input_str = "[TGT] stocks dropped 42% while Samsung rallied."
>>> input = tokenizer(input_str, return_tensors='pt')
>>> output = model.generate(**input, max_length=20)
>>> print(tokenizer.decode(output[0]))
The sentiment for [TGT] in the given sentence is NEGATIVE.
>>> input_str = "Tesla stocks dropped 42% while [TGT] rallied."
>>> input = tokenizer(input_str, return_tensors='pt')
>>> output = model.generate(**input, max_length=20)
>>> print(tokenizer.decode(output[0]))
The sentiment for [TGT] in the given sentence is POSITIVE.
```
## Evaluation Results
Using a test split arbitarly extracted from [SEntFiN 1.0](https://asistdl.onlinelibrary.wiley.com/doi/10.1002/asi.24634?af=R) the model scores an average accuracy of 87%.