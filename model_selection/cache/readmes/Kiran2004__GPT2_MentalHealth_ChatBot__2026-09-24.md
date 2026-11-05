---
license: apache-2.0
modelId: unique-model-identifier
tags:
- conversational
- gpt2
language: en
base_model: gpt2
model-index:
- name: GPT2_Conversational_Bot
  results: []
datasets:
- Kiran2004/MentalHealthConversations
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

## Model description

This model is a fine-tuned version of [openai-community/gpt2](https://huggingface.co/gpt2) on an [MentalHealthConversational](https://huggingface.co/datasets/Kiran2004/MentalHealthConversations) dataset.
It is designed to generate text based on provided depression related prompts and can be used for a variety of natural language generation tasks.
It's been trained on question-answer pairs, including unanswerable questions, for the task of Depression related Conversations for 10 Epochs and obtained following loss:
- Training Loss: 1.6727

## Model Training

- **Training Dataset**: [MentalHealthConversational Dataset](https://huggingface.co/datasets/Kiran2004/MentalHealthConversations)
- **Pretrained Model**: [GPT-2](https://huggingface.co/gpt2)

## Evaluation

The model's performance can be evaluated using various metrics such as F1 score, BLEU score, and ROUGE score.
- F1 Score: 0.0908
- BLEU Score: 2.910400064753437e-05
- ROUGE Score: 0.1498

## Example Usage

```python
from transformers import pipeline, GPT2Tokenizer, GPT2LMHeadModel

# Load tokenizer and model
model_name = "Kiran2004/GPT2_MentalHealth_ChatBot"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Generate text
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)
prompt = "Your prompt goes here"
output = generator(prompt, max_length=50, num_return_sequences=1)
print(output[0]["generated_text"])
```

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 3
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Framework versions

- Transformers 4.38.2
- Pytorch 2.2.1+cu121
- Tokenizers 0.15.2