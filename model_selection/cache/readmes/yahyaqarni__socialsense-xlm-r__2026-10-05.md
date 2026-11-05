---
library_name: transformers
pipeline_tag: text-classification
language:
  - ur
  - multilingual
license: apache-2.0
tags:
  - urdu
  - roman-urdu
  - xlm-roberta
  - text-classification
  - sentiment-analysis
  - sentiment-classification
  - social-media
---

# socialsense-xmlr
Fine-tuned XLM-R for Urdu & Roman Urdu text sentiment classification.

## Labels
- 0: NEGATIVE
- 1: NEUTRAL
- 2: POSITIVE

## Usage
```python
from transformers import pipeline
pipe = pipeline("text-classification",
                model="yahyaqarni/socialsense-xmlr",
                tokenizer="yahyaqarni/socialsense-xmlr",
                top_k=None)
print(pipe("یہ بہت اچھا ہے"))
print(pipe("me bilkul khush nai hoon"))
```

## Acknowledgements

This model was fine-tuned from [cardiffnlp/twitter-xlm-roberta-base-sentiment](https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment), originally released under the Apache 2.0 License.
