---
title: "Indonesian GPT2 Medical Chatbot"
tags:
  - gpt2
base_model:
  - indonesian-nlp/gpt2
datasets:
  - Danda245/medical-qa-id-llama-split
---

# Indonesian GPT2 Medical Chatbot

This model is a fine-tuned version of GPT-2 for medical chatbot in the Indonesian language. It can be used to generate answers to various medical questions.

#### Model Sources
- **Repository:** [indonesian-nlp/gpt2](https://huggingface.co/indonesian-nlp/gpt2)

#### Dataset
- **Repository:** [Danda245/medical-qa-id-llama-split](https://huggingface.co/datasets/Danda245/medical-qa-id-llama-split)

| Metric                           | Value                        |
|----------------------------------|------------------------------|
| **Global Steps**                 | 14480                        |
| **Training Loss**                | 0.3822                       |
| **Training Runtime**             | 15150.72 seconds             |
| **Training Samples per Second**  | 11.47 samples/sec            |
| **Training Steps per Second**    | 0.96 steps/sec               |
| **Total FLOPs**                  | 4.54e+16                     |
| **Epoch**                        | 5.0                          |

#### How to Use

```bash
!pip install transformers torch

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "lafarizo/indo_medical_gpt2_v2"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

input_text = input("Pertanyaan: ")

inputs = tokenizer(input_text, return_tensors="pt", truncation=True, padding=True, max_length=512)

input_ids = inputs['input_ids'].to(device)
attention_mask = inputs['attention_mask'].to(device)

outputs = model.generate(
    input_ids=input_ids,
    attention_mask=attention_mask,
    max_length=512,            
    num_beams=5,               
    temperature=0.7,           
    top_k=50,                  
    top_p=0.9,                 
    no_repeat_ngram_size=2,   
    do_sample=True,           
    eos_token_id=tokenizer.eos_token_id,  
    pad_token_id=tokenizer.pad_token_id
)

generated_answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

if generated_answer.lower().startswith(input_text.lower()):
    generated_answer = generated_answer[len(input_text):].strip()

print("Jawaban: ", generated_answer)