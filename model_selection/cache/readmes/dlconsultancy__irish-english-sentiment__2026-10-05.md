---
language: en
license: unknown
library_name: transformers
pipeline_tag: text-classification
base_model: cardiffnlp/twitter-roberta-base-sentiment-latest
datasets:
- dlconsultancy/irish-english-review-phrases
tags:
- sentiment-analysis
- irish-english
- hiberno-english
- customer-reviews
widget:
- text: "That dessert was deadly."
- text: "Wouldn't be rushing back."
- text: "Ah sure it was grand."
---

# Irish-English review sentiment

A sentiment model for customer reviews written the way Irish customers actually talk.
It labels a review **Positive**, **Negative** or **Neutral**.

Built by [DL Consultancy](https://dlconsultancy.ie) as a practical experiment in how small businesses can test
and adapt free AI models to their own customers' language.

## Why

Popular sentiment models are trained mostly on American English. In our tests they scored 84-100% on
plain English reviews but far lower on Irish English, reading "That coffee is unreal" as negative and
"Wouldn't be rushing back" as neutral.

## Intended use
A demonstration and starting point for small businesses and developers who want to sort short Irish customer reviews or feedback by sentiment. Not intended for decisions about individuals, or for use without human review.

## How it was made

Fine-tuned from [cardiffnlp/twitter-roberta-base-sentiment-latest](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest) on 300 review-style phrases
covering Irish idioms, intensifiers (savage, deadly, fierce), understatement, understated complaints,
sarcasm, ambiguous words (grand, mad) and conversational phrases (in fairness, sure look), plus
plain-English controls. Training: 4 epochs, learning rate 2e-05, batch size 16.

Training data: [dlconsultancy/irish-english-review-phrases](https://huggingface.co/datasets/dlconsultancy/irish-english-review-phrases)

## Results (5-fold cross-validation, 300 phrases)

Each phrase was tested by a model that had not seen it during training.

| | Base model | Fine-tuned |
|---|---|---|
| All phrases (3 labels) | 55% | 80% |
| Irish English phrases | 50% | 78% |
| Plain English controls | 84% | 95% |
| Neutral phrases | 33% | 73% |
| Understatement | 46% | 80% |
| Understated complaints | 31% | 66% |
| Sarcasm / irony | 25% | 54% |

## Limitations

- Small dataset (300 phrases), labelled by one person, with disputed phrases reviewed by a second. Some of the gain may reflect that person's style rather than Irish English in general.
- Around half the phrases were drafted with AI assistance and then reviewed and edited by the author; testing showed these were somewhat easier for models than phrases written from scratch.
- Sarcasm remains hard (about half correct): spotting it often needs real-world context.
- Short review-style sentences only; not tested on long reviews or social media threads.
- Treat outputs as a guide, not a verdict. For decisions that matter, have a person check.




## How to use

```python
from transformers import pipeline
clf = pipeline("text-classification", model="dlconsultancy/irish-english-sentiment")
clf("The chips were only gorgeous.")
```

## Licence and credits

The base model, cardiffnlp/twitter-roberta-base-sentiment-latest, does not declare a licence, so this fine-tuned version is published for research and demonstration purposes. If you plan to use it commercially, check the base model's terms with Cardiff NLP first.

Built by DL Consultancy. Contact: services@dlconsultancy.ie
