---
license: mit
datasets:
- qiaojin/PubMedQA
language:
- en
tags:
- medical
---

*Author - Hayden Beadles*

This model is meant to evaluate the results of creating an Encoder / Decoder generative model using BERT. The model is then finetuned on 30000 samples of the PubMedQA dataset. Instead of being finetuned on the columns question and final_answer, where final_answer is a set of yes / no answers, we instead fine tune on the more challenging long_answer column, which gives a short answer to the question.

The model was fine-tuned over 3 epochs, using the Adam learning rate scheduler, with a max length of 128 tokens.

The results are to help gauge BERT's abilities to answer (generate an answer) directly to a question, with no context provided. It is meant to evaluate the overall models training and attention towards a more focused topic, to see if BERTs base training gives it any advantages.
