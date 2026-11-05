---
license: mit
language:
- en
tags:
- Human Preference Alignment
- medical
- mental health
---

# Introduction
MetaAligner-IMHI-7B is part of the <em>MetaAligner</em> project, the first policy-agnostic and generalizable method for multi-objective preference alignment of large
language models. This model is finetuned based on the Meta LLaMA2-7B foundation model and 
the dynamic multi-objective dataset built from the IMHI dataset. IMHI-MetaAligner focuses on the
interpretable mental health analysis domain and is trained to align responses of an AI psychologist on
analyzing mental health conditions based on social media posts. The model is expected to perform multi-objective alignment
efficiently, without tuning the policy models or accessing their parameters. <em>MetaAligner</em> also exerts zero-shot preference alignment
for unseen objectives. To our knowledge, this work marks the first attempt at generalizable multi-
objective preference alignment. Experimental results show that MetaAligner can simultaneously perform effective alignment for multiple unseen objectives
while maintaining performance on aligned objectives.

# Dataset
This model is trained based on the following released dataset: 

# Usage
With the Hugging Face Transformers library, you can use the MetaAligner-IMHI-7B model in your Python project. Here is a simple example of how to load the model:

```python
import torch
from transformers import LlamaTokenizer, LlamaForCausalLM
tokenizer = LlamaTokenizer.from_pretrained('MetaAligner/MetaAligner-IMHI-7B', padding_side='left')
model = LlamaForCausalLM.from_pretrained('MetaAligner/MetaAligner-IMHI-7B', device_map='auto', torch_dtype=torch.bfloat16)
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
```

In this example, LlamaTokenizer is used to load the tokenizer, and LlamaForCausalLM is used to load the model. The `device_map='auto'` argument is used to automatically
use the GPU if it's available.

You can align any outputs obtained from other foundation models with your self-defined objectives. For example, we have the following query from HH-RLHF, 
unaligned output examples from Gemma-7B,
and target objectives:

```python
all_aspects = {'correct': 'Correctness: the explanations should make correct predictions',
               'informative': 'Informative: the response should express clear logic and provide consistent evidence',
               'professional': 'Professional: the response should provide evidence with high quality and reliability'}
aspects = ['correct', 'informative', 'professional']
question = "Consider this post: 'how the coronavirus could damage the US economy' Question: What is the stress cause of this post?"
answer = "The stress cause of this post is the potential damage of the coronavirus to the US economy."
```

To ensure the best performance, use the following template to prompt <em>MetaAligner</em>:

```python
query_prompt = 'Edit the following Question-Answer pair to make it better considering these aspects "{aspects}" | ' \
                   'Question: {question} | Answer: {answer} | Edit: '
aspects = [all_aspects[i] for i in aspects]
aligner_queries = [query_prompt.format(aspects='; '.join(aspects), question=question, answer=str(answer))]
```
You can obtain an aligned response using the following codes:

```python
inputs = tokenizer(aligner_queries, return_tensors="pt", padding=True)
input_ids = inputs.input_ids.to(device)
generate_ids = model.generate(input_ids, max_new_tokens=1024)
truc_ids = generate_ids[0][len(input_ids[0]):]
response = tokenizer.decode(truc_ids, skip_special_tokens=True, spaces_between_special_tokens=False)
print(response)
```

One inference of MetaAligner-IMHI-7B on the above codes has the following response:
```
The stress cause of this post is likely the uncertainty and potential negative impacts of the coronavirus on the US economy. The post is discussing the potential consequences of the pandemic, such as job loss, business closures, and economic downturn. These factors can cause significant stress and anxiety for individuals and organizations.
```

## License

MetaAligner-IMHI-7B is licensed under MIT. For more details, please see the MIT file.