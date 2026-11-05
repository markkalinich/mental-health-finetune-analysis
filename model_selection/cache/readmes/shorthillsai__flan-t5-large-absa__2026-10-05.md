---
language:
- en
tags:
- absa
- AspectBasedSentimentAnalysis
- Classification
- sentiment
base_model: google/flan-t5-large
---

# flan-t5-large-absa

This model is a fine-tuned version of [google/flan-t5-large](https://huggingface.co/google/flan-t5-base) on custom dataset prepared by GPT-4 and verified by human.

## Model description

Text-to-Text model for aspect based sentiment analysis.

## Intended uses & limitations

This is not for commercial use since the dataset was prepared using OpenAI with humans in the loop. It must be tested on the required dataset for accuracy before being released to production.


### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- optimizer: Adam
- num_epochs: 5
- bf16: True

### Package Versions

- Transformers 4.27.2
- torch 1.13.1
- Datasets 2.13.1
- Tokenizers 0.13.3

### Machine Used and time taken
- RTX 3090: 8 hrs. 35 mins.

```python
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model = AutoModelForSeq2SeqLM.from_pretrained("shorthillsai/flan-t5-large-absa", device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("shorthillsai/flan-t5-large-absa", truncation=True)

prompt = """Find the aspect based sentiment for the given review. 'Not present' if the aspect is absent.\n\nReview:I love the screen of this laptop and the battery life is amazing.\n\nAspect:Battery Life\n\nSentiment: """

input_ids = tokenizer(prompt, return_tensors="pt").to("cuda").input_ids
instruct_model_outputs = instruct_model.generate(input_ids=input_ids)
instruct_model_text_output = tokenizer.decode(instruct_model_outputs[0], skip_special_tokens=True)
```