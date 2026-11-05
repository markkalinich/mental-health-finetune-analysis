---
language:
- ru
- en
license: mit
tags:
- finance
- sentiment
- stocks
metrics:
- accuracy
widget:
- text: Нуу, эту папиру надо лонговать!
  example_title: long sentiment
- text: Не уверен. Нужно подумать, перед тем, как брать.
  example_title: neutral sentiment
- text: Такое только хомяки берут. Нужно сливать эту бумажку поскорее.
  example_title: short sentiment
---

## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

- **Developed by:** Alexander Nikitin
- **Model type:** XLM-RoBERTa-base Fine-Tuned on my labelled dataset
- **Language(s) (NLP):** Russian, English
- **License:** MIT
- **Finetuned from model:** FacebookAI/xlm-roberta-base

## Dataset

This transformer model was fine-tuned on parsed comments from "Tinkoff Pulse".

First step:
Comments were preprocessed, for each stock ticker subcomment for ticker was extracted.
Example: "{$GAZP} {$TCSG} {$RTKM} По газрому все хорошо. По Ростелекому не очень. Тинек идет вниз!" -> "{$GAZP} По газрому все хорошо."

Next step: 
Labelling dataset of 10K preprocessed comments, evenly distributed from 10 russian stocks. 
Used Mistral-7b LLM to label comments on 3 categories: "buy" - if author wants or encourages to buy (long), "sell" - if author wants or encourages to sell or short, "neutral" - if this is news or we cannot say for sure.
Plans for further research: label 100k comments and train on them. 

## Bias, Risks, and Limitations

1. Model is trained on Russian/English comments;
2. Model is not good at extracting sentiment from comments with bright keywords in different directions, like "I wanna sell. But probably I should buy back later.";
3. Model performs good on short-medium texts like comments, which are usually skewed to one side (strong buy or strong sell).

### Recommendations

## How to Get Started with the Model

Download the model with huggingface pipeline and use it!

Labels:
- LABEL_0 = SELL
- LABEL_1 = NEUTRAL
- LABEL_2 = BUY

## Evaluation

- Accuracy on validation dataset: 0.786
- Notice: this is accuracy on ~1.5k comments.

## Model Card Authors

https://t.me/pivo_txt