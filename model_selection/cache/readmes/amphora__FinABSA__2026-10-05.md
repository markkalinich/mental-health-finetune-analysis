---
language: en        # <-- my language
widget:
 - text: " Chinese stocks’ plunge on Monday over fears about China’s new leadership team may be misguided, consulting firm Teneo said. Chinese stocks in Hong Kong and New York, especially internet tech giants such as [TGT], dropped on the first trading day after Chinese President Xi Jinping cemented his firm grip on power with a new core leadership team filled with his loyalists."
 - text: "[TGT] stocks dropped 42% while Samsung rallied."
 - text: "Tesla stocks dropped 42% while [TGT] rallied."

tags:
- t5
- finbert
- financial-sentiment-analysis
- sentiment-analysis

license:
- apache-2.0
---

## Model Description

FinABSA is a T5-Large model trained for Aspect-Based Sentiment Analysis(ABSA) tasks using [SEntFiN 1.0](https://asistdl.onlinelibrary.wiley.com/doi/10.1002/asi.24634?af=R). Unlike traditional sentiment analysis models which predict a single sentiment label for each sentence, FinABSA has been trained to disambiguate sentences containing multiple aspects. By replacing the target aspect with a [TGT] token the model predicts the sentiment concentrating to the aspect. [GitHub Repo](https://github.com/guijinSON/FinABSA)

## How to use

You can use this model directly using the AutoModelForSeq2SeqLM class.

```python
>>> from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

>>> tokenizer = AutoTokenizer.from_pretrained("amphora/FinABSA")
>>> model = AutoModelForSeq2SeqLM.from_pretrained("amphora/FinABSA")

>>> input_str = "[TGT] stocks dropped 42% while Samsung rallied."
>>> input = tokenizer(input_str, return_tensors='pt')
>>> output = model.generate(**input, max_length=20)
>>> print(output)
The sentiment for [TGT] in the given sentence is NEGATIVE.

>>> input_str = "Tesla stocks dropped 42% while [TGT] rallied."
>>> input = tokenizer(input_str, return_tensors='pt')
>>> output = model.generate(**input, max_length=20)
>>> print(output)
The sentiment for [TGT] in the given sentence is POSITIVE.
```

## Evaluation Results

Using a test split arbitarly extracted from [SEntFiN 1.0](https://asistdl.onlinelibrary.wiley.com/doi/10.1002/asi.24634?af=R) the model scores an average accuracy of 87%.