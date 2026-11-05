---
library_name: transformers
datasets:
- beomi/KoAlpaca-v1.1a
- beomi/KoAlpaca-RealQA
language:
- ko
base_model:
- YiDuo1999/Llama-3-Physician-8B-Instruct
pipeline_tag: text-generation
---

# Introduction

This repo contains Physician-Ko-8B, a medical language model with 8 billion parameters. This model builds upon the foundation of LLaMA-3-physician-8b-instruct model fine-tuned with a Korean dataset.

## Datasets

- beomi/KoAlpaca-RealQA
- beomi/KoAlpaca-v1.1a
- https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71762


# Approach 1

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "eded0902/Physician-Ko-8B"
tokenizer_name = "YiDuo1999/Llama-3-Physician-8B-Instruct"
device_map = 'auto'

model = AutoModelForCausalLM.from_pretrained( model_name, trust_remote_code=True,use_cache=False,device_map=device_map)
tokenizer = AutoTokenizer.from_pretrained(tokenizer_name, trust_remote_code=True)

tokenizer.chat_template = "{% if not add_generation_prompt is defined %}{% set add_generation_prompt = false %}{% endif %}{% for message in messages %}{{'<|im_start|>' + message['role'] + '\n' + message['content'] + '<|im_end|>' + '\n'}}{% endfor %}{% if add_generation_prompt %}{{ '<|im_start|>assistant\n' }}{% endif %}"
eos_token_id = [tokenizer.eos_token_id, tokenizer.convert_tokens_to_ids("<|eot_id|>"), tokenizer.convert_tokens_to_ids("<|im_end|>")]
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
    outputs = model.generate(**inputs, max_new_tokens=1000, use_cache=True)
    
    # Extract and return the generated text, removing the prompt
    response_text = tokenizer.batch_decode(outputs)[0].strip()
    answer = response_text.split('<|im_start|>assistant')[-1].split('<|im_end|>')[0].strip()
    return answer

# Example usage
# - Context: First describe your problem.
# - Question: Then make the question.
question = '''HIV가 뭐야?'''
print(askme(question))
```

the type of answer is:

```
'HIV는 Human Immunodeficiency Virus의 약자로, 인체 면역결핍 바이러스라고도 불립니다. 이 바이러스는 인간의 면역 체계를 약화시키는 바이러스로, 인체의 면역 세포를 공격하여 면역력을 감소시킵니다. HIV에 감염되면 인체의 면역 체계가 약해져 다양한 감염성 질환과 종양이 발생할 수 있습니다. HIV 감염을 예방하기 위해서는 안전한 성관계 유지, 혈액 및 혈액 제제의 공유를 피하는 등의 예방 조치가 필요합니다.
```

# Approach 2

## Using langchain

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain.llms.huggingface_pipeline import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate

model_name = "eded0902/Physician-Ko-8B"
tokenizer_name = "YiDuo1999/Llama-3-Physician-8B-Instruct"
device_map = 'auto'

model = AutoModelForCausalLM.from_pretrained( model_name, trust_remote_code=True,use_cache=False,device_map=device_map)
tokenizer = AutoTokenizer.from_pretrained(tokenizer_name, trust_remote_code=True)

tokenizer.chat_template = "{% if not add_generation_prompt is defined %}{% set add_generation_prompt = false %}{% endif %}{% for message in messages %}{{'<|im_start|>' + message['role'] + '\n' + message['content'] + '<|im_end|>' + '\n'}}{% endfor %}{% if add_generation_prompt %}{{ '<|im_start|>assistant\n' }}{% endif %}"
eos_token_id = [tokenizer.eos_token_id, tokenizer.convert_tokens_to_ids("<|eot_id|>"), tokenizer.convert_tokens_to_ids("<|im_end|>")]
tokenizer.pad_token = tokenizer.eos_token

pipe = pipeline("text-generation", 
               model=model, 
               tokenizer=tokenizer, 
               max_new_tokens=512
               )
hf = HuggingFacePipeline(pipeline=pipe)

sys_message = """ You are an AI Medical Assistant trained on a vast dataset of health information. Please be thorough and
    provide an informative answer. If you don't know the answer to a specific medical inquiry, advise seeking professional help.
    """
question = "HIV가 뭐야?"
# Create messages structured for the chat template
messages = [{"role": "system", "content": sys_message}, {"role": "user", "content": question}]

# Applying chat template
template = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
prompt = PromptTemplate.from_template(template)

chain = prompt | hf

print(chain.invoke({"question": question})[len(template):].split('<|im_end|>')[0].strip())
```

the type of answer is:

```
HIV는 인간 면역 결핍 바이러스(Human Immunodeficiency Virus, HIV)의 약자입니다. 이 바이러스는 인체의 면역 체계를 약화시켜 감염을 일으키는 바이러스입니다. HIV는 주로 성적 접촉, 혈액 전파, 태아 감염 등을 통해 전파됩니다. HIV에 감염되면 면역 세포들이 파괴되어 다양한 감염성 질환과 종양이 발생할 수 있습니다. HIV 감염을 예방하기 위해서는 안전한 성행위와 혈액 및 혈액 제품의 안전한 사용이 중요합니다. 또한 HIV 감염 여부를 확인하기 위해 정기적인 검사를 받는 것이 필요합니다.
```