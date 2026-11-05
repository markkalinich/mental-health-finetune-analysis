---
license: llama3
---
The official instruct model weights for "Efficient Continual Pre-training by Mitigating the Stability Gap".

## Introduction
This repo contains Llama-3-Physician-8B-Instruct, a medical language model with 8 billion parameters. This model builds upon the foundation of Llama 3 and has been firstly continual pretrained on high-quality medical sub-corpus from the RefinedWeb dataset and then tuned with diverse medical and general instructions. We also use the three strategies in the paper to mitigate the stability gap during continual pretraining and instruction tuning, which boosts the model's medical task performance and reduces the computation consumption.

## 💻 Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch
model_name = "YiDuo1999/Llama-3-Physician-8B-Instruct"
device_map = 'auto'
model = AutoModelForCausalLM.from_pretrained( model_name, trust_remote_code=True,use_cache=False,device_map=device_map)
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token
def askme(question):
    sys_message = ''' 
    You are an AI Medical Assistant trained on a vast dataset of health information. Please be thorough and
    provide an informative answer. If you don't know the answer to a specific medical inquiry, advise seeking professional help.
    '''   
    # Create messages structured for the chat template
    messages = [{"role": "system", "content": sys_message}, {"role": "user", "content": question}]
    
    # Applying chat template
    prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    outputs = model.generate(**inputs, max_new_tokens=100, use_cache=True)
    
    # Extract and return the generated text, removing the prompt
    response_text = tokenizer.batch_decode(outputs)[0].strip()
    answer = response_text.split('<|im_start|>assistant')[-1].strip()
    return answer
# Example usage
# - Context: First describe your problem.
# - Question: Then make the question.
question = '''What is HIV?'''
print(askme(question))
```
the type of answer is :
```
HIV, or Human Immunodeficiency Virus, is a retrovirus that primarily infects cells of the human immune system, particularly CD4+ T cells, which are crucial to the body's ability to fight off infection. HIV infection can lead to AIDS, or Acquired Immune Deficiency Syndrome, a condition that causes severe damage to the immune system and makes individuals more susceptible to life-threatening infections. HIV
is transmitted through sexual contact, sharing needles, or through mother-to-child transmission during pregnancy.
```

## 🏆 Evaluation
For question-answering tasks, we have

| Model                          | MMLU-Medical | PubMedQA | MedMCQA | MedQA-4-Option | Avg  |
|:--------------------------------|:--------------|:----------|:---------|:----------------|:------|
| Mistral-7B-instruct   | 55.8         | 17.8     | 40.2    | 41.1           | 37.5 |
| Zephyr-7B-instruct-β  | 63.3         | 46.0     | 43.0    | 48.5           | 48.7 |
| PMC-Llama-7B        | 59.7         | 59.2     | 57.6    | 49.2           | 53.6 |
| Medalpaca-13B     | 55.2         | 50.4     | 21.2    | 20.2           | 36.7 |
| AlpaCare-13B    | 60.2         | 53.8     | 38.5    | 30.4           | 45.7 |
| BioMedGPT-LM 7B  | 52.0         | 58.6     | 34.9    | 39.3           | 46.2 |
| Me-Llama-13B      | -            | 70.0     | 44.9       | 42.7              | -    |
| Llama-3-8B instruct                  | 82.0         | 74.6     | 57.1    | 60.3           | 68.5 |
| JSL-Med-Sft-Llama-3-8B  | 83.0     | 75.4     | 57.5    | 74.8           | 72.7 |
| GPT-3.5-turbo-1106                   | 74.0         | 72.6     | 34.9    | 39.3           | 60.6 |
| GPT-4                  | 85.5         | 69.2     | 69.5    | 83.9           | 77.0 |
| Llama-3-physician-8B instruct (ours) | 80.0         | 76.0     | 80.2    | 60.3           | 74.1 |

For Medical claasification, relation extraction, natural language inference, summarization tasks, we have


| Task type                      | Classification | Relation extraction | Natural Language Inference | Summarization |
|:--------------------------------|:----------------|:----------------------|:----------------------------|:---------------|
| Datasets                       | HOC            | DDI-2013             | BioNLI                     | MIMIC-CXR     |
| Mistral-7B-instruct  | 35.8           | 14.1                 | 16.7                       | 12.5          |
| Zephyr-7B-instruct-β  | 26.1           | 19.4                 | 19.9                       | 10.5          |
| PMC-Llama-7B  | 18.4           | 14.7                  | 15.9                       | 13.9          |
| Medalpaca-13B  | 24.6           | 5.8                  | 16.4                       | 1.0           |
| AlpaCare-13B | 26.7           | 11.0                 | 17.0                       | 13.4          |
| BioMedGPT-LM 7B  | 23.4           | 15.5                 | 17.9                       | 6.2           |
| Me-Llama-13B  | 33.5           | 21.4                 | 19.5                       | 40.0          |
| JSL-Med-Sft-Llama-3-8B  | 25.6           | 19.7                 | 16.6                       | 13.8          |
| Llama-3-8B instruct             | 31.0           | 15.1                 | 18.8                       | 10.3          |
| GPT-3.5-turbo-1106              | 54.5           | 21.6                 | 31.7                       | 13.5          |
| GPT-4             | 60.2           | 29.2                 | 57.8                       | 15.2          |
| Llama-3-physician-8B instruct (ours) | 78.9           | 33.6                 | 76.2                       | 37.7          |

## Citation
```
@inproceedings{Guo2024EfficientCP,
  title={Efficient Continual Pre-training by Mitigating the Stability Gap},
  author={Yiduo Guo and Jie Fu and Huishuai Zhang and Dongyan Zhao and Yikang Shen},
  year={2024},
  url={https://api.semanticscholar.org/CorpusID:270688100}
}
```