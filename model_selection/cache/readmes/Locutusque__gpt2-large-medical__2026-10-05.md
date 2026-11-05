---
datasets:
- BI55/MedText
- pubmed_qa
metrics:
- bleu
- perplexity
pipeline_tag: text-generation
widget:
- text: <|USER|> What is Schizophrenia? <|ASSISTANT|>
inference:
  parameters:
    temperature: 0.8
    top_p: 0.14
    top_k: 41
    max_new_tokens: 15
    repetition_penalty: 1.176
tags:
- medical
---
A further fine-tuned version of Locutusque/gpt2-large-conversational on MedText and pubmed_qa

# Evaluation
This model was evaluated using GPT-3.5, and it was asked medical questions. It achieved an average accuracy of 80%.