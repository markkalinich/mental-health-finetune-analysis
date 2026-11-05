---
license: llama3
language:
- tr
pipeline_tag: text-generation
base_model: ytu-ce-cosmos/Turkish-Llama-8b-Instruct-v0.1
tags:
- Turkish
- turkish
- Llama
- Llama3
---

<img src="./cosmosLLaMa2_r2.png"/>


# Cosmos LLaMa Instruct-DPO

This is the newest and the most advanced iteration of CosmosLLama. The model has been developed by merging two distinctly trained CosmosLLaMa-Instruct DPO models.

The CosmosLLaMa-Instruct DPO is designed for text generation tasks, providing the ability to continue a given text snippet in a coherent and contextually relevant manner. Due to the diverse nature of the training data, which includes websites, books, and other text sources, this model can exhibit biases. Users should be aware of these biases and use the model responsibly.

You can easily demo the model from here: https://cosmos.yildiz.edu.tr/cosmosllama

#### Transformers pipeline

```python
import transformers
import torch

model_id = "ytu-ce-cosmos/Turkish-Llama-8b-DPO-v0.1"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
)

messages = [
    {"role": "system", "content": "Sen bir yapay zeka asistanısın. Kullanıcı sana bir görev verecek. Amacın görevi olabildiğince sadık bir şekilde tamamlamak. Görevi yerine getirirken adım adım düşün ve adımlarını gerekçelendir."},
    {"role": "user", "content": "Soru: Bir arabanın deposu 60 litre benzin alabiliyor. Araba her 100 kilometrede 8 litre benzin tüketiyor. Depo tamamen doluyken araba kaç kilometre yol alabilir?"},
]

terminators = [
    pipeline.tokenizer.eos_token_id,
    pipeline.tokenizer.convert_tokens_to_ids("<|eot_id|>")
]

outputs = pipeline(
    messages,
    max_new_tokens=256,
    eos_token_id=terminators,
    do_sample=True,
    temperature=0.6,
    top_p=0.9,
)
print(outputs[0]["generated_text"][-1])
```

#### Transformers AutoModelForCausalLM

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "ytu-ce-cosmos/Turkish-Llama-8b-DPO-v0.1"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

messages = [
    {"role": "system", "content": "Sen bir yapay zeka asistanısın. Kullanıcı sana bir görev verecek. Amacın görevi olabildiğince sadık bir şekilde tamamlamak. Görevi yerine getirirken adım adım düşün ve adımlarını gerekçelendir."},
    {"role": "user", "content": "Soru: Bir arabanın deposu 60 litre benzin alabiliyor. Araba her 100 kilometrede 8 litre benzin tüketiyor. Depo tamamen doluyken araba kaç kilometre yol alabilir?"},
]

input_ids = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt"
).to(model.device)

terminators = [
    tokenizer.eos_token_id,
    tokenizer.convert_tokens_to_ids("<|eot_id|>")
]

outputs = model.generate(
    input_ids,
    max_new_tokens=256,
    eos_token_id=terminators,
    do_sample=True,
    temperature=0.6,
    top_p=0.9,
)
response = outputs[0][input_ids.shape[-1]:]
print(tokenizer.decode(response, skip_special_tokens=True))
```


# Acknowledgments
- Thanks to the generous support from the Hugging Face team, it is possible to download models from their S3 storage 🤗
- Computing resources used in this work were provided by the National Center for High Performance Computing of Turkey (UHeM) under grant numbers 1016912023 and 
1018512024
- Research supported with Cloud TPUs from Google's TPU Research Cloud (TRC)

### Contact
COSMOS AI Research Group, Yildiz Technical University Computer Engineering Department <br>
https://cosmos.yildiz.edu.tr/ <br>
cosmos@yildiz.edu.tr

# Citation
```bibtex
@inproceedings{kesgin2024optimizing,
  title={Optimizing Large Language Models for Turkish: New Methodologies in Corpus Selection and Training},
  author={Kesgin, H Toprak and Yuce, M Kaan and Dogan, Eren and Uzun, M Egemen and Uz, Atahan and {\.I}nce, Elif and Erdem, Yusuf and Shbib, Osama and Zeer, Ahmed and Amasyali, M Fatih},
  booktitle={2024 Innovations in Intelligent Systems and Applications Conference (ASYU)},
  pages={1--6},
  year={2024},
  organization={IEEE}
}
```

---
license: llama3
---