---
datasets:
- ai4bharat/IndicQuestionGeneration
- ai4bharat/IndicSentiment
- ai4bharat/IndicParaphrase
- smallstepai/marathi-instruction-tuning-alpaca

language:
- mr
metrics:
- accuracy
tags:
- marathi
- sentiment analysis
- reading comprehension
- paraphrasing
- translation
library_name: transformers
pipeline_tag: text-generation
license: apache-2.0
---

# Misal-1B-instruct-v0.1

Built by - [smallstep.ai](https://smallstep.ai/)

## What is Misal?

Misal 1B, a pretrained and instruction tuned large language model based on TinyLlama 1B architecture for Marathi.

## Making of Misal?

Detailed blog [here](https://smallstep.ai/making-misal).

## Evaluation :
We did a manual round of evaluations using internet data. This is a fairly small dataset with 100 questions taken from the internet. We understand that a better evaluation method is needed to benchmark our model, this being the first iteration we decided to proceed with manual evaluation. Our main aim was to see if the model understands basic instructions, if so how well is it able to understand it, hence we have limited our evaluation to Reading comprehension, Translation, Sentiment Analysis, Paraphrasing like tasks.

| Model       | Reading Comprehension | Sentiment Analysis | Paraphrase | Translation | Average |
|-------------|-----------------------|--------------------|------------|-------------|---------|
| Misal-7B   | 88                    | 68                  | 92         | 76          | 81      |
| Misal-1B   | 48                    | 68                  | 72         | 36          | 56      |
| ChatGPT3.5 | 68                    | 76                  | 100        | 96          | 85      |
| Krutrim     | 40                    | 60                  | 88         | 80          | 67      |
| MahaMarathi | 0                     | 0                   | 0          | 0          | 0       | 

We have released the evaluation data here:
- [Manual Evaluation Set](https://huggingface.co/datasets/smallstepai/Misal-Evaluation-v0.1)



![image/png](https://framerusercontent.com/images/oYRJ925hmTBDjd6RMucvD1qtl7s.jpeg)


## License

The model inherits the license from [TinyLlama](https://huggingface.co/TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T). 


## Usage

[Colab Link](https://colab.research.google.com/drive/1USRytNCbPBfIgobzgv4knZXawlWf9Pom?usp=sharing#scrollTo=1vQIxoBusFoi)

### Installation

```bash
pip install transformers accelerate
```

### Prompt

```python
आपण एक मदतगार, आदरणीय आणि प्रामाणिक सहाय्यक आहात.नेहमी शक्य तितकी उपयुक्त उत्तर द्या. तुमची उत्तरे हानिकारक, अनैतिक, वर्णद्वेषी, लैंगिकतावादी, हानिकारक, धोकादायक किंवा बेकायदेशीर नसावीत. कृपया खात्री करा की तुमची उत्तरे सामाजिक दृष्टिकोनाने निष्पक्ष आणि सकारात्मक स्वरूपाची आहेत. जर एखाद्या प्रश्नाला काही अर्थ नसेल किंवा वस्तुस्थितीशी सुसंगती नसेल, तर उत्तर देण्याऐवजी काहीतरी बरोबर का नाही हे स्पष्ट करा. तुम्हाला एखाद्या प्रश्नाचे उत्तर माहित नसल्यास, कृपया चुकीची माहिती देऊ नये.

### Instruction:

<instruction>

### Input:

<input data>

### Response:
```

### PyTorch

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
device = "cuda"
model = AutoModelForCausalLM.from_pretrained("smallstepai/Misal-1B-instruct-v0.1", torch_dtype=torch.bfloat16, device_map='auto')
tokenizer = AutoTokenizer.from_pretrained("smallstepai/Misal-1B-instruct-v0.1")

def ask_misal(model, tokenizer, instruction, inputs='', system_prompt='', max_new_tokens=200, device='cuda'):

    ip = dict(system_prompt=system_prompt, instruction=instruction, inputs=inputs)
    model_inputs = tokenizer.apply_chat_template(ip, return_tensors='pt')
    outputs = model.generate(model_inputs.to(device), max_new_tokens=max_new_tokens)
    response = tokenizer.decode(outputs[0]).split('### Response:')[1].strip()
    return response

instruction="वाक्य सकारात्मक किंवा नकारात्मक आहे ते स्थिती निर्दिष्ट करा."
inputs="मला हे आवडते त्या मार्गाने हे खूप उबदार आहे"
resp = ask_misal(model, tokenizer, instruction=instruction, inputs=inputs, max_new_tokens=200)
print(resp)
```

## Limitations

- Misal-1B-instruct-v0.1, built upon the TinyLlama model for Marathi, demonstrates an understanding of the language but currently falls short of Misal-7B in performance. This might be due to its smaller size and the data used for training TinyLlama.
- However, we're actively working on improvements, we aim to significantly enhance Misal-1B-instruct-v0.1's capabilities and bring it closer to its full potential.


## Team

Sagar Sarkale, Prasad Mane, Shravani Chavan