---
license: llama3.2
datasets:
- Tibi29/PhishingEmail
language:
- en
base_model:
- meta-llama/Llama-Guard-3-1B
pipeline_tag: text-classification
---

Fine-Tuned model Llama-Guard-3-1B using a dataset composed of 4.6k phishing and safe emails.

The phishing emails were generated using different LLMs (each generated about 300 emails, in total 2151 emails): 
- bartowski/Llama-3_1-Nemotron-51B-Instruct-GGUF,
- bartowski/QwQ-32B-Preview-GGUF,
- bartowski/gemma-2-9b-it-GGUF,
- TheBloke/Manticore-13B-GGUF,
- TheBloke/Mistral-7B-Instruct-v0.2-GGUF,
- TheBloke/llama2_70b_chat_uncensored-GGUF,
- TheBloke/Dolphin-Llama-13B-GGUF

The safe emails were selected from Kaggle: https://www.kaggle.com/datasets/venky73/spam-mails-dataset (only the ham emails)

|           | Results of the Llama-Guard-3-1B before fine-tune (on the test set)  |  Results of the fine-tuned model |
|-----------|---------------------------------------------------------------------|----------------------------------|
| Accuracy  |                          0.5236559139784946                         | 0.877741935483871               |
| Precision |                          0.5328376703841388                         | 0.92469797979798                |
| Recall    |                          0.8669354838709677                         | 0.8237677419354839               |
| F1-score  |                          0.6600153491941673                         | 0.8699727547931383               |